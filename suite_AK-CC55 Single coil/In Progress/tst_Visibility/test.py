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
    Visibility_Rules()
    Visibile_Parameters()

def Visibility_Rules():
    with codecs.open('C:\gitworkspace\TestAutomation-AKCC5XX\Test_Automation\SourceCode\Dependent_Files\Latest_CDF\device.jso',encoding='utf-8') as data_file:
        content = data_file.read()
        content = content.replace(u'\ufeff','') 
        data = json.loads(content)
        Parameter_Count = len(data["Parameters"])
        Enum_Count = len(data["Enumerations"])
        for j in range (0, Enum_Count):
             Enum_Values = data["Enumerations"][j]["Values"]
        Group_Count = len(data["Groups"])
        
        for i in range (0, Parameter_Count):
            Visibility_Idx = data["Parameters"][i]["VisibilityIdx"]
            
            
    file = "C:\gitworkspace\TestAutomation-AKCC5XX\Test_Automation\SourceCode\Global_scripts\Visib_Result.csv"
    openfile = open(file,'wt') 
    writer = csv.writer(openfile)
    writer.writerow(["PName", "Visibility"])

    with open("C:\\gitworkspace\\TestAutomation-AKCC5XX\\Test_Automation\\SourceCode\\Dependent_Files\\Latest_CDF\\visib.js", "r") as visibility_file:
        vis = visibility_file.readlines()
        vis = str(vis)
        array = []
        for x in vis.split('\\n'):
            array.append(x)
#             print (x)
            myItem = "RuleId"
            if myItem in x:
                array_1 = []
                for y in x.split('return'):
                    #test.log(str(y))
                    
                    if "RuleId" in y: 
                        ##Id is the visibility rule number##
                        Id = ''.join(filter(lambda x: x.isdigit(),y))
#                         test.log(str(y))
#                         test.log(str(Id))
                       
                    if "GetVar" in y:
                        visibleText= ""
                        z = y.replace(";", "")
#                         test.log(str(y))
#                         for z in y.split(" "):
#                             test.log(str(z))
                        if "GetVar" in z:
                            Rule = z.replace("GetVar", "")
#                                 test.log(str(Rule))
                            visibleText += Rule
#                                 Rule_Final = Rule[Rule.find("(")+1:Rule.find(")")]
#                                 test.log(str(Rule_Final))         
#                               
                        else:
                            visibleText += z+" "
#                                 
#                         
#                                 
                        Visibility =  visibleText.strip()    
                          
                    if "GetVar" not in y:
                        z = y.replace(";", "")
#                         if "0" in y:
#                             Visibility = "0"
#                         else:
                        Visibility = z 
#                     test.log(str(Visibility))   
                    
                for i in range (0, Parameter_Count):
                    Visibility_Idx = data["Parameters"][i]["VisibilityIdx"]
#                     Param_Name = data["Parameters"][i]["Text"]
                    
                    for j in range (0, len(Enum_Values)):
                        if(i==j):
                            Enum_Visibility_Idx = Enum_Values[i]["VisibilityIdx"]
#                             Enum_Name = Enum_Values[i]["Text"] 
                            
                    for k in range (0, Group_Count):
                        if (i == k):
                            Group_Visibility_Idx = data["Groups"][i]["VisibilityIdx"]
#                             Group_Name = data["Groups"][i]["Text"]
                            
                    if (str(Id) == str(Visibility_Idx)):
                        writer.writerow([str(Id), str(Visibility)])
                        break
                    
                    elif (str(Id) == str(Enum_Visibility_Idx)):
                        writer.writerow([str(Id), str(Visibility)])
                        break
                    
                    elif (str(Id) == str(Group_Visibility_Idx)):
                        writer.writerow([str(Id), str(Visibility)])
                        break
                    
def Visibile_Parameters():
    with codecs.open('C:\gitworkspace\TestAutomation-AKCC5XX\Test_Automation\SourceCode\Dependent_Files\Latest_CDF\device.jso',encoding='utf-8') as data_file:
        content = data_file.read()
        content = content.replace(u'\ufeff','') 
        data = json.loads(content)
        Parameter_Count = len(data["Parameters"])
        Enum_Count = len(data["Enumerations"])
#         for j in range (0, Enum_Count):
#              Enum_Values = data["Enumerations"][j]["Values"]
        Group_Count = len(data["Groups"])
        
    file_1 = r"C:\gitworkspace\TestAutomation-AKCC5XX\Test_Automation\SourceCode\Global_scripts\Visible_Parameters.csv"
    file = r"C:\gitworkspace\TestAutomation-AKCC5XX\Test_Automation\SourceCode\Global_scripts\Visib_Result.csv"
    
    openfile = open(file_1,'wt') 
    writer = csv.writer(openfile)
    writer.writerow(["ID","Rule", "Param/Enum/Groups"])
    
    records = testData.dataset(file)       
    for rec in records:
            Visib_Idx = testData.field(rec, 0)
            Visib_Rule = testData.field(rec, 1)
            
            for i in range (0, Parameter_Count):
                
                if (Visib_Idx == data["Parameters"][i]["VisibilityIdx"]):
                    Param_Name = data["Parameters"][i]["Text"]
                    writer.writerow([str(Visib_Idx), str(Visib_Rule), str(Param_Name)])
            
            for j in range (0, Enum_Count):
                Enum_Values = data["Enumerations"][j]["Values"]
                for j_1 in range (0, len(Enum_Values)):
                    if (Visib_Idx == Enum_Values[j_1]["VisibilityIdx"]):
                        Enum_Name = Enum_Values[j_1]["Text"]
                        writer.writerow([str(Visib_Idx), str(Visib_Rule), str(Enum_Name)])
                    
            for k in range (0, Group_Count):
                if (Visib_Idx == data["Groups"][k]["VisibilityIdx"]):
                    Group_Name = data["Groups"][k]["Text"]
                    writer.writerow([str(Visib_Idx), str(Visib_Rule), str(Group_Name)])
                    
            
                                    