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
#print now.strftime("%d-%m-%Y_%H_%M")
Timestr = now.strftime("%d-%m-%Y_%H_%M")


def main():
    source(findFile("scripts", "Global_scripts"));
#     Parse_Json()
#     Moving_Files()

    file = "Danfoss.AK-CC_550_Parameters.csv"
    records = testData.dataset(file)
    for j in range(0,10):
       for rec in records:
           Unique_ID = testData.field(rec, 0)
           name = testData.field(rec, 1)
           enum = testData.field(rec,2) 

def Parse_Json():
    
    with codecs.open('device.jso',encoding='utf-8') as data_file:
        content = data_file.read()
        content = content.replace(u'\ufeff','') 
        data = json.loads(content)
        Parameter_Count = len(data["Parameters"])
        #print (count)
        
        Alarm_List = data["Alarms"]
        Alarm_List_count = len(Alarm_List)
        
        
        Enum_List = data["Enumerations"]
        Enum_List_count = len(data["Enumerations"])
        
        Unit_List = data["EngUnitTypes"]
        Unit_List_count = len(data["EngUnitTypes"])
        
        Groups_List = data["Groups"]
        Groups_List_count = len(data["Groups"])#print (Groups_List_count)
        IO_Config = data["IOConfig"]
        IO_Config_count = len(data["IOConfig"])