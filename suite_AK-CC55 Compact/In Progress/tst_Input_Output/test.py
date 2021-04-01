import json
import csv
from pprint import pprint
import datetime
import os
import shutil
import string
import xdrlib
import codecs

now = datetime.datetime.now()

Timestr = now.strftime("%d-%m-%Y_%H_%M")

def main():
    startApplication("KoolProg")
    snooze(3)
    mouseClick(waitForObject(":KoolProg_Image_3"),MouseButton.PrimaryButton)
    snooze(15)
    waitForObject(":KoolProg.System.Windows.Controls.Image_Button")
    
    
    mouseClick(waitForObject(":Danfoss.T4CClient.TreeViewParameters_TreeItem_4"), MouseButton.PrimaryButton)
    snooze(30)
    
    
    mouseClick(waitForObject(":KoolProg.Input/Output_TabItem"), MouseButton.PrimaryButton)
    
    AKCC_IO_ManualOverride()




def AKCC_IO_ManualOverride():
    result = False
    waitForObject(":KoolProg.System.Windows.Controls.Image_Button")

    window=waitForObject(":KoolProg_Window")
    tbl = getControl(window, "Table" , "datagridInputOutput")

#     doubleClick(waitForObject(":Danfoss.T4CClient.TreeViewParameters.Danfoss.T4CClient.TreeViewParameters_TreeItem_3"), MouseButton.PrimaryButton)
    
    tv=getControl(window, "Tree", "treeViewManualIO")
    test.log("tv is:"+ str(tv))
    
    print("Expander length"+str(len(gExpanderList)))
    print("Parameter length"+str(len(gParamList)))
    
    if(tv != None):
        AKCCparseTreeView(tv, tbl)  
        
        
        test.log("Expander length"+str(len(gExpanderList)))
        test.log("Parameter length"+str(len(gParamList)))
        
        for expander in gExpanderList:
            test.log ("Expander:" + expander)
        for param in gParamList:
            test.log ("Parameters:" + param)
            
    else:
        test.log("Treeview not found")     
    snooze(1)
        
gExpanderList=[]
gParamList=[]


global gExpanderList
global gParamList

def AKCCparseTreeView(parent, tbl):    
    if (parent != None):
        children=object.children(parent)
        if(children != None):
            for child in children:
                if (child["class"] == "System.Windows.Controls.TreeViewItem"):
                    if((child.nativeObject.Tag != "Favourites") & (child.nativeObject.Tag != "Selected logs")& (child.itemCount == 0 )):
                        #gHeader_List.append(child.nativeObject.Header.AllMenu)                       
                        doubleClick(child)
                        #print("Expander:" + child.nativeObject.Header.AllMenu)
                        Expander, Expander_Name, ItemCount = parseAKCCVisibleExpander(tbl)
                         
                        #print (Expander)
                        
                        if(Expander != None):
#                             gExpanderList.append(Expander_Name+":"+str(ItemCount))
                            Parameters = parseAKCCVisibleRows(Expander) 
                            test.log(str(Parameters))                           
                            for param in Parameters:
                                AKCC_IO_SG_Comparison(Expander_Name, param)                                 
                    else:
                        if((child.nativeObject.Tag != "Favourites")&(child.nativeObject.Tag != "Selected logs")&(child.nativeObject.Tag != "All")):
                            doubleClick(child)
                            AKCCparseTreeView(child, tbl)
                        else:
                            AKCCparseTreeView(child, tbl)
                        #print (child.nativeObject.Header.AllMenu)
    return       


        
def AKCC_IO_SG_Comparison(Expander_Name, param):
#     print Expander_Name
#     print param
    SG_Comparison_File = "C:\gitworkspace\TestAutomation-AKCC5XX\Test_Automation\SourceCode\Global_scripts\IO_SGParameters.csv"
    openfile = open(SG_Comparison_File,'wt') 
    writer = csv.writer(openfile)
    writer.writerow(["GroupNameKP","GroupNameDB", "ParameterNameKP", "ParameterNameDB", "Result_SG", "Result_PN"]) 
    
    file = "C:\gitworkspace\TestAutomation-AKCC5XX\Test_Automation\SourceCode\Global_scripts\AK_CC_DB_Squish.csv"
      
    records = testData.dataset(file)
    for rec in records: 
        GroupName = testData.field(rec, 2)
        ParameterName = testData.field(rec, 3)
        for item in ParameterName: 
            if (param == ParameterName):
                 Result_1 = test.compare(GroupName,Expander_Name)
                 Result_2 = test.compare(param, ParameterName)
                 writer.writerow([Expander_Name,GroupName,Result_1, param, ParameterName, Result_2])
                 break
             
                 result = True
#     print (Expander_Name)


gHeader_List = []
def parseAKCCVisibleExpander(tbl):
    Expander_Name = None
    Item_Count = None
    Expander = None
    fieldsTable={}    
    items=object.children(tbl)
    for item in items:        
        if(object.properties(item)["type"] ==  "WPFControl"):
            expander=object.children(item)
            for child in expander:                
                if(object.properties(child)["type"] ==  "Expander" and child.nativeObject.IsExpanded == True):
                    Expander_Name = child.nativeObject.DataContext.Name
                    Item_Count = child.nativeObject.DataContext.ItemCount
#                     print ("Expander:%s "% Expander_Name)
#                     print ("Items:%s "% Item_Count)
                    Expander = child
                    return (Expander, Expander_Name, Item_Count)
#                     rows=object.children(child)
#                     for row in rows:
#                         if(object.properties(row)["type"] == "TableRow" and row.nativeObject.IsVisible == True and row.nativeObject.DataContext.IsEnabled == True):
#                             fields=object.children(row)
#                             fieldName=None        
#                             for field in fields:                                                                
#                                 if(object.properties(field)["type"] == "TableCell" and object.properties(field)["column"] == 4):
#                                     fieldName=object.properties(field)["text"]                            
#                                 if(object.properties(field)["type"] == "TableCell" and object.properties(field)["column"] == 7 and fieldName != ""):
#                                     edits=object.children(field)                                    
#                                     for edit in edits:
#                                         if((object.properties(edit)["type"] == "Edit" and object.properties(edit)["name"] == "txtValue")) or( (object.properties(edit)["type"] == "ComboBox" and object.properties(edit)["name"] == "cmbEnums")):
#                                             #if (fieldName != None):
#                                                 #test.log("Parsing:%s" % (fieldName))                                                
#                                             fieldsTable[fieldName]=edit
                                                                                                                                              
    return None, None, None

def parseAKCCVisibleRows(child):
    fieldNames = []
    rows=object.children(child)
    for row in rows:
        if(object.properties(row)["type"] == "TableRow" and row.nativeObject.IsVisible == True and row.nativeObject.DataContext.IsEnabled == True):
            fields=object.children(row)
            fieldName=None 
            for field in fields:                                                                
                if(object.properties(field)["type"] == "TableCell" and object.properties(field)["column"] == 4):
                    fieldName=object.properties(field)["text"]   
                    fieldNames.append(fieldName)
                     
    return (fieldNames)  


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
