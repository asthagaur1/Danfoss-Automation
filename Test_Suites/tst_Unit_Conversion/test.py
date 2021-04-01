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

def main():                 	                                         ##Create output files and call functions##   
    Temp_List, Diff_List, Pressure_List = parseCDF()
    
    startApplication("KoolProg")
    
#     mouseClick(waitForObject(":KoolProg.System.Windows.Controls.Image_Button"), MouseButton.PrimaryButton)            
    mouseClick(waitForObject("{container=':KoolProg_Window' name='btnSettings' text='System.Windows.Controls.Image' type='Button'}"), MouseButton.PrimaryButton)
    mouseClick(waitForObject(":Settings.Unit:_ComboBox"), MouseButton.PrimaryButton)
    type(waitForObject(":Settings.Unit:_ComboBox"), "Metric")
    snooze(2)
    type(waitForObject(":Settings.Unit:_ComboBox"), "<Return>")
    mouseClick(":Settings.Save_Button"), MouseButton.PrimaryButton
    mouseClick(waitForObject(":MessageBoxDisplay.OK_Button"), MouseButton.PrimaryButton)
    
    mouseClick(waitForObject("{container=':KoolProg_Window' name='imgServicetest' type='Image'}"), MouseButton.PrimaryButton)
    snooze(30)
    
    waitForObject(":KoolProg.System.Windows.Controls.Image_Button")
    window=waitForObject(":KoolProg_Window")
    
    mouseClick(waitForObject("{container=':KoolProg_Tree_2' occurrence='3' text='Danfoss.T4CClient.models.TreeViewParameters' type='TreeItem'}"), MouseButton.PrimaryButton)
    tbl=waitForObjectExists(":KoolProg_Table")
    
    MetricCheck(tbl,Temp_List, Diff_List, Pressure_List)
    
    mouseClick(waitForObject(":KoolProg.System.Windows.Controls.Image_Button"), MouseButton.PrimaryButton)            
    mouseClick("{container=':KoolProg_Window' name='btnSettings' text='System.Windows.Controls.Image' type='Button'}")
    mouseClick(waitForObject(":Settings.Unit:_ComboBox"), MouseButton.PrimaryButton)
    type(waitForObject(":Settings.Unit:_ComboBox"), "Imperial")
    snooze(2)
    type(waitForObject(":Settings.Unit:_ComboBox"), "<Return>")
    mouseClick(":Settings.Save_Button"), MouseButton.PrimaryButton
    mouseClick(waitForObject(":MessageBoxDisplay.OK_Button"), MouseButton.PrimaryButton)
    
    mouseClick(waitForObject("{container=':KoolProg_Window' name='imgServicetest' type='Image'}"), MouseButton.PrimaryButton)
    snooze(30)
    waitForObject(":KoolProg.System.Windows.Controls.Image_Button")
    window=waitForObject(":KoolProg_Window")
    
    mouseClick(waitForObject("{container=':KoolProg_Tree_2' occurrence='3' text='Danfoss.T4CClient.models.TreeViewParameters' type='TreeItem'}"), MouseButton.PrimaryButton)
    tbl=waitForObjectExists(":KoolProg_Table")
    
    
    ImperialCheck(tbl,Temp_List, Diff_List, Pressure_List)

    
