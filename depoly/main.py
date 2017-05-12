import deploy
import os
import utils
import sys

if __name__ != "__main__":
    pass

activateRemotes = sys.argv[1:]

print "Activate remotes: {}" % activateRemotes

if len(activateRemotes) == 0:
    print "No activate remotes, exit."
    exit(0)

config = utils.get_config("config.json")

print config

source_folder = config["source_folder"]
temp_folder = config["temp_folder"]

if not os.path.exists(source_folder):
    print "Invalid source paths."
    exit(1)

config_path = config["config_folder"]
extension_path = config["extension_folder"]

war_configs = config["war_configs"]

debug_compile = config["debug"]["compile"]
debug_compile_extensions = config["debug"]["compile_extensions"]
debug_backup = config["debug"]["backup"]
debug_upload = config["debug"]["upload"]
debug_run_jars = config["debug"]["run_jars"]
debug_run_wars = config["debug"]["run_wars"]

jars, wars, exts, deps = deploy.compile_all(source_folder, temp_folder, debug_compile, debug_backup)


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
    if "excludes" in remote:
        remote_excludes = remote["excludes"]

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

    dep_identified = deploy.resolve_dependencies(remote_jars, remote_wars, remote_exts, deps)

    zipFile = deploy.package_files(remote_jars, remote_wars, remote_exts, dep_identified, temp_folder, remote_id,
                                   config_path, remote_config_type, extension_path, debug_compile_extensions)

    ssh = deploy.upload_files(zipFile, remote_folder, remote_wars, remote_host, remote_user, remote_password, debug_upload)

    deploy.exec_jars(ssh, remote_jars, remote_folder, debug_run_jars)

    deploy.exec_wars(ssh, remote_wars, war_configs, remote_folder, remote_apache_package, debug_run_wars)





