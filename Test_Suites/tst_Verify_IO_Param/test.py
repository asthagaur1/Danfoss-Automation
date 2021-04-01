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


def getName3():
   global name3
   if(name3 == None):        
       window=waitForObject(":KoolProg_Window_0")
       test.log("%s"%len(window))
   else:
       return name3


def main():
    source(findFile("scripts", "global.py"));
    startApplication("KoolProg")
    mouseClick(waitForObject(":KoolProg_Image_3"), MouseButton.PrimaryButton)
    snooze(30)
    mouseClick(waitForObject(":Danfoss.T4CClient.models.TreeViewParameters_TreeItem"))
    snooze(15)
    Fetch_Vis_Rule()
    
    

def Fetch_Vis_Rule():
    with codecs.open(findFile("testdata", r"\Latest_CDF\device.jso"),encoding='utf-8') as data_file:
        content = data_file.read()
        content = content.replace(u'\ufeff','')
        data = json.loads(content)
        
        Parameters = data["Parameters"]
        Parameters_Count = len(data["Parameters"])
        
        Squish_DB = Global_Scripts_Path+"\AK_CC_DB_Squish.csv"
        records = testData.dataset(Squish_DB)
        for rec in records:
            Param_Name = testData.field(rec, 3)
            Vis_Rule = testData.field(rec, 17)
            for i in range (0, Parameters_Count):
                if (str(Param_Name) == str(data["Parameters"][i]["Text"])):
                    Visibility_Rule = Vis_Rule
                    result = eval(Visibility_Rule)
                    test.log("For Parameter" + str(Param_Name)+" Result for"+str(Visibility_Rule)+"is " + str(result))        
 
 
 
    
def GetVar(val):            ##GetVar has no function call. Runs from "eval(val)". val points to the visibility rule in AKCC_DB_Squish.csv##
    with codecs.open(findFile("testdata", r"\Latest_CDF\device.jso"),encoding='utf-8') as data_file:
        content = data_file.read()
        content = content.replace(u'\ufeff','') 
        data = json.loads(content)
        Parameter_Count = len(data["Parameters"])
        for i in range (0, Parameter_Count):
            Index = data["Parameters"][i]["Idx"]
            if (Index == val):
                Param_Name = data["Parameters"][i]["Text"]
                Param_Label = data["Parameters"][i]["Label"]
                EnumIdx = data["Parameters"][i]["EnumIdx"]
                if (Param_Name != "Application mode"):
                    for j in range (0, len(data["Enumerations"][EnumIdx]["Values"])):
                        Enum_Value = data["Enumerations"][EnumIdx]["Values"][j]["Text"]
                        searchKoolProg(Param_Label, Enum_Value, Param_Name)
                
def searchKoolProg(Param_Label, Enum_Value, Param_Name):
    window=waitForObject(":KoolProg_Window")
    tbl = getControl(window, "Table" , "datagridParameters")
    
    mouseClick(waitForObjectExists(":KoolProg_Edit"), MouseButton.PrimaryButton)
    type(waitForObject(":KoolProg_Edit"), Param_Label)
    type(waitForObject(":KoolProg_Edit"), "<Return>")
    snooze(5)
    try:
        mouseClick(":MessageBoxDisplay.OK_Button"), MouseButton.PrimaryButton
    except:
        fieldstable = parseVisibleRow(tbl)
        setParameterValue(fieldstable, Param_Name, Enum_Value)
    
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
                       if((object.properties(row)["type"] == "TableRow") and (row.nativeObject.IsVisible == True) and (row.nativeObject.DataContext.IsEnabled == True)):
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
    
def setParameterValue(fieldsTable, parameterName, value):
   print parameterName
   print value
   found = False
   if(fieldsTable != None):                            
       if(parameterName in fieldsTable):
           found=True
           edit=fieldsTable[parameterName]  
           if (value != ""):  
               mouseClick(waitForObject(edit))
               type(waitForObject(edit), value)
               type(waitForObject(edit), "<Return>") 
       else:
           test.log(str(parameterName)+" :Is hidden under visibility rules")                                                                                               
   return found     
           
def Check_IO_Parameters():
   waitForObject(":KoolProg.System.Windows.Controls.Image_Button")
   snooze(30)
    
   window=waitForObject(":KoolProg_Window")
   tbl = getControl(window, "Table" , "datagridParameters")
   items=tbl.nativeObject.Items
     
#    file = Output_Global_Path+"\Input_Output.csv"
#    file = file + Timestr
#    file = file + ".csv"
#    openfile = open(file,'wt') 
#    writer = csv.writer(openfile)
#    writer.writerow(["ParameterName", "KP_ParameterName", "Result", "IO_Value", "KP_IO_Value", "IO_Result"])
    
