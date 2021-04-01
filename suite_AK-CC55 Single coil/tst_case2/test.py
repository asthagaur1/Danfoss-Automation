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
   with codecs.open(findFile("testdata", r"\Latest_CDF\device.jso"),encoding='utf-8') as data_file:
       content = data_file.read()
       content = content.replace(u'\ufeff','') 
       data = json.loads(content)
       Groups = data["Groups"]
       Group_Count = len(data["Groups"])
       QuickWizard_Group = data["Groups"][Group_Count-1]
       QuickWizard_Group_Count = len(QuickWizard_Group)
       test.log(str(QuickWizard_Group_Count))                           
       print (type(QuickWizard_Group_Count))
       for j in range (0,QuickWizard_Group_Count):
           QW = QuickWizard_Group[j]["Items"]
           print(QW)
       