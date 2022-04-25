
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
        os.system("adb root")
        command= "adb pull /system/ /home/osboxes/ "
        if (os.system(command))!=0:
            raise Exception()
        else:
            print(colored("Extraction succeded!",'green'))
    except:
        print(" E Make sure you have enough free space!")
    
########################################

def extraction(file,i):

    try:

        command="adb shell 'dd if="+file+"' > X"+str(i)+".img"
        if os.system(command) != 0:
            raise Exception('Make sure that the name of the file to extract is correct')  

    except:
        print(colored('ERROR:Make sure that the name is correct and that you have enough space in your machine!','red'))

#extraction("/dev/block/loop15000000",1)#This is just a test!
#default_extraction()

####################Code

ext = True
while ext == True :

    #print(colored(">============================================================<",'green'))
    #print(colored(">========================<Extraction>========================<",'green'))
    #print(colored(">============================================================<\n",'green'))

    print(colored(">========================<Extraction Options: >==============<\n",'green'))
    print(colored(" [1] => Default Extraction : The whole system will be extracted \n",'white'))
    print(colored(" [2] => Extraction : You can choose which directory to extract \n",'white'))
    print(colored(" [3] => Extract an APK file \n",'white'))
    print(colored(" [0] => To come back to home options \n",'white'))

    try: 

        Choice = int(input(colored("Tap the number of your choice : \n",'green')))
    
        if Choice == 1:
            print(colored(" Your Choice => [1]: Default Extraction ",'yellow'))
            default_extraction()
            ext = False

        elif Choice == 2:
            overview()
            more_details()
            #extraction(file,i)
            print("Choice 2")
            ext = False

        elif Choice == 3:
            print("Choice 3")
            ext = False

        elif Choice == 0:
            print("home")
            ext = False
        else: 
            print(colored("\n => !!! The available options are : [0], [1], [2], and [3]. There is no option for :",'yellow'), Choice, "\n")
    except ValueError :

        print(colored("\n !!! SYNTAX ERROR : Please Tap the right number of the option from the list below !!! \n",'yellow'))
        ext = True
        
            





