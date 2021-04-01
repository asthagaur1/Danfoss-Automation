import os
import exceptions
import sys
import glob
import csv
import random
import __builtin__
import datetime
import shutil

def main():
#     st = "hello"
#     test.log(str(st[2::]))
#     text = "Address: C:\KoolProg\Configurations"
#     text = text.replace("Address: ", "")
#     test.log(str(text))
#     test.log("This has more than 20 characters 123@#{}]"[0:20])
#     ab = "AK-CC55 Compact"
#     res = ab[8::]
#     test.log(str(res))


#     startApplication("KoolProg")
#     mouseClick(waitForObject(":KoolProg_Image"))
#     mouseClick(waitForObject(":SetParameters_List_3"))
#     mouseClick(waitForObject(":System.Windows.Controls.StackPanel.Import controller model_Label"))
#     box = waitForObject("{type='Toolbar'}")
#     type(box, "<F4>")
#     type(box, "<Ctrl+A>")
#     type(box , "C:\KoolProg\Configurations")
#     type(box , "<Return>")
#     snooze(10)
    #mouseClick(waitForObject(":Open_Dialog"), 1290, 9, MouseButton.PrimaryButton)
    


    startApplication("KoolProg")
    mouseClick(waitForObject(":KoolProg_Window"), 902, 872, MouseButton.PrimaryButton)
    
    mouseClick(waitForObject("{container=':KoolProg_Window' name='btnCopytocontroller' text='System.Windows.Controls.DockPanel' type='Button'}"))
    mouseClick(waitForObject(":KoolProg.BROWSE_Button"), MouseButton.PrimaryButton)
#     mouseClick(waitForObject(":_List"))
    box = waitForObject("{type='Toolbar'}")
    type(box, "<F4>")
    type(box, "<Ctrl+A>")
    type(box , "C:\KoolProg\Configurations")
    type(box , "<Return>")
    snooze(10)
    

#     minVal = float("0.88")
#     maxVal = float("10.9")
# 
#     itemVal = random.uniform(minVal, maxVal)
#     itemVal = int(itemVal)
#     print (itemVal)
#     
#     val_a = "9.88"
#     val_b = "1.9"
#     val_new = float(val_a)
#     val_new_1 = float(val_b)
#     
#     rand_val = random.uniform(val_new, val_new_1)
#     val_new = int(val_new)
#     print(type(val_new))
#     test.log(str(val_new))
#     val_new_1 = int(val_new_1)
#     print (type(val_new_1))
#     test.log(str(val_new_1))
#     test.log(str(rand_val))
# define the name of the directory to be deleted
#     path = "C:\KoolProg\Configurations\New folder"
#     
#     try:  
#         shutil.rmtree(path)
#     except OSError:  
#         test.log ("Deletion of the directory %s failed" % str(path))
#     else:  
#         test.log ("Successfully deleted the directory %s" % str(path))
