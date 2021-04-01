# -*- coding: utf-8 -*-

import json
import csv
from pprint import pprint
import datetime
import os
import shutil
import string
import xdrlib
import os
import zipfile
import gzip
import codecs


def main():
    startApplication("KoolProg")
    waitForObject(":SetParameters_List_2")
    mouseClick(waitForObject(":KoolProg_Image_3"), MouseButton.PrimaryButton)
    snooze(5)
    waitForObject(":KoolProg_Image_5")
    waitForObject(":KoolProg.System.Windows.Controls.Image_Button")
    
    
    test.compare(waitForObjectExists(":KoolProg_Table").type, "Table")
    test.compare(waitForObjectExists(":KoolProg_Table").name, "datagridParameters")
   
    window=waitForObject(":KoolProg_Window")
    print("count:%s"% len(window))
    
    tbl=waitForObjectExists(":KoolProg_Table")
    
    name1=getControl(window,"Label","txtApp")  
    if(name1 == None):
        print "None"
    else:    
        test.log("type:%s "% name1["type"])
        test.log("name:%s "% name1["name"])
        test.log("text:%s "% name1["text"])
        Controller_CodeNumber = (name1["text"])
        
    count = getControl(window,"Table","datagridParameters")
    if(count == None):
        print "None"
    else:    
        test.log("type:%s "% count["type"])
        test.log("name:%s "% count["name"])
        test.log("text:%s "% count["rowCount"])
        Row_Count = (count["rowCount"])
        
    verifyActiveAlarm()
    
def verifyActiveAlarm():
    result = False
    alarmTable = []
    tbl=waitForObjectExists(":KoolProg_Table")
    mouseClick(":KoolProg.Alarms_TabItem"), MouseButton.PrimaryButton
    
    snooze(20)
    waitForObject(":KoolProg_Table_3")
    
    
    tblActiveAlarm=waitForObjectExists(":KoolProg_Table_3")
    
    items_1=object.children(tblActiveAlarm)
    
    for WPF_obj in items_1:    
        if(object.properties(WPF_obj)["type"] =="WPFControl"):
            item_2 = object.children(WPF_obj)
            for Exp_obj in item_2:
                if (object.properties(Exp_obj)["type"] =="Expander"):
                    item_3 = object.children(Exp_obj)
                    for TblRw_obj in item_3:
                         if(object.properties(TblRw_obj)["type"] =="TableRow"):
                            fields=object.children(TblRw_obj)
                            for field in fields: 
                                test.log("Field 1 is: "+str(field))
                                if(object.properties(field)["type"] =="TableCell" and object.properties(field)["column"] == 2):
                                    ##COLUMN IS 2 because 1 NOT AVAILABLE##
                                    test.log("Field 2 is: "+str(field))
                                    if(field != None):
                                        alarmName=object.properties(field)["text"]
                                        alarmTable.append(alarmName)
                    activeAlarmsCount = len(alarmTable)
                    test.log(alarmName)
                    Object=tbl.nativeObject
                    items=tbl.nativeObject.Items
                #     for i in range (0, items.Count-1):
                #         item=items.at(i)
                    for i in range (0,activeAlarmsCount):        
                        name = alarmTable[i]
                        for j in range (0, items.Count-1):
                            item=items.at(j)
                            if(name == item.ParameterName):
                                test.compare(item.Value, "Alarm: "+ name)
                    result = True
                    return result


