#!/bin/python

from subprocess import Popen, PIPE, STDOUT
import os
import time
import paramiko
import scp
import zipfile
import re
from xml.dom import minidom
import utils
import sys

time_stamp = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
war_deploy_pom_file = "pom_deploy.xml"

#解决依赖
def resolve_dependencies(jars, wars, exts, deps):

    needed_deps = map(lambda x: os.path.basename(x), reduce(lambda x, y: x + y, [dep for jar, dep in jars] +
                                                            [dep for war, dep in wars] + [dep for ext, dep in exts]))

    dep_helper = set()
    dep_identified = []
    for dep in deps:
        if os.path.basename(dep) in dep_helper:
            continue

        if os.path.basename(dep) not in needed_deps:
            continue

        dep_identified.append(dep)
        dep_helper.add(os.path.basename(dep))

    return dep_identified

#读缓冲
def read_buffer_line(f):
    line_buf = ""
    while not f.channel.exit_status_ready():
        line_buf += f.read(1)
        if line_buf.endswith('\n'):
            yield line_buf
            line_buf = ''

    line_buf += f.read()
    yield line_buf

#定义一个执行等待的方法，设置对象：description cmd wd ，当wd存在将cwd封装到wd
def wait_run(description, cmd, wd=""):
    print description
    if len(wd) != 0:
        p = Popen(cmd, stdout=PIPE, stderr=STDOUT, shell=True, cwd=wd)
    else:
        p = Popen(cmd, stdout=PIPE, stderr=STDOUT, shell=True)
    #
    while p.poll() is None:
        print p.stdout.readline(),

    print p.stdout.read()
    return p.returncode

#定义获取文件路径的方法
def get_file_path_relative(root_path):
    paths = []
    rootBase = os.path.basename(root_path)
    for root, dirs, files in os.walk(root_path):
        relative_root = os.path.join(rootBase, root[len(root_path) + len(os.path.sep):])
        for f in files:
            paths.append((os.path.abspath(os.path.join(root, f)), os.path.join(relative_root, f)))
    return paths

#定义远程等待执行 方法
def remote_wait_run(ssh, cmd):
    stdin, stdout, sterr = ssh.exec_command(cmd)

    for l in read_buffer_line(stdout):
        print l,
    ret = stdout.channel.recv_exit_status()

    return ret

#定义写压缩文件 方法
def write_zip_file(z, file_path, relative_path):
    print "Writing " + file_path + " to " + relative_path + "..."
    z.write(file_path, relative_path)

#定义编译方法
def compile_all(root_path, out_path, debug_compile, debug_backup):
    projects = utils.get_project_paths(root_path)

    print "Runnable projects: \n\t" + reduce(lambda x, y: os.path.abspath(x) + "\n\t" + os.path.abspath(y), projects)

    if debug_compile and wait_run("Cleaning...", "mvn -T4 clean", root_path) != 0:
        exit()

    if debug_compile and wait_run("Packaging...", "mvn -T4 -Dmaven.test.skip=true install", root_path) != 0:
        exit()

    exts = []
    jars = []
    wars = []
    dependencies = []
    for project_path in projects:

        pom_path = os.path.join(project_path, "pom.xml")
        if not os.path.exists(pom_path):
            continue

        target_folder = os.path.join(project_path, "target")
        dependencies_folder = os.path.join(target_folder, "lib")

        file_path = utils.get_ext(target_folder)

        if file_path is not None:
            deps = utils.get_dependencies(dependencies_folder)
            exts.append((file_path, deps))
            dependencies += deps
        else:
            file_path = utils.get_war(target_folder)
            if file_path is not None:

                if debug_compile and wait_run("Packaging war packages...",
                                              "mvn -f " + war_deploy_pom_file + " -Dmaven.test.skip=true install",
                                              project_path) != 0:

                    print "Missing " + war_deploy_pom_file + " of web project " + project_path
                    continue

                deps = utils.get_dependencies(dependencies_folder)
                dependencies += deps
                wars.append((file_path, deps))
            else:
                file_path = utils.get_jar(target_folder)

                if file_path is not None:
                    deps = utils.get_dependencies(dependencies_folder)
                    jars.append((file_path, deps))
                    dependencies += deps
                else:
                    continue

        src_path = file_path
        tar_path = os.path.join(out_path, os.path.basename(file_path))

        if not debug_backup:
            continue
        # back up
        if os.path.exists(tar_path):
            print "backing up...%s > %s" % (tar_path, tar_path + "." + time_stamp + ".backup")

            with open(tar_path + "." + time_stamp + ".backup", "wb") as back_file, open(tar_path, "rb") as tar_file:
                back_file.write(tar_file.read())
        else:
            if not os.path.exists(os.path.dirname(tar_path)):
                os.makedirs(os.path.dirname(tar_path))

        print "copying...%s > %s" % (src_path, tar_path)
        with open(tar_path, "wb") as back_file, open(src_path, "rb") as tar_file:
            back_file.write(tar_file.read())

    return jars, wars, exts, dependencies

