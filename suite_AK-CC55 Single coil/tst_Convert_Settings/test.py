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
from zipfile import ZipFile
import zipfile
from os import path

gControl=None

def getControl(control,type,name):
   global gControl    
   if(control["type"] == type and control["name"] == name):
       print("inside match")    
       gControl=control            
       return gControl
   else:
       #print("inside else")
       children=object.children(control)
       if(children != None):
           for child in children:            
               gControl=getControl(child,type,name)                                        
   return gControl

def main():
    source(findFile("scripts", "global.py"));
    SW_List_Offline =[]
      
    startApplication("KoolProg")
    mouseClick(waitForObject(":KoolProg_Image"))
    #mouseClick(waitForObject(":SetParameters_List"))
    Cdf_1 = Dependent_Files+r"\CDFs\Compact_1.50\edf\084B4081.cdf"
    json_1 = Dependent_Files+r"\CDFs\Compact_1.50\cdf\device.jso"
    Import(Cdf_1)
      
    Cdf_2 = Dependent_Files+r"\CDFs\Compact_1.70\edf\084B4081.cdf"
    json_2 = Dependent_Files+r"\CDFs\Compact_1.70\cdf\device.jso"
    Import(Cdf_2)
    SW_List_Offline = Create_New(json_1)
      
    window=waitForObject(":KoolProg_Window")
      
    name1=getControl(window,"Label","tbProductInfoValue0")  
    if(name1 == None):
        print "None"
        result = False
    else:    
        Controller_Name = (name1["text"])
          
    name2=getControl(window,"Label","tbProductInfoValue1")  
    if(name2 == None):
        print "None"
        result = False
    else:    
        Code_Number = (name2["text"])
          
    name3=getControl(window,"Label","tbProductInfoValue2")  
    if(name3 == None):
        print "None"
        result = False
    else:    
        SW_Version = (name3["text"])
                   
    Convert_Settings(Controller_Name,Code_Number, SW_Version, SW_List_Offline)
    mouseClick("{container=':ConvertSettingFile_Window' text='X' type='Button'}")
    snooze(2)
      
    File_Name = Project_Name()
    Database_Verify()
 
def Project_Name(): ##Project name test cases in convert settings##
    mouseClick(waitForObject("{container=':KoolProg_Window' name='btnConvSetfile' type='Button'}"))
    Initial_textBox = waitForObject("{class='System.Windows.Controls.TextBox' name='txtprojectName' type='Edit'}").text
    if (Initial_textBox == ""):
        Text = True
    else:
        Text= false
    
    test.log("Is Textbox empty initially? - " +str(Text))   
    ##Click on Convert settings without project name - Give OK##
    mouseClick("{container=':ConvertSettingFile_Window' text='CONVERT FILE' type='Button'}")
    snooze(2)
    waitForObject("{container=':MessageBoxDisplay_Window' text='Please Enter the ProjectName' type='Label'}")
    mouseClick("{container=':MessageBoxDisplay_Window' text='OK' type='Button'}")
    snooze(2)
    ##Click on Convert settings without project name - Give 'X'##
    mouseClick("{container=':ConvertSettingFile_Window' text='CONVERT FILE' type='Button'}")
    snooze(2)
    waitForObject("{container=':MessageBoxDisplay_Window' text='Please Enter the ProjectName' type='Label'}")
    mouseClick("{container=':MessageBoxDisplay_Window' text='X' type='Button'}")
    snooze(2)
    
    mouseClick(waitForObject("{class='System.Windows.Controls.TextBox' name='txtprojectName' type='Edit'}"))
    File_Name = "File_1"
    type(waitForObject("{class='System.Windows.Controls.TextBox' name='txtprojectName' type='Edit'}"), File_Name)
    mouseClick("{container=':ConvertSettingFile_Window' text='CONVERT FILE' type='Button'}")
    try:
        ##NO- Not overwriting file##
        mouseClick(waitForObject(":MessageBoxDisplay_Window"))
        snooze(2)
        mouseClick("{container=':MessageBoxDisplay_Window' text='NO' type='Button'}")
        mouseClick(waitForObject("{text='ConvertSettingFile' type='Window'}"))
        snooze(2)
        ##YES - overwriting file##
        type(waitForObject("{class='System.Windows.Controls.TextBox' name='txtprojectName' type='Edit'}"), File_Name)
        mouseClick("{container=':ConvertSettingFile_Window' text='CONVERT FILE' type='Button'}")
        mouseClick(waitForObject(":MessageBoxDisplay_Window"))
        snooze(2)
        mouseClick("{container=':MessageBoxDisplay_Window' text='YES' type='Button'}")
        snooze(10)
    except:   
        snooze(10)
        
    mouseClick(waitForObject(":MessageBoxDisplay.OK_Button"), MouseButton.PrimaryButton)
    
    window = waitForObject(":KoolProg_Window")
    name1=getControl(window,"Label","txtprojectFilename")  
    if(name1 == None):
        print "None"
        result = False
    else:    
        Project_File_Name = (name1["text"])
        
    FileName_Comparison= test.compare(str(File_Name)+".cbk" , Project_File_Name)
    if (FileName_Comparison == True):
        test.log("File name given in convert settings file is the same as project name after saving")
    else:
        test.log("File name given in convert settings file is NOT the same as project name after saving")
        
    return File_Name
   
