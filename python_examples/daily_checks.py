#!/usr/bin/env python

import platdorm
import os
import subprocess
import sys

from time import strftime


def clear_screen():
    if os.name == "posix":
        os.system('clear')
    elif os.name in ("nt", "dos", "ce"):
        os.system('CLS')

def print_docs():
    print ("Printing Daily Check Sheets:")
    # The command below passes the command line string to open word, open the document, print it then close word down
    subprocess.Popen(["C:\\Program Files (x86)\Microsoft Office\Office14\winword.exe", 
                      "P:\\\\Documentiong\\Daily Docs\\Back office Daily Checks.doc", 
                      "/mFilePrintDefault",
                      "/mFileExit"]).communicate()

def putty_sessions(conffilename):
    for server in open(conffilename):
        subprocess.Popen(('putty -load '+server))

def rdp_sessions():
    print ("Loading RPD Sessions:")
    subprocess.Popen("mstsc eclr.rdp")

def euroclear_docs():
    # The command below opens IE and loads the EUROclear password document
    subprocess.Popen('"C:\\Program Files\\Internet Explorer\\iexplore.exe"'
                     '"file://fs1\pub_Pub_Admin\Documention\Settlements_Files\PWD\Eclr.doc"')

def main():
    filename = sys.argv[0]
    confdir = os.getenv("my_config")
    conffile = ('daily_checs_server.conf')
    conffilename = os.path.join(confdir, conffie)
    clear_screen()

    print ("Good Mornig " + os.getenv('USERNAME') + ", "+
           filename, "ran at", strftime("%Y-%m-%d %H:%M:%S"), "on",platform.node(), "run from",os.getcwd())

    print_docs()
    putty_sessions(conffilename)
    rdp_sessions()
    euroclear_docs()

if __name__ == "__main__":
    main()
