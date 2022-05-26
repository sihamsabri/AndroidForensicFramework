import os
import sys
import time
from termcolor import colored
import subprocess
from androguard.core.bytecodes import apk
#from tabulate import tabulate
#import pandas as pd

###########################################################################

def Certificate_Validation():
    apk="/home/osboxes/Framework/96462df95b266d6f775967e5aa798d09.apk"   
    command = "jarsigner -verify -verbose -certs "+apk
    output = subprocess.check_output(command, shell=True) 
    C=""
    limit=str(output)
    position=limit.index("jar verified")
    C=limit[position:-3]
    L=list(str(C).split("\\n"))

    for elm in L :
        print(elm)

#Certificate_Validation()
##########################################################################
 
MyApk="/home/osboxes/Desktop/bootevent.apk"

def Permissions_Classification(MyApk):


    
    a = apk.APK(MyApk)
    D=a.get_details_permissions()
    mylist=""
    for i in D:
        mylist=mylist+"\n => "+colored(str(i[19:]),'green')+" : "+str(D[i])+" \n"
    result=colored("\n\n************** Static Analysis **************\n\n",'green')+colored("\n\n APK Validation ",'yellow')+str((a.is_valid_APK()))+colored("\n\n App name: ",'yellow')+str((a.get_app_name()))+colored("\n\n PAckage name : ",'yellow')+str((a.get_package()))+colored("\n\n This apk contains the following files: ",'yellow')+str((a.get_files()))+colored("\n\n<===> Detailed Description of Permissions: <===>\n\n",'yellow')+str(mylist)+colored("\n\n Activities : ",'yellow')+str((a.get_activities()))+colored("\n\n Android Version Code ",'yellow')+str((a.get_androidversion_code()))+colored("\n\n Android Version name ",'yellow')+str((a.get_androidversion_name()))+colored("\n\n Libraries: ",'yellow')+str((a.get_libraries()))+colored("\n\n Main Activities :",'yellow')+str((a.get_main_activity()))+colored("\n\n Receivers: ",'yellow')+str((a. get_receivers()))+colored("\n\n Permissions of third party apps: ",'yellow')+str((a.get_requested_third_party_permissions()))+colored("\n\n Services: ",'yellow')+str((a.get_services()))+colored("\n\n Signature :",'yellow')+str((a.get_signatures()))+colored("\n\n Does the app require touch screen? ",'yellow')+str((a.is_androidtv()))+colored("\n\n The app is build for TV? ",'yellow')+str((a.is_leanback()))+colored("\n\n The App is Signed? ",'yellow')+str((a. is_signed()))
    #print("")
    return(result)

#print(Permissions_Classification(MyApk))
#####################
def dump(MyApk):
    package=""
    a=apk.APK(MyApk)
    package=a.get_package()
    command="adb shell dumpsys appops --package "+package
    os.system(command)
#dump(MyApk)