def Convert_Settings(Controller_Name,Code_Number,SW_Version,  SW_List_Offline): ##SW Version test cases in convert settings##
    mouseClick(waitForObject("{container=':KoolProg_Window' name='btnConvSetfile' type='Button'}"))
    window = waitForObject(":ConvertSettingFile_Window")
    
    name1=getControl(window,"Label","tbProductInfoValue0")  
    if(name1 == None):
        print "None"
        result = False
    else:    
        ConvertSettings_ControllerName = (name1["text"])
        
    name2=getControl(window,"Label","tbProductInfoValue1")  
    if(name2 == None):
        print "None"
        result = False
    else:    
        ConvertSettings_CodeNumber = (name2["text"])
    
    test.compare(Controller_Name,ConvertSettings_ControllerName)
    test.log("Controller Name displayed offline and in Convert setting window are same") 
    
    test.compare(Code_Number, ConvertSettings_CodeNumber)
    test.log("Code Number displayed offline and in Convert setting window are same") 
    
    mouseClick(waitForObject(":ConvertSettingFile.Software version:_ComboBox"))
    SW_Combo = waitForObject(":ConvertSettingFile.Software version:_ComboBox")
    ConvertSetting_SW_List = parseForSW(SW_Combo)
    
    SW_Result = test.compare(SW_List_Offline,ConvertSetting_SW_List)
    if (SW_Result == False):
        test.log("SW versions displayed offline and in Convert setting window, are different or in a different order")
    else:
        test.log("SW Versions displayed offline and in Convert setting window are same")       

    mouseClick(waitForObject(":ConvertSettingFile.Software version:_ComboBox"))
    type(waitForObject(":ConvertSettingFile.Software version:_ComboBox"), SW_Version)
    #type(waitForObject(":ConvertSettingFile.Software version:_ComboBox"), "<Return>")
    snooze(5)
    Error_message = waitForObject(":ConvertSettingFile.*Select different Software version_Label").enabled
    test.log("Error message is enabled? - "+str(Error_message))
    snooze(2)
    #waitForObject("{container=':ConvertSettingFile_Window' text='CONVERT FILE' type='Button'}").enabled == "false"
    
    for i in range (0, len(ConvertSetting_SW_List)):
        if (ConvertSetting_SW_List[i] != SW_Version):
            SW = ConvertSetting_SW_List[i]
            mouseClick(waitForObject(":ConvertSettingFile.Software version:_ComboBox"))
            type(waitForObject(":ConvertSettingFile.Software version:_ComboBox"), SW)
            type(waitForObject(":ConvertSettingFile.Software version:_ComboBox"), "<Return>")
            Convert_Button = waitForObject("{container=':ConvertSettingFile_Window' text='CONVERT FILE' type='Button'}").enabled
            test.log("Convert settings button is enabled - ? - "+str(Convert_Button)) 
        break
   
