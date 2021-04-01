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
    minval = None
    test.log(str(type(minval)))
    dictA={1:"A", 2:"B", 3:"C"}
    dictB = {1:"D", 2:"E", 3:"C"}
    for i in dictA.keys():
        for j in dictB.keys():
            if (i == j) :
                test.log(str(dictA[i]))
            else: 
                test.log("Check again")
    word = "9.88"
    word = float(word)
    test.log(str(type(word)))
    
    
#     a = "GetVar(184) != 7 and GetVar(184) != 8"
#     result = eval(a)
#     test.log("Result is:"+str(result))
          
# def GetVar(val):
#     with codecs.open(findFile("testdata", r"\Latest_CDF\device.jso"),encoding='utf-8') as data_file:
#         content = data_file.read()
#         content = content.replace(u'\ufeff','') 
#         data = json.loads(content)
#         Parameter_Count = len(data["Parameters"])
#         for i in range (0, Parameter_Count):
#             Index = data["Parameters"][i]["Idx"]
#             if (Index == val):
#                 default = data["Parameters"][i]["Default"]
#                 
#     