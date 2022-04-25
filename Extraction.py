
import os
import sys
import time
from termcolor import colored
import subprocess
from androguard.core.bytecodes import apk
from tabulate import tabulate
import pandas as pd

#####################

def overview():
    print("")
    print(colored("====================================================================================================================================================================================================",'green'))
    print(colored("===================Here is an Overview of the system================================================================================================================================================",'green'))
    print("")
    time.sleep(1)
    print(os.system(" adb shell ls "))

####################################################################################
#################Function that gives more details about a directory#################

def more_details():
    try:
        Directory_name = input("==================Please chose the directory you want to get more details about it : ")
        if os.system("adb shell ls -l -R /"+Directory_name) !=0:
            raise Exception("")
        else:
            print("Here are more details about the content of: "+Directory_name)
    except:
        print(colored('ERROR:Please tap the right name of the directory!','red'))

###################################################################################
def default_extraction():
    try:
        command= "adb shell scp / osboxes@10.224.138.190:/home/osboxes"
        if (os.system(command))!=0:
            raise Exception()
        else:
            print(colored("Extraction succeded!",'green'))
    except:
        print("Make sure you have enough free space!")
    
#########Error: We need an incrementer to name images + a variable for image to extract

def extraction(file,i):

    try:

        command="adb shell 'dd if="+file+"' > X"+str(i)+".img"
        if os.system(command) != 0:
            raise Exception('Make sure that the name of the file to extract is correct')  

    except:
        print(colored('ERROR:Make sure that the name is correct and that you have enough space in your machine!','red'))

extraction("/dev/block/loop15000000",1)#This is just a test!
