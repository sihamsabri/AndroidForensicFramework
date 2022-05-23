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
 
#MyApk="/home/osboxes/Desktop/bootevent.apk"

def Permissions_Classification(MyApk):


    
    a = apk.APK(MyApk)
    print(colored("\n APK Validation ",'yellow'),a.is_valid_APK())
    print(colored("\n App name: ",'yellow'),a.get_app_name())
    print(colored("\n PAckage name : ",'yellow'),a. get_package())
    print(colored("\n This apk contains the following files: ",'yellow'),a.get_files())

    print(colored("\n<===> Detailed Description of Permissions: <===>\n",'yellow'))
    D=a.get_details_permissions()
    for i in D :
        print(" => ",colored(i[19:],'green')," : ",D[i],"\n")

    print(colored("\n Activities : ",'yellow'),a.get_activities())
    print(colored("\n Android Version Code ",'yellow'),a.get_androidversion_code())
    print(colored("\n Android Version name ",'yellow'),a.get_androidversion_name())
    #print(a.get_effective_target_sdk_version())
    print(colored("\n Libraries: ",'yellow'),a.get_libraries())
    print(colored("\n Main Activities :",'yellow'),a.get_main_activity())
    print(colored("\n Receivers: ",'yellow'),a. get_receivers())
    print(colored("\n Permissions of third party apps: ",'yellow'),a.get_requested_third_party_permissions())
    print(colored("\n Services: ",'yellow'),a.get_services())
    print(colored("\n Signature :",'yellow'),a.get_signatures())
    print(colored("\n Does the app require touch screen? ",'yellow'),a.is_androidtv())
    print(colored("\n The app is build for TV? ",'yellow'),a.is_leanback())
    print(colored("\n The App is Signed? ",'yellow'),a. is_signed())
    print("")

#Permissions_Classification(MyApk)
#####################
def dump(MyApk):
    package=""
    a=apk.APK(MyApk)
    package=a.get_package()
    command="adb shell dumpsys appops --package "+package
    os.system(command)
#dump(MyApk)