def MetricCheck(tbl, Temp_List, Diff_List, Pressure_List):
    file = "Default_Unit_Comparison.csv"
    openfile = open(file,'wt') 
    writer_1 = csv.writer(openfile)
    writer_1.writerow(["ParameterName", "CDF_Min", "KP_Min", "Result", "CDF_Max", "KP_Max", "Result", "CDF_Default", "KP_Default", "Result"])       
    
    
    Visible_Param = []
    MinVal_Dict ={}
    MaxVal_Dict = {}
    DefaultVal_Dict = {}
    
    Visible_Param, MinVal_Dict, MaxVal_Dict, DefaultVal_Dict = parseForValues(tbl)
    
    for i in range (0, len(Temp_List)):
        for j in range (0, len(Visible_Param)):
            if (str(Temp_List[i]) == str(Visible_Param[j])):
                Param_Name, Cdf_Min, Min,result, Cdf_Max, Max, result_1, Cdf_Default, Default, result_2 = checkWithCDF(Temp_List[i], MinVal_Dict, MaxVal_Dict, DefaultVal_Dict)
                writer_1.writerow([Param_Name, float(Cdf_Min), float(Min), result, float(Cdf_Max), float(Max), result_1, float(Cdf_Default), float(Default), result_2])
                
    for k in range (0, len(Diff_List)):
        for l in range (0, len(Visible_Param)):
            if (str(Diff_List[k]) == str(Visible_Param[l])):
                Param_Name, Cdf_Min, Min,result, Cdf_Max, Max, result_1, Cdf_Default, Default, result_2 = checkWithCDF(Diff_List[k], MinVal_Dict, MaxVal_Dict, DefaultVal_Dict)
                writer_1.writerow([Param_Name, float(Cdf_Min), float(Min), result, float(Cdf_Max), float(Max), result_1, float(Cdf_Default), float(Default), result_2])
                
    for m in range (0, len(Pressure_List)):
        for n in range (0, len(Visible_Param)):
            if (str(Pressure_List[m]) == str(Visible_Param[n])):
                Param_Name, Cdf_Min, Min,result, Cdf_Max, Max, result_1, Cdf_Default, Default, result_2 = checkWithCDF(Pressure_List[m], MinVal_Dict, MaxVal_Dict, DefaultVal_Dict)
                writer_1.writerow([Param_Name, float(Cdf_Min), float(Min), result, float(Cdf_Max), float(Max), result_1, float(Cdf_Default), float(Default), result_2])
    
def ImperialCheck(tbl, Temp_List, Diff_List, Pressure_List): 
    file_1 = "Imperial_Unit_Comparison.csv"
    openfile = open(file_1,'wt') 
    writer_2 = csv.writer(openfile)
    writer_2.writerow(["ParameterName", "CDF_Min", "KP_Min", "Result", "CDF_Max", "KP_Max", "Result", "CDF_Default", "KP_Default", "Result"])       
    
    Visible_Param = []
    MinVal_Dict ={}
    MaxVal_Dict = {}
    DefaultVal_Dict = {}
    
    Visible_Param, MinVal_Dict, MaxVal_Dict, DefaultVal_Dict = parseForValues(tbl)
    
    for i in range (0, len(Temp_List)):
        for j in range (0, len(Visible_Param)):
            if (str(Temp_List[i]) == str(Visible_Param[j])):
                Param_Name, Cdf_Min, Min,result, Cdf_Max, Max, result_1, Cdf_Default, Default, result_2 = ConvertFromCDF(Temp_List[i], MinVal_Dict, MaxVal_Dict, DefaultVal_Dict)
                writer_2.writerow([Param_Name, float(Cdf_Min), float(Min), result, float(Cdf_Max), float(Max), result_1, float(Cdf_Default), float(Default), result_2])
                
                
    for k in range (0, len(Diff_List)):
        for l in range (0, len(Visible_Param)):
            if (str(Diff_List[k]) == str(Visible_Param[l])):
                Param_Name, Cdf_Min, Min,result, Cdf_Max, Max, result_1, Cdf_Default, Default, result_2 = ConvertFromCDF(Diff_List[k], MinVal_Dict, MaxVal_Dict, DefaultVal_Dict)
                writer_2.writerow([Param_Name, float(Cdf_Min), float(Min), result, float(Cdf_Max), float(Max), result_1, float(Cdf_Default), float(Default), result_2])
                
                
    for m in range (0, len(Pressure_List)):
        for n in range (0, len(Visible_Param)):
            if (str(Pressure_List[m]) == str(Visible_Param[n])):
                Param_Name, Cdf_Min, Min,result, Cdf_Max, Max, result_1, Cdf_Default, Default, result_2 = ConvertFromCDF(Pressure_List[m], MinVal_Dict, MaxVal_Dict, DefaultVal_Dict)
                writer_2.writerow([Param_Name, float(Cdf_Min), float(Min), result, float(Cdf_Max), float(Max), result_1, float(Cdf_Default), float(Default), result_2])
    
    
