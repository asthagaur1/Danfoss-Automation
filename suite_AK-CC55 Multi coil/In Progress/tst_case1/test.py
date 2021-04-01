import json
import csv
from pprint import pprint
import datetime
import os
import shutil
import string
import xdrlib
import codecs

def main():
    StorageType_List=[]
    enum_counter =0

    with codecs.open('C:\gitworkspace\TestAutomation-AKCC5XX\Test_Automation\SourceCode\Dependent_Files\Latest_CDF\device.jso',encoding='utf-8') as data_file:
        content = data_file.read()
        content = content.replace(u'\ufeff','') 
        data = json.loads(content)
        Parameter_Count = len(data["Parameters"])
        for a in range (0, Parameter_Count):
            if (data["Parameters"][a]["EnumIdx"] != -1):
                enum_counter = enum_counter +1 
        test.log("No.of Enum Parameters are: "+str(enum_counter))
        
        for i in range (0, Parameter_Count):
            Storage_Type = data["Parameters"][i]["StorageType"]
            if (data["Parameters"][i]["EnumIdx"] == -1):
                StorageType_List.append(Storage_Type)
            
        StorageType_Elements = ElementCount(StorageType_List)
        test.log("EL:" +str(StorageType_Elements))
        
        StorageType_4 = StorageType_List.count(4)
        StorageType_7 = StorageType_List.count(7)
        StorageType_2 = StorageType_List.count(2)
        StorageType_9 = StorageType_List.count(9)
        StorageType_3 = StorageType_List.count(3)
        test.log("Int16:"+str(StorageType_4))
        test.log("Real32:"+str(StorageType_7))
        test.log("UInt16:"+str(StorageType_2))
        test.log("String20:"+str(StorageType_9))
        test.log("UInt32:"+str(StorageType_3))
        
        
def ElementCount(StorageType_List):
    counter = 0
    ElementList =[]
    for i in range(0, len(StorageType_List)):
        if (StorageType_List[i] not in ElementList):
            counter=counter+1
            ElementList.append(StorageType_List[i])
    return ElementList               
                
                
                
    
    
    
    
    
    