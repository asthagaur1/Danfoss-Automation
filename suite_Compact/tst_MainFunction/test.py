import os
import exceptions
import sys
import glob
import csv
import random
import __builtin__
import datetime

a = r""

def initialize(deviceidlist):  
    source(findFile("scripts", "global.py"));
    source(findFile("scripts", "Functions.py"));
    source(findFile("scripts", "Actions.py"));
    try:
        print "Current working dir : %s" % os.getcwd()
        print "Current working dir 2: %s" % os.getcwdu()

        for d in deviceidlist: #making all the device in disbled stat
            os.popen(DevManView+"\DevManView.exe /disable "+d)
    except exceptions.Exception, e:
            test.log("Error occurred in %s" % (e))

def testcontrollers(devicelist):
    for dev in devicelist:
        os.popen(DevManView+"\DevManView.exe /enable "+dev)
#         snooze(2)
#         startApplication("KoolProg")
#         #mouseClick(waitForObject(":KoolProg.System.Windows.Controls.Image_Button_9"), MouseButton.PrimaryButton)
#         waitForObject(":Settings_Window")
#         mouseClick(waitForObject(":Settings.CAN Baudrate:_ComboBox"), MouseButton.PrimaryButton)
#         type(waitForObject(":Settings.CAN Baudrate:_ComboBox"), "Auto")
#         type(waitForObject(":Settings.CAN Baudrate:_ComboBox"), "<Return>")
#         snooze(2)
#         Baudrate_Combobox = ":Settings.CAN Baudrate:_ComboBox"
#         test.compare(waitForObject(Baudrate_Combobox).nativeObject.Text, "Auto","PASS")
#         snooze(2)
#         mouseClick(":Settings.Save_Button"), MouseButton.PrimaryButton
#         mouseClick(waitForObject(":MessageBoxDisplay.OK_Button"), MouseButton.PrimaryButton)      
#         snooze(3)
#         mouseClick(waitForObject(":KoolProg_Image_3"), MouseButton.PrimaryButton)
#         snooze(30) 
#         cashWidget = waitForObject("{name='txtProuctName' type='Label'}")
#         controllername = cashWidget.text
#         if "ETC" in controllername:
#             controllername=controllername[0:3]+" "+controllername[3:6]
#         elif "EKE" in controllername:
#             controllername=controllername[0:3]
#         test.log(controllername)
#         snooze(30)
#         clickButton(waitForObject(":KoolProg.System.Windows.Controls.Image_Button"))
#         snooze(5)
#         os.popen(r"Taskkill /IM KoolProg.exe /F")
#         snooze(5)
#         startApplication("KoolProg")
#         snooze(10)
          
#         ##COMMON TEST CASES##
#         d=r"C:\gitworkspace\KoolProg-TestAutomation"       
#         foldername="CommonTestcases"
#         k=[]
#         k=os.listdir(d)
#         for ke in k:
#             if foldername in ke:
#                 test.log(foldername)
#                 q=os.path.join(d,ke)
#                 test.log(q)
#                 for t in os.listdir(q):
#                     if "tst_" in t:
#                         global a
#                         a = os.path.join(q, t)
#                         test.log(a)
#                         source(os.path.join(q, t,"test.py"))
#                         try:
#                             eval("main()") # Executes the source'd test case's main() function
#                         except exceptions.Exception, e:
#                             test.log("Error occurred in test case: %s: %s" % (q, e))
#                             os.popen(r"Taskkill /IM KoolProg.exe /F")
#                             snooze(4)
#                             #startApplication("KoolProg")
#                             snooze(3)#             else: 
#                     test.log("Folder not found")   
#         snooze(4)
#         os.popen(r"Taskkill /IM KoolProg.exe /F")
#         snooze(2)
#         #clickButton(waitForObject(":MessageBoxDisplay.OK_Button"))
#         os.popen(DevManView+"\DevManView.exe /disable "+dev) 
        
        
        ##CONTROLLER SPECIFIC TEST CASES##
        d=SourceCode_Directory
        startApplication("KoolProg")
        controllername="suite_AK-CC55 Compact"
        k=[]
        k=os.listdir(d)
        for ke in k:
            if controllername in ke:
                test.log(controllername)
                q=os.path.join(d,ke)
                test.log(q)
                for t in os.listdir(q):
                    if "tst_Json_Parsing_Process" == t:
                        global a 
                        snooze(3)
                        a = os.path.join(q, t)
                        test.log(a)
                        source(os.path.join(q, t,"test.py"))
                        try:
                            eval("main()") # Executes the source'd test case's main() function
                        except exceptions.Exception, e:
                            test.log("Error occurred in test case: %s: %s" % (q, e))
                            os.popen(r"Taskkill /IM KoolProg.exe /F")
                            snooze(4)
                            startApplication("KoolProg")
                            snooze(3)
                    else: 
                        test.log("Folder not found")   
        snooze(4)
        os.popen(r"Taskkill /IM KoolProg.exe /F")
        snooze(2)
        #clickButton(waitForObject(":MessageBoxDisplay.OK_Button"))
        os.popen(DevManView+"\DevManView.exe /disable "+dev)     
    
def main():        
    devicelist=[r'"USB\VID_0403&PID_6001\A603NQZQ"']
    initialize(devicelist)
    snooze(5)
    testcontrollers(devicelist)
    
  
        

