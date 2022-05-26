from datetime import date,time
import time
import os
import system
from write_report import *


 
date=str(date.today())

time0=str(time.time())
myfile=date+"_"+time0+"_report.txt"
command="touch "+myfile
os.system(command)
with open(myfile, "w") as f:
    f.write("Hello world!")

    Title=""
    while Title=="":
        Title=input("\n Give a title to your work ")
    f.write("\nProject title: "+Title)
    First_name=""
    while First_name=="":
        First_name=input("\nFirst Name : ")
    f.write("\nFirst Name : "+First_name)

    Last_name=""
    while Last_name=="":
        Last_name=input("\nLast Name : ")
    f.write("\nLast Name : "+Last_name)
    Gmail=""
    while Gmail=="":
        Gmail=input("\nYour Mail:  ")
    f.write("\nEmail :"+Gmail)
