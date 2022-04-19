import os
import sys
import time
#This line is for adb connection;
####################################Connection###############################################

def connection():

    add=sys.argv[1]
    com = "adb connect "+add
    comand = os.system(com)
    print(comand)
    #Start adb as root
    #We should have an exeption in case the device was not rooted!
    print(os.system("adb root"))
    #connect with shell
    #print(os.system("adb shell"))
    #Partition = os.system("adb shell ls")

########################This is an Introduction of the Framework####################
def introduction():
    time.sleep(5)
    print("========================Welcome to Hence Framework for Mobile Forensics============================")
    print("===================================================================================================")
    print("===================================================================================================")
    time.sleep(5)
####################################################################################
#################Function that gives an overview of the system######################
def overview():
    print("===================Here is an Overview of the system===================")
    print(os.system(" adb shell ls "))

#################Function that gives more details about a directory#################
def more_details():
        Directory_name = input("==================Please chose the directory you want to get more details about it : ")
        print("Here are more details about the content of : "+Directory_name)
        print(os.system("adb shell ls -l -R /"+Directory_name))

####################################################################################
def extraction():
    os.system("")

########################Code########################################################
introduction()
connection()
overview=True
more=True

while 1:

    if overview:
        overview()
        overview=False
        
        if more:
            more_details()
            more=False
            print("If you want to continue with details tap: 1 ")
            continue = input()
            print("If you want to ")
            


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
