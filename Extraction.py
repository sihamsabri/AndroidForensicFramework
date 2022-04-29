import os
import sys
import time
from termcolor import colored
import subprocess



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

##############################################

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
    
###############################################

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
            
######################################################

