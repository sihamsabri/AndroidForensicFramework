import os
import sys

#This line is for adb connection;

####################################Connection###############################################

add = sys.argv[1]
com = "adb connect "+add
comand = os.system(com)
print(comand)
#Start adb as root
#We should have an exeption in case the device was not rooted!

print(os.system("adb root"))

#connect with shell
#print(os.system("adb shell"))
####################################Display System#############################################

#We display the whole partition to the analyst to choose the file to extract
Partition = os.system("adb shell ls")
print(os.system("adb shell ls -l "))
List_Of_Partition = Partition.split()

print(List_Of_Partition)

####################################User Choice################################################

#Here we give the choice to the analyst to choose
#This condition is set to manage user input!

condition = "0"

while condition =="0"


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
