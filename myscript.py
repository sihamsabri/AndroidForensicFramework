import os
import sys
import time
from termcolor import colored
import subprocess
from androguard.core.bytecodes import apk

#from tabulate import tabulate
#import pandas as pd

#######################

def Certificate_Validation():
    apk="/home/osboxes/96462df95b266d6f775967e5aa798d09.apk"   
    command = "jarsigner -verify -verbose -certs "+apk
    output = subprocess.check_output(command, shell=True) 
    C=""
    limit=str(output)
    position=limit.index("jar verified")
    C=limit[position:-3]
    L=list(str(C).split("\\n"))
    for elm in L :
        print(elm)

Certificate_Validation()

#########################################

def test_androguard():
    permissions=[]
    Dangerous_Permissions = [ 'ACCESS_NETWORK_STATE','READ_CALENDAR','INTERNET', 'WRITE_CALENDAR', 'CAMERA', 'READ_CONTACTS', 'WRITE_CONTACTS', 
                            'RECORD_AUDIO', 'READ_PHONE_NUMBERS', 'CALL_PHONE', 'ANSWER_PHONE_CALLS', 'SEND_SMS'] 

    Normal_Permissions = ['ACCESS_NOTIFICATION_POLICY', 'ACCESS_WIFI_STATE', 'BLUETOOTH', 'BLUETOOTH_ADMIN', 'INTERNET', 
                        'KILL_BACKGROUND_PROCESSES', 'MANAGE_OWN_CALLS', 'MODIFY_AUDIO_SETTINGS', 'SET_ALARM', 'SET_WALLPAPER', 'VIBRATE']
    
    a = apk.APK("/home/osboxes/96462df95b266d6f775967e5aa798d09.apk")
    pk_name = a.get_package()
    L = a.get_permissions() 

    for elm in L:
        permissions.append(elm[19:])
    LN=[]
    LD=[]
    for elm in permissions:
        if elm in Dangerous_Permissions:
            LD.append(elm)
        else:
            LN.append(elm)
    print(colored("\n>========Full list of permissions: ",'green'),"\n\n  ",permissions)        
    print(colored("\n>========Normal Permissions : ",'yellow'))
    i=1
    for elm in LN:
        print("\n ",i,"=>",elm)
        i=i+1
    j=1
    print(colored("\n>========Dangerous Permissions : ",'red'))
    for elm in LD:
        print("\n ",j,"=>",elm) 
        j=j+1
    print("")
    
test_androguard()
####################################Extraction##############################################
####################################Connection##############################################

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

##################################################################################
def display_options():

    print("")
    print(colored(">===============================================================================================<",'blue'))
    print(colored(">==========================<Here are the options of the framework>==============================<",'green'))
    print(colored(">===============================================================================================<\n",'blue'))
    print(colored("  [1] : Default Extraction (The framework will extract the whole system of the phone)\n",'green'))
    print(colored("  [2] : Configured Extraction (You can choose which part to extract)\n",'green'))
    print(colored("  [3] : Extract an apk file\n",'green'))
    print(colored("  [4] : Static Analysis => Extract Static Characteristics of an apk\n",'green'))
    print(colored("  [5] : Static Analysis => Reverse Engineer an apk\n",'green'))
    print(colored("  [6] : Dynamic Analysis\n",'green'))
    print(colored(">================================================================================================<",'blue'))
    print(colored(">================================================================================================<",'green'))
    print(colored(">================================================================================================<\n",'blue'))
    option=input(colored("  => To choose an option, tap its number : ",'yellow'))
    print(colored("",'green'))
    print(colored("",'green'))
    print(colored("",'green'))


#################################################################################
def display_info():

    print()
    command= "adb shell getprop ro.build.version.release"
    command1= "adb shell getprop ro.product.model"
    Product_model = subprocess.check_output(command1, shell=True)
    version = subprocess.check_output(command,shell=True)
    print("Phone Information: " )
    print("version : "+colored(str(version)[2:-3], 'green'))
    print("Product Model : "+colored(str(Product_model)[2:-3],'green'))

   
########################This is an Introduction of the Framework###################

def introduction():

    print("")
    print(colored(">================================================================================================<",'blue'))    
    print(colored(">========================Welcome to Hence Framework for Mobile Forensics=========================<",'green'))
    print(colored(">================================================================================================<\n",'blue'))
    #print(colored(">==================================================================================================<",'blue'))
    print(colored("Before starting, make sure that: \n",'green'))

def verification():    
    print(colored(" [1] => Your device and your machine are connected in the same network;\n",'green'))
    print(colored(" [2] => Mode USB Debbuging enabled in your phone;\n",'green'))
    print(colored(" [3] => The Device and The Machine can ping each other;\n",'green'))
    print(colored(" [4] => The Device is rooted!\n",'green'))
    print(colored(" [4] => You installed the tools indicated in requirements.txt file.\n",'green'))
    print(colored(" [5] => An emulator/virtual machine(ip address) in case you want to do dynamic analysis.\n",'green'))
    print(colored(" NB: The requirements [1],[2],[3], and [4] are necessary just for extraction! ",'yellow'))
    
introduction()
verification()
display_options()

####################################################################################
#################Function that gives an overview of the system######################

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

########################Code########################################################

def extract_apk():

    command1 = "adb shell pm list packages | cut -d ':' -f2 "
    print("")
    print(colored("========================================================================================================================================================================================================",'green'))
    print(colored("=======Here a full list of application packages : ======================================================================================================================================================",'green'))
    print(colored("========================================================================================================================================================================================================",'green'))
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
    


####################################################################################

####################################################################################
var = os.system(" hostname -I | awk '{print $1}' ")
print(var)


#introduction()
#verification()
#connection()
#overview()
#extract_apk()



#print(os.system("adb shell ls -l -R /data/data "))
#List_Of_Partition = Partition.split()

#print(List_Of_Partition)

####################################User Choice################################################

#Here we give the choice to the analyst to choose
#This condition is set to manage user input!

condition = "0"


        #com = "ip "+var
#dir = os.system(com)
#print(com)
#####################################################Static Analysis#################
