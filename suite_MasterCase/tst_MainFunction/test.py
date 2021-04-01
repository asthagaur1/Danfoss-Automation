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
    #test.log("inside initialize funcation")
    source(findFile("scripts", "global.py"));
    source(findFile("scripts", "Functions.py"));
    source(findFile("scripts", "Actions.py"));
    try:
        print "Current working dir : %s" % os.getcwd()
        print "Current working dir 2: %s" % os.getcwdu()

        for d in deviceidlist: #making all the device in disbled stat
            #test.log("before disable the port")
            os.popen(DevManView+"\DevManView.exe /disable "+d)
            
    except exceptions.Exception, e:
        #test.log("inside except1")
        test.log("Error occurred in %s" % (e))
        #test.log("after error message")

# def testcontrollers(devicelist):
#     for dev in devicelist:
#         os.popen(DevManView+"\DevManView.exe /enable "+dev)
#         startApplication("KoolProg")
#         snooze(3)
#         mouseClick(waitForObject("{container=':KoolProg_Window' name='imgServicetest' type='Image'}"), MouseButton.PrimaryButton)
#         snooze(30) 
#         cashWidget = waitForObject("{name='txtProuctName' type='Label'}") 
#         controllername = cashWidget.text
#         os.popen(DevManView+"\DevManView.exe /enable "+dev)
#         snooze(2)
#         startApplication("KoolProg")
#          mouseClick(waitForObject(":KoolProg.System.Windows.Controls.Image_Button_9"), MouseButton.PrimaryButton)
#          waitForObject(":Settings_Window")
#          mouseClick(waitForObject(":Settings.CAN Baudrate:_ComboBox"), MouseButton.PrimaryButton)
#          type(waitForObject(":Settings.CAN Baudrate:_ComboBox"), "Auto")
#          type(waitForObject(":Settings.CAN Baudrate:_ComboBox"), "<Return>")
#          snooze(2)
#          Baudrate_Combobox = ":Settings.CAN Baudrate:_ComboBox"
#          test.compare(waitForObject(Baudrate_Combobox).nativeObject.Text, "Auto","PASS")
#          snooze(2)
#          mouseClick(":Settings.Save_Button"), MouseButton.PrimaryButton
#          mouseClick(waitForObject(":MessageBoxDisplay.OK_Button"), MouseButton.PrimaryButton)      
#           snooze(3)
#           mouseClick(waitForObject(":KoolProg_Image_3"), MouseButton.PrimaryButton)
#           snooze(30) 
#           cashWidget = waitForObject("{name='txtProuctName' type='Label'}")
#           controllername = cashWidget.text
#          if "ETC" in controllername:
#              controllername=controllername[0:3]+" "+controllername[3:6]
#          elif "EKE" in controllername:
#              controllername=controllername[0:3]
#         test.log(controllername)
#         snooze(30)
#         #clickButton(waitForObject(":KoolProg.System.Windows.Controls.Image_Button"))
#         snooze(2)
#         #test.log("1")
#         #os.popen(r"Taskkill /IM KoolProg.exe /F")
#         #snooze(2)
#         #test.log("2")
#         #startApplication("KoolProg")
# #        snooze(5)
#         #test.log("3")
# #         ##COMMON TEST CASES##
# #         d=r"C:\gitworkspace\KoolProg-TestAutomation"       
# #         foldername="CommonTestcases"
# #         k=[]
# #         k=os.listdir(d)
# #         for ke in k:
# #             if foldername in ke:
# #                 test.log(foldername)
# #                 q=os.path.join(d,ke)
# #                 test.log(q)
# #                 for t in os.listdir(q):
# #                     if "tst_" in t:
# #                         global a
# #                         a = os.path.join(q, t)
# #                         test.log(a)
# #                         source(os.path.join(q, t,"test.py"))
# #                         try:
# #                             eval("main()") # Executes the source'd test case's main() function
# #                         except exceptions.Exception, e:
# #                             test.log("Error occurred in test case: %s: %s" % (q, e))
# #                             os.popen(r"Taskkill /IM KoolProg.exe /F")
# #                             snooze(4)
# #                             #startApplication("KoolProg")
# #                             snooze(3)#             else: 
# #                     test.log("Folder not found")   
# #         snooze(4)
# #         os.popen(r"Taskkill /IM KoolProg.exe /F")
# #         snooze(2)
# #         #clickButton(waitForObject(":MessageBoxDisplay.OK_Button"))
# #         os.popen(DevManView+"\DevManView.exe /disable "+dev) 
#         
#         ##CONTROLLER SPECIFIC TEST CASES##
#         d=SourceCode_Directory
#         #startApplication("KoolProg")
#         #controllername="CommonTestcases"
#         controllername="suite_EETa 2W" 
#         test.log(controllername)
#         
#         k=[]
#         k=os.listdir(d)
#         for ke in k:
#             if controllername in ke:
#                 test.log(controllername)
#                 q=os.path.join(d,ke)
#                 test.log(q)
#                 for t in os.listdir(q):
#                     if "tst_Open" in t:
#                         global a 
#                         snooze(3)
#                         a = os.path.join(q, t)
#                         test.log(a)
#                         source(os.path.join(q, t,"test.py"))
#                         try:
#                             #test.log("inside the try1")
#                             eval("main()") # Executes the source'd test case's main() function
#                             #est.log("inside the try")
#                         except exceptions.Exception, e:
#                             #test.log("inside the except")
#                             test.log("Error occurred in test case: %s: %s" % (q, e))
#                             os.popen(r"Taskkill /IM KoolProg.exe /F")
#                             snooze(4)
#                             startApplication("KoolProg")
#                             #test.log("inside the except end")
#                             snooze(3)
#                     else: 
#                         test.log("Folder not found")   
#         snooze(4)
#         os.popen(r"Taskkill /IM KoolProg.exe /F")
#         snooze(2)
#         #clickButton(waitForObject(":MessageBoxDisplay.OK_Button"))
#         os.popen(DevManView+"\DevManView.exe /disable "+dev) 
#         
        
