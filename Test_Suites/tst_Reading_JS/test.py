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
    with codecs.open(findFile("scripts", r"C:\gitworkspace\KoolProg-TestAutomation\Master_Functions\Test_Automation\SourceCode\suite_MasterCase\shared\testdata\Latest_CDF\visib.js"),encoding='utf-8') as data_file:
#         test.log(str(data_file))
        content = data_file.read()
        content = content.replace(u'\ufeff','') 
        data = read
        test.log(str(data))