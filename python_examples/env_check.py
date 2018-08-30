'''
This script will check to see if all of the enviroment variables I require are set.
'''

import os

confdir = os.getenv("my_config")    #Set the variable confdir from the OS environment variables
conffile = 'env_check.conf'         #Set the variable conffile
conffilename = os.path.join(confdir, conffile)  #Set variable conffilename by joining confdir and conffile together

for env_check in open(conffilename):
    env_check = env_check.strip()
    print '[{}]'.format(env_check)
    newenv = os.getenv(env_check)

    if newenv is None:
        print env_check, 'is not set'
    else:
        print 'Current Setting for {}=[]\\n'.format(env_check, newenv)
