import glob, os
import csv
import random
import __builtin__
import datetime

now = datetime.datetime.now()
#print now.strftime("%d-%m-%Y_%H_%M")
Timestr = now.strftime("%d-%m-%Y_%H_%M")

gList = []

def Comparison():
    test.compare(waitForObjectExists(":KoolProg_Table").type, "Table")
    test.compare(waitForObjectExists(":KoolProg_Table").name, "datagridParameters")
   
    window=waitForObject(":KoolProg_Window")
    print("count:%s"% len(window))  
    
      
    tbl=waitForObjectExists(":KoolProg_Table")
    #fieldsTable=parseFields(tbl)
    Object=tbl.nativeObject
    items=tbl.nativeObject.Items
    
    for ParameterName in gList[0]:
        if (ParameterName == item.ParameterName):
            test.compare (gList[1] , item.Value)
        break
    
   

def main():
    startApplication("KoolProg")
    mouseClick(waitForObject(":KoolProg_Image"),MouseButton.PrimaryButton)
    mouseClick(waitForObject(":SetParameters_Window"),  MouseButton.PrimaryButton)
    mouseClick(waitForObject(":System.Windows.Controls.DockPanel.Open_Label"),  MouseButton.PrimaryButton)
    mouseClick(waitForObject(":Open_Dialog"),  MouseButton.PrimaryButton)
    mouseClick(waitForObject(":Open_Edit"),  MouseButton.PrimaryButton)
    type((":Open_Edit"), "AKCC-110-CC.xml")
    snooze(2)
    type((":Open_Edit"), "<Return>")
#     startApplication("KoolProg")
#     test.compare(waitForObjectExists(":KoolProg_Window").type, "Window")
#     test.compare(waitForObjectExists(":KoolProg_Window").text, "KoolProg")
#     test.compare(waitForObjectExists(":KoolProg_Window")["class"], "Danfoss.T4CClient.HomePage")
#     mouseClick(waitForObject(":KoolProg_Image"), MouseButton.PrimaryButton)
#     waitForObject(":SetParameters_Window")
#     mouseClick(waitForObject(":Danfoss.T4CClient.SetParameters+ListFileItems_ListItem_3"), MouseButton.PrimaryButton)
#     snooze(5)
    waitForObject(":KoolProg.System.Windows.Controls.Image_Button")
    Value_Generation()

def parseFields(tbl):
            fieldsTable={}        
            items_1=object.children(tbl)
            for item_1 in items_1:        
                if(object.properties(item_1)["type"] ==  "WPFControl"):
                    expander=object.children(item_1)
                    for child in expander:                
                        if(object.properties(child)["type"] ==  "Expander"):
                            rows=object.children(child)
                            for row in rows:
                                if((object.properties(row)["type"] == "TableRow")):#and (row.nativeObject.IsVisible == True)):
                                    fields=object.children(row)
                                    fieldName=None        
                                    for field in fields:                                                                
                                        if(object.properties(field)["type"] == "TableCell" and object.properties(field)["column"] == 4):
                                            fieldName=object.properties(field)["text"]                            
                                        if(object.properties(field)["type"] == "TableCell" and object.properties(field)["column"] == 7 and fieldName != None):
                                            edits=object.children(field)                                    
                                            for edit in edits:
                                                if(object.properties(edit)["type"] == "Edit" and object.properties(edit)["name"] == "txtValue"):
                                                    #if (fieldName != None):
                                                    test.log("Parsing:%s" % (fieldName))                                                
                                                    fieldsTable[fieldName]=edit
                                                                                                                                                      
            return fieldsTable



def setParameterEnumValue(fieldsTable, parameterName, value):
    
    found = False    
    if(fieldsTable != None):   
        if parameterName in visibleParamName:
            test.log(parameterName)
                                 
            if(fieldsTable[str(parameterName)] != None):
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
            gList.append(parameterName, value)                                                                                                
    return found

def setParameterRandomValue(fieldsTable, parameterName, value):
    global gList
    test.log (parameterName)
    test.log (value)
    found = False
    if(fieldsTable != None):                            
        if(fieldsTable[str(parameterName)] != None):
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
            gList.append(parameterName)
            gList.extend((value))
            Comparison()
                                                                                 
    return gList

def setParameterValue(fieldsTable, parameterName, value):
    test.log (parameterName)
    test.log (value)
    found = False
    if(fieldsTable != None):                            
        if(fieldsTable[str(parameterName)] != None):
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