#     a = "Id_1053441 > 0 && Id_1053441 != 7 && Id_1053441 != 8"
 
   with codecs.open(findFile("testdata", r"\Latest_CDF\device.jso"),encoding='utf-8') as data_file:
       content = data_file.read()
       content = content.replace(u'\ufeff','')
       data = json.loads(content)
        
       Parameters = data["Parameters"]
       Parameters_Count = len(data["Parameters"])
        
       Virtual_IO = data["VirtualIO"]
       Virtual_IO_Count = len(data["VirtualIO"])
        
       IO_Config = data["IOConfig"]
        
       IO_Config_count = len(data["IOConfig"])
       for i in range (0, IO_Config_count):
           IOFuncVarIDX = data["IOConfig"][i]["IOFunctionVarIdx"]
#             test.log("is:" +str(IOFuncVarIDX))
           OverRideIDX = data["IOConfig"][i]["OverrideVarIdx"]
#             test.log("ORIDX is-" +str(OverRideIDX))
            
            
           IO_Parameter = data["Parameters"][IOFuncVarIDX]["Text"]
           test.log("IO_Parameter is:" +str(IO_Parameter))
            
           IO_Unique_ID = data["Parameters"][IOFuncVarIDX]["UniqueID"]
           IO_Parameter_Label = data["Parameters"][IOFuncVarIDX]["Label"]
            
           doubleClick(waitForObject(":KoolProg_Edit"), MouseButton.PrimaryButton)
           type(waitForObject(":KoolProg_Edit"), str(IO_Parameter_Label))
           type(waitForObject(":KoolProg_Edit"), "<Return>")
            
           try:
#                 waitForObjectExists(":MessageBoxDisplay.OK_Button")
               mouseClick(":MessageBoxDisplay.OK_Button"), MouseButton.PrimaryButton
           except:
               snooze(2)
            
           IO_Param, IO_Value = parseIOVisibleRow(tbl) ##IO Param is AI1 Function. IO Value is Pe Evap Pressure##
            
           for i in range (0, Parameters_Count):
               if (data["Parameters"][i]["Text"] == str(IO_Value)):
                   IO_Value_IDX = data["Parameters"][i]["Idx"]
                   IO_Value_Label = data["Parameters"][i]["Label"]
#                     test.log ("Idx is:" +str(IO_Value_IDX))
                    
                   for j in range (0, Virtual_IO_Count):
#                         test.log ("it is"+str(data["VirtualIO"][j]["ParamIdx"]))
                       if (data["VirtualIO"][j]["ParamIdx"] == IO_Value_IDX):
                           Override_IDX = data["VirtualIO"][j]["OverrideVarIdx"]
                           test.log("Override is:" +str(Override_IDX))
          
                           if (Override_IDX != -1):
                               for k in range(0, Parameters_Count):
                                   if (data["Parameters"][k]["Idx"] == Override_IDX):
                                       Manual_IO_Param = data["Parameters"][k]["Text"]
                                       Manual_IO_Label = data["Parameters"][k]["Label"]
#                                         Dummy_Name, IO_Status = parseVisibleRow(tbl)
#                                         test.log("IO_Status is"+str(IO_Status))
                                                
                           else: 
                               Manual_IO_Label = str(IO_Value_Label)
#                                 test.log("IO_Status is"+str(IO_Status))
                            
                           doubleClick(waitForObject(":KoolProg_Edit"), MouseButton.PrimaryButton)
                           type(waitForObject(":KoolProg_Edit"), str(Manual_IO_Label))
                           type(waitForObject(":KoolProg_Edit"), "<Return>")
                            
                           try:
#                                 waitForObjectExists(":MessageBoxDisplay.OK_Button")
                               mouseClick(":MessageBoxDisplay.OK_Button"), MouseButton.PrimaryButton
                                
                           except:
                               snooze(2)
                            
                           Input_Output_Param , Input_Output_Value = parseIOVisibleRow(tbl)
                           writer.writerow([Input_Output_Param, "","", Input_Output_Value, "", ""])
    
    
    
       mouseClick(waitForObject(":KoolProg.Input/Output_TabItem"), MouseButton.PrimaryButton)
       snooze(20)
        
       IO_tbl = getControl(window, "Table" , "datagridInputOutput")
       items=IO_tbl.nativeObject.Items
        
       openfile = open(file,'wt') 
       writer = csv.writer(openfile)
   #     writer.writerow(["ParameterName", "DB_Menucode","KP_Menucode","Result" ,"DB_DefaultValue", "KP_DefaultValue", "Result", "DB_MinValue", "KP_MinValue", "Result" ,"DB_MaxValue", "KP_MaxValue", "Result", "DB_Unit", "KP_Unit", "Result", "DB_Info", "KP_Info", "Result"])
       records = testData.dataset(file)
       for rec in records:
           Param_Name = testData.field(rec, 0)
           IO_Value = testData.field(rec, 3)
           for i in range (0, items.Count-1):
               item=items.at(i)
#                 test.log("PN:" +str(item.ParameterName))
               if (Param_Name == item.ParameterName): 
                   test.log("PN:" +str(item.ParameterName))
                   result_1 = test.compare(str(IO_Value), str(item.Value))
                   result_2 = test.compare(str(Param_Name), str(item.ParameterName))
                    
                   writer.writerow(["", item.ParameterName, result_1, "", item.Value, result_2])   
                                  
