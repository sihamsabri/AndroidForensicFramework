from dynamic import *
from write_report import *
from Connection import *
#from Apk_Dynamic_Analysis import *
#from Introduction import *
from Apk_static_Analysis import *
from Extraction import *
import os
import sys
import time
#from colored import fg, bg, attr
from termcolor import colored
from datetime import date,time
#import colored
import subprocess
from androguard.core.bytecodes import apk

####Code############################
#print ('%s%s Hello World !!! %s' % (fg('white'), bg('yellow'), attr('reset')))
UserChoice=""
Framework=True

while Framework:

    #Start Welcome
    print("\nWelcome to: \n")
    import os
    import time 

    from pyfiglet import Figlet

    f = Figlet(font='slant')
    word = ' Forensics Framework'
    curr_word = ''
    print (colored(f.renderText(word),'blue'))
    print("                                                         Copyright 2022 © By Henceforth \n")
    print("\n Here are The Options Offered By <",colored("-Forensics Framework-",'blue'),"> :\n")    
    time.sleep(1)
    #fin Welcome

    #Display Options
    print("\n",colored(" ===--->",'blue'),"[1] Extraction       ---> system extraction, Apk extraction, and memory dump \n")
    print("\n",colored(" ===--->",'blue'),"[2] Static Analysis  ---> from a given .apk file, you will be able to extract static characteristics such as permissions and their classification, signature, certificate, etc.\n")
    print("\n",colored(" ===--->",'blue'),"[3] Dynamic Analysis ---> runs an .apk file in a sandbox and extract its traces in the system such as network capture, CPU Usage, Battery stats, etc. \n")
    print("\n",colored(" ===--->",'blue'),"[0] Exit \n")
    print(colored("\n< NB : This Framework is for Android Systems >\n",'yellow'))
    time.sleep(1)
    print("Before starting please fill in your information to add to the final report of the forensics analysis ")

    #= Create a file + Add Reporter Information to the report
    time.sleep(1)
     
    date=str((date.today()))

    time0=str(time.time())
    myfile=date+"_"+time0+"_report.txt"
    command="touch "+myfile
    os.system(command)
    with open(myfile, "w") as f:
        f.write("======Forensics Report======")
        f.write(colored("\n ******** General Information ********",'green'))
        Title=""
        while Title=="":
            Title=input("\n Give a title to your work ")
        f.write(colored("\n\nProject title: ",'yellow')+Title)
        First_name=""
        while First_name=="":
            First_name=input("\nFirst Name : ")
        f.write(colored("\n\nFirst Name : ",'yellow')+First_name)

        Last_name=""
        while Last_name=="":
            Last_name=input("\nLast Name : ")
        f.write(colored("\n\nLast Name : ",'yellow')+Last_name)
        Gmail=""
        while Gmail=="":
            Gmail=input("\nYour Mail:  ")
        f.write(colored("\n\nEmail :",'yellow')+Gmail)
        date_time=str(datetime.now())
        f.write(colored("\n\nDate and time of investigation: ",'yellow')+date_time)

    #Give hand to the user to choose

    while UserChoice=="":
        UserChoice=input("\n\nPlease Choose your Option Number ! ")
    if UserChoice =="2":

        print("!!! Static Analysis !!!")
        Static=True

        while Static==True:
            Apk=""
            try:

                while Apk=="":
                    Apk=input("!!! Please Enter the whole path of your APK !!!")
                with open(myfile, "a") as f:
                    f.write("\n")
                    result=Permissions_Classification(Apk)
                    f.write(result)
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
        period=""
        while period=="":
            period=input(colored("\n Please enter the period of the dynamic analysis (in secondes)\n ",'yellow'))
        
        add=""
        try:

            while add=="":
                add=input("please enter your emulator address!")
            print(colored("\n !!!Connection!!! \n",'yellow'))
            connection(add)
            apk=""
            while apk=="":
                apk=input("Please enter the whole path of your Apk file to be intstalled : ")
            print(colored("\n !!!Installation!!! \n",'yellow'))
            installation(apk)
            #print(colored("\n ==<Information About the Installed Package>== \n",'yellow'))
            print(colored("\n ===---===---===---===---===---===---===---===---===---===",'blue'))
            print(colored(" ===---===---===Captures will start after ===---===---=== ",'green'),period,"secondes ")
            print(colored(' ===---===---===---===---===---===---===---===---===---===\n','blue'))
            time.sleep(int(period))
        
            print(colored("\n ===---=== Information About The Installed Package ===---===\n",'yellow'))
            time.sleep(4)
            package_Detailed_Information(apk)
            print(colored("\n !!! Memory Usage !!!\n",'yellow'))
            time.sleep(4)
            dump(apk)
            print(colored("\n !!! CPU Information !!! \n",'yellow'))
            time.sleep(4)
            cpu_information()
            print(colored("\n !!! Battery Usage By The Application !!! \n",'yellow'))
            time.sleep(4)
            battery_information(apk)
            print(colored("\n !!! Processes Stattus !!! \n",'yellow'))
            time.sleep(4)
            proc_information(apk)
            print(colored("\n !!! Network Capture !!! \n",'yellow'))
            time.sleep(4)
            network_capture(add)
            Framework=False

        except:
            print("Emulator not found!")
            Frameework=False

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
    elif UserChoice=="0":
        print("finished!")
        Framework=False
    else: 
        print("\n\nThere is no option for ",UserChoice)
        UserChoice=""
        Framework=True
        print("\n\n !!!Wait!!! \n")
        time.sleep(4)
