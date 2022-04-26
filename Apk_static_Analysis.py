import os
import sys
import time
from termcolor import colored
import subprocess
from androguard.core.bytecodes import apk
from tabulate import tabulate
import pandas as pd

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

Certificate_Validation()
##########################################################################

def test_androguard():

    permissions=[]

    Dangerous_Permissions = ['READ_CALENDAR','WRITE_CALENDAR','CAMERA','READ_CONTACTS','WRITE_CONTACTS','GET_ACCOUNTS','ACCESS_FINE_LOCATION',
                            'ACCESS_COARSE_LOCATION','RECORD_AUDIO','READ_PHONE_STATE','READ_PHONE_NUMBERS','CALL_PHONE','ANSWER_PHONE_CALLS',
                            'READ_CALL_LOG','WRITE_CALL_LOG','ADD_VOICEMAIL','USE_SIP','PROCESS_OUTGOING_CALLS','BODY_SENSORS','SEND_SMS',
                            'RECEIVE_SMS','READ_SMS','RECEIVE_WAP_PUSH','RECEIVE_MMS','READ_EXTERNAL_STORAGE','WRITE_EXTERNAL_STORAGE',
                            'ACCESS_MEDIA_LOCATION','ACCEPT_HANDOVER','ACCESS_BACKGROUND_LOCATION','ACTIVITY_RECOGNITION']

    Normal_Permissions = ['ACCESS_LOCATION_EXTRA_COMMANDS','ACCESS_NETWORK_STATE','ACCESS_NOTIFICATION_POLICY','ACCESS_WIFI_STATE','BLUETOOTH',
                            'BLUETOOTH_ADMIN','BROADCAST_STICKY','CHANGE_NETWORK_STATE','CHANGE_WIFI_MULTICAST_STATE','CHANGE_WIFI_STATE','DISABLE_KEYGUARD',
                            'EXPAND_STATUS_BAR','GET_PACKAGE_SIZE','INSTALL_SHORTCUT','INTERNET','KILL_BACKGROUND_PROCESSES','MODIFY_AUDIO_SETTINGS','NFC',
                            'READ_SYNC_SETTINGS','READ_SYNC_STATS','RECEIVE_BOOT_COMPLETED','REORDER_TASKS','REQUEST_IGNORE_BATTERY_OPTIMIZATIONS',
                            'REQUEST_INSTALL_PACKAGES','SET_ALARM','SET_TIME_ZONE','SET_WALLPAPER','SET_WALLPAPER_HINTS','TRANSMIT_IR','UNINSTALL_SHORTCUT',
                            'USE_FINGERPRINT','VIBRATE','WAKE_LOCK','WRITE_SYNC_SETTINGS']
    
    a = apk.APK("/home/osboxes/Framework/96462df95b266d6f775967e5aa798d09.apk")
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
