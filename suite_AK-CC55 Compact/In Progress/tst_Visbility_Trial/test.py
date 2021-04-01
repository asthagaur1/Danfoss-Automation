import glob, os
import csv
import random
import __builtin__
import datetime
import json
from pprint import pprint
import collections

def main():


    startApplication("KoolProg")
    mouseClick(waitForObject(":KoolProg_Image"),MouseButton.PrimaryButton)
    mouseClick(waitForObject(":SetParameters_Window"),  MouseButton.PrimaryButton)
    mouseClick(waitForObject(":System.Windows.Controls.DockPanel.Open_Label"),  MouseButton.PrimaryButton)
    mouseClick(waitForObject(":Open_Dialog"),  MouseButton.PrimaryButton)
    mouseClick(waitForObject(":Open_Edit"),  MouseButton.PrimaryButton)
    type((":Open_Edit"), "AKCC_AD_300.xml")
    snooze(2)
    type((":Open_Edit"), "<Return>")
    
    snooze(10)

    tbl=waitForObjectExists(":KoolProg_Table")
    Visibility_ID(tbl)
#     fieldsArray = []
#     fieldsArray = fieldsArray.append(parseVisibleRow(tbl))
#     print (fieldsArray)
    
    
def parseVisibleRow(tbl,ParameterName, Unique_ID, VB_rule):
    fieldsTable={}    
    items=object.children(tbl)
    for item in items:        
        if(object.properties(item)["type"] ==  "WPFControl"):
            expander=object.children(item)
            for child in expander:                
                if(object.properties(child)["type"] ==  "Expander"):
                    rows=object.children(child)
#                     ParameterName, ID = Visibility_ID()
                    for row in rows:
                        if(object.properties(row)["type"] == "TableRow" and (ParameterName == row.nativeObject.Item.ParameterName) and (Unique_ID == row.nativeObject.Item.Key)):
                            if (VB_rule.strip() == "" and row.nativeObject.IsVisible == True):
                                test.log (ParameterName +" :is always enabled") 
#                             Unique_Id = row.nativeObject.Item.Key
#                             Param_Name = row.nativeObject.Item.ParameterName
#                             Visibility_ID(Unique_Id, Param_Name)
                            elif(VB_rule.strip() == '0' and row.nativeObject.IsVisible == True):
                                test.log (ParameterName + " :has VB_Rule 0 and is enabled")
                                
                            elif ((VB_rule.strip() != "") & (VB_rule.strip() != '0')):
                                if ((VB_rule)== True):
                                    test.log( ParameterName + " with " + VB_rule + " is true")
                                                             
                            
def Visibility_ID(tbl):
     file_DB = "Squish_DB_AK_CC.csv"
     file_ans = "result.csv"
     openfile = open(file_ans,'wt') 
     writer = csv.writer(openfile)
     writer.writerow(["Parameter_Name", "VB_rule"])
     records = testData.dataset(file_DB)
     for rec in records:
         Parameter_Name = testData.field(rec, 3)
         Variable_ID = testData.field(rec, 15)
         VB_rule = testData.field(rec, 17)
         if (VB_rule.strip() == ""):
           ParameterName = Parameter_Name
           Unique_ID = Variable_ID
           parseVisibleRow(tbl,ParameterName, Unique_ID, VB_rule)
         elif (VB_rule.strip() == '0'):
            test.log("inside ELIF")
            ParameterName = Parameter_Name
            Unique_ID = Variable_ID
            parseVisibleRow(tbl,ParameterName, Unique_ID, VB_rule)
         elif ((VB_rule.strip() != "") & (VB_rule.strip() != '0')):
            test.log("inside ELIF- VB rules")
            ParameterName = Parameter_Name
            Unique_ID = Variable_ID
            parseVisibleRow(tbl,ParameterName, Unique_ID, VB_rule)
             
# def setParameterValue(fieldsTable, parameterName, value):
#     print parameterName
#     print value
#     found = False
#     if(fieldsTable != None):                            
#         if(fieldsTable[parameterName] != None):
#             found=True
#             edit=fieldsTable[parameterName]  
#             if (value != ""):  
#                 mouseClick(waitForObject(edit))
#                 type(waitForObject(edit), value)
#                 type(waitForObject(edit), "<Tab>")   
#                 try:
#                     mouseClick(":MessageBoxDisplay.OK_Button"), MouseButton.PrimaryButton
#                 except:
#                     snooze(0.1)                                                                                               
#     return found    
#      
# if ((Unique_ID == item.Key)&((item.Datatype == "Enum") | (item.Datatype == "BIT"))&(item.ReadOnly == False)&(item.IsEnabled == True)):              
#                     if(enum != ""):
#                         #print("Raja"+item.ParameterName+"-"+enum)
#                         for x in enum.split(','):
#                             test1 = x.split(':')
#                             val = test1[1]                       
#                             enumList.append(val)
#                         count = len(enumList)                    
#                         i = random.randint(0,count-1)
#                         if ((name != "Predefined applications" ) & (name != "Zero crossing")):
#                             enumValue = enumList[i]
#                             if (enumValue != None):
#                                 item.Value = enumValue
#                                 #test.log("Result:%s" % setParameterValue(fieldsTable,item.ParameterName, enumValue))
#                                 writer.writerow([item.Key, item.ParameterName, enumValue])  
#                             else:
#                                 snooze(1)
#                         else:
#                             snooze(1)                 
#                     enumList = []     
     
     
               
                 