def ConvertFromCDF(Param_Name,MinVal_Dict, MaxVal_Dict, DefaultVal_Dict):                                                     ##Get CDF values and compare with KP values##
    with codecs.open(findFile("testdata", r"\Latest_CDF\device.jso"),encoding='utf-8') as data_file:
        content = data_file.read()
        content = content.replace(u'\ufeff','') 
        data = json.loads(content)
        EngUnit_Count = len(data["EngUnitTypes"])
        for i in range (0, len(data["Parameters"])):
            if (str(Param_Name) == data["Parameters"][i]["Text"]):
                Cdf_Min = data["Parameters"][i]["Min"]
                Cdf_Max = data["Parameters"][i]["Max"]
                Cdf_Default = data["Parameters"][i]["Default"]
                Unit_Idx = data["Parameters"][i]["EngUnitIdx"] 
                           
                for j in range (0, EngUnit_Count):
                    UniqueID = data["EngUnitTypes"][Unit_Idx]["UniqueID"]
                    Unit_Text = data["EngUnitTypes"][Unit_Idx]["Text"]
                    Offset = data["EngUnitTypes"][Unit_Idx]["Offset"]
                    Factor = data["EngUnitTypes"][Unit_Idx]["Factor"]
                    
                    if (UniqueID == -37):
                        New_Min = (Cdf_Min*1.8)+32
                        New_Max = (Cdf_Max*1.8)+32
                        New_Default = (Cdf_Default*1.8)+32
                        for key in MinVal_Dict:
                            if (str(Param_Name) == str(key)):
                                Min = MinVal_Dict[key]
                                result = test.compare(float(Min), float(New_Min))                            
                       
                        for key in MaxVal_Dict:
                            if (str(Param_Name) == str(key)):
                                Max = MaxVal_Dict[key]
                                result_1 = test.compare(float(Max), float(New_Max))                           
                               
                        for key in DefaultVal_Dict:
                            if (str(Param_Name) == str(key)):
                                Default = DefaultVal_Dict[key]
                                result_2 = test.compare(float(Default), float(New_Default))
                        
                    elif (UniqueID == -38):
                        New_Min = Cdf_Min*1.8
                        New_Max = Cdf_Max*1.8
                        New_Default = Cdf_Default*1.8
                        for key in MinVal_Dict:
                            if (str(Param_Name) == str(key)):
                                Min = MinVal_Dict[key]
                                result = test.compare(float(Min), float(New_Min))                            
                       
                        for key in MaxVal_Dict:
                            if (str(Param_Name) == str(key)):
                                Max = MaxVal_Dict[key]
                                result_1 = test.compare(float(Max), float(New_Max))                           
                               
                        for key in DefaultVal_Dict:
                            if (str(Param_Name) == str(key)):
                                Default = DefaultVal_Dict[key]
                                result_2 = test.compare(float(Default), float(New_Default))
                        
                    elif (UniqueID == -32):
                        New_Min = Cdf_Min*14.504
                        New_Max = Cdf_Max*14.504
                        New_Default = Cdf_Default*14.504
                        for key in MinVal_Dict:
                            if (str(Param_Name) == str(key)):
                                Min = MinVal_Dict[key]
                                result = test.compare(float(Min), float(New_Min))                            
                       
                        for key in MaxVal_Dict:
                            if (str(Param_Name) == str(key)):
                                Max = MaxVal_Dict[key]
                                result_1 = test.compare(float(Max), float(New_Max))                           
                               
                        for key in DefaultVal_Dict:
                            if (str(Param_Name) == str(key)):
                                Default = DefaultVal_Dict[key]
                                result_2 = test.compare(float(Default), float(New_Default))
                    else:
                        break
                                
        return Param_Name, New_Min, Min,result, New_Max, Max, result_1, New_Default, Default, result_2
                    
                                       
                    
    
