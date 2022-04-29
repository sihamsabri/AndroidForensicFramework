
from Apk_static_Analysis import Permissions_Classification
import os
import sys
import time
from termcolor import colored
import subprocess
from androguard.core.bytecodes import apk
#from tabulate import tabulate
#import pandas as pd

#####################

def overview():
    print("")
    print(colored("====================================================================================================================================================",'green'))
    print(colored("===================Here is an Overview of the system================================================================================================",'green'))
    print("")
    time.sleep(1)
    print(os.system(" adb shell ls "))


#################Function that gives more details about a directory#################

def more_details():
    try:
        Directory_name = ""
        while Directory_name =="":
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
        
        command= "adb pull /storage/ /home/osboxes/Framework "
        if (os.system(command))!=0:
            raise Exception()
        else:
            print(colored("Extraction succeded!",'green'))
    except:
        print(" E Make sure you have enough free space!")
    
########################################

def extraction(file):

    try:
        
        
        os.system("adb root")
        command="adb pull "+file+" /home/osboxes/Framework/ "
        #command="adb shell 'dd if="+file+"' > X"+str(i)+".img"

        if (os.system(command)) != 0:
            raise Exception('Make sure that the name of the file to extract is correct')  
        else:
            print(colored(" Extracted !!!",'yellow'))
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
    time.sleep(2)
    os.system(command1)
    print("")
    package=""
    try:
        
        while package == "" :
            package = str(input(colored("==> Please enter the right name of the package you want to extract ",'yellow')))
            
        command2 = "adb shell pm path "+package 
        output = subprocess.check_output(command2, shell=True)    
        path=""
        path=(str(output))[10:len(output)+1]
        command3 = "adb pull "+path+" /home/osboxes/Framework/ "  
        os.system(command3)
        print(colored("\n !!!!! APK Extracted , Check [/home/osboxes/Framework/] out !!! \n",'yellow'))
            

    except:

        print(colored("\n ERROR : It seems that you did not tap the right name of the pacakge!",'yellow'))
        print(colored("\n ERROR DETAILS: ",'yellow'), sys.exc_info())
            
####################Code############################
UserChoice=""
Framework=True

while Framework:

    print("\n [1] Extraction \n")
    print("\n [2] Static Analysis \n")
    print("\n [3] Dynamic Analysis \n")
    print("\n [0] Exit \n")

    while UserChoice=="":
        UserChoice=input("Please Choose your Option!")

    if UserChoice =="2":
        
        Static=True

        while Static==True:
            Apk=""
            try:

                while Apk=="":
                    Apk=input("!!! Please Enter the whole path of your APK !!!")
                Permissions_Classification(Apk)
                qst=""
                qst=input("\n => To continue with Static Analysis Tap 1 \n => Press Any Key To Exit\n")
                if qst=="1":
                    Static=True
                else:
                    Static=False
                    Framework=True
                    UserChoice=""
            except:
                print("!!! ERROR: !!!")
                Tap=input("Tap 0 To Exit !!!")
                if Tap=="0":
                    UserChoice=""
                    break

    elif UserChoice=="3":
        print("!!!Dynamic Analysis!!!")
        Framework=False

    elif UserChoice=="1":

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
                    print(colored(" Your Choice => [1] : Detailed Extraction \n",'yellow'))
                    i=1
                    while i!=0:
                        overview()
                        qst0=input(colored("\n => Tap 0 To back to Extraction Options \n => Press Any key To continue \n",'yellow'))

                        if qst0=="0":
                            break

                        else:

                            more_details()
                            qst = input(colored("\n => Tap 0 to back to Extraction Options \n => Tap 1 to extract a Directory  \n => Press any key to continue with phone details \n  ",'yellow'))
                            if qst=="1":
                                print(colored("!!! Going To Extraction !!!",'yellow'))
                                To_extract=""
                                while To_extract=="":
                                    To_extract=str(input(colored("Tap the full path of the part you want to extract : ",'yellow')))
                                extraction(To_extract)

                                qst1=input(colored("\n => Tap 1 To continue with details and Extraction :\n => Press Any key to back to Extraction Options \n",'yellow'))
                                if qst1 == "1":
                                    i=1
                                else:
                                    i=0
                                    ext = True
                            elif qst=="0":
                                break
                            else:
                                i=1
                                print(colored("!!! More Details !!!",'yellow'))

                    print(colored("\n ==> Finished With Detailed Extraction !!!\n",'yellow'))
                    ext = True

                elif Choice == 3:
                    print(colored(" Your Choice => [3] : Apk Extraction ",'yellow'))
                    m=1
                    while m!=0:

                        extract_apk()
                        #print(colored("!!! Apk Extracted , Check your current directory out !!!",'yellow'))
                        qst= input(colored("\n => Press Any key to back to Extraction Options \n => To Continue with Apk Extraction Tap 1: \n",'yellow'))
                        if qst =="1":
                            m=1
                        else:
                            m=0
                            print(colored("\n ==> Going Home Page ==> \n",'yellow'))
                            ext = True

                elif Choice == 0:
                    print("home")
                    UserChoice=""     
                    ext = False
                    break
                else:
                    print(colored("\n => !!! The available options are : [0], [1], [2], and [3]. There is no option for :",'yellow'), Choice, "\n")

            except ValueError :

                print(colored("\n !!! SYNTAX ERROR : Please Tap the right number of the option from the list below !!! \n",'yellow'))
                ext = True
                Framework=False
    else:
        print("finished!")
        Framework=False