def Import(CDF_Path):##Import two different CDF paths in the same controller name##
    mouseClick(waitForObject(":System.Windows.Controls.StackPanel.Import controller model_Label"))
    mouseClick(waitForObject(":Open_Dialog"), MouseButton.PrimaryButton) 
    
    mouseClick(waitForObject(":Open_Edit"), MouseButton.PrimaryButton)  
    snooze(2)
    type(waitForObject(":Open_Edit"), (CDF_Path))
    snooze(4)
    mouseClick(waitForObject(":Open.Open_Button"), MouseButton.PrimaryButton)
    snooze(30)
    mouseClick(waitForObjectExists(":MessageBoxDisplay.OK_Button"), MouseButton.PrimaryButton)

def Create_New(JSON_Path): ##Create project using one CDF. Convert it to another SW version in another function##
    mouseClick(waitForObject(":KoolProg_Image"))
    mouseClick(waitForObject(":System.Windows.Controls.DockPanel_ListItem"))
    
    tbl = waitForObjectExists(":Newproject_TabFolder")
    with codecs.open(findFile("testdata", JSON_Path),encoding='utf-8') as data_file:
       content = data_file.read()
       content = content.replace(u'\ufeff','') 
       data = json.loads(content)
       
       Parameter_Count = len(data["Parameters"])
       
       Headers = len(data["Header"])
       
       Code_Number = data["Header"]["Name"] ##ADD data["Header"]["CodeNumbers"] for CDF with more code numbers##
       Description = data["Header"]["Description"]
       Product_Variant =str(Description)
       test.log("Product Variant from CDF file is: " +str(Product_Variant))
       
       Controller_Fam = Product_Variant[0:7]
       selectControllerparse(tbl, Controller_Fam, Product_Variant)
    mouseClick(waitForObject(":Newproject.NEXT >_Button"), MouseButton.PrimaryButton)
    mouseClick(waitForObject(":Product Name_ComboBox"))
    SW_Combo = waitForObject(":Product Name_ComboBox")
    SW_List = parseForSW(SW_Combo) 
    
    mouseClick(waitForObject(":Product Name.System.Windows.Controls.StackPanel_Edit"))
    type(waitForObject(":Product Name.System.Windows.Controls.StackPanel_Edit"), "New File")
    mouseClick(waitForObject(":Newproject.Use a wizard for controller configuration_CheckBox"))
    mouseClick(waitForObject(":Newproject.FINISH_Button"))
    try:
        snooze(5)      
        mouseClick(":MessageBoxDisplay.YES_Button"), MouseButton.PrimaryButton
        snooze(10)
    except:
        snooze(5)
    waitForObjectExists(":KoolProg.System.Windows.Controls.Image_Button")
    snooze(10)
    
    return SW_List

def parseForSW(SW_ComboBox):##Check SW version in offline and save in a list to compare with CDF versions inside convert settings##
    SW_List=[]
    item = SW_ComboBox
    children=object.children(item)
    for child in children:
        if (object.properties(child)["type"] == "ComboBoxItem"):
            SW_Options = object.properties(child)["text"]
            SW_List.append(SW_Options)
    return SW_List  
       
