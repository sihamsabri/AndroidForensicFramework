import os
from datetime import *
import sys
from androguard.core.bytecodes import apk
import subprocess

################Installation###################
def installation(apk):

    command=" adb shell cmd activity get-current-user"
    output=subprocess.check_output(command, shell=True)
    c=""
    userID=str(output)
    print(userID[2:len(userID)-3])
    push="adb push "+apk+" /data/local/tmp"
    os.system(push)
    l=apk.split("/")
    install=" adb shell pm install --user "+userID[2:len(userID)-3]+" /data/local/tmp/"+l[len(l)-1]
    os.system(install)
#installation("/home/osboxes/Framework/bootevent.apk")

MyApk="/home/osboxes/Framework/bootevent.apk"

###############package#####################
def package_apk(MyApk):
    package=""
    a=apk.APK(MyApk)
    return a.get_package()

################pid#######################
def pid(MyApk):
    package_name=package_apk(MyApk)
    command="adb shell pidof "+package_name
    pid=""
    pid=str(subprocess.check_output(command,shell=True))
    return pid[2:len(pid)-3]

#################syscalls#####################
def system_calls(MyApk):
    pID=pid(MyApk)
    command="adb shell strace -p "+pID+" -c"
    os.system(command)
#system_calls(MyApk)

#############dump#############################
def dump(MyApk):
    
    print("Memory Usage")
    command=" adb shell dumpsys appops --package "+package
    command0=" adb shell dumpsys meminfo "+package
    os.system(command0)

#dump(MyApk)

################cpuinfo#######################
def cpu_information():
    os.system("adb shell dumpsys cpuinfo")

###############battery_usage#################
def battery_information(MyApk):
    package_name=package_apk(MyApk)
    command=" adb shell dumpsys batterystats --charged "+package_name
    os.system(command)

##############proc stat#######################
def proc_information(MyApk):
    package_name=package_apk(MyApk)
    command="adb shell dumpsys procstats --hours 3 "+package_name
    os.system(command)

##############Detailed Package information####
def package_Detailed_Information(MyApk):
    package_name=package_apk(MyApk)
    command="adb shell dumpsys package "+package_name
    os.system(command)

#######################Network Traffic: 10 packets by default!##################
def network_capture(android_ip):
    #try:
    date=str(datetime.now())
    fil="capture"+date+".pcap"
    os.system(("touch "+fil))
    capture = "sudo tcpdump -i eth0 -c10 -nn -XX src "+android_ip
    output =subprocess.check_output(capture,shell=True)
    os.system(("echo "+str(output)+" >> "+fil))
    #if (
    capture="sudo tcpdump "
    os.system(capture)

#network_capture("10.224.138.42")

################################################################################
