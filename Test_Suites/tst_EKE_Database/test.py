import datetime
import csv
from pprint import pprint
import datetime
import os
import shutil
import string
import xdrlib
import codecs
import xml.etree.ElementTree as ET


def parseXML():
    result = False
    xmlfile = r"C:\Users\U322075\Desktop\EKE\EKE_2.02\EKE_1V.xml"
    
    tree = ET.parse(xmlfile)                            #get the tree structure by parsing the XML    
    root = tree.getroot()                               #Get the main root of the XML
    Param_List =[]                                      #Initialize a list, to store the dictionary values 
    
    
    for item in root.findall('./ParamList/Parameter'):  #Get the attributes under "Parameter"
        if (len(item)) > 3:                             #XML has some Parameter items without description, label etc. So, hardcoded length of item to more then 3. #Find a better solution                 
            param = {}                                  #Initialize a dictionary to get easy Key-Value pairs
            for child in item:
                param[child.tag] = child.text           #Assign each value of an attribute ("text") to that attribute's Key. #Example- [{'Min': '0'}]                                    
            Param_List.append(param)                    #Put all key-value pairs in the array     
    result = True
    return (Param_List), result

def writeToCSV(Param_DB_List, filename):
    Wizard_XML = r"C:\Users\U322075\Desktop\Screen.xml" #Parse XML file with wizard screen details - to check if parameters are displayed correctly.  
    Wizard_Screen_Parameter =[]
    tree = ET.parse(Wizard_XML)                         #get the tree structure by parsing the XML
    root = tree.getroot()                               #Get the main root of the XML
    
    openfile = open(filename,'wt') 
    writer = csv.writer(openfile)
    writer.writerow(['MenuCode','Parameter_Name','Param_ID', 'Min', 'Max','Default_Value','Unit','Wizard_Screen','Visibility', 'Variable_Name'])
    
    for i in range (0, (len(Param_DB_List))):
        name = (Param_DB_List[i]['Description'])
        Label = (Param_DB_List[i]['Label'])
        Param_ID = (Param_DB_List[i]['ParamID'])
        Min = (Param_DB_List[i]['Min'])
        Max = (Param_DB_List[i]['Max'])
        DefaultValue = (Param_DB_List[i]['DefaultValue'])
        Unit = (Param_DB_List[i]['Unit'])
        Visibility = (Param_DB_List[i]['Visibility'])
        VariableName = (Param_DB_List[i]['VariableName'])

        for item in root:                               #Run a for loop to compare VariableName and the tag/text in the XML file, you enter wizard screen number. 
            if (str(VariableName) == str(item.text)):
                Wizard_Screen = str(item.tag)
                Wizard_Screen_P = VariableName
                Wizard_Screen_Parameter.append(Wizard_Screen)
                Wizard_Screen_Parameter.append(Wizard_Screen_P)
        if VariableName in Wizard_Screen_Parameter:
            writer.writerow([Label, name,Param_ID, Min, Max,DefaultValue, Unit,Wizard_Screen, Visibility, VariableName])

        else:
            writer.writerow([Label, name,Param_ID, Min, Max,DefaultValue, Unit,"", Visibility, VariableName])
             

def main():
    Param_DB_List, result = parseXML()                  #Parsing XML file to get the databse details  
    print("No of parameters in DB is " + (str(len(Param_DB_List))))
    print(result)
    
    writeToCSV(Param_DB_List, "DatabaseEKE.csv")     #store those values in a CSV file
    
    
    
    
    