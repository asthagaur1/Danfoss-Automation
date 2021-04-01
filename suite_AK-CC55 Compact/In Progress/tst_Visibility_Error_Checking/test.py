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
    result = False
    with codecs.open('C:\gitworkspace\TestAutomation-AKCC5XX\Test_Automation\SourceCode\Dependent_Files\Latest_CDF\device.jso',encoding='utf-8') as data_file:
        content = data_file.read()
        content = content.replace(u'\ufeff','') 
        data = json.loads(content)
        Parameter_Count = len(data["Parameters"])
   
        x = "(RuleId == 23) return GetVar(189) != 6 && GetVar(189) != 7 && GetVar(138) == 1 && ((GetVar(199) == 7) || (GetVar(200) == 7) || (GetVar(201) == 7))"
        myItem = "RuleId"
        if myItem in x:
            array_1 = []
            for y in x.split('return'):
                if "RuleId" in y: 
                    Id = ''.join(filter(lambda x: x.isdigit(),y))
                   
                if "GetVar" in y:
                    visibleText= ""
                    y = y.replace(";", "")
                    for z in y.split(" "):
                        if "GetVar(" in z:
                            Rule = z.replace("GetVar(", "").replace(")", "")
    
                            if "(" in Rule:
                                test.log("IF "+str(Rule))
                                Rule = Rule.replace("(", "")
                                test.log("IF2 "+str(Rule))
                                for i in range (0, Parameter_Count):
                                    Rule_Idx = data["Parameters"][i]["Idx"]
                                    if (Rule == str(Rule_Idx)):
                                        Rule_Idx_ID = data["Parameters"][Rule_Idx]["UniqueID"]
                                        visibleText += "(Id_"+str(Rule_Idx_ID)+" "
                                        
                                    
                            else:
                                test.log("ELSE "+str(Rule))
                                for i in range (0, Parameter_Count):
                                    Rule_Idx = data["Parameters"][i]["Idx"]
                                    if (Rule == str(Rule_Idx)):
                                        Rule_Idx_ID = data["Parameters"][Rule_Idx]["UniqueID"]
                                        visibleText += "Id_"+str(Rule_Idx_ID)+" "
                        
                        else:
                            visibleText += z+" "
        
        