gControl = None
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
    #waitForObject(":KoolProg_Image_5", 20000)
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
    ##Controller - controller type##    
#     name1_cont=getControl(window,"Label","txtProuctName")  
#     if(name1_cont == None):
#         print "None"
#         result = False
#     else:    
#         test.log("type:%s "% name1_cont["type"])
#         test.log("name:%s "% name1_cont["name"])
#         test.log("text:%s "% name1_cont["text"])
#         Controller_cont = (name1_cont["text"])
#         print Controller_cont[0:5]
#         result = True
    ##ERCWS##   
    if ((Controller_file == "Compact coil") | (Controller_file =="Single coil")):
        fieldsTable=parseFields(tbl)
        Object=tbl.nativeObject
        items=tbl.nativeObject.Items
        file = "AK_CC_DB_Squish.csv"
        
   
#     file_1 = "Comparison_Sheet.csv"
#     openfile = open(file_1,'wt') 
#     writer = csv.writer(openfile)
#     writer.writerow(["Parameter_Name", "Random_Value", "", ""])
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
            name = testData.field(rec, 3)
            enum = testData.field(rec,11)
            for i in range (0,items.Count-1):
                
                item=items.at(i) 
                if ((name == item.ParameterName)&(item.Datatype == "Float")&(item.ReadOnly == False)&(item.IsEnabled == True)&(obj.IsVisible == True)):
                    #Object.SelectedIndex = i
                    minVal = float(item.Minvalue)
                    #print ("min_value"+str(minVal))
                    maxVal = float(item.Maxvalue) 
                    #print ("max_value"+str(maxVal))  
#                     if(functions[j] == 'Min'):
#                         test.log("Result:%s" % setParameterValue(fieldsTable,item.ParameterName, str(minVal)))
#                     elif(functions[j] == 'Max'):
#                         test.log("Result:%s" % setParameterValue(fieldsTable,item.ParameterName, str(maxVal)))
#                     else:
                    item_Val = random.uniform(minVal, maxVal)
                    #print ("0_"+str(item_Val))
                    itemVal = float(item_Val)
                    #print ("1_"+str(itemVal))
                    itemVal = round(item_Val,2)
                    #print ("2_"+str(itemVal))
                    (setParameterRandomValue(fieldsTable,item.ParameterName, str(itemVal)))
                    #writer.writerow([item.ParameterName, itemVal])  
                         
                elif ((name == item.ParameterName)&(item.Datatype == "INT")&(item.ReadOnly == False)&(item.IsEnabled == True)&(obj.IsVisible == True)):
                    #Object.SelectedIndex = i
                    minVal = float(item.Minvalue)
                    maxVal = float(item.Maxvalue)  
#                     if(functions[j] == 'Min'):
#                         test.log("Result:%s" % setParameterValue(fieldsTable,item.ParameterName, minVal))
#                     elif(functions[j] == 'Max'):
#                         test.log("Result:%s" % setParameterValue(fieldsTable,item.ParameterName, maxVal))
#                     else:
                    itemVal = random.randint(minVal, maxVal)
                    try:
                        (setParameterRandomValue(fieldsTable,item.ParameterName, itemVal))
                        #writer.writerow([item.ParameterName, itemVal])
                    except:
                        snooze(1)
                    
                elif ((name == item.ParameterName)&((item.Datatype == "enum") | (item.Datatype == "BIT"))&(item.ReadOnly == False)&(item.IsEnabled == True)&(obj.IsVisible == True)):              
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
                                    (setParameterEnumValue(fieldsTable,item.ParameterName, enumValue))
#                                     #writer.writerow([item.ParameterName, enumValue])
#                                     if ((item.ParameterName in checkParameters) | (item.ParameterName == "Main switch")):
#                                         visibleParamName = []
#                                         test.log(item.ParameterName,"Check")
#                                         fieldsTable = parseVisibleRow(tbl)
#                                         writer.writerow([item.ParameterName, enumValue])
#                                     else:
#                                         snooze(1)
                                else: 
                                    item.Value = enumValue
                                    #test.log("Result:%s" % setParameterValue(fieldsTable,item.ParameterName, enumValue))
                                    #writer.writerow([item.ParameterName, enumValue])
                                    gList.append(item.ParameterName)
                                    gList.extend([enumValue])
                                    print gList  
                            else:
                                snooze(1)
                        else:
                            snooze(1)                 
                    enumList = []
        result = True
    return result