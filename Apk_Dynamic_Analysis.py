import os
from Connection import *
import sys
import subprocess


########### adb installation ###########

def installation(apk):
    command=" adb shell cmd activity get-current-user" 
    output=subprocess.check_output(command, shell=True)
    c=""
    userID=str(output)
    print(userID[2:len(userID)-3])
    push="adb push "+apk+" /data/local/tmp"
    os.system(push)
    install = "adb shell pm install --user "+userID[2:len(userID)-3]+" /data/local/tmp/bootevent.apk"
    os.system(install)

apk="/home/osboxes/Desktop/bootevent.apk"
#installation(apk)

############# adb running ###########

def running():
    print("Not yet!")

############### Network Traffic #################
def capture(android_ip):
    os.system("sudo apt install tcpdump ")
    capture=" sudo tcpdump -i eth0 -c5 -nn host "+android_ip
    os.system(capture)
#capture("10.224.138.248")
###############################################

def capture0(android_ip):

    try:
        
        capture="sudo tcpdump -i eth0 -c5 -nn -XX src "+android_ip
        if (os.system(capture))!=0:
            raise Exception
    
    except :
        print("tcpdump is not installed!")
        

capture0("10.224.138.248")
