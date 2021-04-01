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
    startApplication("KoolProg")
    mouseClick(waitForObject(":Danfoss.T4CClient.SetParameters+ListFileItems_ListItem"), MouseButton.PrimaryButton)
    mouseClick(waitForObject(":Danfoss.T4CClient.SetParameters+ListFileItems_ListItem_3"), MouseButton.PrimaryButton)
    snooze(30)
    mouseClick(waitForObject(":KoolProg.ucParameterDisplay_WPFControl"), 1019, 118, MouseButton.PrimaryButton)
    mouseClick(waitForObject(":KoolProg.ucParameterDisplay_WPFControl"), 1303, 103, MouseButton.PrimaryButton)
    mouseClick(waitForObject(":KoolProg.btnQuickSetting_Button"), MouseButton.PrimaryButton)
    wizard_win = waitForObject(":NewWizard_Window")
    QuickWizard(wizard_win)
    
def QuickWizard(wizard_win):
    with codecs.open(findFile("testdata", r"\Latest_CDF\device.jso"),encoding='utf-8') as data_file:
       content = data_file.read()
       content = content.replace(u'\ufeff','') 
       data = json.loads(content)
       Groups = data["Groups"]
       Group_Count = len(data["Groups"])
       
       Parameter_Count = len(data["Parameters"])
       
       Headers = len(data["Header"])
       
       Controller_Variant = data["Header"]["Description"]
       Code_Number = data["Header"]["Name"]
       SWVersion = data["Header"]["SWVersion"]
       SWVersion = SWVersion/256
       
       
       name1=getControl(wizard_win,"Label","txtProductNumber")  
       if(name1 == None):
            print "None"
       else:    
            QW_Cont_Variant = (name1["text"])
            test.compare(Controller_Variant,QW_Cont_Variant)
        
       name2=getControl(wizard_win,"Label","txtCodeNumber")  
       if(name2 == None):
            print "None"
       else:    
            QW_CodeNum = (name2["text"])
            test.compare(Code_Number,QW_CodeNum)
        
       name3=getControl(wizard_win,"Label","txtVersionNumber")  
       if(name3 == None):
            print "None"
       else:    
            QW_SW_Ver = (name3["text"])
            test.compare(SWVersion,QW_SW_Ver)
           
    items_1=object.children(wizard_win)
    for item_1 in items_1:        
       if((object.properties(item_1)["type"] ==  "ListView")and(object.properties(item_1)["name"] ==  "lstQuickWizardSetting")) :
           List=object.children(item_1)
           for ListItem in List:
               if((object.properties(ListItem)["type"] == "ListViewItem")& (ListItem.nativeObject.IsVisible == True)):
                   childs = object.children(ListItem)
                   for child in childs:                
                       if((object.properties(child)["type"] ==  "Label") and (object.properties(child)["class"] ==  "System.Windows.Controls.TextBlock")):
                           
                           Param_Name_QW = object.properties(child)["text"]
                           QuickWizard_Group = data["Groups"][Group_Count-1]
                           QuickWizard_Group_Count = len(QuickWizard_Group)                           
                           
                           QW_Items = QuickWizard_Group["Items"]
                           for j in range (0, len(QW_Items)):
                               Param_Index = QW_Items[j]["Index"]
                               for k in range (0,Parameter_Count):
                                   if (Param_Index == data["Parameters"][k]["Idx"]):
                                       Param_Name = data["Parameters"][k]["Text"]
                                       if (str(Param_Name_QW.strip()) == str(Param_Name.strip())):
                                           for child_1 in childs:
                                               if(object.properties(child_1)["type"] == "ComboBox"):
                                                   Enums = child_1.nativeObject.DataContext.Enums
                                                   if (Enums == ""):
                                                       if (data["Parameters"][k]["Decimals"] == 0):
                                                           value = random.randint(data["Parameters"][k]["Min"], data["Parameters"][k]["Max"])
                                                           mouseClick(child_1, MouseButton.PrimaryButton)
                                                           type((child_1), value)
                                                           snooze(2)
                                                       elif (data["Parameters"][k]["Decimals"] == 1):
                                                           value = random.uniform(data["Parameters"][k]["Min"], data["Parameters"][k]["Max"])
                                                           mouseClick(child_1, MouseButton.PrimaryButton)
                                                           type((child_1), value)
                                                           snooze(2)
                                                   elif (Enums != ""):
                                                       enumIdx = data["Parameters"][k]["EnumIdx"]
                                                       for l in (0, (len(data["Enumerations"]))-1):
                                                           if (enumIdx == data["Enumerations"][l]["Idx"]):
                                                               enum_values_count = len(data["Enumerations"][l]["Values"])
                                                               random_enum = random.randint(0, enum_values_count)
                                                               Enum_Val = data["Enumerations"][l]["Values"][random_enum]["Text"]
                                                               mouseClick(child_1, MouseButton.PrimaryButton)
                                                               type((child_1), Enum_Val)
                                           
                                            
    
    
    
