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
    mouseClick(waitForObject(":KoolProg_Image"), MouseButton.PrimaryButton)
    snooze(4)
    mouseClick(waitForObject(":Danfoss.T4CClient.SetParameters+ListFileItems_ListItem_3"),MouseButton.PrimaryButton)
    snooze(5)
    waitForObject(":KoolProg_Window")
    Value_Generation()
    
    
def DataGrid_Verification_Offline():
    result = False
    test.compare(waitForObjectExists(":KoolProg_Table").type, "Table")
    test.compare(waitForObjectExists(":KoolProg_Table").name, "datagridParameters")
   
    window=waitForObject(":KoolProg_Window")
    print("count:%s"% len(window))
    
    name1=getControl(window,"Label","tbProductInfoValue0")  
    if(name1 == None):
        print "None"
        result = False
    else:
        test.log("type:%s "% name1["type"])
        test.log("name:%s "% name1["name"])
        test.log("text:%s "% name1["text"])
        Controller = (name1["text"])
#         print (Controller[0:9])
        result = True   
        
    name2=getControl(window,"Label","tbProductInfoValue1")  
    if(name2 == None):
        print "None"
        result = False
    else:    
        test.log("type:%s "% name2["type"])
        test.log("name:%s "% name2["name"])
        test.log("text:%s "% name2["text"])
        Application = (name2["text"])
        #print (Application)
        result = True

    if ((Controller == ("ETC1RL"))|(Controller == ("ETC2RL"))):
        
#         src_file = 'C:\\Users\\U322075\\Desktop\\squish6.0\\test suites\\suite_json\\tst_1_Json_Parsing_Process\\testdata\\AK_CC_DB_Squish.csv'
#         dest_file = 'C:\\Users\\U322075\\Desktop\\squish6.0\\test suites\\suite_json\\tst_3_Offline_Features\\testdata\\Squish_DB_AK_CC.csv'                    
#         shutil.copy(src_file, dest_file)
#         
#         src_file_1 = 'C:\\Users\\U322075\\Desktop\\squish6.0\\test suites\\suite_json\\tst_1_Json_Parsing_Process\\testdata\\AK_CC_DB_Squish.csv'
#         dest_file_1 = 'C:\\Users\\U322075\\Desktop\\squish6.0\\test suites\\suite_AKCC\\tst_3_Offline_Features\\testdata\\Squish_DB_AK_CC.csv'                    
#         shutil.copy(src_file_1, dest_file_1)
        
        
        file = "C:\gitworkspace\TestAutomation-AKCC5XX\Test_Automation\SourceCode\Global_scripts\AK_CC_DB_Squish.csv"
                
        file_1= "C:\gitworkspace\TestAutomation-AKCC5XX\Test_Automation\SourceCode\Global_scripts\AKCC_DB_Comparison.csv"
