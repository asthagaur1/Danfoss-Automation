import glob, os
import csv
from random import randint
import random
import __builtin__
import datetime
import json
from pprint import pprint
import shutil
import string
import xdrlib
import codecs
from distutils.util import strtobool

def main():
    startApplication("KoolProg")
    waitForObject(":Settings_Window")
    mouseClick(waitForObject(":Settings.CAN Baudrate:_ComboBox"), MouseButton.PrimaryButton)
    type(waitForObject(":Settings.CAN Baudrate:_ComboBox"), "250K")
    type(waitForObject(":Settings.CAN Baudrate:_ComboBox"), "<Return>")
    snooze(2)
    Baudrate_Combobox = ":Settings.CAN Baudrate:_ComboBox"
    test.compare(waitForObject(Baudrate_Combobox).nativeObject.Text, "250K","PASS")
    snooze(2)
    mouseClick(":Settings.Save_Button"), MouseButton.PrimaryButton
    mouseClick(":MessageBoxDisplay.OK_Button"), MouseButton.PrimaryButton
    os.popen(r"Taskkill /IM KoolProg.exe /F")
    
    
    mastercase_path = r"C:\gitworkspace\TestAutomation-AKCC5XX\Test_Automation\SourceCode\suite_AK-CC_mastercase"
    for t in os.listdir(mastercase_path):
        if "tst_MainFunction_AKCC" in t:
            global a
            a = os.path.join(mastercase_path, t)
            test.log(a)
            source(os.path.join(mastercase_path, t,"test.py"))
            try:
                eval("main()") # Executes the source'd test case's main() function
            except exceptions.Exception, e:
                test.log("Error occurred in test case: %s: %s" % (q, e))
                            
                            
                            
                            
                            