#定义打包文件方法
def package_files(jars, wars, exts, dependencies, out_path, config_id, config_dir, config_type, extension_dir, debug_compile_extensions):
    # pack jars

    zip_path = os.path.abspath(os.path.join(out_path, "vwvo" + config_id + ".zip"))
    if os.path.exists(zip_path):
        os.remove(zip_path)
    else:
        try:
            os.mkdir(os.path.dirname(zip_path))
        except:
            pass

    z = zipfile.ZipFile(zip_path, mode="w", compression=zipfile.ZIP_STORED)

    for dep in dependencies:
        write_zip_file(z, dep, "lib/" + os.path.basename(dep))

    for jar, xxxxx in jars:
        write_zip_file(z, jar, os.path.basename(jar))

    for war, xxxxx in wars:
        write_zip_file(z, war, os.path.basename(war))

    for config_file in get_file_path_relative(config_dir):
        if os.path.basename(config_file[0]) == "vwconfig.root":
            tmp_config_root_path = out_path + "/vwconfig.root"

            with open(tmp_config_root_path, "wb") as tmp_file, open(config_file[0], "rb") as origin_file:
                tmp_file.write(origin_file.read())

            utils.modify_root_config(tmp_config_root_path, config_type)
            write_zip_file(z, tmp_config_root_path, config_file[1])

        else:
            write_zip_file(z, config_file[0], config_file[1])

    # if not compiling extensions, copy extensions from specified folder.
    if not debug_compile_extensions:
        for config_file in get_file_path_relative(extension_dir):
            write_zip_file(z, config_file[0], config_file[1])
    else:
        for ext, xxxxx in exts:
            write_zip_file(z, ext, os.path.join(os.path.basename(extension_dir), os.path.basename(ext)))

    z.close()
    return zip_path

#scp类
class ScpProgress:
    def __init__(self, total_size):
        self.total_size = total_size
        self.sent_size = 0
        self.last_time = time.time()

    def progress(self, file_name, total, progress):
        if (total == 0):
            self.last_time = time.time()

        now_time = time.time()

        if (now_time - self.last_time >= 1):
            speed = (progress - self.sent_size) / (now_time - self.last_time)
            self.last_time = now_time
            self.sent_size = progress
            sys.stdout.write(file_name + "    %s/%s   %s/s    %f%%   \r" % (
                utils.sizeof_fmt(progress),
                utils.sizeof_fmt(self.total_size),
                utils.sizeof_fmt(speed),
                (float(self.sent_size) / float(self.total_size)) * 100))
            sys.stdout.flush()

        if (progress == self.total_size):
            print ""
            print "Done."
            self.sent_size = progress
            return

