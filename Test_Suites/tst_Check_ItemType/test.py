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
    startApplication("KoolProg")
    mouseClick(waitForObject(":KoolProg_Image"), MouseButton.PrimaryButton)
    snooze(2)
    mouseClick(waitForObject(":SetParameters_Window"), MouseButton.PrimaryButton)
    snooze(2)
    mouseClick(waitForObject(":Danfoss.T4CClient.SetParameters+ListFileItems_ListItem_3"), MouseButton.PrimaryButton)
    snooze(30)
    waitForObject(":KoolProg.System.Windows.Controls.Image_Button")
    ItemType_Table = parseCDF()
    fieldsTable = Value_Generation_AK_CC()
    ItemTypeList = CheckItemTypeParameters(ItemType_Table,fieldsTable)
    getParameterValue(fieldsTable, ItemTypeList)

def checkparametervalue(fieldsTable, ItemTypeList, default):
    tbl=waitForObjectExists(":KoolProg_Table")
    
    
    
def setParameterValue(min, max, default, enum_list,fieldsTable, ItemTypeList, value):
    found = False
    edit=fieldsTable[value]
    ItemType = ItemTypeList[value]
    if (str(ItemType) == "F"):
        if (enum_list != []):
            enum_ad = random.randint(0, len(enum_list)-1)
            param_value = enum_list[enum_ad] 
            param_value = str(param_value)      
        else:
            param_value = random.uniform(min, max)
        mouseClick(waitForObject(edit))
        snooze(2)
        type((edit), param_value)
        snooze(2)
        type((edit), "<Return>")   
        try:
            mouseClick(":MessageBoxDisplay.OK_Button"), MouseButton.PrimaryButton
        except:
            snooze(0.1) 
        mouseClick(":KoolProg.System.Windows.Controls.Image_Button_4"), MouseButton.PrimaryButton
        snooze(2)
        mouseClick(":MessageBoxDisplay.OK_Button"), MouseButton.PrimaryButton
        
        checkparametervalue(fieldsTable, ItemTypeList, default)

   
def getParameterValue(fieldsTable, ItemTypeList):
    found = False
    if(fieldsTable != None):
        for value in ItemTypeList: 
            for value_1 in fieldsTable:
                if (str(value).strip() == str(value_1).strip()):  
                    if (value_1 != ""):  
                        min, max, default, enum_list = parseCDFforvalue(value_1)
                        setParameterValue(min, max, default, enum_list,fieldsTable, ItemTypeList, value_1)
#                         type(waitForObject(edit), value)
#                         type(waitForObject(edit), "<Tab>")   
#                         try:
#                             mouseClick(":MessageBoxDisplay.OK_Button"), MouseButton.PrimaryButton
#                         except:
#                             snooze(0.1)                                                                                               
#     return found

def parseVisibleRow(tbl):
    fieldsTable={}    
    items=object.children(tbl)
    for item in items:        
        if(object.properties(item)["type"] ==  "WPFControl"):
            expander=object.children(item)
            for child in expander:                
                if(object.properties(child)["type"] ==  "Expander"):
                    rows=object.children(child)
                    for row in rows:
                        if(object.properties(row)["type"] == "TableRow" and row.nativeObject.IsVisible == True and row.nativeObject.DataContext.IsEnabled == True):
                            fields=object.children(row)
                            fieldName=None        
                            for field in fields:                                                                
                                if(object.properties(field)["type"] == "TableCell" and object.properties(field)["column"] == 4):
                                    fieldName=object.properties(field)["text"]                            
                                if(object.properties(field)["type"] == "TableCell" and object.properties(field)["column"] == 7 and fieldName != ""):
                                    edits=object.children(field)                                    
                                    for edit in edits:
                                        if((object.properties(edit)["type"] == "Edit" and object.properties(edit)["name"] == "txtValue")) or( (object.properties(edit)["type"] == "ComboBox" and object.properties(edit)["name"] == "cmbEnums")):
                                            #if (fieldName != None):
                                                #test.log("Parsing:%s" % (fieldName))                                                
                                            fieldsTable[fieldName]=edit                                                                                                                                              
    return fieldsTable  

def parseCDF():
    ItemType_Table={}
    with codecs.open(findFile("testdata", r"\Latest_CDF\device.jso"),encoding='utf-8') as data_file:
        content = data_file.read()
        content = content.replace(u'\ufeff','') 
        data = json.loads(content)
        Parameter_Count = len(data["Parameters"])
        for i in range (0, Parameter_Count):
            Parameter_Name = data["Parameters"][i]["Text"]
            Item_Type = data["Parameters"][i]["ItemType"]
            ItemType_Table[Parameter_Name] = Item_Type
    return ItemType_Table
                
def Value_Generation_AK_CC():    
    result = False
    test.compare(waitForObjectExists(":KoolProg_Table").type, "Table")
    test.compare(waitForObjectExists(":KoolProg_Table").name, "datagridParameters")
   
    window=waitForObject(":KoolProg_Window")
    print("count:%s"% len(window))  
      
    tbl=waitForObjectExists(":KoolProg_Table")
    name1=getControl(window,"Label","tbProductInfoValue0")  
    if(name1 == None):
        print "None"
        result = False
    else:    
        test.log("type:%s "% name1["type"])
        test.log("name:%s "% name1["name"])
        test.log("text:%s "% name1["text"])
        Controller_file = (name1["text"])
        result = True
        
    fieldsTable=parseVisibleRow(tbl)
    return fieldsTable

def CheckItemTypeParameters(ItemType_Table,fieldsTable): 
    Item_Type_List = {}
    for key in fieldsTable:
        for key_1 in ItemType_Table:
            if (str(key) == str(key_1)):
                Item_Type_List[key]= ItemType_Table[key_1]
#     test.log(str(len(Item_Type_List)))
    return Item_Type_List
    
def parseCDFforvalue(value):
    Enum_Value_List = []
    with codecs.open(findFile("testdata", r"\Latest_CDF\device.jso"),encoding='utf-8') as data_file:
        content = data_file.read()
        content = content.replace(u'\ufeff','') 
        data = json.loads(content)
        Parameter_Count = len(data["Parameters"])
        for i in range (0, Parameter_Count):
            if (str(value) == data["Parameters"][i]["Text"]):
               Min_Value =  data["Parameters"][i]["Min"]
               Max_Value = data["Parameters"][i]["Max"]
               Default = data["Parameters"][i]["Default"]
               if (data["Parameters"][i]["EnumIdx"] != -1):
                   Enum_Idx = data["Parameters"][i]["EnumIdx"]
                   for j in range (0, len(data["Enumerations"])):
                       if (str(Enum_Idx) == str(data["Enumerations"][j]["Idx"])):
                           for k in range (0, len(data["Enumerations"][j]["Values"])):
                               Enum_Values = data["Enumerations"][j]["Values"][k]["Text"]
                               Enum_Value_List.append(Enum_Values)
               else:
                   Enum_Value_List = []
                   
    return (Min_Value, Max_Value, Default, Enum_Value_List)
    
    
       
    
    
    
    
    
    
    
    
    
    
    
    
    
     
