import deploy
import os
import utils
import sys

###定义参数、引用config.json文件
#检查文件名字是否存在
if __name__ != "__main__":
    pass
#定义、列出活动的远程主机
activateRemotes = sys.argv[1:]

print "Activate remotes: {}" % activateRemotes

#没有活动的主机，退出
if len(activateRemotes) == 0:
    print "No activate remotes, exit."
    exit(0)
#定义config方法
config = utils.get_config("config.json")

print config
    #定义源代码、临时文件夹 使用config.json中的路径
source_folder = config["source_folder"]
temp_folder = config["temp_folder"]

        #检查源代码文件路径
if not os.path.exists(source_folder):
    print "Invalid source paths."
    exit(1)
    #定义配置文件、扩展文件路径、war包路径
config_path = config["config_folder"]
extension_path = config["extension_folder"]

war_configs = config["war_configs"]
    #debug相关定义
debug_compile = config["debug"]["compile"]
debug_compile_extensions = config["debug"]["compile_extensions"]
debug_backup = config["debug"]["backup"]
debug_upload = config["debug"]["upload"]
debug_run_jars = config["debug"]["run_jars"]
debug_run_wars = config["debug"]["run_wars"]


###编译程序###
#使用deploy的compile_all 操作
jars, wars, exts, deps = deploy.compile_all(source_folder, temp_folder, debug_compile, debug_backup)

###检查、配置远程服务器###
#使用config.json来配置
for remote in config["remotes"]:

    remote_id = remote["id"]

    if remote_id not in activateRemotes:
        continue

    remote_config_type = remote["config_type"]

    remote_host = remote["host"]
    remote_user = remote["user"]
    remote_password = remote["password"]

    remote_folder = remote["folder"]
    remote_apache_package = remote["apache_package"]

    remote_jars = jars
    remote_wars = wars
    remote_exts = exts
    #检查忽略(使用config.json utils.py中的函数）
    if "excludes" in remote:
        remote_excludes = remote["excludes"]
        #关于项目和正则匹配的忽略
        exclude_projects = []
        exclude_regexs = []

        for include in remote_excludes:
            if include["type"] == "regex":
                exclude_regexs.append(include["value"])
            elif include["type"] == "full_match":
                exclude_projects += include["value"]

        remote_jars = [(jar_path, jar_dep) for jar_path, jar_dep in jars if
                       not utils.match_regexs(exclude_regexs, os.path.basename(jar_path)) and
                       not utils.match_projects(exclude_projects, jar_path)]

        remote_wars = [(war_path, war_dep) for war_path, war_dep in wars if
                       not utils.match_regexs(exclude_regexs, os.path.basename(war_path)) and
                       not utils.match_projects(exclude_projects, war_path)]
    elif "includes" in remote:
        remote_includes = remote["includes"]

        include_projects = []
        include_regexs = []

        for include in remote_includes:
            if include["type"] == "regex":
                include_regexs.append(include["value"])
            elif include["type"] == "full_match":
                include_projects += include["value"]

        remote_jars = [(jar_path, jar_dep) for jar_path, jar_dep in jars if
                       utils.match_regexs(include_regexs, os.path.basename(jar_path)) or
                       utils.match_projects(include_projects, jar_path)]

        remote_wars = [(war_path, war_dep) for war_path, war_dep in wars if
                       utils.match_regexs(include_regexs, os.path.basename(war_path)) or
                       utils.match_projects(include_projects, war_path)]

###安装前准备、引用deploy中的函数进行打包上传等###
#定义 解决依赖、打包文件、通过ssh上传文件
    dep_identified = deploy.resolve_dependencies(remote_jars, remote_wars, remote_exts, deps)

    zipFile = deploy.package_files(remote_jars, remote_wars, remote_exts, dep_identified, temp_folder, remote_id,
                                   config_path, remote_config_type, extension_path, debug_compile_extensions)

    ssh = deploy.upload_files(zipFile, remote_folder, remote_wars, remote_host, remote_user, remote_password, debug_upload)
###执行安装、引用deploy中的函数进行安装###
    deploy.exec_jars(ssh, remote_jars, remote_folder, debug_run_jars)

    deploy.exec_wars(ssh, remote_wars, war_configs, remote_folder, remote_apache_package, debug_run_wars)