def checkWithCDF(Param_Name,MinVal_Dict, MaxVal_Dict, DefaultVal_Dict):  ##Get CDF values and compare with KP values##
    with codecs.open(findFile("testdata", r"\Latest_CDF\device.jso"),encoding='utf-8') as data_file:
        content = data_file.read()
        content = content.replace(u'\ufeff','') 
        data = json.loads(content)
        for i in range (0, len(data["Parameters"])):
            if (str(Param_Name) == data["Parameters"][i]["Text"]):
                Cdf_Min = data["Parameters"][i]["Min"]
                Cdf_Max = data["Parameters"][i]["Max"]
                Cdf_Default = data["Parameters"][i]["Default"]
                for key in MinVal_Dict:
                    if (str(Param_Name) == str(key)):
                        Min = MinVal_Dict[key]
                        result = test.compare(float(Min), float(Cdf_Min))                            
                       
                for key in MaxVal_Dict:
                    if (str(Param_Name) == str(key)):
                        Max = MaxVal_Dict[key]
                        result_1 = test.compare(float(Max), float(Cdf_Max))                           
                       
                for key in DefaultVal_Dict:
                    if (str(Param_Name) == str(key)):
                        Default = DefaultVal_Dict[key]
                        result_2 = test.compare(float(Default), float(Cdf_Default))                           
        
        return Param_Name, Cdf_Min, Min,result, Cdf_Max, Max, result_1, Cdf_Default, Default, result_2
                       
def parseForValues(tbl):                                                 ##Parse KP table to get parname, min, max and default values##
    Min_Dict={}
    Max_Dict = {}
    Default_Dict={}
    fieldsTable=[]
      
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
                                    fieldsTable.append(fieldName) 
                                    Min_Value = field.nativeObject.DataContext.Minvalue
                                    Min_Dict[fieldName] = Min_Value
                                    Max_Value = field.nativeObject.DataContext.Maxvalue
                                    Max_Dict[fieldName] = Max_Value
                                    Def_Value = field.nativeObject.DataContext.DefaultValue
                                    Default_Dict[fieldName] = Def_Value
                                                                                                                                                                                            
    return fieldsTable, Min_Dict, Max_Dict, Default_Dict            

def parseCDF():                     	                                 ##Get parameters of Temp or pressure units##
    Temp_List=[] 
    Diff_List=[] 
    Pressure_List=[]
    
    with codecs.open(findFile("testdata", r"\Latest_CDF\device.jso"),encoding='utf-8') as data_file:
        content = data_file.read()
        content = content.replace(u'\ufeff','') 
        data = json.loads(content)
        Parameter_Count = len(data["Parameters"])
        EngUnit_Count = len(data["EngUnitTypes"])
        for i in range (0, Parameter_Count):
            Parameter_Name = data["Parameters"][i]["Text"]
            Unit_Idx = data["Parameters"][i]["EngUnitIdx"]
            
            for j in range (0, EngUnit_Count):
                UniqueID = data["EngUnitTypes"][Unit_Idx]["UniqueID"]
                Unit_Text = data["EngUnitTypes"][Unit_Idx]["Text"]
                
                if (UniqueID == -37):
                    Temp_List.append(Parameter_Name)
                elif (UniqueID == -38):
                    Diff_List.append(Parameter_Name)
                elif (UniqueID == -32):
                    Pressure_List.append(Parameter_Name)
                break
                    
    return Temp_List, Diff_List, Pressure_List
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                


