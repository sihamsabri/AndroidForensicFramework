
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
    print(colored("====================================================================================================================================================",'green'))
    print(colored("===================Here is an Overview of the system================================================================================================",'green'))
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
        else:
            print("image X",i,".img ",colored(" Extracted !!!",'yellow'))
    except:
        print(colored('ERROR:Make sure that the name is correct and that you have enough space in your machine!','red'))

#extraction("/dev/block/loop15000000",1)#This is just a test!
#default_extraction()

#################################################

def extract_apk():

    command1 = "adb shell pm list packages | cut -d ':' -f2 "
    print("")
    print(colored(">==================================================================================================================<",'green'))
    print(colored(">=======<Here a full list of application packages : >==============================================================<",'green'))
    print(colored(">==================================================================================================================<",'green'))
    print("")
    time.sleep(3)
    os.system(command1)
    print("")

    try:

        package = input(colored("==Please enter the application package name you want to extract : ",'green'))
        command2 = "adb shell pm path "+package 
        output = subprocess.check_output(command2, shell=True)    
        path=""
        path=(str(output))[10:len(output)+1]
        command3 = "adb pull "+path+" ~ "  
        os.system(command3)

    except:

        print("ERROR : It seems that you did not tap the right name of the pacakge!")
        print(colored("ERROR DETAILS: ",'yellow'), sys.exc_info())
        print(output,path)

####################Code############################

j = 1
Choice = 0
ext = True
while ext == True :

    print(colored("\n>========================<Extraction Options: >==============<\n",'green'))
    print(colored(" [1] => Default Extraction : The whole system will be extracted \n",'white'))
    print(colored(" [2] => Extraction : You can choose which directory to extract \n",'white'))
    print(colored(" [3] => Extract an APK file \n",'white'))
    print(colored(" [0] => To come back to home options \n",'white'))

    try: 

        Choice = int(input(colored("Tap the number of your choice : \n",'green')))
    
        if Choice == 1:
            print(colored(" Your Choice => [1]: Default Extraction ",'yellow'))
            default_extraction()
            ext = True

        elif Choice == 2:

            i=1
            while i!=0:
                overview()
                more_details()
                qst = input("\n => To go to Extraction Tap 1 !  \n")
                if qst=="1":
                    print(colored("!!! Go To Extraction !!!",'yellow'))
                    To_extract=str(input(colored("Tap the full path of the part you want to extract : ",'yellow')))
                    extraction(To_extract,j)
                    j=j+1
                    qst1=input("\n => To continue with details and Extraction tap 1: ")
                    if qst1 == "1":
                        i=1
                    else:
                        i=0
                        ext = True
                else:
                    i=1
                    print(colored("!!! More Details !!!",'yellow'))
            
            print(colored("\n ==> Finished With Detailed Extraction !!!\n",'yellow'))
            ext = True

        elif Choice == 3:
            j=1
            while j!=0:

                extract_apk()
                print(colored("!!! Apk Extracted !!!",'yellow'))
                qst= input("\n => To Continue with Apk Extraction Tap 1: ")
                if qst =="1":
                    j=1
                else:
                    j=0
                    print(colored("\n ==> Going Home Page ==> \n",'yellow'))
                    ext = True

        elif Choice == 0:
            print("home")
            ext = False
        else: 
            print(colored("\n => !!! The available options are : [0], [1], [2], and [3]. There is no option for :",'yellow'), Choice, "\n")

    except ValueError :

        print(colored("\n !!! SYNTAX ERROR : Please Tap the right number of the option from the list below !!! \n",'yellow'))
        ext = True
        
            





