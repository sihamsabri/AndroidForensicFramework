
import os
import sys
import time
from termcolor import colored
import subprocess
from androguard.core.bytecodes import apk
from tabulate import tabulate
import pandas as pd

def connection():
    try:
        
        add=sys.argv[1]
        com = "adb connect "+add
        if os.system(com)!=0:
            raise Exception("")
        else:
            print(colored("Connection succeded!",'green'))
            
    except:
        print(colored("Failed to connect to device!",'red'))
        
    #Start adb as root
    #We should have an exeption in case the device was not rooted!
    try:
        if os.system("adb root")!=0:
            raise Exception()
    except:
        print(colored("The phone is not rooted! It should be already rooted ",'red'))