#         file_1 = file_1 + Timestr
#         file_1 = file_1 + ".csv"
        tbl=waitForObjectExists(":KoolProg_Table")
        items=tbl.nativeObject.Items
        data = tbl.nativeObject.DataContext.Parameters.CurrentItem
        
        
        openfile = open(file_1,'wt') 
        writer = csv.writer(openfile)
        writer.writerow(["ParameterName", "DB_Menucode","KP_Menucode","Result" ,"DB_DefaultValue", "KP_DefaultValue", "Result", "DB_MinValue", "KP_MinValue", "Result" ,"DB_MaxValue", "KP_MaxValue", "Result", "DB_Unit", "KP_Unit", "Result", "DB_Info", "KP_Info", "Result"])
        
        records = testData.dataset(file)
        for rec in records:
            groupCode = testData.field(rec, 0)
            Menu_Code = testData.field(rec, 1)
            Group_Name = testData.field(rec, 2)
            Parameter_Name = testData.field(rec, 3)
            PNU = testData.field(rec, 4)
            Default = testData.field(rec, 5)
            Min = testData.field(rec, 6)
            Max = testData.field(rec, 7)
            Unit = testData.field(rec, 8)
            Scaling = testData.field(rec, 9)
            Datatype = testData.field(rec, 10)
            Enum = testData.field(rec, 11)
            Read_Only =  testData.field(rec, 12)
            Info_Help = testData.field(rec, 13)
            Decimals = testData.field(rec, 14)
            Variable_Name= testData.field(rec, 15)
            mylist=[]
            if(Enum != ""):
                for x in Enum.split(','):
                    for y in x.split(':'): 
                        if(y == Default):                        
                            for z in x.split(':'):
                                mylist.append(z)
                                Default = z 
            
            for i in range (0, items.Count-1):
                item=items.at(i)
                if ((Parameter_Name == item.ParameterName)& (Datatype != "")):        
                    MenuCode_Result = test.compare(Menu_Code, item.MenuCode)
                    DefaultValue_Result = test.compare(Default, item.DefaultValue)
                    MinValue_Result = test.compare(Min, item.Minvalue)
                    MaxValue_Result = test.compare(Max, item.Maxvalue)
                    Unit_Result = test.compare(Unit, item.Unit)
                    Help_Result = test.compare(Info_Help, item.Description)
                    writer.writerow([item.ParameterName,Menu_Code, item.MenuCode, MenuCode_Result, Default, item.DefaultValue, DefaultValue_Result, Min, item.Minvalue, MinValue_Result, Max, item.Maxvalue, MaxValue_Result, Unit, item.Unit, Unit_Result])            
 
def Value_Generation():
    result = False
    test.compare(waitForObjectExists(":KoolProg_Table").type, "Table")
    test.compare(waitForObjectExists(":KoolProg_Table").name, "datagridParameters")
   
    window=waitForObject(":KoolProg_Window")
    print("count:%s"% len(window))  
    
      
    tbl=waitForObjectExists(":KoolProg_Table")
#     fieldsTable=parseFields(tbl)
#     fieldsTable=parseVisibleRow(tbl)
#     Object=tbl.nativeObject
#     items=tbl.nativeObject.Items
    ##file - controller type##
        
    file = r"C:\gitworkspace\TestAutomation-AKCC5XX\Test_Automation\SourceCode\suite_AK-CC_mastercase\tst_New_ETC_SpotTest\testdata\ETC1RL.csv"
    file_1 = "Comparison_Sheet.csv"
    openfile = open(file_1,'wt') 
    writer = csv.writer(openfile)
    writer.writerow(["Parameter_Name", "Random_Value", "", ""])
    enumList = []
    test1 = []
    functions = ['Min', 'Max', 'Val']
    records = testData.dataset(file)