#定义上传方法
def upload_files(local_path, remote_folder, wars, host, user, password, debug_upload):

    # upload
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(policy=paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=host, username=user, password=password)
    ssh_client.load_system_host_keys()

    if debug_upload:
        remote_wait_run(ssh_client, "rm -rf " + remote_folder)
        remote_wait_run(ssh_client, "mkdir -p " + remote_folder)

        remote_zip_path = remote_folder + "/" + os.path.basename(local_path)
        progress = ScpProgress(os.stat(local_path).st_size)
        scp_client = scp.SCPClient(ssh_client.get_transport(), progress=progress.progress)

        print "Uploading files..."
        scp_client.put(local_path, remote_zip_path)

        # unzip
        remote_wait_run(ssh_client, "unzip " + remote_zip_path + " -d" + remote_folder)

        for war, war_dep in wars:

            tmp_dir = "/tmp/vwvo_war_deploy"
            tmp_lib_dir = tmp_dir + "/WEB-INF/lib"
            remote_wait_run(ssh_client, "rm -rf " + tmp_dir)
            remote_wait_run(ssh_client, "mkdir -p " + tmp_lib_dir)
            remote_war = remote_folder + "/" + os.path.basename(war)

            print "Updating " + os.path.basename(war)
            for dep in war_dep:
                remote_wait_run(ssh_client, "cp -v " + remote_folder + "/lib/" + os.path.basename(dep) + " " + tmp_lib_dir)

            remote_wait_run(ssh_client, "cd " + tmp_dir + " && jar uf " + remote_war + " WEB-INF/lib/*")

    return ssh_client

#定义jars的执行方法
def exec_jars(ssh, jars, remote_folder, debug_run_jars):

    if not debug_run_jars:
        return

    scp_client = scp.SCPClient(ssh.get_transport())
    scp_client.put(os.path.dirname(os.path.abspath(__file__)) + "/start.sh", remote_folder)
    remote_wait_run(ssh, "ps -ef | grep \'java -jar vwvo-\'| grep -v grep | awk \'{print $2}\' | xargs kill -9")

    for jar, xxxxx in jars:
        jar_name = os.path.basename(jar)
        pos = re.search(r'-[0-9]', jar_name)
        log_name = jar_name[:pos.start()]

        remote_wait_run(ssh, "/bin/sh " + remote_folder + "/start.sh " + remote_folder + " " + os.path.basename(jar) + " " + log_name + ".log")

#定义wars执行方法
def exec_wars(ssh, wars, war_configs, remote_folder, apache_package, debug_run_wars):

    if not debug_run_wars:
        return

    scp_client = scp.SCPClient(ssh.get_transport())
    scp_client.put(os.path.dirname(os.path.abspath(__file__)) + "/kill_tomcat.sh", remote_folder)

    remote_wait_run(ssh, "/bin/sh " + remote_folder + "/kill_tomcat.sh")

    app_folder = apache_package + "/webapps"
#kill 不掉 tomcat，后边的删除app_folder也没执行
    remote_wait_run(ssh, "rm -rf " + app_folder + "/*")

    #remote_lib_folder = remote_folder + "/lib"

    for war, war_deps in wars:
        war_name = os.path.basename(war)
        war_key = war_name[:war_name.find("-0.0.1-SNAPSHOT")]
        print war_key

        if war_key not in war_configs:
            print "Invalid war package, couldn't find webapp folder name: " + war_name
            continue
        war_folder = war_configs[war_key]["folder"]
           #未来要放在/home/services/apache-tomcat-8.5.15/webapps/的所有子项目目录
        remote_war = remote_folder + "/" + war_name
          #/home/services/vwvo/里边的war文件
        war_folder = app_folder + "/" + war_folder
          #/home/services/apache-tomcat-8.5.15/下的war文件  
        #lib_folder = war_folder + "/WEB-INF/lib"

        config_xml_path = war_folder + "/WEB-INF/classes/config/w、eb_service_config.xml"
        config_xml_content = "\"<?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\"?><WebServiceConfig><configPath>" + remote_folder + "</configPath></WebServiceConfig>\""

#创建tomcat的目录，将war文件移到此文件
        remote_wait_run(ssh, "mkdir " + war_folder + " && cd " + war_folder + " && jar -xvf " + remote_war + " && echo " + config_xml_content + " >" + config_xml_path)

        #remote_wait_run(ssh, "mkdir -p " + lib_folder)
        #for dep in war_deps:
        #    remote_wait_run(ssh, "cp " + remote_lib_folder + "/" + os.path.basename(dep) + " " + lib_folder + "/" + os.path.basename(dep))
        
        #启动tomcat
    remote_wait_run(ssh, "/bin/sh " + apache_package + "/bin/startup.sh")