def testcontrollers(devicelist):
    #test.log("inside the testcontrollers function")
    for dev in devicelist:
        #test.log("before enable the port first time")
        os.popen(DevManView+"\DevManView.exe /enable "+dev)
        snooze(2)
        d=SourceCode_Directory
        #test.log("before start the application first time")
        startApplication("KoolProg")
        #folder_name="CommonTestcases"
        #folder_name="suite_EETa 2W"
        folder_name="suite_ERC112D"
        #test.log("before clicking on service and test")
#         mouseClick(waitForObject(":KoolProg_Image_3"), MouseButton.PrimaryButton)
#         snooze(30) 
#         cashWidget = waitForObject("{name='txtProuctName' type='Label'}")
#         controllername = cashWidget.text
#         #test.log(controllername)
#         snooze(30)
#         #test.log("before clicking on home button")
#         clickButton(waitForObject(":KoolProg.System.Windows.Controls.Image_Button"))
#         snooze(5)
        #test.log("before killing the application on service and test")
        os.popen(r"Taskkill /IM KoolProg.exe /F")
        snooze(5)
        #test.log("before the starting the application after service and test")
        startApplication("KoolProg")
        snooze(10)
          
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
#         d=SourceCode_Directory
#         startApplication("KoolProg")
#         controllername="CommonTestcases"
        #controllername="suite_EETa 2W" 
        
        k=[]
        k=os.listdir(d)
        for ke in k:
            if folder_name in ke:
                #test.log(controllername)
                test.log(folder_name)
                q=os.path.join(d,ke)
                test.log(q)
                for t in os.listdir(q):
                    #test.log("inside the for3")
                    if "tst_Unit_Conversion" == t:
                        #test.log("inside the if")
                        global a 
                        snooze(3)
                        a = os.path.join(q, t)
                        test.log(a)
                        source(os.path.join(q, t,"test.py"))
                        try:
                            #test.log("inside the try2")
                            eval("main()") # Executes the source'd test case's main() function
                        except exceptions.Exception, e:
                            #test.log("inside the except2")
                            #test.log("before error message")
                            test.log("Error occurred in test case: %s: %s" % (q, e))
                        
                        #test.log("before kill the application after excuting the tset case")    
                        os.popen(r"Taskkill /IM KoolProg.exe /F")
                        snooze(4)
                        #test.log("start the application for new test case")
                        startApplication("KoolProg")
                        snooze(3)
                    else: 
                        test.log("Folder not found")  
                os.popen(r"Taskkill /IM KoolProg.exe /F")   
                startApplication("KoolProg")     
                 
        snooze(4)
        os.popen(r"Taskkill /IM KoolProg.exe /F")
        snooze(2)
        #clickButton(waitForObject(":MessageBoxDisplay.OK_Button"))
        os.popen(DevManView+"\DevManView.exe /disable "+dev)     
    
def main():  
    #test.log("inside the main")      
    devicelist=[r'"USB\VID_1E46&PID_000B&MI_05\6&27DE0A32&0&0005"']
    initialize(devicelist)
    snooze(5)
    testcontrollers(devicelist)
    
  
        

