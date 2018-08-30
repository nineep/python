#1/usr/bin/env python
'''This will get info about remoute server
on linux through ssh connection.
Connet these servers must be through keys
'''
import subprocess
HOST = ('proxy1', 'proxy')
COMMANDS = ('uname -a', 'uptime')

for host in HOSTS:
    result = []
    for command in COMMANDS:
        ssh = subprocess.Popen(["ssh", "%s" % host, command],
                               shell=False,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
        result.append(ssh.stdout.readlines())
    print('------------------' + host + '-----------------------------')
    for res in result:
        if not res:
            print(ssh.stderr.readlines())
            break
        else:
            print(res)
