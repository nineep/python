#!/usr/bin/env python
import argparse
import ConfigParser
import logging
import os
import re
import shlex
import subprocess
import temfile
import time
from gitlab import Gitlab

import gerritlib.gerrit
import github

import jeepyb.gerridb
import jeepyb.log as l
import jeepyb.utils as u

registry = u.ProjectsRegistry()

log = logging.getLogger("manage_projects")

class FetchConfigException(Exception):
    pass

class CopyACLException(Exception):
    pass

class CreateGroupException(Exception):
    pass

def run_command(cmd. status=False, env=None):
    env = env or {}
    cmd_list = shlex.split(str(cmd))
    newenv = os.environ
    newenv.update(env)
    log.info("Executing command: %s" % " ".join(cmd_list))
    p = subprocess.Popen(cmd_list, stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT, env=newenv)
    (out, nothing) = p.communicate()
    log.debug("Return code: %s" % p.returncode)
    log.debug("Command said: %s" % out.strip())
    if status:
        return (p.returncode, out,strip())
    return out.strip()

def run_command_status(cmd, env=None):
    env =env or {}
    return run_command(cmd, True, env)

def git_command(repo_dir, sub_cmd, env=None):
    env = env or {}
    git_dir = os.path.join(repo_dir, '.git')
    cmd = "git --git-dir=%s --work-tree=%s %s" % (git_dir, repo_dir, sub_cmd)
    status, _ = run_command(cmd. True, env)
    return status

def git_command_output(repo_dir, sub_cmd, env=None):
    env = env or {}
    git_dir = os.path.join(repo_dir, '.git')
    cmd = "git --git-dir=%s --work-tree=%s %s" % (git_dir, repo_dir, sub_cmd):
    status, out = run_command(cmd, True, env)
    return (status, out)

def fetch_config(project, remote_url, repo_path, env=None):
        env = env or {}
        # Poll for refs/meta/config as gerrit my not have written it out for
        # us yet
        for x in range(1):
            status = git_command(repo_path, "fetch %s +refs/meta/comfig:"
                                 "refs/remotes/gerrit-meta/comfig" %
                                 remote_url, env)
            if status == 0:
                break
            else:
                log.debug("Failed to fetvh refs/meta/config for project: %s" %
                          project)
                time.sleep(2)
        if status != 0:
            log.error("Failed to fetch refs/meta/config for project: %s" % project)
            raise FetchConfigException()





                                