# mouseClick(waitForObject(":Danfoss.T4CClient.TreeViewParameters_TreeItem_5"), MouseButton.PrimaryButton)
    
        
#     fieldsTable=parseFields(tbl)
#     Object=tbl.nativeObject
#     items=tbl.nativeObject.Items
#     file = "C:\gitworkspace\TestAutomation-AKCC5XX\Test_Automation\SourceCode\Global_scripts\Danfoss.AK-CC_550_Parameters.csv"
#     
#     
#     enumList = []
#     test1 = []
# #     functions = ['Min', 'Max', 'Val']
#     records = testData.dataset(file)
# #     functions.append("Min")
# #     functions.append("Max")
# #     functions.append("Val")
# #     count = len(functions)
# #     for j in range(0,count):
#     for rec in records:
#         Unique_ID = testData.field(rec, 0)
#         name = testData.field(rec, 1)
#         enum = testData.field(rec,2)
#         for i in range (0, items.Count-1):
#             item=items.at(i) 
#             
#             if ((Unique_ID == item.Key)&((item.Datatype == "Enum") | (item.Datatype == "BIT"))&(item.ReadOnly == False)&(item.IsEnabled == True)):              
#                 if(enum != ""):
#                     #print("Raja"+item.ParameterName+"-"+enum)
#                     for x in enum.split(','):
#                         test1 = x.split(':')
#                         val = test1[1]                       
#                         enumList.append(val)
#     #                         for y in x.split(':'):
#     #                             isText = hasTexts(y)
#     #                             if(isText):
#     #                                 enumList.append(y)
#                     count = len(enumList)                    
#                     i = random.randint(0,count-1)
#                     #test.log(str(i)) 
#                     if (name == "Main switch" ):
#                         enumValue = enumList[i]
#                         if (enumValue != None):
#                             item.Value = enumValue
#                             if (item.Value != "Start"):
#                                 
#                             #test.log("Result:%s" % setParameterValue(fieldsTable,item.ParameterName, enumValue))
# #                             writer.writerow([item.Key, item.ParameterName, enumValue])  
#                         else:
#                             snooze(1)
#                     else:
#                         snooze(1)                 
#                 enumList = []
#     result = True
#             
#             
#             
#             
#     
#     for i in range(0,Row_Count):
#         if (items.CurrentItem.)
#         
#     
# def parseFields(tbl):
#             fieldsTable={}        
#             items_1=object.children(tbl)
#             for item_1 in items_1:        
#                 if(object.properties(item_1)["type"] ==  "WPFControl"):
#                     expander=object.children(item_1)
#                     for child in expander:                
#                         if(object.properties(child)["type"] ==  "Expander"):
#                             rows=object.children(child)
#                             for row in rows:
#                                 if((object.properties(row)["type"] == "TableRow") and (row.nativeObject.IsVisible == True)):
#                                     fields=object.children(row)
#                                     fieldName=None        
#                                     for field in fields:                                                                
#                                         if(object.properties(field)["type"] == "TableCell" and object.properties(field)["column"] == 4):
#                                             fieldName=object.properties(field)["text"]                            
#                                         if(object.properties(field)["type"] == "TableCell" and object.properties(field)["column"] == 7 and fieldName != None):
#                                             edits=object.children(field)                                    
#                                             for edit in edits:
#                                                 if(object.properties(edit)["type"] == "Edit" and object.properties(edit)["name"] == "txtValue"):
#                                                     #if (fieldName != None):
#                                                     test.log("Parsing:%s" % (fieldName))                                                
#                                                     fieldsTable[fieldName]=edit
#                                                                                                                                                       
#             return fieldsTable
#     
    
    
    
    
    
    
    
    
#     SQL = "C:\gitworkspace\TestAutomation-AKCC5XX\Test_Automation\SourceCode\Global_scripts\AK_CC_DB_Sql.csv"
#     Squish_file = "C:\gitworkspace\TestAutomation-AKCC5XX\Test_Automation\SourceCode\Global_scripts\AK_CC_DB_Squish.csv"
#     Unit_Result= "C:\gitworkspace\TestAutomation-AKCC5XX\Test_Automation\SourceCode\Global_scripts\Unit_Result.csv"
#     openfile = open(Unit_Result,'wt') 
#     writer = csv.writer(openfile)
#     writer.writerow(["PN","Squish_Unit", "SQL_Unit", "Result"])
#     
#     records = testData.dataset(Squish_file)
#     for rec in records:
#         Squish_Name = testData.field(rec, 3)
#         Squish_unit = testData.field(rec, 8)
#     
#         records_1 = testData.dataset(SQL)
#         for rec_1 in records_1:
#             SQL_Name = testData.field(rec_1, 4)
#             SQL_unit = testData.field(rec_1, 10)
#             
#             if ( Squish_Name == SQL_Name):
#                 result = test.compare(Squish_unit, SQL_unit)
#                 writer.writerow ([Squish_Name, Squish_unit, SQL_unit,result])
#                 
#         
        
    
# def Alarm():
#     New_File = "C:\gitworkspace\TestAutomation-AKCC5XX\Test_Automation\SourceCode\Global_scripts\Alarm_Read.csv"
#     
#     openfile = open(New_File,'wt') 
#     writer = csv.writer(openfile)
#     writer.writerow(["MenuCode","Parameter_Name", "Read_Only", "Para_Variable_Name", "Alarm_Variable_Name"])
#     
#     Squish_file = "C:\gitworkspace\TestAutomation-AKCC5XX\Test_Automation\SourceCode\Global_scripts\AK_CC_DB_Squish.csv"
#     
#     records = testData.dataset(Squish_file)
#     for rec in records:
#         Squish_MenuCode = testData.field(rec, 1)
#         Squish_ParameterName = testData.field(rec, 3)
#         Squish_VariableName = testData.field(rec, 15)
#         print(Squish_VariableName)
#         
#         Squish_AlarmParameter_Idx = testData.field(rec, 18)
# #         print(Squish_AlarmParameter_Idx)
# 
#         
 
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
# 
# 
# def getName3():
#     global name3
#     if(name3 == None):        
#         window=waitForObject(":KoolProg_Window_0")
#         test.log("%s"%len(window))
#     else:
#         return name3        
# 
# gExpanderList=[]
# gParamList=[]
# 
# def AKCC_SG():
#     result = False
#     SG_Comparison_File = "C:\gitworkspace\TestAutomation-AKCC5XX\Test_Automation\SourceCode\Global_scripts\SGParameters.csv"
#     waitForObject(":KoolProg.System.Windows.Controls.Image_Button")
# 
#     window=waitForObject(":KoolProg_Window")
#     tbl = getControl(window, "Table" , "datagridParameters")
# 
#     doubleClick(waitForObject(":Danfoss.T4CClient.TreeViewParameters.Danfoss.T4CClient.TreeViewParameters_TreeItem_3"), MouseButton.PrimaryButton)
#     
#     tv=getControl(window, "Tree", "treeViewParameters")
#     test.log("tv is:"+ str(tv))
#     
#     print("Expander length"+str(len(gExpanderList)))
#     print("Parameter length"+str(len(gParamList)))
#     
#     if(tv != None):
#         AKCCparseTreeView(tv, tbl)  
#         
#         
#         print("Expander length"+str(len(gExpanderList)))
#         print("Parameter length"+str(len(gParamList)))
#         
#         for expander in gExpanderList:
#             print ("Expander:" + expander)
#         for param in gParamList:
#             print ("Parameters:" + param)
#             
# #         if ((Expander_Name != None) & (Parameter_Names != None)):
# #             count = len(Parameter_Names)  
# #         print ("Header Name:" + Expander_Name)
# #         print ("Parameters:" + Parameter_Names ) 
# #         print ("No.of Parameters:" + str(Item_Count))
# #         else:
# #             print ("False")
#     else:
#         test.log("Treeview not found")     
#     snooze(1)    
# 
# global gExpanderList
# global gParamList
# 
# def AKCCparseTreeView(parent, tbl):    
#     if (parent != None):
#         children=object.children(parent)
#         if(children != None):
#             for child in children:
#                 if (child["class"] == "System.Windows.Controls.TreeViewItem"):
#                     if((child.nativeObject.Header.AllMenu != "Favourites") & (child.itemCount == 0)):
#                         #gHeader_List.append(child.nativeObject.Header.AllMenu)                       
#                         doubleClick(child)
#                         #print("Expander:" + child.nativeObject.Header.AllMenu)
#                         Expander, Expander_Name, ItemCount = parseAKCCVisibleExpander(tbl)
#                          
#                         #print (Expander)
#                         
#                         if(Expander != None):
# #                             gExpanderList.append(Expander_Name+":"+str(ItemCount))
#                             Parameters = parseAKCCVisibleRows(Expander)                            
#                             for param in Parameters:
#                                 AKCC_SG_Comparison(Expander_Name, param)
# #                                 gParamList.append(Expander_Name+":"+param)                                   
#                     else:
#                         if((child.nativeObject.Header.AllMenu != "Favourites")&(child.nativeObject.Header.AllMenu != "All")):
#                             doubleClick(child)
#                             AKCCparseTreeView(child, tbl)
#                         else:
#                             AKCCparseTreeView(child, tbl)
#                         #print (child.nativeObject.Header.AllMenu)
#     return
# 
# 
# gHeader_List = []
# def parseAKCCVisibleExpander(tbl):
#     Expander_Name = None
#     Item_Count = None
#     Expander = None
#     fieldsTable={}    
#     items=object.children(tbl)
#     for item in items:        
#         if(object.properties(item)["type"] ==  "WPFControl"):
#             expander=object.children(item)
#             for child in expander:                
#                 if(object.properties(child)["type"] ==  "Expander" and child.nativeObject.IsExpanded == True):
#                     Expander_Name = child.nativeObject.DataContext.Name
#                     Item_Count = child.nativeObject.DataContext.ItemCount
# #                     print ("Expander:%s "% Expander_Name)
# #                     print ("Items:%s "% Item_Count)
#                     Expander = child
#                     return (Expander, Expander_Name, Item_Count)
# #                     rows=object.children(child)
# #                     for row in rows:
# #                         if(object.properties(row)["type"] == "TableRow" and row.nativeObject.IsVisible == True and row.nativeObject.DataContext.IsEnabled == True):
# #                             fields=object.children(row)
# #                             fieldName=None        
# #                             for field in fields:                                                                
# #                                 if(object.properties(field)["type"] == "TableCell" and object.properties(field)["column"] == 4):
# #                                     fieldName=object.properties(field)["text"]                            
# #                                 if(object.properties(field)["type"] == "TableCell" and object.properties(field)["column"] == 7 and fieldName != ""):
# #                                     edits=object.children(field)                                    
# #                                     for edit in edits:
# #                                         if((object.properties(edit)["type"] == "Edit" and object.properties(edit)["name"] == "txtValue")) or( (object.properties(edit)["type"] == "ComboBox" and object.properties(edit)["name"] == "cmbEnums")):
# #                                             #if (fieldName != None):
# #                                                 #test.log("Parsing:%s" % (fieldName))                                                
# #                                             fieldsTable[fieldName]=edit
#                                                                                                                                               
#     return None, None, None
# 
# def parseAKCCVisibleRows(child):
#     fieldNames = []
#     rows=object.children(child)
#     for row in rows:
#         if(object.properties(row)["type"] == "TableRow" and row.nativeObject.IsVisible == True and row.nativeObject.DataContext.IsEnabled == True):
#             fields=object.children(row)
#             fieldName=None 
#             for field in fields:                                                                
#                 if(object.properties(field)["type"] == "TableCell" and object.properties(field)["column"] == 4):
#                     fieldName=object.properties(field)["text"]   
#                     fieldNames.append(fieldName)
#                      
#     return (fieldNames)  
# 
# 
# def AKCC_SG_Comparison(Expander_Name, param):
# #     print Expander_Name
# #     print param
#     
#     openfile = open(SG_Comparison_File,'wt') 
#     writer = csv.writer(openfile)
#     writer.writerow(["GroupNameKP","GroupNameDB", "ParameterNameKP", "ParameterNameDB", "Result_SG", "Result_PN"]) 
#     
#     file = "C:\gitworkspace\TestAutomation-AKCC5XX\Test_Automation\SourceCode\Global_scripts\AK_CC_DB_Squish.csv"
#       
#     records = testData.dataset(file)
#     for rec in records: 
#         GroupName = testData.field(rec, 2)
#         ParameterName = testData.field(rec, 3)
#         for item in ParameterName: 
#             if (param == ParameterName):
#                  Result_1 = test.compare(GroupName,Expander_Name)
#                  Result_2 = test.compare(param, ParameterName)
#                  writer.writerow([Expander_Name,GroupName,Result_1, param, ParameterName, Result_2])
#                  break
# #     print (Expander_Name)
#     print (param)
#          
        
        
        
        
        
        
        
        
        
        
        