#     functions.append("Min")
#     functions.append("Max")
#     functions.append("Val")
    count = len(functions)
    for j in range(0,count):
        for rec in records:
            name = testData.field(rec, 0)
            enum = testData.field(rec,1)
            for i in range (0, items.Count-1):
                item=items.at(i) 
                if ((name == item.ParameterName)&(item.Datatype == "Float")&(item.ReadOnly == False)&(item.IsEnabled == True)):
                    #Object.SelectedIndex = i
                    minVal = float(item.Minvalue)
                    #print ("min_value"+str(minVal))
                    maxVal = float(item.Maxvalue) 
                    #print ("max_value"+str(maxVal))  
                    if(functions[j] == 'Min'):
                        test.log("Result:%s" % setParameterValue(fieldsTable,item.ParameterName, str(minVal)))
                    elif(functions[j] == 'Max'):
                        test.log("Result:%s" % setParameterValue(fieldsTable,item.ParameterName, str(maxVal)))
                    else:
                        item_Val = random.uniform(minVal, maxVal)
                        #print ("0_"+str(item_Val))
                        itemVal = float(item_Val)
                        #print ("1_"+str(itemVal))
                        itemVal = round(item_Val,2)
                        #print ("2_"+str(itemVal))
                        test.log("Result:%s" % setParameterValue(fieldsTable,item.ParameterName, str(itemVal)))
                        writer.writerow([item.Key, item.ParameterName, itemVal])  
                         
                elif ((name == item.ParameterName)&(item.Datatype == "INT")&(item.ReadOnly == False)&(item.IsEnabled == True)):
                    #Object.SelectedIndex = i
                    minVal = float(item.Minvalue)
                    maxVal = float(item.Maxvalue)  
                    if(functions[j] == 'Min'):
                        test.log("Result:%s" % setParameterValue(fieldsTable,item.ParameterName, minVal))
                    elif(functions[j] == 'Max'):
                        test.log("Result:%s" % setParameterValue(fieldsTable,item.ParameterName, maxVal))
                    else:
                        itemVal = random.randint(minVal, maxVal)
                        try:
                            test.log("Result:%s" % setParameterValue(fieldsTable,item.ParameterName, itemVal))
                            writer.writerow([item.Key, item.ParameterName, itemVal])
                        except:
                            snooze(1)
                    
                elif ((name == item.ParameterName)&((item.Datatype == "enum") | (item.Datatype == "BIT"))&(item.ReadOnly == False)&(item.IsEnabled == True)):              
                    if(enum != ""):
                        for x in enum.split(','):
                            test1 = x.split(':')
                            val = test1[1]                       
                            enumList.append(val)
    #                         for y in x.split(':'):
    #                             isText = hasTexts(y)
    #                             if(isText):
    #                                 enumList.append(y)
                        count = len(enumList)                    
                        i = random.randint(0,count-1)
                        #test.log(str(i)) 
                        if ((name != "Predefined applications" ) & (name != "Zero crossing")):
                            enumValue = enumList[i]
                            if (enumValue != None):
                                #item.Value = enumValue
                                if (Controller_cont[0:3] == "EKE"):
                                    test.log("Result:%s" % setParameterEnumValue(fieldsTable,item.ParameterName, enumValue))
                                    writer.writerow([item.ParameterName, enumValue])
                                    if ((item.ParameterName in checkParameters) | (item.ParameterName == "Main switch")):
                                        visibleParamName = []
                                        test.log(item.ParameterName,"Check")
                                        fieldsTable = parseVisibleRow(tbl)
                                        writer.writerow([item.Key, item.ParameterName, enumValue])
                                    else:
                                        snooze(1)
                                else: 
                                    item.Value = enumValue
                                    #test.log("Result:%s" % setParameterValue(fieldsTable,item.ParameterName, enumValue))
                                    writer.writerow([item.ParameterName, enumValue])  
                            else:
                                snooze(1)
                        else:
                            snooze(1)                 
                    enumList = []
        result = True
    return result

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

def setParameterValue(fieldsTable, parameterName, value):
    print parameterName
    print value
    found = False
    if(fieldsTable != None):                            
        if(fieldsTable[parameterName] != None):
            found=True
            edit=fieldsTable[parameterName]  
            if (value != ""):  
                mouseClick(waitForObject(edit))
                type(waitForObject(edit), value)
                type(waitForObject(edit), "<Tab>")   
                try:
                    mouseClick(":MessageBoxDisplay.OK_Button"), MouseButton.PrimaryButton
                except:
                    snooze(0.1)                                                                                               
    return found

def setParameterEnumValue(fieldsTable, parameterName, value):
    found = False    
    if(fieldsTable != None):   
        if parameterName in visibleParamName:
            test.log(parameterName)
                                 
            if(fieldsTable[parameterName] != None):
            #if parameterName in fieldsTable.values():                
                found=True
                edit=fieldsTable[parameterName]
                #mouseClick(waitForObject(edit), MouseButton.PrimaryButton)
                #snooze(2)
                type(waitForObject(edit), value)
                #snooze(2)
                #type(waitForObject(edit), "<Return>")    
                keyPress("<Return>");
                
                #if(parameterName == "Pull down temp limit"):
                try:
                    #waitForObject(":MessageBoxDisplay_Window")
                    mouseClick(":MessageBoxDisplay.OK_Button"), MouseButton.PrimaryButton
            
                except:
                    snooze(0.1)
                                                                                                            
    return found