def selectControllerparse(tbl, fam, val): ##While creating a project, to dynamically click on expander and controller name as per the input from excel sheet##
   ControllerTable={}        
   items_1=object.children(tbl)
   for item_1 in items_1:        
       if((object.properties(item_1)["type"] ==  "TabItem")and(object.properties(item_1)["name"] ==  "tabController")) :
           TableItem=object.children(item_1)
           for table in TableItem:
               if((object.properties(table)["type"] == "Table") and (object.properties(table)["name"] == "datagridProducts")):
                   childs = object.children(table)
                   for child in childs:                
                       if((object.properties(child)["type"] ==  "WPFControl") and (object.properties(child)["class"] ==  "System.Windows.Controls.GroupItem")):
                           expander=object.children(child)
                           for exp in expander:
                               if(object.properties(exp)["type"] == "Expander"):
                                   ExpanderName = None
                                   ExpanderName = exp.nativeObject.DataContext.Name
                                   if (str(ExpanderName).strip() == str(fam).strip()):
                                       mouseClick(exp), MouseButton.PrimaryButton
                                       test.log("Expander name in KoolProg is "+ str(ExpanderName))
                                   rows=object.children(exp)
                                   for row in rows:                                                               
                                       if(object.properties(row)["type"] == "TableRow"):
                                           cells = object.children(row)
                                           for cell in cells:
                                               if (object.properties(cell)["type"] == "TableCell"):
                                                   CellName = None
                                                   CellName = object.properties(cell)["text"]
                                                   if (str(CellName).strip() == str(val).strip()):
                                                       mouseClick(cell), MouseButton.PrimaryButton
                                                       test.log("Controller name in KoolProg is: "+ str(CellName)) 

def Unzip(File_Name):
    file_path = Configurations
    File_Name = File_Name+".cbk"
#     file_1 = "New File.cbk"
    for file in os.listdir(file_path):
        if (file == File_Name):
            x = File_Name.split(".cbk")
            x1 = x[0]
            os.rename(Configurations+str(x1)+".cbk", Configurations+str(x1)+"1.zip",)
    
        zip_ref = zipfile.ZipFile(Configurations+str(x1)+"1.zip" ,'r')
        zip_ref.extractall(Configurations+r"Backup_File")
        zip_ref.close()
    
    Backup_file = Configurations+r"Backup_File\SETTINGS.BCK"
    with codecs.open((Configurations+r"Backup_File\SETTINGS.BCK"),encoding='utf-8') as data_file:
        content = data_file.read()
        content = content.replace(u'\ufeff','') 
        data = json.loads(content)
        test.log(str(data))
        Parameter_Count = len(data["Parameters"])
        ApplicationID = data["Header"]["ApplicationID"]
        test.log("Application ID in Settings.bck file is"+str(ApplicationID))
        CodeNumber = data["Header"]["CodeNumber"]
        ControllerType = data["Header"]["Description"]
        SWVersion = data["Header"]["SWVersion"]
        
        for i in range (0, Parameter_Count):
            CDFIndex = data["Parameters"][i]["CdfIndex"]
            Parameter_Name = data["Parameters"][i]["Text"]
            Unique_ID = data["Parameters"][i]["UniqueID"]
            Parameter_Val = data["Parameters"][i]["Value"]

def Database_Verify():
    window=waitForObject(":KoolProg_Window")
     
    name1=getControl(window,"Label","tbProductInfoValue0")  
    if(name1 == None):
        print "None"
        result = False
    else:    
        Controller_Name = (name1["text"])
          
    name2=getControl(window,"Label","tbProductInfoValue1")  
    if(name2 == None):
        print "None"
        result = False
    else:    
        Code_Number = (name2["text"])
          
    name3=getControl(window,"Label","tbProductInfoValue2")  
    if(name3 == None):
        print "None"
        result = False
    else:    
        SW_Version = (name3["text"])  
    file_path = Dependent_Files+"\CDFs"
    for file in os.listdir(file_path):
        if (file == Controller_Name[8::]+"_"+SW_Version):
            for dirName, subdirList, fileList in os.walk(file):
#                 print('Found directory: %s' % dirName)
                for fname in fileList:
                    if (fname == "device.jso"):
                        test.log(str(fname))
                        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
      
    
    
    
