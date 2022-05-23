
import os
import sys
import time
from termcolor import colored
import subprocess
from androguard.core.bytecodes import apk
from tabulate import tabulate
import pandas as pd

def connection(add):
    try:
        
        #add=sys.argv
        com = "adb connect "+add
        if os.system(com)!=0:
            raise FailedConnection()
        else:
            print(colored("",'green'))
            
    except FailedConnection:
        print(colored("Failed Connection!",'red'))
        
    #Start adb as root
    #We should have an exeption in case the device was not rooted!

    try:
        if os.system("adb root")!=0:
            raise Exception()
    except:
        print(colored("",'red'))
##############
def connection0():
    
    output=str(subprocess.check_output("adb connect 10.224.138.31", shell=True))
    connected="connected to"
    failed="failed"
    if connected in output:
        print(colored("Connection Succeded => "+output[2:len(output)-3],'green'))
    elif failed in output:
        print(colored("Failed Connection => "+output[2:len(output)-3],'red'))

def connect_to_root():
    connection0()
    root="cannot run as root"
    output=str(subprocess.check_output("adb root", shell=True))
    if root in output:
        print(colored("Ooops Your phone is not rooted !",'red'))
    else:
        print(colored("=> "+output[2:len(output)-3],'green'))

#connect_to_root()
