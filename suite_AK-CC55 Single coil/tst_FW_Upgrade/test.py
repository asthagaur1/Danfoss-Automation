def main():
    excel = "FW_Upgrade.xls"
    source(findFile("scripts", "Functions.py"));
    source(findFile("scripts", "Actions.py"));
    #Mapping with Global scripts for Function library and key action.
    keyAction(excel)
         

# import glob, os
# import csv
# from random import randint
# import random
# import __builtin__
# import datetime
# import json
# from pprint import pprint
# import shutil
# import string
# import xdrlib
# import codecs
# from distutils.util import strtobool
# from zipfile import ZipFile
# import zipfile
# from os import path
# 
# gControl=None
# 
# def getControl(control,type,name):
#    global gControl    
#    if(control["type"] == type and control["name"] == name):
#        print("inside match")    
#        gControl=control            
#        return gControl
#    else:
#        #print("inside else")
#        children=object.children(control)
#        if(children != None):
#            for child in children:            
#                gControl=getControl(child,type,name)                                        
#    return gControl# 
# def Before_File_Select():
#     Home_Button_Enable = waitForObject("{container=':KoolProg_Window' name='btnHome' type='Button'})").enabled
#     if (Home_Button_Enable == True):
#         Browse_Button_Enabled= waitForObject("{container=':KoolProg_Window' name='btnfilebrowse' text='BROWSE' type='Button'}").enabled
#         test.log("Browse button enabled? - "+str(Browse_Button_Enabled))
#         Start_Enabled = waitForObject("{container=':KoolProg_Window' name='btnUpdate' type='Button'}").enabled
#         test.log("Start button before selecting file is? - "+str(Start_Enabled))
#         Single_Multiple_Enabled = waitForObject("{container=':KoolProg_Window' text='Single or multiple controller programming:' type='Label'}").enabled
#         test.log("Single or Multiple controller programming before selecting a file is? - "+str(Single_Multiple_Enabled))
#         FW_Upgrade_Browse()
# 
# def FW_Upgrade_Browse():
#     ##.cbk file and location##
#     mouseClick()
# 
# def Open_File_Path(symbolicname, value):
#     waitForObject(symbolicname)
#     mouseClick("{container=':_Pane' type='Toolbar'}")
#     Open_File_Path = ("{container=':_Pane' type='Toolbar'}").text
#     Open_File_Path = Open_File_Path.replace("Address: ", "")
#     path_result = test.compare(value,Open_File_Path)
#     if (path_result == True):
#         snooze(2)
#     else:
#         type(waitForObject("{container=':_Pane' type='Toolbar'}"), value)
#         type(waitForObject("{container=':_Pane' type='Toolbar'}"), "<Return>")
#         
        
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    