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
    Value_Generation_AK_CC()


def setParameterValue(fieldsTable, parameterName, value):
    print parameterName
    print value
    found = False
    if(fieldsTable != None):  
        if (parameterName in fieldsTable):                           
#         if(fieldsTable[parameterName] != None):
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
        
        
def Value_Generation_AK_CC():
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
    #waitForObject(":KoolProg_Image_7", 20000)
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
    Object=tbl.nativeObject
    items=tbl.nativeObject.Items
    file = "C:\gitworkspace\TestAutomation-AKCC5XX\Test_Automation\SourceCode\Global_scripts\Danfoss.AK-CC_550_Parameters.csv"
    
    file_1 = "C:\gitworkspace\TestAutomation-AKCC5XX\Test_Automation\SourceCode\Global_scripts\AKCC-ValueGeneration.csv"
    openfile = open(file_1,'wt') 
    writer = csv.writer(openfile)
    writer.writerow(["Idx","Parameter_Name", "Random_Value", "", ""])
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
            Unique_ID = testData.field(rec, 0)
            name = testData.field(rec, 1)
            enum = testData.field(rec,2)
            for i in range (0, items.Count-1):
                item=items.at(i) 
                if ((Unique_ID == item.Key)&(item.Datatype == "Float")&(item.ReadOnly == False)&(item.IsEnabled == True)):
                    #Object.SelectedIndex = i
                    minVal = float(item.Minvalue)
                    #print ("min_value"+str(minVal))
                    maxVal = float(item.Maxvalue) 
                    test.log("Param is"+str(item.ParameterName)) 
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
                         
                elif ((Unique_ID == item.Key)&(item.Datatype == "INT")&(item.ReadOnly == False)&(item.IsEnabled == True)):
                    #Object.SelectedIndex = i
                    minVal = float(item.Minvalue)
                    maxVal = float(item.Maxvalue)
                    test.log("Param is"+str(item.ParameterName))  
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
                    
                elif ((Unique_ID == item.Key)&((item.Datatype == "Enum") | (item.Datatype == "BIT"))&(item.ReadOnly == False)&(item.IsEnabled == True)&(item.ParameterName != "Main switch")):              
                    if(enum != ""):
                        #print("Raja"+item.ParameterName+"-"+enum)
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
                            test.log("ENUMVALUE IS:"+str(enumValue))
                            if (enumValue != None):
                                test.log("Param is"+str(item.ParameterName)+"  enum is:"+str(enumValue))
                                
                                test.log("Result:%s" % setParameterEnumValue(fieldsTable,item.ParameterName, enumValue))
                                writer.writerow([item.Key, item.ParameterName, enumValue])
                                
                            else:
                                snooze(1)
                        else:
                            snooze(1)                 
                    enumList = []
        result = True
    return result
            

def setParameterEnumValue(fieldsTable, parameterName, value):
    found = False    
    if(fieldsTable != None):   
        test.log(parameterName)  
        if (parameterName in fieldsTable):
                          
            found=True
            edit=fieldsTable[parameterName]
            
            type(waitForObject(edit), value)   
            keyPress("<Return>");
            
            try:
                #waitForObject(":MessageBoxDisplay_Window")
                mouseClick(":MessageBoxDisplay.OK_Button"), MouseButton.PrimaryButton
        
            except:
                snooze(0.1)
                                                                                                        
    return found