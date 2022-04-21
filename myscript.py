import os
import sys
import time
from termcolor import colored
import subprocess
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
def display():
    print()
    command= "adb shell getprop ro.build.version.release"
    command1= "adb shell getprop ro.product.model"
    Product_model = subprocess.check_output(command1, shell=True)
    version = subprocess.check_output(command,shell=True)
    print("Phone Information: " )
    print("version : "+colored(str(version)[2:-3], 'green'))
    print("Product Model : "+colored(str(Product_model)[2:-3],'green'))
display()    
########################This is an Introduction of the Framework###################

def introduction():
    
    print(colored("========================Welcome to Hence Framework for Mobile Forensics============================",'blue'))
    print(colored("===================================================================================================",'blue'))

    print(colored("===================================================================================================",'blue'))
    print(colored("Before starting the extraction, make sure that: ",'blue'))

def verification():    
    print(colored("1-Your device and your machine are connected in the same network ",'green'))
    print(colored("2-Mode USB Debbuging enabled in your phone",'green'))
    print(colored("3-The Device and The Machine can ping each other.",'green'))
    print(colored("4-The Device is rooted!",'green'))
    

####################################################################################
#################Function that gives an overview of the system######################

def overview():
    print("")
    print(colored("====================================================================================================================================================================================================",'green'))
    print(colored("===================Here is an Overview of the system================================================================================================================================================",'green'))
    print("")
    time.sleep(3)
    print(os.system(" adb shell ls "))

###################################################################################
#################Function that gives more details about a directory################

def more_details():
    try:
        Directory_name = input("==================Please chose the directory you want to get more details about it : ")
        if os.system("adb shell ls -l -R /"+Directory_name) !=0:
            raise Exception("")
        else:
            print("Here are more details about the content of: "+Directory_name)
    except:
        print(colored('ERROR:Please tap the right name of the directory!','red'))
more_details()

####################################################################################
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

    package = input(colored("==Please enter the application package name you want to extract : ",'green'))
    command2 = "adb shell pm path "+package 
    output = subprocess.check_output(command2, shell=True)    
    path=""
    path=(str(output))[10:len(output)+1]
    command3 = "adb pull "+path+" osboxes@10.224.138.182:/home/osboxes/"   
    os.system(command3)
    print(output,path)
    


####################################################################################

####################################################################################
var = os.system(" hostname -I | awk '{print $1}' ")
print(var)


#introduction()
#verification()
#connection()
#overview()
extract_apk()



#print(os.system("adb shell ls -l -R /data/data "))
#List_Of_Partition = Partition.split()

#print(List_Of_Partition)

####################################User Choice################################################

#Here we give the choice to the analyst to choose
#This condition is set to manage user input!

condition = "0"

while condition =="0":


    print("---------------If you want to extract a file, please tap 1---------------")
    print("---------------If you want more details about files tap 2----------------")
    choice = input ("Please tap the number of your choice : ")
    
    print(choice)

    if choice == "1":

        Path= input("Please select the absolute path of the file you want to extract :  ")
        condition = 1
        
    else:

        print("else")

        #com = "ip "+var
#dir = os.system(com)
#print(com)
#####################################################Static Analysis###################################################################################
