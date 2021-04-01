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
from timeit import time

global File_Path

#from datetime import datetime
now = datetime.datetime.now()
#print now.strftime("%d-%m-%Y_%H_%M")
Timestr = now.strftime("%d-%m-%Y_%H_%M")

gControl=None

def TimedWait(value):
    test.log("Entered Timed Wait - Time in seconds")
    time.sleep(float(value))
    test.log("Exited Timed Wait - "+str(value)+" seconds as passed")
    

def Factory_Reset_Online(): 
   test.log("inside factory reset online")
   result = False
   global File_Copy_Textbox
   test.compare(waitForObjectExists(":KoolProg_Table").type, "Table")
   test.compare(waitForObjectExists(":KoolProg_Table").name, "datagridParameters")
  
   window=waitForObject(":KoolProg_Window")
   print("count:%s"% len(window))
   
   ############### right side controller name
   
   name1=getControl(window,"Label","txtProuctName")  
   if(name1 == None):
       print "None"
   else:    
       #test.log("type:%s "% name1["type"])
       #test.log("name:%s "% name1["name"])
       #test.log("text:%s "% name1["text"])
       Controller = (name1["text"]) 
       #test.log("right side controller name is "+Controller)
       #test.log(Controller) 
       #test.log(Controller [0:3]) 
       #test.log(Controller [0:4]) 
       #test.log(Controller [0:6]) 
   
   ################### right side code number or application name
       
   if ((Controller [0:4]== "ERC1") | (Controller [0:3]== "EET")):
       name2=getControl(window,"Label","txtCodeNumber")  
       if(name2 == None):
           print "None"
       else:    
           #test.log("type:%s "% name2["type"])
           #test.log("name:%s "% name2["name"])
           #test.log("text:%s "% name2["text"])
           Code_Number = (name2["text"])
           test.log("right side code number is "+Code_Number)
           #test.log(Code_Number)
   else:       
       name2=getControl(window,"Label","txtApp")  
       if(name2 == None):
           print "None"
       else:    
           test.log("type:%s "% name2["type"])
           test.log("name:%s "% name2["name"])
           test.log("text:%s "% name2["text"])
           Application = (name2["text"])
           test.log("application name")
           test.log (Application)
       
   if (Controller[0:3] == "ETC"):
       ETC_App_List = ['STANDARD', 'GDM101', 'DUALBAND102', 'DOUBLEDOOR', 'WINECOOLER', 'MEDICINECOOLER', 'COND101', 'DUALDEFROST']
       count = len(ETC_App_List)
       for i in range (0, count):
           file = Global_Scripts_Path+"\Danfoss.ETC1H."+Application+"_DB.csv"
           file_1= "Result_Sheet_"+Application+".csv"
           tbl=waitForObjectExists(":KoolProg_Table")
           items=tbl.nativeObject.Items
   
           openfile = open(file_1,'wt') 
           writer = csv.writer(openfile)
           writer.writerow(["ParameterName", "DB_Menucode","KP_Menucode","Result" ,"DB_DefaultValue", "KP_DefaultValue", "Result", "DB_MinValue", "KP_MinValue", "Result" ,"DB_MaxValue", "KP_MaxValue", "Result", "DB_Unit", "KP_Unit", "Result", "DB_Info", "KP_Info", "Result"])
           records = testData.dataset(file)
           for rec in records:
               id = testData.field(rec, 0)
               name = testData.field(rec, 1)
               Default = testData.field(rec, 2)
               Min = testData.field(rec, 3)
               Max = testData.field(rec, 4)
               Unit = testData.field(rec, 5) 
               Enum = testData.field(rec, 6)
               Info_Help = testData.field(rec, 7)
               mylist=[]
               if(Enum != ""):
                   for x in Enum.split(','):
                       for y in x.split(':'): 
                           if(y == Default):                        
                               for z in x.split(':'):
                                   mylist.append(z)
                                   Default = z 
               
#                 for i in range (0, items.Count-1):
#                     item=items.at(i)
#                     if (name == item.ParameterName): 
#                         test.log(item.ParameterName)       
#                         MenuCode_Result = test.compare((id).strip(), (item.MenuCode).strip())
#                         MinValue_Result = test.compare((Min).strip(), (item.Minvalue).strip())
#                         MaxValue_Result = test.compare((Max).strip(), (item.Maxvalue).strip())
#                         Unit_Result = test.compare((Unit).strip(), (item.Unit).strip())
#                         Help_Result = test.compare((Info_Help).strip(), (item.Description).strip())
#                         writer.writerow([item.ParameterName,id, item.MenuCode, MenuCode_Result, Default, item.DefaultValue, DefaultValue_Result, Min, item.Minvalue, MinValue_Result, Max, item.Maxvalue, MaxValue_Result, Unit, item.Unit, Unit_Result, Info_Help, item.Description, Help_Result])            
# 

           for i in range (0, items.Count-1):
               item=items.at(i)
               if (name == item.ParameterName):
                   test.log(item.ParameterName)        
                   MenuCode_Result = test.compare((id).strip(), (item.MenuCode).strip())
                   if '.00' in item.DefaultValue:
                           num,dec=item.DefaultValue.split(".")
                           DefaultValue_Result = test.compare((Default).strip(), (num).strip())
                   else:
                           DefaultValue_Result = test.compare((Default).strip(), (item.DefaultValue).strip()) 
                   if '.00' in item.Minvalue:
                           num,dec=item.Minvalue.split(".")
                           MinValue_Result = test.compare((Min).strip(), (num).strip())
                   else:
                           MinValue_Result = test.compare((Min).strip(), (item.Minvalue).strip())
                   if '.00' in item.Maxvalue:
                           num,dec=item.Maxvalue.split(".")
                           MaxValue_Result = test.compare((Max).strip(), (num).strip())
                   else:
                           MaxValue_Result = test.compare((Max).strip(), (item.Maxvalue).strip())
                   Unit_Result = test.compare((Unit).strip(), (item.Unit).strip())
                   Help_Result = test.compare((Info_Help).strip(), (item.Description).strip())
                   writer.writerow([item.ParameterName,id, item.MenuCode, MenuCode_Result, Default, item.DefaultValue, DefaultValue_Result, Min, item.Minvalue, MinValue_Result, Max, item.Maxvalue, MaxValue_Result, Unit, item.Unit, Unit_Result, Info_Help, item.Description, Help_Result])            
                   break            
           
   elif (Controller[0:4] == "ERC2"):
       ERCWS_App_List = ['App0', 'App1', 'App2', 'App3', 'App4', 'App5', 'App6']
       count = len(ERCWS_App_List)
       for i in range (0, count):
           file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_DB.csv"
           file_1= "Result_Sheet_"+Application+".csv"
                   
           tbl=waitForObjectExists(":KoolProg_Table")
           items=tbl.nativeObject.Items
           
           openfile = open(file_1,'wt') 
           writer = csv.writer(openfile)
           writer.writerow(["ParameterName", "DB_Menucode","KP_Menucode","Result" ,"DB_DefaultValue", "KP_DefaultValue", "Result", "DB_MinValue", "KP_MinValue", "Result" ,"DB_MaxValue", "KP_MaxValue", "Result", "DB_Unit", "KP_Unit", "Result", "DB_Info", "KP_Info", "Result"])
   
           records = testData.dataset(file)
           for rec in records:
               id = testData.field(rec, 0)
               name = testData.field(rec, 1)
               if (Application == "App0"):
                   Default = testData.field(rec, 2)
               elif (Application == "App1"):
                   Default = testData.field(rec, 3)
               elif (Application == "App2"):
                   Default = testData.field(rec, 4)
               elif (Application == "App3"):
                   Default = testData.field(rec, 5)
               elif (Application == "App4"):
                   Default = testData.field(rec, 6)
               elif (Application == "App5"):
                   Default = testData.field(rec, 7)
               elif (Application == "App6"):
                   Default = testData.field(rec, 8)
               Min = testData.field(rec, 9)
               Max = testData.field(rec, 10)
               Unit = testData.field(rec, 11) 
               Enum = testData.field(rec, 12)
               Info_Help = testData.field(rec, 13)
               mylist=[]
               if(Enum != ""):
                   for x in Enum.split(','):
                       for y in x.split(':'): 
                           if(y == Default):                        
                               for z in x.split(':'):
                                   mylist.append(z)
                                   Default = z 
               
#                 for i in range (0, items.Count-1):
#                     item=items.at(i)
#                     if (name == item.ParameterName):    
#                         test.log(item.ParameterName)    
#                         MenuCode_Result = test.compare((id).strip(), (item.MenuCode).strip())
#                         DefaultValue_Result = test.compare((Default).strip(), (item.DefaultValue).strip())
#                         MinValue_Result = test.compare((Min).strip(), (item.Minvalue).strip())
#                         MaxValue_Result = test.compare((Max).strip(), (item.Maxvalue).strip())
#                         Unit_Result = test.compare((Unit).strip(), (item.Unit).strip())
#                         Help_Result = test.compare((Info_Help).strip(), (item.Description).strip())
#                         writer.writerow([item.ParameterName,id, item.MenuCode, MenuCode_Result, Default, item.DefaultValue, DefaultValue_Result, Min, item.Minvalue, MinValue_Result, Max, item.Maxvalue, MaxValue_Result, Unit, item.Unit, Unit_Result, Info_Help, item.Description, Help_Result])                        
#         

           for i in range (0, items.Count-1):
               item=items.at(i)
               if (name == item.ParameterName):
                   test.log(item.ParameterName)        
                   MenuCode_Result = test.compare((id).strip(), (item.MenuCode).strip())
                   if '.00' in item.DefaultValue:
                           num,dec=item.DefaultValue.split(".")
                           DefaultValue_Result = test.compare((Default).strip(), (num).strip())
                   else:
                           DefaultValue_Result = test.compare((Default).strip(), (item.DefaultValue).strip()) 
                   if '.00' in item.Minvalue:
                           num,dec=item.Minvalue.split(".")
                           MinValue_Result = test.compare((Min).strip(), (num).strip())
                   else:
                           MinValue_Result = test.compare((Min).strip(), (item.Minvalue).strip())
                   if '.00' in item.Maxvalue:
                           num,dec=item.Maxvalue.split(".")
                           MaxValue_Result = test.compare((Max).strip(), (num).strip())
                   else:
                           MaxValue_Result = test.compare((Max).strip(), (item.Maxvalue).strip())
                   Unit_Result = test.compare((Unit).strip(), (item.Unit).strip())
                   Help_Result = test.compare((Info_Help).strip(), (item.Description).strip())
                   writer.writerow([item.ParameterName,id, item.MenuCode, MenuCode_Result, Default, item.DefaultValue, DefaultValue_Result, Min, item.Minvalue, MinValue_Result, Max, item.Maxvalue, MaxValue_Result, Unit, item.Unit, Unit_Result, Info_Help, item.Description, Help_Result])            
                   break

   elif (Controller [0:4] == "ERC1"):
       name2=getControl(window,"Label","txtApp")  
       if(name2 == None):
           print "None"
       else:    
#            test.log("type:%s "% name2["type"])
#            test.log("name:%s "% name2["name"])
#            test.log("text:%s "% name2["text"])
           Product_Version = (name2["text"])
           
       if (Controller[0:6] == "ERC111"):
           if (Code_Number == "080G3237")| (Code_Number == "080G3247")|(Code_Number == "080G3234"):
               file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_"+Code_Number+"_"+Product_Version+"_DB.csv"
               file_1= "Result_Sheet_"+Code_Number+"-"+Product_Version+".csv"
           else:
               file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_std_DB.csv"
               file_1= "Result_Sheet_"+Code_Number+"-"+Product_Version+".csv"
               
       elif(Controller[0:6] == "ERC112"):
           if ((Code_Number == "080G3202")|(Code_Number == "080G3203")|(Code_Number == "080G3206")|(Code_Number == "080G3207")|(Code_Number == "080G3212")|(Code_Number == "080G3213")|(Code_Number == "080G3216")|(Code_Number == "080G3217"))&(Product_Version == "PV03"):##ALL STD CODE NUMBERS WITH MAINTENANCE DATABSE##
               file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_M_"+Product_Version+"_DB.csv"
               file_1= "Result_Sheet_"+Code_Number+"-"+Product_Version+".csv"
               
           elif (Code_Number == "080G3221")|(Code_Number == "080G3248")|(Code_Number == "080G3276")|(Code_Number == "080G3259"):
               file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_"+Code_Number+"_"+Product_Version+"_DB.csv"
               file_1= "Result_Sheet_"+Code_Number+"-"+Product_Version+".csv"
           
           elif (Code_Number == "080G3408")|(Code_Number == "080G3409")|(Code_Number == "080G3410")|(Code_Number == "080G3414")|(Code_Number == "080G3413")|(Code_Number == "080G3419"): ##SPECIAL CODE NUMBERS##, ##3408 uses 112M DB, but PV version is PV01, hence added here##
               file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_"+Code_Number+"_"+Product_Version+"_DB.csv"
               file_1= "Result_Sheet_"+Code_Number+"-"+Product_Version+".csv"
           
           elif (Code_Number == "080G3220")|(Code_Number == "080G3243"):##COMMON DB_3220##
               file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_080G3220_DB.csv"
               file_1= "Result_Sheet_"+Code_Number+"-"+Product_Version+".csv"
               
           elif (Code_Number == "080G3229")|(Code_Number == "080G3274"):##COMMON DB_3229##
               file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_080G3229_DB.csv"
               file_1= "Result_Sheet_"+Code_Number+"-"+Product_Version+".csv"
               
           elif (Code_Number == "080G3275")|(Code_Number == "080G3239"):##COMMON DB_3275##
               file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_080G3275_DB.csv"
               file_1= "Result_Sheet_"+Code_Number+"-"+Product_Version+".csv"
               
           else:##ALL CODE NUMBERS WITH STANDARD DATABASE##
               file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_std_DB.csv"
               file_1= "Result_Sheet_"+Code_Number+"-"+Product_Version+".csv"
       
       elif (Controller[0:6]== "ERC113"):##ALL STD CODES FOR MAINTENANCE##
           if ((Code_Number == "080G3252")|(Code_Number == "080G3253")|(Code_Number == "080G3406")|(Code_Number == "080G3407"))&(Product_Version == "PV02"):
               file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_M_"+Product_Version+"_DB.csv"
               file_1= "Result_Sheet_"+Code_Number+"-"+Product_Version+".csv"
           
           else:##ALL CODE NUMBERS WITH STANDARD DATABASE##
               file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_std_DB.csv"
               file_1= "Result_Sheet_"+Code_Number+"-"+Product_Version+".csv"
       
       tbl=waitForObjectExists(":KoolProg_Table_3")
       items=tbl.nativeObject.Items
           
       openfile = open(file_1,'wt') 
       writer = csv.writer(openfile)
       writer.writerow(["ParameterName", "DB_Menucode","KP_Menucode","Result" ,"DB_DefaultValue", "KP_DefaultValue", "Result", "DB_MinValue", "KP_MinValue", "Result" ,"DB_MaxValue", "KP_MaxValue", "Result", "DB_Unit", "KP_Unit", "Result", "DB_Info", "KP_Info", "Result"])

       records = testData.dataset(file)
       for rec in records:
           id = testData.field(rec, 0)
           name = testData.field(rec, 1)
           Default = testData.field(rec, 2)
           Min = testData.field(rec, 3)
           Max = testData.field(rec, 4)
           Unit = testData.field(rec, 5) 
           Enum = testData.field(rec, 6)
           Info_Help = testData.field(rec, 7)
           mylist=[]
           if(Enum != ""):
               for x in Enum.split(','):
                   for y in x.split(':'): 
                       if(y == Default):                        
                           for z in x.split(':'):
                               mylist.append(z)
                               Default = z 
           
#             for i in range (0, items.Count-1):
#                 item=items.at(i)
#                 if (name == item.ParameterName):        
#                   test.log(item.ParameterName) 
#                   MenuCode_Result = test.compare((id).strip(), (item.MenuCode).strip())
#                   DefaultValue_Result = test.compare((Default).strip(), (item.DefaultValue).strip())
#                   MinValue_Result = test.compare((Min).strip(), (item.Minvalue).strip())
#                   MaxValue_Result = test.compare((Max).strip(), (item.Maxvalue).strip())
#                   Unit_Result = test.compare((Unit).strip(), (item.Unit).strip())
#                   Help_Result = test.compare((Info_Help).strip(), (item.Description).strip())
#                   writer.writerow([item.ParameterName,id, item.MenuCode, MenuCode_Result, Default, item.DefaultValue, DefaultValue_Result, Min, item.Minvalue, MinValue_Result, Max, item.Maxvalue, MaxValue_Result, Unit, item.Unit, Unit_Result, Info_Help, item.Description, Help_Result])                  
#             

           for i in range (0, items.Count-1):
               item=items.at(i)
               if (name == item.ParameterName):
                   test.log(item.ParameterName)        
                   MenuCode_Result = test.compare((id).strip(), (item.MenuCode).strip())
                   if '.00' in item.DefaultValue:
                           num,dec=item.DefaultValue.split(".")
                           DefaultValue_Result = test.compare((Default).strip(), (num).strip())
                   else:
                           DefaultValue_Result = test.compare((Default).strip(), (item.DefaultValue).strip()) 
                   if '.00' in item.Minvalue:
                           num,dec=item.Minvalue.split(".")
                           MinValue_Result = test.compare((Min).strip(), (num).strip())
                   else:
                           MinValue_Result = test.compare((Min).strip(), (item.Minvalue).strip())
                   if '.00' in item.Maxvalue:
                           num,dec=item.Maxvalue.split(".")
                           MaxValue_Result = test.compare((Max).strip(), (num).strip())
                   else:
                           MaxValue_Result = test.compare((Max).strip(), (item.Maxvalue).strip())
                   Unit_Result = test.compare((Unit).strip(), (item.Unit).strip())
                   Help_Result = test.compare((Info_Help).strip(), (item.Description).strip())
                   writer.writerow([item.ParameterName,id, item.MenuCode, MenuCode_Result, Default, item.DefaultValue, DefaultValue_Result, Min, item.Minvalue, MinValue_Result, Max, item.Maxvalue, MaxValue_Result, Unit, item.Unit, Unit_Result, Info_Help, item.Description, Help_Result])            
                   break
               
   elif (Controller[0:3] == "EET"):
       test.log("inside the EET controller")
       file = Global_Objects_Path+"\Danfoss."+Controller[0:7]+"_"+Code_Number[0:8]+"_DB.csv"
       #test.log(Controller[0:7])
       #test.log(Code_Number[0:8])
       file_1= "Factory_Reset_Generation.csv"
       
       File_Copy_Textbox = file_1
       tbl=waitForObjectExists(":KoolProg_Table")
       items=tbl.nativeObject.Items
          
       openfile = open(file_1,'wt')  
       writer = csv.writer(openfile)
       writer.writerow(["DB_Parameter_Name","KP_Parameter_Name","Result_Parameter_Name","DB_Menu_Code","KP_Menu_Code","Result_Menu_Code" ,"DB_Default_Value", "KP_Default_Value", "Result_Default_Value","DB_Unit", "KP_Unit", "Result_Unit","KP_Text_Old_Value", "", "", ""])

       records = testData.dataset(file)
       
       for rec in records:
           #test.log("inside the loop")
           Menu_Code =testData.field(rec, 0)
           Parameter_Name = testData.field(rec, 1)
           Default = testData.field(rec, 2)
           Min = testData.field(rec, 3)
           Max = testData.field(rec, 4)
           Unit = testData.field(rec, 5) 
           Enum = testData.field(rec, 6)
           Help = testData.field(rec, 7)
           mylist=[]
           if(Enum != ""):
               for x in Enum.split(','):
                   for y in x.split(':'): 
                       if(y == Default):                        
                           for z in x.split(':'):
                               mylist.append(z)
                               Default = z 
                               
           #test.log("outside the loop")     
           for i in range (0, items.Count):
               item=items.at(i)
               #test.log(Parameter_Name)
               #test.log(item.ParameterName)
               if (Parameter_Name == item.ParameterName):
                   #test.log("information of "+item.ParameterName+ " parameter") 
                   Parameter_Name_Result = test.compare((Parameter_Name).strip(), (item.ParameterName).strip())
                   Menu_Code_Result = test.compare((Menu_Code).strip(), (item.MenuCode).strip())
                   if '.00' in item.DefaultValue:
                       num,dec=item.DefaultValue.split(".")
                       Default_Value_Result = test.compare((Default).strip(), (num).strip())
                   else:
                       Default_Value_Result = test.compare((Default).strip(), (item.DefaultValue).strip()) 

                   Unit_Result = test.compare((Unit).strip(), (item.Unit).strip())
                   Help_Result = test.compare((Help).strip(), (item.Description).strip())
                   test.log("default value is "+str(item.Value)+" for "+item.ParameterName+"parameter" )
                   writer.writerow([Parameter_Name,item.ParameterName,Parameter_Name_Result,Menu_Code,item.MenuCode, Menu_Code_Result, Default, item.DefaultValue,Default_Value_Result,Unit,item.Unit,Unit_Result,str(item.Value)])            
                   break
   
   result = True
   return result


def Factory_Reset_Verification_Online(): ## last function name is Value_Verification_New_ETC
    test.log("inside factory reset verification")
    result = False
    tbl=waitForObjectExists(":KoolProg_Table")
    items=tbl.nativeObject.Items
    file= "Factory_Reset_Generation.csv"
    records = testData.dataset(file)
    
    file_1= "Factory_Reset_Verification.csv"
    openfile = open(file_1,'wt')
    writer = csv.writer(openfile)
    writer.writerow(["DB_Parameter_Name","KP_Parameter_Name","Result_Parameter_Name","DB_Menu_Code","KP_Menu_Code","Result_Menu_Code" ,"DB_Default_Value", "KP_Default_Value", "Result_Default_Value","DB_Unit", "KP_Unit", "Result_Unit","KP_Text_Old_Value", "KP_Text_New_Value","DB_DefaultValue", "Result"])
    
    #test.log("outside the loop")
    
    for rec in records:
        #test.log("inside loop")
        DB_Parameter_Name = testData.field(rec, 0)
        #test.log(DB_Parameter_Name)
        KP_Parameter_Name = testData.field(rec, 1) 
        #test.log(KP_Parameter_Name)
        Result_Parameter_Name = testData.field(rec, 2)
        #test.log(Result_Parameter_Name)
        DB_Menu_Code = testData.field(rec, 3)
        #test.log(DB_Menu_Code)
        KP_Menu_Code = testData.field(rec, 4)
        #test.log(KP_Menu_Code)
        Result_Menu_Code = testData.field(rec, 5)
        #test.log(Result_Menu_Code)
        DB_Default = testData.field(rec, 6)
        #test.log(DB_Default)
        KP_Default = testData.field(rec, 7)
        #test.log(KP_Default)
        Result_Default = testData.field(rec, 8)
        #test.log(Result_Default)
        DB_Unit = testData.field(rec, 9)
        #test.log(DB_Unit)
        KP_Unit = testData.field(rec, 10) 
        #test.log(KP_Unit)
        Result_Unit = testData.field(rec, 11)
        #test.log(Result_Unit)
        KP_Textbox_Value = testData.field(rec, 12)
        #test.log(KP_Textbox_Value)
        #test.log("outside the loop1")
        
        for i in range (0, items.Count-1):
            #test.log("inside the loop")
            item=items.at(i)
            #test.log(str(item.Key))
            #test.log(str(item.ParameterName))
            #test.log(str(DB_Parameter_Name))
            if(item.ParameterName == DB_Parameter_Name):
                #test.log("inside if condition")
                if ((item.Datatype == "Enum")|(item.Datatype == "BIT")):
                    writer.writerow([DB_Paramater_Name,KP_Parameter_Name,Result_Parameter_Name,DB_Menu_Code,KP_Menu_Code, Result_Menu_Code, DB_Default, KP_Default, Result_Default, DB_Unit, KP_Unit, Result_Unit, KP_Textbox_Value,item.Value, DB_Default, result])            
                else:
                    #test.log("inside else condition")
                    if '.00' in item.Value:
                        #test.log(str(item.Value))
                        num,dec=item.Value.split(".")
                        #test.log(str(num))
                        #test.log(str(DB_Default))
                        result = test.compare(str(DB_Default.strip()), str(num.strip()))
                    else:
                        result = test.compare((DB_Default).strip(), (item.Value).strip()) 
                    writer.writerow([DB_Parameter_Name,KP_Parameter_Name,Result_Parameter_Name,DB_Menu_Code,KP_Menu_Code, Result_Menu_Code, DB_Default,KP_Default, Result_Default,DB_Unit, KP_Unit, Result_Unit, KP_Textbox_Value, item.Value, DB_Default, result])            
                    result = True
                    #writer.writerow([paramter_name, db_menucode,kp_menucode, result_menu, str(db_default), str(kp_default), result_default, str(db_min), str(kp_min), result_min, str(db_max), str(kp_max), result_max, db_unit, kp_unit, result_unit,db_help, kp_help,result_help, str(kp_textbox_value),db_default,(item.Value), (X)])             
            #else:
                #test.log("error")
    #test.log("loop outside")
    #if(X == True):
        #result = True
    #else:
       #result = False
       
    #return result
    return result

def getControl(control,type,name):
    global gControl    
    if(control["type"] == type and control["name"] == name):
        test.log(str("inside match"))    
        gControl=control 
        return gControl
    
    else:
        #print("inside else")
        children=object.children(control)
        if(children != None):
            for child in children:            
                gControl=getControl(child,type,name)                                        
            

def getName3():
   global name3
   if(name3 == None):        
       window=waitForObject(":KoolProg_Window_0")
       test.log("%s"%len(window))
   else:
       return name3


def Launch():
   test.log("inside launch")
   result = False
   startApplication("KoolProg")
   waitFor("object.exists(':KoolProg_WPFControl')", 20000)
   snooze(2)
   result = True
   return result 


def hasTexts(inputString):
   test.log("inside hastexts")
   result = False
   return any(char.isalpha() for char in inputString)
   result = True 
   return result 


def hasNumbers(inputString):
   test.log("inside hasNumbers")
   result = False
   return any(char.isdigit() for char in inputString)
   result = True 
   return result


def Highted_Folder():
   test.log("inside highlighted folder")
   result = False
   tbl=waitForObjectExists(":Settings.Save Files on:_Edit")  
   tbl_text= tbl.text
   test.log(tbl_text)
   test.log(tbl_text[11:26])
   result = True 
   return result

	
def DataGrid_Verification_Offline():
    test.log("inside datagrid verification offline")
    result = False
    test.compare(waitForObjectExists(":KoolProg_Table").type, "Table")
    test.compare(waitForObjectExists(":KoolProg_Table").name, "datagridParameters")
   
    window=waitForObject(":KoolProg_Window")
    print("count:%s"% len(window))
    
    ########## Left Side Controller Name
    
    name1=getControl(window,"Label","tbProductInfoValue0")  
    if(name1 == None):
        print "None"
        #result = False
    else:
        #test.log("type:%s "% name1["type"])
        #test.log("name:%s "% name1["name"])
        #test.log("text:%s "% name1["text"])
        Controller = (name1["text"])
        test.log("left side controller name is " + Controller)
        #result = True   
        
      ########## Left Side Code Number
    if (Controller [0:7] == "AK-CC55"): 
        name2=getControl(window,"Label","tbProductInfoValue1")  
        if(name2 == None):
            print "None"
        else:
            test.log("left side code number is " +name2["text"] )
            Code_Number = (name2["text"])
            result = True
           
        if (Controller[9::] == "Compact"):
            file = Global_Scripts_Path+"\Danfoss."+Controller[9::]+"_DB.csv"
        elif (Controller[9:13] == "Multi"):
            file = Global_Scripts_Path+"\Danfoss."+Controller[8:13]+"_DB.csv"
        elif (Controller[9:14] == "Single"):
            file = Global_Scripts_Path+"\Danfoss."+Controller[8:14]+"_DB.csv"
        
        file_1= Output_Global_Path+"\Offline_Datagrid_Verification"
        file_1 = file_1 + Code_Number
        file_1 = file_1 + ".csv"
        tbl=waitForObjectExists(":KoolProg_Table")
        items=tbl.nativeObject.Items
        
        openfile = open(file_1,'wt') 
        writer = csv.writer(openfile)
        writer.writerow(["ParameterName", "DB_Menucode","KP_Menucode","Result" ,"DB_DefaultValue", "KP_DefaultValue", "Result", "DB_MinValue", "KP_MinValue", "Result" ,"DB_MaxValue", "KP_MaxValue", "Result", "DB_Unit", "KP_Unit", "Result", "DB_Info", "KP_Info", "Result", "DB_Enum", "KP_Enum", "Result"])
        
        records = testData.dataset(file)
        for rec in records:
            groupCode = testData.field(rec, 0)
            Menu_Code = testData.field(rec, 1)
            Group_Name = testData.field(rec, 2)
            Parameter_Name = testData.field(rec, 3)
            PNU = testData.field(rec, 4)
            Default = testData.field(rec, 5)
            Min = testData.field(rec, 6)
            Max = testData.field(rec, 7)
            Unit = testData.field(rec, 8)
            Scaling = testData.field(rec, 9)
            Datatype = testData.field(rec, 10)
            Enum = testData.field(rec, 11)
            Read_Only =  testData.field(rec, 12)
            Info_Help = testData.field(rec, 13)
            Decimals = testData.field(rec, 14)
            Variable_Name= testData.field(rec, 15)
            mylist=[]
            if(Enum != ""):
                for x in Enum.split(','):
                    for y in x.split(':'): 
                        if(y == Default):                        
                            for z in x.split(':'):
                                mylist.append(z)
                                Default = z 
            
            for i in range (0, items.Count-1):
                item=items.at(i)
                if (Parameter_Name == item.ParameterName):
                    test.log(item.ParameterName)        
                    MenuCode_Result = test.compare((Menu_Code).strip(), (item.MenuCode).stript())
                    DefaultValue_Result = test.compare((Default).strip(), (item.DefaultValue).strip())
                    MinValue_Result = test.compare((Min).strip(), (item.Minvalue).strip())
                    MaxValue_Result = test.compare((Max).strip(), (item.Maxvalue).strip())
                    Enum_Result = test.compare((Enum).strip(), (item.EnumText).strip())
                    Unit_Result = test.compare((Unit).strip(), (item.Unit).strip())
                    Help_Result = test.compare((Info_Help).strip(), (item.Description).strip())
                    writer.writerow([item.ParameterName,Menu_Code, item.MenuCode, MenuCode_Result, Default, item.DefaultValue, DefaultValue_Result, Min, item.Minvalue, MinValue_Result, Max, item.Maxvalue, MaxValue_Result, Unit, item.Unit, Unit_Result, Enum, item.EnumText, Enum_Result])            
                    break
                
    elif (Controller[0:3] == "ETC"):
        name2=getControl(window,"Label","tbProductInfoValue1")  
        if(name2 == None):
            print "None"
            #result = False
        else:    
            Application = (name2["text"])
            #print (Application)
            result = True
        
        ETC_App_List = ['STANDARD', 'GDM101', 'DUALBAND102', 'DOUBLEDOOR', 'WINECOOLER', 'MEDICINECOOLER', 'COND101', 'DUALDEFROST']
        count = len(ETC_App_List)
        for i in range (0, count):
            file = Global_Scripts_Path+"\Danfoss.ETC1H."+Application+"_DB.csv"
            file_1 = "Result_Sheet_"+Application+".csv"
            tbl=waitForObjectExists(":KoolProg_Table")
            items=tbl.nativeObject.Items
    
            openfile = open(file_1,'wt') 
            writer = csv.writer(openfile)
            writer.writerow(["ParameterName", "DB_Menucode","KP_Menucode","Result" ,"DB_DefaultValue", "KP_DefaultValue", "Result", "DB_MinValue", "KP_MinValue", "Result" ,"DB_MaxValue", "KP_MaxValue", "Result", "DB_Unit", "KP_Unit", "Result", "DB_Info", "KP_Info", "Result", "DB_Enum", "KP_Enum", "Result"])
            records = testData.dataset(file)
            for rec in records:
                id = testData.field(rec, 0)
                name = testData.field(rec, 1)
                Default = testData.field(rec, 2)
                Min = testData.field(rec, 3)
                Max = testData.field(rec, 4)
                Unit = testData.field(rec, 5) 
                Enum = testData.field(rec, 6)
                Info_Help = testData.field(rec, 7)
                mylist=[]
                if(Enum != ""):
                    for x in Enum.split(','):
                        for y in x.split(':'): 
                            if(y == Default):                        
                                for z in x.split(':'):
                                    mylist.append(z)
                                    Default = z 
                
                for i in range (0, items.Count-1):
                    item=items.at(i)
                    if (name == item.ParameterName):       
                        test.log(item.ParameterName) 
                        MenuCode_Result = test.compare((id).strip(), (item.MenuCode).strip())
                        DefaultValue_Result = test.compare((Default).strip(), (item.DefaultValue).strip())
                        MinValue_Result = test.compare((Min).strip(), (item.Minvalue).strip())
                        MaxValue_Result = test.compare((Max).strip(), (item.Maxvalue).strip())
                        Enum_Result = test.compare((Enum).strip(), (item.EnumText).strip())
                        Unit_Result = test.compare((Unit).strip(), (item.Unit).strip())
                        Help_Result = test.compare((Info_Help).strip(), (item.Description).strip())
                        writer.writerow([item.ParameterName,id, item.MenuCode, MenuCode_Result, Default, item.DefaultValue, DefaultValue_Result, Min, item.Minvalue, MinValue_Result, Max, item.Maxvalue, MaxValue_Result, Unit, item.Unit, Unit_Result, Info_Help, item.Description, Help_Result, Enum, item.EnumText, Enum_Result])            
            
    elif (Controller[0:4] == "ERC2"):
        name2=getControl(window,"Label","tbProductInfoValue1")  
        if(name2 == None):
            print "None"
            #result = False
        else:    
            #test.log("type:%s "% name2["type"])
            #test.log("name:%s "% name2["name"])
            #test.log("text:%s "% name2["text
            Application = (name2["text"])
            #print (Application)
            result = True
        
        ERCWS_App_List = ['App0', 'App1', 'App2', 'App3', 'App4', 'App5', 'App6']
        count = len(ERCWS_App_List)
        for i in range (0, count):
            file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_DB.csv"
            file_1= "Result_Sheet_"+Application+".csv"
                    
            tbl=waitForObjectExists(":KoolProg_Table")
            items=tbl.nativeObject.Items
            
            openfile = open(file_1,'wt') 
            writer = csv.writer(openfile)
            writer.writerow(["ParameterName", "DB_Menucode","KP_Menucode","Result" ,"DB_DefaultValue", "KP_DefaultValue", "Result", "DB_MinValue", "KP_MinValue", "Result" ,"DB_MaxValue", "KP_MaxValue", "Result", "DB_Unit", "KP_Unit", "Result", "DB_Info", "KP_Info", "Result", "DB_Enum","KP_Enum", "Result" ])
    
            records = testData.dataset(file)
            for rec in records:
                id = testData.field(rec, 0)
                name = testData.field(rec, 1)
                if (Application == "App0"):
                    Default = testData.field(rec, 2)
                elif (Application == "App1"):
                    Default = testData.field(rec, 3)
                elif (Application == "App2"):
                    Default = testData.field(rec, 4)
                elif (Application == "App3"):
                    Default = testData.field(rec, 5)
                elif (Application == "App4"):
                    Default = testData.field(rec, 6)
                elif (Application == "App5"):
                    Default = testData.field(rec, 7)
                elif (Application == "App6"):
                    Default = testData.field(rec, 8)
                Min = testData.field(rec, 9)
                Max = testData.field(rec, 10)
                Unit = testData.field(rec, 11) 
                Enum = testData.field(rec, 12)
                Info_Help = testData.field(rec, 13)
                mylist=[]
                if(Enum != ""):
                    for x in Enum.split(','):
                        for y in x.split(':'): 
                            if(y == Default):                        
                                for z in x.split(':'):
                                    mylist.append(z)
                                    Default = z 
                
                for i in range (0, items.Count-1):
                    item=items.at(i)
                    if (name == item.ParameterName):        
                        test.log(item.ParameterName) 
                        MenuCode_Result = test.compare((id).strip(), (item.MenuCode).strip())
                        DefaultValue_Result = test.compare((Default).strip(), (item.DefaultValue).strip())
                        MinValue_Result = test.compare((Min).strip(), (item.Minvalue).strip())
                        MaxValue_Result = test.compare((Max).strip(), (item.Maxvalue).strip())
                        Enum_Result = test.compare((Enum).strip(), (item.EnumText).strip())
                        Unit_Result = test.compare((Unit).strip(), (item.Unit).strip())
                        Help_Result = test.compare((Info_Help).strip(), (item.Description).strip())
                        writer.writerow([item.ParameterName,id, item.MenuCode, MenuCode_Result, Default, item.DefaultValue, DefaultValue_Result, Min, item.Minvalue, MinValue_Result, Max, item.Maxvalue, MaxValue_Result, Unit, item.Unit, Unit_Result, Info_Help, item.Description, Help_Result, Enum, item.EnumText, Enum_Result])            
    
    elif (Controller [0:4] == "ERC1"): ##Added by Aashika## - 3.4.25.x
        name2=getControl(window,"Label","tbProductInfoValue1")  
        if(name2 == None):
            print "None"
            #result = False
        else:    
            #test.log("type:%s "% name2["type"])
            #test.log("name:%s "% name2["name"])
            #test.log("text:%s "% name2["text"])
            test.log("left side code number is " +name2["text"] )
            Code_Number = (name2["text"])
            #print (Application)
            result = True
            
        name3=getControl(window,"Label","tbProductInfoValue3")  
        if(name3 == None):
            print "None"
            #result = False
        else:    
            #test.log("type:%s "% name2["type"])
            #test.log("name:%s "% name2["name"])
            #test.log("text:%s "% name2["text"])
            Product_Version = (name2["text"])
            #print (Application)
            result = True
        if (Controller[0:6] == "ERC111"):
            if (Code_Number == "080G3237")| (Code_Number == "080G3247")|(Code_Number == "080G3234"):
                file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_"+Code_Number+"_"+Product_Version+"_DB.csv"
                file_1= "Result_Sheet_"+Code_Number+"-"+Product_Version+".csv"
            else:
                file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_std_DB.csv"
                file_1= "Result_Sheet_"+Code_Number+"-"+Product_Version+".csv"
                
        elif(Controller[0:6] == "ERC112"):
            if ((Code_Number == "080G3202")|(Code_Number == "080G3203")|(Code_Number == "080G3206")|(Code_Number == "080G3207")|(Code_Number == "080G3212")|(Code_Number == "080G3213")|(Code_Number == "080G3216")|(Code_Number == "080G3217"))&(Product_Version == "PV03"):##ALL STD CODE NUMBERS WITH MAINTENANCE DATABSE##
                file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_M_"+Product_Version+"_DB.csv"
                file_1= "Result_Sheet_"+Code_Number+"-"+Product_Version+".csv"
                
            elif (Code_Number == "080G3221")|(Code_Number == "080G3248")|(Code_Number == "080G3276")|(Code_Number == "080G3259"):
                file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_"+Code_Number+"_"+Product_Version+"_DB.csv"
                file_1= "Result_Sheet_"+Code_Number+"-"+Product_Version+".csv"
            
            elif (Code_Number == "080G3408")|(Code_Number == "080G3409")|(Code_Number == "080G3410")|(Code_Number == "080G3414")|(Code_Number == "080G3413")|(Code_Number == "080G3419"): ##SPECIAL CODE NUMBERS##, ##3408 uses 112M DB, but PV version is PV01, hence added here##
                file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_"+Code_Number+"_"+Product_Version+"_DB.csv"
                file_1= "Result_Sheet_"+Code_Number+"-"+Product_Version+".csv"
            
            elif (Code_Number == "080G3220")|(Code_Number == "080G3243"):##COMMON DB_3220##
                file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_080G3220_DB.csv"
                file_1= "Result_Sheet_"+Code_Number+"-"+Product_Version+".csv"
                
            elif (Code_Number == "080G3229")|(Code_Number == "080G3274"):##COMMON DB_3229##
                file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_080G3229_DB.csv"
                file_1= "Result_Sheet_"+Code_Number+"-"+Product_Version+".csv"
                
            elif (Code_Number == "080G3275")|(Code_Number == "080G3239"):##COMMON DB_3275##
                file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_080G3275_DB.csv"
                file_1= "Result_Sheet_"+Code_Number+"-"+Product_Version+".csv"
                
            else:##ALL CODE NUMBERS WITH STANDARD DATABASE##
                file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_std_DB.csv"
                file_1= "Result_Sheet_"+Code_Number+"-"+Product_Version+".csv"
        
        elif (Controller[0:6]== "ERC113"):##ALL STD CODES FOR MAINTENANCE##
            if ((Code_Number == "080G3252")|(Code_Number == "080G3253")|(Code_Number == "080G3406")|(Code_Number == "080G3407"))&(Product_Version == "PV02"):
                file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_M_"+Product_Version+"_DB.csv"
                file_1= "Result_Sheet_"+Code_Number+"-"+Product_Version+".csv"
            
            elif ((Code_Number == "080G0993")&(Product_Version == "PV01")):##ADDED FOR TREU - Aashika##
                file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_"+Code_Number+"_"+Product_Version+"_DB.csv"
                file_1= "Result_Sheet_"+Code_Number+"-"+Product_Version+".csv"
            
            else:##ALL CODE NUMBERS WITH STANDARD DATABASE##
                file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_std_DB.csv"
                file_1= "Result_Sheet_"+Code_Number+"-"+Product_Version+".csv"
        
        #test.log("after if condition")
        tbl=waitForObjectExists(":KoolProg_Table")
        items=tbl.nativeObject.Items    
        openfile = open(file_1,'wt') 
        writer = csv.writer(openfile)
        #test.log("after if condition 1")
        
        writer.writerow(["ParameterName", "DB_Menucode","KP_Menucode","Result" ,"DB_DefaultValue", "KP_DefaultValue", "Result", "DB_MinValue", "KP_MinValue", "Result" ,"DB_MaxValue", "KP_MaxValue", "Result", "DB_Enum", "KP_Enum", "Result", "DB_Unit", "KP_Unit", "Result", "DB_Info", "KP_Info", "Result"])
        #test.log("after if condition 2")
        records = testData.dataset(file)
        for rec in records:
            #test.log("inside data file")
            Menu_Code = testData.field(rec, 0)
            Parameter_Name = testData.field(rec, 1)
            Default = testData.field(rec, 2)
            Min = testData.field(rec, 3)
            Max = testData.field(rec, 4)
            Unit = testData.field(rec, 5) 
            Enum = testData.field(rec, 6)
            Help = testData.field(rec, 7)
            mylist=[]
            if(Enum != ""):
                for x in Enum.split(','):
                    for y in x.split(':'): 
                        if(y == Default):                        
                            for z in x.split(':'):
                                mylist.append(z)
                                Default = z 
            #test.log("inside2")
            for i in range (0, items.Count):
                item=items.at(i)
                #test.log(Parameter_Name)
                #test.log(item.ParameterName)
                if (Menu_Code == item.MenuCode):        
    #                 test.log("information of "+item.ParameterName+ " parameter") 
                    #Group_Name_Result = test.compare((Group_Name).strip(), (item.GroupName).strip())
                    #GroupCode_Result = test.compare((Group_Code).strip(), (item.GroupCode).strip())
                    Parameter_Name_Result = test.compare((Parameter_Name).strip(), (item.ParameterName).strip())
                    Menu_Code_Result = test.compare((Menu_Code).strip(), (item.MenuCode).strip())
                    if '.00' in item.DefaultValue:
                            num,dec=item.DefaultValue.split(".")
                            Default_Value_Result = test.compare((Default).strip(), (num).strip())
                    else:
                            #test.log(Parameter_Name)
                            #test.log(item.ParameterName)
                            #test.log(Default)
                            Default_Value_Result = test.compare((Default).strip(), (item.DefaultValue).strip()) 
                    if '.00' in item.Minvalue:
                            num,dec=item.Minvalue.split(".")
                            Min_Value_Result = test.compare((Min).strip(), (num).strip())
                    else:
                            Min_Value_Result = test.compare((Min).strip(), (item.Minvalue).strip())
                    if '.00' in item.Maxvalue:
                            num,dec=item.Maxvalue.split(".")
                            Max_Value_Result = test.compare((Max).strip(), (num).strip())
                    else:
                            Max_Value_Result = test.compare((Max).strip(), (item.Maxvalue).strip())
                            
                         
                    Enum_Result = test.compare((Enum).strip(), (item.EnumText).strip())
                    Unit_Result = test.compare((Unit).strip(), (item.Unit).strip())
                    Enum_Result = test.compare((Enum.strip()), (item.EnumText.strip()))
                    Help_Result = test.compare((Help).strip(), (item.Description).strip())                               
                    writer.writerow([item.ParameterName,Menu_Code, item.MenuCode, Menu_Code_Result, Default, item.DefaultValue, Default_Value_Result, Min, item.Minvalue, Min_Value_Result, Max, item.Maxvalue, Max_Value_Result, Unit, item.Unit, Unit_Result, Enum, item.EnumText, Enum_Result, Help, item.Description, Help_Result])            
    elif (Controller[0:3] == "EET"):
        test.log(str("inside EETa controller"))
        
        name2=getControl(window,"Label","tbProductInfoValue1")  
        if(name2 == None):
            print "None"
            #result = False
        else:    
            test.log("type:%s "% name2["type"])
            test.log("name:%s "% name2["name"])
            test.log("text:%s "% name2["text"])
            test.log("left side code number is " +name2["text"] )
            Code_Number = (name2["text"])
            #print (Application)
            result = True
        
        file = Global_Scripts_Path+"\Danfoss."+Controller[0:7]+"_"+Code_Number[0:8]+"_DB.csv"
        file_1= Output_Global_Path+"\Offline_Datagrid_Verification_"+Code_Number[0:8]+".csv"  
#         else:
#             test.log("inside else condition of EET controller")
#             file = "C:\gitworkspace\TestAutomation-Maintenance\Test_Automation\SourceCode\Global_scripts\Danfoss."+Controller[0:6]+"_std_DB.csv"
#             file_1= "Offline_Datagrid_Verification_"+Lyt_Code_Number[0:8]+"std_.csv"
        
        #test.log("after if condition")
        tbl=waitForObjectExists(":KoolProg_Table")
        items=tbl.nativeObject.Items    
        openfile = open(file_1,'wt') 
        writer = csv.writer(openfile)
        #test.log("after if condition 1")
        
        writer.writerow(["ParameterName", "DB_Menucode","KP_Menucode","Result" ,"DB_DefaultValue", "KP_DefaultValue", "Result", "DB_MinValue", "KP_MinValue", "Result" ,"DB_MaxValue", "KP_MaxValue", "Result", "DB_Unit", "KP_Unit", "Result", "DB_Info", "KP_Info", "Result"])
        #test.log("after if condition 2")
        records = testData.dataset(file)
        for rec in records:
            #test.log("inside data file")
            Menu_Code = testData.field(rec, 0)
            Parameter_Name = testData.field(rec, 1)
            Default = testData.field(rec, 2)
            Min = testData.field(rec, 3)
            Max = testData.field(rec, 4)
            Unit = testData.field(rec, 5) 
            Enum = testData.field(rec, 6)
            Help = testData.field(rec, 7)
            mylist=[]
            if(Enum != ""):
                for x in Enum.split(','):
                    for y in x.split(':'): 
                        if(y == Default):                        
                            for z in x.split(':'):
                                mylist.append(z)
                                Default = z 
            #test.log("inside2")
            for i in range (0, items.Count):
                item=items.at(i)
                #test.log(Parameter_Name)
                #test.log(item.ParameterName)
                if (Parameter_Name.strip() == item.ParameterName.strip()):        
                    test.log("information of "+item.ParameterName+ " parameter") 
                    #Group_Name_Result = test.compare((Group_Name).strip(), (item.GroupName).strip())
                    #GroupCode_Result = test.compare((Group_Code).strip(), (item.GroupCode).strip())
                    Parameter_Name_Result = test.compare((Parameter_Name).strip(), (item.ParameterName).strip())
                    Menu_Code_Result = test.compare((Menu_Code).strip(), (item.MenuCode).strip())
                    if '.00' in item.DefaultValue:
                            num,dec=item.DefaultValue.split(".")
                            Default_Value_Result = test.compare((Default).strip(), (num).strip())
                    else:
                            #test.log(Parameter_Name)
                            #test.log(item.ParameterName)
                            #test.log(Default)
                            Default_Value_Result = test.compare((Default).strip(), (item.DefaultValue).strip()) 
                    if '.00' in item.Minvalue:
                            num,dec=item.Minvalue.split(".")
                            Min_Value_Result = test.compare((Min).strip(), (num).strip())
                    else:
                            Min_Value_Result = test.compare((Min).strip(), (item.Minvalue).strip())
                    if '.00' in item.Maxvalue:
                            num,dec=item.Maxvalue.split(".")
                            Max_Value_Result = test.compare((Max).strip(), (num).strip())
                    else:
                            Max_Value_Result = test.compare((Max).strip(), (item.Maxvalue).strip())
                    Unit_Result = test.compare((Unit).strip(), (item.Unit).strip())
                    Help_Result = test.compare((Help).strip(), (item.Description).strip())                               
                    writer.writerow([item.ParameterName,Menu_Code, item.MenuCode, Menu_Code_Result, Default, item.DefaultValue, Default_Value_Result, Min, item.Minvalue, Min_Value_Result, Max, item.Maxvalue, Max_Value_Result, Unit, item.Unit, Unit_Result, Help, item.Description, Help_Result])                   
    result = True
    return result


def DataGrid_Verification_Online():
    test.log("inside online datagrid verification")
    result = False
    test.compare(waitForObjectExists(":KoolProg_Table").type, "Table")
    test.compare(waitForObjectExists(":KoolProg_Table").name, "datagridParameters")
   
    window=waitForObject(":KoolProg_Window")
    print("count:%s"% len(window))
    
    
    ############### right side controller name
    
    name1=getControl(window,"Label","txtProuctName")  
    if(name1 == None):
        print "None"
    else:    
        #test.log("type:%s "% name1["type"])
        #test.log("name:%s "% name1["name"])
        #test.log("text:%s "% name1["text"])
        Controller_Name = (name1["text"]) 
        test.log("right side controller name is " + Controller_Name) 
    
    
    ################### right side code number or application name
        
    if ((Controller_Name [0:4]== "ERC1") | (Controller_Name [0:3]== "EET")):
        name2=getControl(window,"Label","txtCodeNumber")  
        if(name2 == None):
            print "None"
        else:    
            #test.log("type:%s "% name2["type"])
            #test.log("name:%s "% name2["name"])
            #test.log("text:%s "% name2["text"])
            Code_Number = (name2["text"])
            test.log("right side code number is "+ Code_Number)
    else:       
        name2=getControl(window,"Label","txtApp")  
        if(name2 == None):
            print "None"
        else:    
            test.log("type:%s "% name2["type"])
            test.log("name:%s "% name2["name"])
            test.log("text:%s "% name2["text"])
            Application = (name2["text"])
            test.log("application name")
            test.log (Application)
#added by priyanka
    if (Controller_Name[0:7] == "AK-CC55"):
        name2=getControl(window,"Label","txtCodeNumber")  
        if(name2 == None):
            print "None"
        else:
            Code_Number = (name2["text"])
            result = True
           
        if (Controller_Name[9::] == "Compact"):
            file = Global_Scripts_Path+"\Danfoss."+Controller_Name[9::]+"_DB.csv"
        elif (Controller_Name[9:13] == "Multi"):
            file = Global_Scripts_Path+"\Danfoss."+Controller_Name[8:13]+"_DB.csv"
        elif (Controller_Name[9:14] == "Single"):
            file = Global_Scripts_Path+"\Danfoss."+Controller_Name[8:14]+"_DB.csv"
        
        file_1= Output_Global_Path+"\Online_Datagrid_Verification"
        file_1 = file_1 + Code_Number
        file_1 = file_1 + ".csv"
        tbl=waitForObjectExists(":KoolProg_Table")
        items=tbl.nativeObject.Items

        openfile = open(file_1,'wt') 
        writer = csv.writer(openfile)
        writer.writerow(["ParameterName", "DB_Menucode","KP_Menucode","Result" ,"DB_DefaultValue", "KP_DefaultValue", "Result", "DB_MinValue", "KP_MinValue", "Result" ,"DB_MaxValue", "KP_MaxValue", "Result", "DB_Unit", "KP_Unit", "Result", "DB_Info", "KP_Info", "Result", "DB_Enum", "KP_Enum", "Result"])
        records = testData.dataset(file)
        for rec in records:
            id = testData.field(rec, 0)
            name = testData.field(rec, 1)
            Default = testData.field(rec, 2)
            Min = testData.field(rec, 3)
            Max = testData.field(rec, 4)
            Unit = testData.field(rec, 5) 
            Enum = testData.field(rec, 6)
            Info_Help = testData.field(rec, 7)
            mylist=[]
            if(Enum != ""):
                for x in Enum.split(','):
                    for y in x.split(':'): 
                        if(y == Default):                        
                            for z in x.split(':'):
                                mylist.append(z)
                                Default = z 
            
#                 for i in range (0, items.Count-1):
#                     item=items.at(i)
#                     if (name == item.ParameterName): 
#                         test.log(item.ParameterName)       
#                         MenuCode_Result = test.compare((id).strip(), (item.MenuCode).strip())
#                         MinValue_Result = test.compare((Min).strip(), (item.Minvalue).strip())
#                         MaxValue_Result = test.compare((Max).strip(), (item.Maxvalue).strip())
#                         Unit_Result = test.compare((Unit).strip(), (item.Unit).strip())
#                         Help_Result = test.compare((Info_Help).strip(), (item.Description).strip())
#                         writer.writerow([item.ParameterName,id, item.MenuCode, MenuCode_Result, Default, item.DefaultValue, DefaultValue_Result, Min, item.Minvalue, MinValue_Result, Max, item.Maxvalue, MaxValue_Result, Unit, item.Unit, Unit_Result, Info_Help, item.Description, Help_Result])            
# 

        for i in range (0, items.Count-1):
            item=items.at(i)
            if (name == item.ParameterName):
                test.log(item.ParameterName)        
                MenuCode_Result = test.compare((id).strip(), (item.MenuCode).strip())
                if '.00' in item.DefaultValue:
                        num,dec=item.DefaultValue.split(".")
                        DefaultValue_Result = test.compare((Default).strip(), (num).strip())
                else:
                        DefaultValue_Result = test.compare((Default).strip(), (item.DefaultValue).strip()) 
                if '.00' in item.Minvalue:
                        num,dec=item.Minvalue.split(".")
                        MinValue_Result = test.compare((Min).strip(), (num).strip())
                else:
                        MinValue_Result = test.compare((Min).strip(), (item.Minvalue).strip())
                if '.00' in item.Maxvalue:
                        num,dec=item.Maxvalue.split(".")
                        MaxValue_Result = test.compare((Max).strip(), (num).strip())
                else:
                        MaxValue_Result = test.compare((Max).strip(), (item.Maxvalue).strip())
                Unit_Result = test.compare((Unit).strip(), (item.Unit).strip())
                Help_Result = test.compare((Info_Help).strip(), (item.Description).strip())
                writer.writerow([item.ParameterName,id, item.MenuCode, MenuCode_Result, Default, item.DefaultValue, DefaultValue_Result, Min, item.Minvalue, MinValue_Result, Max, item.Maxvalue, MaxValue_Result, Unit, item.Unit, Unit_Result, Info_Help, item.Description, Help_Result, Enum, item.EnumText, Enum_Result])            
                break            
            
   
    if (Controller_Name[0:3] == "ETC"):
        ETC_App_List = ['STANDARD', 'GDM101', 'DUALBAND102', 'DOUBLEDOOR', 'WINECOOLER', 'MEDICINECOOLER', 'COND101', 'DUALDEFROST']
        count = len(ETC_App_List)
        for i in range (0, count):
            file = rGlobal_Scripts_Path+"\Danfoss.ETC1H."+Application+"_DB.csv"
            file_1= "Result_Sheet_"+Application+".csv"
            tbl=waitForObjectExists(":KoolProg_Table")
            items=tbl.nativeObject.Items
    
            openfile = open(file_1,'wt') 
            writer = csv.writer(openfile)
            writer.writerow(["ParameterName", "DB_Menucode","KP_Menucode","Result" ,"DB_DefaultValue", "KP_DefaultValue", "Result", "DB_MinValue", "KP_MinValue", "Result" ,"DB_MaxValue", "KP_MaxValue", "Result", "DB_Unit", "KP_Unit", "Result", "DB_Info", "KP_Info", "Result", "DB_Enum", "KP_Enum", "Result"])
            records = testData.dataset(file)
            for rec in records:
                id = testData.field(rec, 0)
                name = testData.field(rec, 1)
                Default = testData.field(rec, 2)
                Min = testData.field(rec, 3)
                Max = testData.field(rec, 4)
                Unit = testData.field(rec, 5) 
                Enum = testData.field(rec, 6)
                Info_Help = testData.field(rec, 7)
                mylist=[]
                if(Enum != ""):
                    for x in Enum.split(','):
                        for y in x.split(':'): 
                            if(y == Default):                        
                                for z in x.split(':'):
                                    mylist.append(z)
                                    Default = z 
                
#                 for i in range (0, items.Count-1):
#                     item=items.at(i)
#                     if (name == item.ParameterName): 
#                         test.log(item.ParameterName)       
#                         MenuCode_Result = test.compare((id).strip(), (item.MenuCode).strip())
#                         MinValue_Result = test.compare((Min).strip(), (item.Minvalue).strip())
#                         MaxValue_Result = test.compare((Max).strip(), (item.Maxvalue).strip())
#                         Unit_Result = test.compare((Unit).strip(), (item.Unit).strip())
#                         Help_Result = test.compare((Info_Help).strip(), (item.Description).strip())
#                         writer.writerow([item.ParameterName,id, item.MenuCode, MenuCode_Result, Default, item.DefaultValue, DefaultValue_Result, Min, item.Minvalue, MinValue_Result, Max, item.Maxvalue, MaxValue_Result, Unit, item.Unit, Unit_Result, Info_Help, item.Description, Help_Result])            
# 

            for i in range (0, items.Count-1):
                item=items.at(i)
                if (name == item.ParameterName):
                    test.log(item.ParameterName)        
                    MenuCode_Result = test.compare((id).strip(), (item.MenuCode).strip())
                    if '.00' in item.DefaultValue:
                            num,dec=item.DefaultValue.split(".")
                            DefaultValue_Result = test.compare((Default).strip(), (num).strip())
                    else:
                            DefaultValue_Result = test.compare((Default).strip(), (item.DefaultValue).strip()) 
                    if '.00' in item.Minvalue:
                            num,dec=item.Minvalue.split(".")
                            MinValue_Result = test.compare((Min).strip(), (num).strip())
                    else:
                            MinValue_Result = test.compare((Min).strip(), (item.Minvalue).strip())
                    if '.00' in item.Maxvalue:
                            num,dec=item.Maxvalue.split(".")
                            MaxValue_Result = test.compare((Max).strip(), (num).strip())
                    else:
                            MaxValue_Result = test.compare((Max).strip(), (item.Maxvalue).strip())
                            
                    Enum_Result = test.compare((Enum).strip(), (item.EnumText).strip())
                    Unit_Result = test.compare((Unit).strip(), (item.Unit).strip())
                    Help_Result = test.compare((Info_Help).strip(), (item.Description).strip())
                    writer.writerow([item.ParameterName,id, item.MenuCode, MenuCode_Result, Default, item.DefaultValue, DefaultValue_Result, Min, item.Minvalue, MinValue_Result, Max, item.Maxvalue, MaxValue_Result, Unit, item.Unit, Unit_Result, Info_Help, item.Description, Help_Result, Enum, item.EnumText, Enum_Result])            
                    break            
            
    elif (Controller_Name[0:4] == "ERC2"):
        ERCWS_App_List = ['App0', 'App1', 'App2', 'App3', 'App4', 'App5', 'App6']
        count = len(ERCWS_App_List)
        for i in range (0, count):
            file = rGlobal_Scripts_Path+"\Danfoss."+Controller[0:6]+"_DB.csv"
            file_1= "Result_Sheet_"+Application+".csv"
                    
            tbl=waitForObjectExists(":KoolProg_Table")
            items=tbl.nativeObject.Items
            
            openfile = open(file_1,'wt') 
            writer = csv.writer(openfile)
            writer.writerow(["ParameterName", "DB_Menucode","KP_Menucode","Result" ,"DB_DefaultValue", "KP_DefaultValue", "Result", "DB_MinValue", "KP_MinValue", "Result" ,"DB_MaxValue", "KP_MaxValue", "Result", "DB_Unit", "KP_Unit", "Result", "DB_Info", "KP_Info", "Result", "DB_Enum", "KP_Enum", "Result"])
    
            records = testData.dataset(file)
            for rec in records:
                id = testData.field(rec, 0)
                name = testData.field(rec, 1)
                if (Application == "App0"):
                    Default = testData.field(rec, 2)
                elif (Application == "App1"):
                    Default = testData.field(rec, 3)
                elif (Application == "App2"):
                    Default = testData.field(rec, 4)
                elif (Application == "App3"):
                    Default = testData.field(rec, 5)
                elif (Application == "App4"):
                    Default = testData.field(rec, 6)
                elif (Application == "App5"):
                    Default = testData.field(rec, 7)
                elif (Application == "App6"):
                    Default = testData.field(rec, 8)
                Min = testData.field(rec, 9)
                Max = testData.field(rec, 10)
                Unit = testData.field(rec, 11) 
                Enum = testData.field(rec, 12)
                Info_Help = testData.field(rec, 13)
                mylist=[]
                if(Enum != ""):
                    for x in Enum.split(','):
                        for y in x.split(':'): 
                            if(y == Default):                        
                                for z in x.split(':'):
                                    mylist.append(z)
                                    Default = z 
                
#                 for i in range (0, items.Count-1):
#                     item=items.at(i)
#                     if (name == item.ParameterName):    
#                         test.log(item.ParameterName)    
#                         MenuCode_Result = test.compare((id).strip(), (item.MenuCode).strip())
#                         DefaultValue_Result = test.compare((Default).strip(), (item.DefaultValue).strip())
#                         MinValue_Result = test.compare((Min).strip(), (item.Minvalue).strip())
#                         MaxValue_Result = test.compare((Max).strip(), (item.Maxvalue).strip())
#                         Unit_Result = test.compare((Unit).strip(), (item.Unit).strip())
#                         Help_Result = test.compare((Info_Help).strip(), (item.Description).strip())
#                         writer.writerow([item.ParameterName,id, item.MenuCode, MenuCode_Result, Default, item.DefaultValue, DefaultValue_Result, Min, item.Minvalue, MinValue_Result, Max, item.Maxvalue, MaxValue_Result, Unit, item.Unit, Unit_Result, Info_Help, item.Description, Help_Result])                        
#         

            for i in range (0, items.Count-1):
                item=items.at(i)
                if (name == item.ParameterName):
                    test.log(item.ParameterName)        
                    MenuCode_Result = test.compare((id).strip(), (item.MenuCode).strip())
                    if '.00' in item.DefaultValue:
                            num,dec=item.DefaultValue.split(".")
                            DefaultValue_Result = test.compare((Default).strip(), (num).strip())
                    else:
                            DefaultValue_Result = test.compare((Default).strip(), (item.DefaultValue).strip()) 
                    if '.00' in item.Minvalue:
                            num,dec=item.Minvalue.split(".")
                            MinValue_Result = test.compare((Min).strip(), (num).strip())
                    else:
                            MinValue_Result = test.compare((Min).strip(), (item.Minvalue).strip())
                    if '.00' in item.Maxvalue:
                            num,dec=item.Maxvalue.split(".")
                            MaxValue_Result = test.compare((Max).strip(), (num).strip())
                    else:
                            MaxValue_Result = test.compare((Max).strip(), (item.Maxvalue).strip())
                            
                    Enum_Result = test.compare((Enum).strip(), (item.EnumText).strip())
                    Unit_Result = test.compare((Unit).strip(), (item.Unit).strip())
                    Help_Result = test.compare((Info_Help).strip(), (item.Description).strip())
                    writer.writerow([item.ParameterName,id, item.MenuCode, MenuCode_Result, Default, item.DefaultValue, DefaultValue_Result, Min, item.Minvalue, MinValue_Result, Max, item.Maxvalue, MaxValue_Result, Unit, item.Unit, Unit_Result, Info_Help, item.Description, Help_Result, Enum, item.EnumText, Enum_Result])            
                    break

    elif (Controller_Name [0:4] == "ERC1"):##Added by Aashika## - 3.4.25.x
        name2=getControl(window,"Label","txtApp")  
        if(name2 == None):
            print "None"
        else:    
            Product_Version = (name2["text"])
#             test.log("application name")
#             test.log (Product_Version)
            
        if (Controller_Name[0:6] == "ERC111"):
            if (Code_Number == "080G3237")| (Code_Number == "080G3247")|(Code_Number == "080G3234"):
                file = Global_Scripts_Path+"\Danfoss."+Controller_Name[0:6]+"_"+Code_Number+"_"+Product_Version+"_DB.csv"
                file_1= "Result_Sheet_"+Code_Number+"-"+Product_Version+".csv"
            else:
                file = Global_Scripts_Path+"\Danfoss."+Controller_Name[0:6]+"_std_DB.csv"
                file_1= "Result_Sheet_"+Code_Number+"-"+Product_Version+".csv"
                
        elif(Controller_Name[0:6] == "ERC112"):
            if ((Code_Number == "080G3202")|(Code_Number == "080G3203")|(Code_Number == "080G3206")|(Code_Number == "080G3207")|(Code_Number == "080G3212")|(Code_Number == "080G3213")|(Code_Number == "080G3216")|(Code_Number == "080G3217"))&(Product_Version == "PV03"):##ALL STD CODE NUMBERS WITH MAINTENANCE DATABSE##
                file = Global_Scripts_Path+"\Danfoss."+Controller_Name[0:6]+"_M_"+Product_Version+"_DB.csv"
                file_1= "Result_Sheet_"+Code_Number+"-"+Product_Version+".csv"
                
            elif (Code_Number == "080G3221")|(Code_Number == "080G3248")|(Code_Number == "080G3276")|(Code_Number == "080G3259"):
                file = Global_Scripts_Path+"\Danfoss."+Controller_Name[0:6]+"_"+Code_Number+"_"+Product_Version+"_DB.csv"
                file_1= "Result_Sheet_"+Code_Number+"-"+Product_Version+".csv"
            
            elif (Code_Number == "080G3408")|(Code_Number == "080G3409")|(Code_Number == "080G3410")|(Code_Number == "080G3414")|(Code_Number == "080G3413")|(Code_Number == "080G3419"): ##SPECIAL CODE NUMBERS##, ##3408 uses 112M DB, but PV version is PV01, hence added here##
                file = Global_Scripts_Path+"\Danfoss."+Controller_Name[0:6]+"_"+Code_Number+"_"+Product_Version+"_DB.csv"
                file_1= "Result_Sheet_"+Code_Number+"-"+Product_Version+".csv"
            
            elif (Code_Number == "080G3220")|(Code_Number == "080G3243"):##COMMON DB_3220##
                file = Global_Scripts_Path+"\Danfoss."+Controller_Name[0:6]+"_080G3220_DB.csv"
                file_1= "Result_Sheet_"+Code_Number+"-"+Product_Version+".csv"
                
            elif (Code_Number == "080G3229")|(Code_Number == "080G3274"):##COMMON DB_3229##
                file = Global_Scripts_Path+"\Danfoss."+Controller_Name[0:6]+"_080G3229_DB.csv"
                file_1= "Result_Sheet_"+Code_Number+"-"+Product_Version+".csv"
                
            elif (Code_Number == "080G3275")|(Code_Number == "080G3239"):##COMMON DB_3275##
                file = Global_Scripts_Path+"\Danfoss."+Controller_Name[0:6]+"_080G3275_DB.csv"
                file_1= "Result_Sheet_"+Code_Number+"-"+Product_Version+".csv"
                
            else:##ALL CODE NUMBERS WITH STANDARD DATABASE##
                file = Global_Scripts_Path+"\Danfoss."+Controller_Name[0:6]+"_std_DB.csv"
                file_1= "Result_Sheet_"+Code_Number+"-"+Product_Version+".csv"
        
        elif (Controller_Name[0:6]== "ERC113"):##ALL STD CODES FOR MAINTENANCE##
            if ((Code_Number == "080G3252")|(Code_Number == "080G3253")|(Code_Number == "080G3406")|(Code_Number == "080G3407"))&(Product_Version == "PV02"):
                file = Global_Scripts_Path+"\Danfoss."+Controller_Name[0:6]+"_M_"+Product_Version+"_DB.csv"
                file_1= "Result_Sheet_"+Code_Number+"-"+Product_Version+".csv"
            
            elif ((Code_Number == "080G0993")&(Product_Version == "PV01")):##ADDED FOR TREU - Aashika##
                file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_"+Code_Number+"_"+Product_Version+"_DB.csv"
                file_1= "Result_Sheet_"+Code_Number+"-"+Product_Version+".csv"
            
            else:##ALL CODE NUMBERS WITH STANDARD DATABASE##
                file = Global_Scripts_Path+"\Danfoss."+Controller_Name[0:6]+"_std_DB.csv"
                file_1= "Result_Sheet_"+Code_Number+"-"+Product_Version+".csv"
            
        
        tbl=waitForObjectExists(":KoolProg_Table")
        items=tbl.nativeObject.Items
            
        openfile = open(file_1,'wt') 
        writer = csv.writer(openfile)
        writer.writerow(["ParameterName", "DB_Menucode","KP_Menucode","Result" ,"DB_DefaultValue", "KP_DefaultValue", "Result", "DB_MinValue", "KP_MinValue", "Result" ,"DB_MaxValue", "KP_MaxValue", "Result", "DB_Enum", "KP_Enum", "Result", "DB_Unit", "KP_Unit", "Result", "DB_Info", "KP_Info", "Result"])

        records = testData.dataset(file)
        for rec in records:
            id = testData.field(rec, 0)
            name = testData.field(rec, 1)
            Default = testData.field(rec, 2)
            Min = testData.field(rec, 3)
            Max = testData.field(rec, 4)
            Unit = testData.field(rec, 5) 
            Enum = testData.field(rec, 6)
            Info_Help = testData.field(rec, 7)
            mylist=[]
            if(Enum != ""):
                for x in Enum.split(','):
                    for y in x.split(':'): 
                        if(y == Default):                        
                            for z in x.split(':'):
                                mylist.append(z)
                                Default = z 
            
#             for i in range (0, items.Count-1):
#                 item=items.at(i)
#                 if (name == item.ParameterName):        
#                   test.log(item.ParameterName) 
#                   MenuCode_Result = test.compare((id).strip(), (item.MenuCode).strip())
#                   DefaultValue_Result = test.compare((Default).strip(), (item.DefaultValue).strip())
#                   MinValue_Result = test.compare((Min).strip(), (item.Minvalue).strip())
#                   MaxValue_Result = test.compare((Max).strip(), (item.Maxvalue).strip())
#                   Unit_Result = test.compare((Unit).strip(), (item.Unit).strip())
#                   Help_Result = test.compare((Info_Help).strip(), (item.Description).strip())
#                   writer.writerow([item.ParameterName,id, item.MenuCode, MenuCode_Result, Default, item.DefaultValue, DefaultValue_Result, Min, item.Minvalue, MinValue_Result, Max, item.Maxvalue, MaxValue_Result, Unit, item.Unit, Unit_Result, Info_Help, item.Description, Help_Result])                  
#             

            for i in range (0, items.Count-1):
                item=items.at(i)
                if (id == item.MenuCode):
                    test.log(item.ParameterName)        
                    MenuCode_Result = test.compare((id).strip(), (item.MenuCode).strip())
                    if '.00' in item.DefaultValue:
                            num,dec=item.DefaultValue.split(".")
                            DefaultValue_Result = test.compare((Default).strip(), (num).strip())
                    else:
                            DefaultValue_Result = test.compare((Default).strip(), (item.DefaultValue).strip()) 
                    if '.00' in item.Minvalue:
                            num,dec=item.Minvalue.split(".")
                            MinValue_Result = test.compare((Min).strip(), (num).strip())
                    else:
                            MinValue_Result = test.compare((Min).strip(), (item.Minvalue).strip())
                    if '.00' in item.Maxvalue:
                            num,dec=item.Maxvalue.split(".")
                            MaxValue_Result = test.compare((Max).strip(), (num).strip())
                    else:
                            MaxValue_Result = test.compare((Max).strip(), (item.Maxvalue).strip())
                    
                    Enum_Result = test.compare((Enum).strip(), (item.EnumText).strip())
                    Unit_Result = test.compare((Unit).strip(), (item.Unit).strip())
                    Help_Result = test.compare((Info_Help).strip(), (item.Description).strip())
                    writer.writerow([item.ParameterName,id, item.MenuCode, MenuCode_Result, Default, item.DefaultValue, DefaultValue_Result, Min, item.Minvalue, MinValue_Result, Max, item.Maxvalue, MaxValue_Result, Unit, item.Unit, Unit_Result, Enum, item.EnumText, Enum_Result, Info_Help, item.Description, Help_Result])            
                    break

    elif (Controller_Name[0:3] == "EET"):
        test.log("inside EET controller")
        file = Global_Scripts_Path+"\Danfoss."+Controller_Name[0:7]+"_"+Code_Number[0:8]+"_DB.csv"
        file_1= Output_Global_Path+"\Online_Datagrid_Verification_"+Code_Number[0:8]+".csv"
#         else:
#             test.log("inside else condition of EET controller")
#             file = Global_Scripts_Path+"\Danfoss."+Controller_Name[0:6]+"_std_DB.csv"
#             file_1= "Online_Datagrid_Verification_"+Code_Number[0:8]+".csv"
        
        #test.log("after if condition")
        tbl=waitForObjectExists(":KoolProg_Table")
        items=tbl.nativeObject.Items    
        openfile = open(file_1,'wt') 
        writer = csv.writer(openfile)
        #test.log("after if condition 1")
        writer.writerow(["ParameterName", "DB_Menucode","KP_Menucode","Result" ,"DB_DefaultValue", "KP_DefaultValue", "Result", "DB_MinValue", "KP_MinValue", "Result" ,"DB_MaxValue", "KP_MaxValue", "Result", "DB_Unit", "KP_Unit", "Result", "DB_Info", "KP_Info", "Result"])
        #test.log("after if condition 2")
        records = testData.dataset(file)
        for rec in records:
            #test.log("inside data file")
            Menu_Code = testData.field(rec, 0)
            Parameter_Name = testData.field(rec, 1)
            Default = testData.field(rec, 2)
            Min = testData.field(rec, 3)
            Max = testData.field(rec, 4)
            Unit = testData.field(rec, 5) 
            Enum = testData.field(rec, 6)
            Help = testData.field(rec, 7)
            mylist=[]
            if(Enum != ""):
                for x in Enum.split(','):
                    for y in x.split(':'): 
                        if(y == Default):                        
                            for z in x.split(':'):
                                mylist.append(z)
                                Default = z 
            #test.log("inside2")
            for i in range (0, items.Count):
                item=items.at(i)
                #test.log("parameter in db is " +Parameter_Name +"and parameter in koolprog "+item.ParameterName) 
                if (str(Parameter_Name).strip() == str(item.ParameterName).strip()):        
                    test.log("information of "+item.ParameterName+ " parameter") 
                    #Group_Name_Result = test.compare((Group_Name).strip(), (item.GroupName).strip())
                    #GroupCode_Result = test.compare((Group_Code).strip(), (item.GroupCode).strip())
                    Parameter_Name_Result = test.compare((Parameter_Name).strip(), (item.ParameterName).strip())
                    Menu_Code_Result = test.compare((Menu_Code).strip(), (item.MenuCode).strip())
                    if '.00' in item.DefaultValue:
                            num,dec=item.DefaultValue.split(".")
                            #test.log(num)
                            #test.log(Default)
                            #test.log(item.DefaultValue)
                            Default_Value_Result = test.compare((Default).strip(), (num).strip())
                    else:
                            Default_Value_Result = test.compare((Default).strip(), (item.DefaultValue).strip()) 
                    if '.00' in item.Minvalue:
                            num,dec=item.Minvalue.split(".")
                            Min_Value_Result = test.compare((Min).strip(), (num).strip())
                    else:
                            Min_Value_Result = test.compare((Min).strip(), (item.Minvalue).strip())
                    if '.00' in item.Maxvalue:
                            num,dec=item.Maxvalue.split(".")
                            Max_Value_Result = test.compare((Max).strip(), (num).strip())
                    else:
                            Max_Value_Result = test.compare((Max).strip(), (item.Maxvalue).strip())
                    Unit_Result = test.compare((Unit).strip(), (item.Unit).strip())
                    Help_Result = test.compare((Help).strip(), (item.Description).strip())
                    writer.writerow([item.ParameterName,Menu_Code, item.MenuCode, Menu_Code_Result, Default, item.DefaultValue, Default_Value_Result, Min, item.Minvalue, Min_Value_Result, Max, item.Maxvalue, Max_Value_Result, Unit, item.Unit, Unit_Result, Help, item.Description, Help_Result])            
                    #result = True
                #else:
                    #test.log("DB parameter " +Parameter_Name+"  is not matching with KoolProg parameter " +item.ParameterName)
    result = True
    return result


def DataGrid_Verification_Offline_EKE():
    test.compare(waitForObjectExists(":KoolProg_Table").type, "Table")
    test.compare(waitForObjectExists(":KoolProg_Table").name, "datagridParameters")
   
    window=waitForObject(":KoolProg_Window_0")
    print("count:%s"% len(window))
    
    name1=getControl(window,"Label","tbProductInfoValue0")  
    if(name1 == None):
        print "None"
    else:    
        test.log("type:%s "% name1["type"])
        test.log("name:%s "% name1["name"])
        test.log("text:%s "% name1["text"])
        Controller = (name1["text"])
        
        
        
    name2=getControl(window,"Label","tbProductInfoValue1")  
    if(name2 == None):
        print "None"
    else:    
        test.log("type:%s "% name2["type"])
        test.log("name:%s "% name2["name"])
        test.log("text:%s "% name2["text"])
        Application = (name2["text"])
        
    name3=getControl(window,"Label","tbProductInfoValue2")  
    if(name3 == None):
        print "None"
    else:    
        test.log("type:%s "% name3["type"])
        test.log("name:%s "% name3["name"])
        test.log("text:%s "% name3["text"])
        SoftwareVersion = (name3["text"])
        print SoftwareVersion
        
    tbl=waitForObjectExists(":KoolProg_Table")
    items=tbl.nativeObject.Items
    if(SoftwareVersion == "PV01"):
        file = "EKE1C_PV01_DB.csv"
        file_1 = "Result_Sheet_EKE1C_PV01.csv"
        
    else:
        test.log ("Unknown EKE Product Version detected")
    
    openfile = open(file_1,'wt') 
    file1 = ""
     
    writer = csv.writer(openfile)
    writer.writerow(["ParameterName", "DB_Menucode","KP_Menucode","Result" ,"DB_DefaultValue", "KP_DefaultValue", "Result", "DB_MinValue", "KP_MinValue", "Result" ,"DB_MaxValue", "KP_MaxValue", "Result", "DB_Unit", "KP_Unit", "Result"])
    records = testData.dataset(file)
    file = ""
    for rec in records:
        id = testData.field(rec, 0)
        name = testData.field(rec, 1)        
        Default = testData.field(rec, 2)        
        Min = testData.field(rec, 3)
        Max = testData.field(rec, 4)
        Unit = testData.field(rec, 5) 
        Enum = testData.field(rec, 6)
        mylist=[]
        if(Enum != ""):
            for x in Enum.split(','):
                for y in x.split(':'): 
                    if(y == Default):                        
                        for z in x.split(':'):
                            mylist.append(z)
                            Default = z 
        
        for i in range (0, items.Count-1):
            item=items.at(i)
            #test.log(" MenuCode:"+item.MenuCode+" ParameterName:"+item.ParameterName+" DefaultValue:"+ item.DefaultValue + " Minvalue:"+item.Minvalue+" Maxvalue:"+item.Maxvalue+" Unit:"+item.Unit)
            #test.log("Minvalue of is "+getMinvalue(items, "Differential")
            if (name == item.ParameterName):
                MenuCode_Result = test.compare(id, item.MenuCode)
                DefaultValue_Result = test.compare(Default, item.DefaultValue)
                MinValue_Result = test.compare(Min, item.Minvalue)
                MaxValue_Result = test.compare(Max, item.Maxvalue)
                Unit_Result = test.compare(Unit, item.Unit)
                writer.writerow([item.ParameterName,id, item.MenuCode, MenuCode_Result, Default, item.DefaultValue, DefaultValue_Result, Min, item.Minvalue, MinValue_Result, Max, item.Maxvalue, MaxValue_Result, Unit, item.Unit, Unit_Result]) 

				
def Enable(symbolicname, value):
   result = False 
   test.log("inside enable function")
   tbl=waitForObjectExists(symbolicname)  
   Object=tbl.nativeObject
   test.compare(bool(strtobool((value))), Object.IsEnabled) 
   result = True
   return result 
   
   
def FinishButton(symbolicname):
   test.log("inside Finish Button")
   result = False
   mouseClick(waitForObject(symbolicname), MouseButton.PrimaryButton)
   try:
        snooze(5)      
        mouseClick(":MessageBoxDisplay.YES_Button"), MouseButton.PrimaryButton
        snooze(10)
   except:
           snooze(5)
   result = True 
   return result  

           
def Snooze():
   test.log("inside snooze")
   result = False
   snooze(20)
   result = True
   return result  


def Value_Generation():
   test.log("inside value generation")
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
   waitForObject(":KoolProg.UCconnectedcontrol_WPFControl", 20000)
   
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
       
   ###### right side controller name   
   name1_cont=getControl(window,"Label","txtProuctName")  
   if(name1_cont == None):
       print "None"
       result = False
   else:    
       test.log("type:%s "% name1_cont["type"])
       test.log("name:%s "% name1_cont["name"])
       test.log("text:%s "% name1_cont["text"])
       Controller_cont = (name1_cont["text"])
       result = True
       test.log(Controller_cont)
       test.log(Controller_cont[0:4])
       
   ##ERCWS##  
    
   if ((Controller_cont[0:4] == "ERC2")):
       fieldsTable=parseFields(tbl)
       Object=tbl.nativeObject
       items=tbl.nativeObject.Items
       file = Global_Scripts_Path+"\Danfoss."+Controller_cont[0:6]+"_Parameters.csv"
       
   ##ERCV2##    
   
   elif (Controller_cont[0:4] == "ERC1"):
       fieldsTable=parseFields(tbl)
       Object=tbl.nativeObject
       items=tbl.nativeObject.Items
       
   ############ right side code number 
       
       name2=getControl(window,"Label","txtCodeNumber") 
       PV_Version =  getControl(window,"Label","txtApp")  
       if(name2 == None):
           print "None"
       else:    
#            test.log("type:%s "% name2["type"])
#            test.log("name:%s "% name2["name"])
#            test.log("text:%s "% name2["text"])
           Code_Number = (name2["text"])
           test.log("code number")
           test.log(Code_Number)
       if (PV_Version == None):
           print "None"
       else:    
#            test.log("type:%s "% PV_Version["type"])
#            test.log("name:%s "% PV_Version["name"])
#            test.log("text:%s "% PV_Version["text"])
           Product_Version = (PV_Version["text"])
           test.log("Product_Version")
           test.log(Product_Version)
       
       if (Controller_cont[0:6] == "ERC111"):
           if (Code_Number == "080G3237")| (Code_Number == "080G3247")|(Code_Number == "080G3234"):
               file = Global_Scripts_Path+"\Danfoss."+Controller_cont[0:6]+"_"+Code_Number+"_"+Product_Version+"_Parameters.csv"
           else:
               file = Global_Scripts_Path+"\Danfoss."+Controller_cont[0:6]+"_std_Parameters.csv"
               
       elif(Controller_cont[0:6] == "ERC112"):
           if ((Code_Number == "080G3202")|(Code_Number == "080G3203")|(Code_Number == "080G3206")|(Code_Number == "080G3207")|(Code_Number == "080G3212")|(Code_Number == "080G3213")|(Code_Number == "080G3216")|(Code_Number == "080G3217"))&(Product_Version == "PV03"):##ALL STD CODE NUMBERS WITH MAINTENANCE DATABSE##
               file = Global_Scripts_Path+"\Danfoss."+Controller_cont[0:6]+"_M_"+Product_Version+"_Parameters.csv"
               
           elif (Code_Number == "080G3221")|(Code_Number == "080G3248")|(Code_Number == "080G3276")|(Code_Number == "080G3259"):
               file = Global_Scripts_Path+"\Danfoss."+Controller_cont[0:6]+"_"+Code_Number+"_"+Product_Version+"_Parameters.csv"
           
           elif (Code_Number == "080G3408")|(Code_Number == "080G3409")|(Code_Number == "080G3410")|(Code_Number == "080G3414")|(Code_Number == "080G3413")|(Code_Number == "080G3419"): ##SPECIAL CODE NUMBERS##, ##3408 uses 112M DB, but PV version is PV01, hence added here##
               file = Global_Scripts_Path+"\Danfoss."+Controller_cont[0:6]+"_"+Code_Number+"_"+Product_Version+"_Parameters.csv"
           
           elif (Code_Number == "080G3220")|(Code_Number == "080G3243"):##COMMON DB_3220##
               file = Global_Scripts_Path+"\Danfoss."+Controller_cont[0:6]+"_080G3220_Parameters.csv"
               
           elif (Code_Number == "080G3229")|(Code_Number == "080G3274"):##COMMON DB_3229##
               file = Global_Scripts_Path+"\Danfoss."+Controller_cont[0:6]+"_080G3229_Parameters.csv"
               
           elif (Code_Number == "080G3275")|(Code_Number == "080G3239"):##COMMON DB_3275##
               file = Global_Scripts_Path+"\Danfoss."+Controller_cont[0:6]+"_080G3275_Parameters.csv"
               
           else:##ALL CODE NUMBERS WITH STANDARD DATABASE##
               file = Global_Scripts_Path+"\Danfoss."+Controller_cont[0:6]+"_std_Parameters.csv"
       
       elif (Controller_cont[0:6]== "ERC113"):##ALL STD CODES FOR MAINTENANCE##
           if ((Code_Number == "080G3252")|(Code_Number == "080G3253")|(Code_Number == "080G3406")|(Code_Number == "080G3407"))&(Product_Version == "PV02"):
               file = Global_Scripts_Path+"\Danfoss."+Controller_cont[0:6]+"_M_"+Product_Version+"_Parameters.csv"
           
           elif ((Code_Number == "080G0993")&(Product_Version == "PV01")):##ADDED FOR TRUE - Aashika##
               file = Global_Scripts_Path+"\Danfoss."+Controller_cont[0:6]+"_"+Code_Number+"_"+Product_Version+"_Parameters.csv"
           
           else:##ALL CODE NUMBERS WITH STANDARD DATABASE##
               file = Global_Scripts_Path+"\Danfoss."+Controller_cont[0:6]+"_std_Parameters.csv"

   ##ETC##   
   
   elif ((Controller_cont[0:3] == "ETC")):
       fieldsTable=parseFields(tbl)
       Object=tbl.nativeObject
       items=tbl.nativeObject.Items
       name2_cont=getControl(window,"Label","txtApp")
       if(name2_cont == None):
           print "None"
           result = False
       else:    
           test.log("type:%s "% name2_cont["type"])
           test.log("name:%s "% name2_cont["name"])
           test.log("text:%s "% name2_cont["text"])
           ETC_Application = (name2_cont["text"])
           print ETC_Application
           file = Global_Scripts_Path+"\Danfoss.ETC1H."+ETC_Application+"_Parameters.csv" 
           
   ##EKE##
   elif ((Controller_cont[0:3] == "EKE")):
       checkEnableVisibleEKE()
       fieldsTable=parseVisibleRow(tbl)
       Object=tbl.nativeObject
       items=tbl.nativeObject.Items
       name3_cont=getControl(window,"Label","txtApp")
       if(name3_cont == None):
           print "None"
           result = False
       else:    
           test.log("type:%s "% name3_cont["type"])
           test.log("name:%s "% name3_cont["name"])  
           test.log("text:%s "% name3_cont["text"])
           PV = (name3_cont["text"])
           EKE_PV = PV[4:8] 
           print EKE_PV
           file = Global_Scripts_Path+"\Danfoss.EKE1C."+EKE_PV+"_Parameters.csv"
   
##EET##
       
   elif (Controller_cont[0:3] == "EET"):
       test.log("inside EET controller")
       fieldsTable=parseFields(tbl)
       test.log("outside of parsing")
       Object=tbl.nativeObject
       #test.log("1")
       items=tbl.nativeObject.Items
       #test.log("2")
       file = Global_Scripts_Path+"\Danfoss."+Controller_cont[0:7]+"_"+Code_Number[0:8]+"_Parameters.csv"
#        else:
#            test.log("inside else")
#            file = Global_Scripts_Path+"\Danfoss."+Controller_cont[0:6]+"_std_Parameters.csv"   
#    

   
   file_1 = "Comparison_Sheet.csv"
   openfile = open(file_1,'wt') 
   writer = csv.writer(openfile)
   writer.writerow(["Idx", "Parameter_Name", "Random_Value", "", ""])
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
           name = testData.field(rec, 0)
           enum = testData.field(rec,1)
           for i in range (0, items.Count-1):
               item=items.at(i) 
               if ((name == item.ParameterName)&(item.Datatype == "Float")&(item.ReadOnly == False)&(item.IsEnabled == True)):
                   #Object.SelectedIndex = i
                   minVal = float(item.Minvalue)
                   #print ("min_value"+str(minVal))
                   maxVal = float(item.Maxvalue) 
                   #print ("max_value"+str(maxVal))  
                   if(functions[j] == 'Min'):
                       test.log("Result:%s" % setParameterValue(fieldsTable,item.ParameterName, str(minVal)))
                   elif(functions[j] == 'Max'):
                       test.log("Result:%s" % setParameterValue(fieldsTable,item.ParameterName, str(maxVal)))
                   else:
                       item_Val = random.uniform(minVal, maxVal)
                       #print ("0_"+str(item_Val))
                       itemVal = float(item_Val)
                       #print ("1_"+str(itemVal))
                       itemVal = round(item_Val,2)
                       #print ("2_"+str(itemVal))
                       test.log("Result:%s" % setParameterValue(fieldsTable,item.ParameterName, str(itemVal)))
                       writer.writerow([item.Key, item.ParameterName, itemVal])  
                        
               elif ((name == item.ParameterName)&(item.Datatype == "INT")&(item.ReadOnly == False)&(item.IsEnabled == True)):
                   #Object.SelectedIndex = i
                   minVal = float(item.Minvalue)
                   maxVal = float(item.Maxvalue)  
                   if(functions[j] == 'Min'):
                       test.log("Result:%s" % setParameterValue(fieldsTable,item.ParameterName, minVal))
                   elif(functions[j] == 'Max'):
                       test.log("Result:%s" % setParameterValue(fieldsTable,item.ParameterName, maxVal))
                   else:
                       itemVal = random.randint(minVal, maxVal)
                       try:
                           test.log("Result:%s" % setParameterValue(fieldsTable,item.ParameterName, itemVal))
                           writer.writerow([item.Key, item.ParameterName, itemVal])
                       except:
                           snooze(1)
                   
               elif ((name == item.ParameterName)&((item.Datatype == "enum") | (item.Datatype == "BIT"))&(item.ReadOnly == False)&(item.IsEnabled == True)):              
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
                                   test.log("Result:%s" % setParameterEnumValue(fieldsTable,item.ParameterName, enumValue))
                                   writer.writerow([item.Key, item.ParameterName, enumValue])
                                   if ((item.ParameterName in checkParameters) | (item.ParameterName == "Main switch")):
                                       visibleParamName = []
                                       test.log(item.ParameterName,"Check")
                                       fieldsTable = parseVisibleRow(tbl)
                                       writer.writerow([item.Key, item.ParameterName, enumValue])
                                   else:
                                       snooze(1)
                               else: 
                                   item.Value = enumValue
                                   #test.log("Result:%s" % setParameterValue(fieldsTable,item.ParameterName, enumValue))
                                   writer.writerow([item.Key, item.ParameterName, enumValue])  
                           else:
                               snooze(1)
                       else:
                           snooze(1)                 
                   enumList = []
       result = True
   return result
      
  
def Window(symbolicname, value):
   test.log("inside window")
   result = False 
   tbl=waitForObjectExists(symbolicname)   
   test.compare(value, tbl.type)
   result = True 
   return result  


def Text(symbolicname, value):
   test.log("inside text")
   result = False
   tbl=waitForObjectExists(symbolicname)   

   test.compare(value.strip(), tbl.text) 
   #Object=tbl.nativeObject
   result = True 
   return result

   
def Text_Box(symbolicname, value):
   test.log("inside textbox ")
   result = False
   doubleClick(waitForObject(symbolicname), MouseButton.PrimaryButton)
   snooze(2)
   type(waitForObject(symbolicname), value)
   snooze(2)
   type(waitForObject(symbolicname), "<Return>")
   snooze(2)
   result = True
   return result

      
def Text_Box1(symbolicname, value):
   test.log("inside textbox1")
   result = False
   doubleClick(waitForObject(symbolicname), MouseButton.PrimaryButton)
   snooze(2)
   type(waitForObject(symbolicname), value)
   snooze(2)
   result = True 
   return result

   
def Tooltip(symbolicname, value):
   test.log("inside tooltip")
   result = False   
   tbl=waitForObjectExists(symbolicname)
   test.compare(value, tbl.tooltip) 
   result = True 
   return result  


def ComboBox_Edit(symbolicname, value):
   test.log("inside Combobox_edit")
   result = False
   mouseClick(waitForObject(symbolicname), MouseButton.PrimaryButton)
   snooze(2) 
   type(waitForObject(symbolicname), value)
   snooze(2)
   type(waitForObject(symbolicname), "<Return>")  
   result = True
   return result


def SaveAs_Text_Box(symbolicname, value):
   test.log("inside SaveAs_TextBox")
   result = False
   doubleClick(waitForObject(symbolicname), MouseButton.PrimaryButton)
   snooze(2)
   type(waitForObject(symbolicname), value)
   snooze(2)
   type(waitForObject(symbolicname), "<Return>")
   snooze(2)
   try:
       waitForObject(":Confirm Save As_Dialog")
       mouseClick(":Confirm Save As.Yes_Button"), MouseButton.PrimaryButton
           
   except:
       snooze(0.1)
   result = True
   return result

def Code_No(symbolicname):
   #waitForObject(":KoolProg.UCconnectedcontrol_WPFControl"),2000
   result = False
   test.compare(waitForObjectExists(":KoolProg_Table").type, "Table")
   test.compare(waitForObjectExists(":KoolProg_Table").name, "datagridParameters")
  
   window=waitForObject(":KoolProg_Window")
   print("count:%s"% len(window))
   
   name1=getControl(window,"Label","txtProuctName")
   if(name1 == None):
       print "None"
   else:    
       test.log("type:%s "% name1["type"])
       test.log("name:%s "% name1["name"])
       test.log("text:%s "% name1["text"])
       Product = (name1["text"])
       Product_Name = Product[0:4]

   if (Product_Name == "ERC1"):
       name1=getControl(window,"Label","txtCodeNumber")  
       if(name1 == None):
           print "None"
       else:    
           test.log("type:%s "% name1["type"])
           test.log("name:%s "% name1["name"])
           test.log("text:%s "% name1["text"])
           Code_N = (name1["text"])
           Code_Number = Code_N[4:7]
   else:
       
       name1=getControl(window,"Label","txtCodeNumber")  
       if(name1 == None):
           print "None"
       else:    
           test.log("type:%s "% name1["type"])
           test.log("name:%s "% name1["name"])
           test.log("text:%s "% name1["text"])
           Code_Number = (name1["text"])
       
       doubleClick(waitForObject(symbolicname), MouseButton.PrimaryButton)
       type(waitForObject(symbolicname),Code_Number)
       result = True
   return result


def SnoozeForPlot(value):
   test.log("inside snooze for plot")
   result = False
   val = float(value)   
   snooze(val)
   result = True
   return result

                  
def App_Verify():
   result = False
   tbl=waitForObjectExists(":KoolProg_Table")   
   Object=tbl.nativeObject
   items=tbl.nativeObject.Items
   file = Global_Scripts_Path+"\Danfoss.ERC21X_DB"
   window=waitForObject(":KoolProg_Window_0")
   name2_cont=getControl(window,"Label","txtApp")  #can change. right now App not displayed
   if(name2_cont == None):
       print "None"
       result = False
   else:    
       test.log("type:%s "% name2_cont["type"])
       test.log("name:%s "% name2_cont["name"])
       test.log("text:%s "% name2_cont["text"])
       Application_cont = (name2_cont["text"])
   records = testData.dataset(file)
   for rec in records:
       menucode = testData.field(rec, 0)
       name = testData.field(rec, 1)
       Enum = testData.field(rec, 12)
       if (Application_cont == "SV: App0"):
           Default = testData.field(rec, 2)
       elif (Application_cont == "SV: App1"):
           Default = testData.field(rec, 3)
       elif (Application_cont == "SV: App2"):
           Default = testData.field(rec, 4)
       elif (Application_cont == "SV: App3"):
           Default = testData.field(rec, 5)
       elif (Application_cont == "SV: App4"):
           Default = testData.field(rec, 6)
       elif (Application_cont == "SV: App5"):
           Default = testData.field(rec, 7)
       elif (Application_cont == "SV: App6"):
           Default = testData.field(rec, 8)
       mylist=[]
       if(Enum != ""):
           for x in Enum.split(','):
               for y in x.split(':'): 
                   if(y == Default):                        
                       for z in x.split(':'):
                           mylist.append(z)
                           Default = z
       for i in range (0, items.Count-1):
           item=items.at(i) 
           if ((name == item.ParameterName)&(item.ReadOnly == False)):
               test.compare(item.DefaultValue, Default,item.ParameterName)
               break
       result = True
   return result
         #result = test.compare(item.Value, Application_cont)
            #if (result == True):

		  		
def Compatibility():
   test.log("inside compatibility")
   snooze(5)
   result = False
   waitForObject(":KoolProg.UCconnectedcontrol_WPFControl"),2000
   #test.compare(waitForObjectExists(":KoolProg_Table").type, "Table")
   #test.compare(waitForObjectExists(":KoolProg_Table").name, "datagridParameters")
  
   window=waitForObject(":KoolProg_Window")
   print("count:%s"% len(window))
   
   
   
   name1=getControl(window,"Label","tbProductInfoValue0")  ###### left side controller name 
   if(name1 == None):
       print "None"
   else:    
       Controller = (name1["text"])
       test.log("left side controller name is "+ Controller)
      
   name3=getControl(window,"Label","txtProuctName")        ####right side controller name
   if(name3 == None):
       print "None"
   else:    
       Online_Controller = (name3["text"])
       test.log("right side controller name is "+Online_Controller)
       
   if ((Controller != Online_Controller)):
       message = "Not compliant controller" 
             
   name2=getControl(window,"Label","tbProductInfoValue1")   #### left side code number 
   if(name2 == None):
       print "None"
   else:    
       Code_Number = (name2["text"])
       test.log("left side code number is "+Code_Number)
       
       
   name4=getControl(window,"Label","txtCodeNumber")         ###### right side code number
   if(name4 == None):
       print "None"

   else:    
       Online_Code_Number = (name4["text"])
       test.log("right side code number is "+Code_Number)
       
   if ((Controller == Online_Controller) and (Code_Number != Online_Code_Number)):
       message = "Code Number Mismatch"
       
       
   #name5=getControl(window,"Label","tbProductInfoValue3")   #### left side SW version 
   name5=getControl(window,"Label","txtVersion")
   if(name5 == None):
       print "None"
   else:    
       SW_Version = (name5["text"])
       test.log("left side SW version is "+SW_Version)
       
       
   #name6=getControl(window,"Label","txtApp")         ###### right side SW Version
   name6=getControl(window,"Label",":tbProductInfoValue2") 
   if(name6 == None):
       print "None"

   else:    
       Online_SW_Version = (name6["text"])
       test.log("right side SW_Version is "+Online_SW_Version)
       
   if ((Controller == Online_Controller) and (SW_Version != Online_SW_Version)):
       message = "SW Version Mismatch"
       
    
   if((Controller == Online_Controller) and (SW_Version != Online_SW_Version) and (Code_Number != Online_Code_Number)):
       message = ""
       test.log("Compatible controller - or PV version error (Check for Maintenance)")
       
    
   if (message != ""):
       snooze(5)
       Status_Msg = getControl(window,"Label","txtStatus") 
       status = Status_Msg["text"]
       #test.log(str(status))
       test.log("Error Message to be displayed: " +str(message))
       #test.log("Error Message displayed in KoolProg: " +str(status))
       test.compare(str(message).strip(), str(status).strip())
          
          
def Unit_Change():
   result = False
   test.compare(waitForObjectExists(":KoolProg_Table").type, "Table")
   test.compare(waitForObjectExists(":KoolProg_Table").name, "datagridParameters")
  
   window=waitForObject(":KoolProg_Window")
   print("count:%s"% len(window))
   
   name1=getControl(window,"Label","txtProuctName")  
   if(name1 == None):
       print "None"
       result = False
   else:    
       test.log("type:%s "% name1["type"])
       test.log("name:%s "% name1["name"])
       test.log("text:%s "% name1["text"])
       Controller = (name1["text"])
       result = True
       
       
       
   name2=getControl(window,"Label","txtApp")  
   if(name2 == None):
       print "None"
       result = False
   else:    
       test.log("type:%s "% name2["type"])
       test.log("name:%s "% name2["name"])
       test.log("text:%s "% name2["text"])
       Application = (name2["text"])
       #print (Application)
       result= True
       
   tbl=waitForObjectExists(":KoolProg_Table")
   items=tbl.nativeObject.Items
   file = "Unit_Change_DB.csv"
   if (item.Unit == "C"):
       if (Application == "SV: App0"):
           file_1 = "Unit_Change_Result_App0.csv"
           openfile = open(file_1,'wt') 
           writer = csv.writer(openfile)
           writer.writerow(["ParameterName", "App0_C_Default", "App0_F_Default", "Result_App0_Default", "App0_C_Min", "App0_F_Min", "Result_App0_Min", "App0_C_Max", "App0_F_Max", "Result_App0_Max", "Unit"])
       elif (Application == "SV: App1"):
           file_1 = "Unit_Change_Result_App1.csv"
           openfile = open(file_1,'wt') 
           writer = csv.writer(openfile)
           writer.writerow(["ParameterName", "App1_C_Default", "App1_F_Default", "Result_App1_Default", "App1_C_Min", "App1_F_Min", "Result_App1_Min", "App1_C_Max", "App1_F_Max", "Result_App1_Max", "Unit"])
       elif (Application == "SV: App2"):
           #Default = testData.field(rec, 4)
           file_1 = "Unit_Change_Result_App2.csv"
           openfile = open(file_1,'wt') 
           writer = csv.writer(openfile)
           writer.writerow(["ParameterName", "App2_C_Default", "App2_F_Default", "Result_App2_Default", "App2_C_Min", "App2_F_Min", "Result_App2_Min", "App2_C_Max", "App2_F_Max", "Result_App2_Max", "Unit"])
       elif (Application == "SV: App3"):
           #Default = testData.field(rec, 5)
           file_1 = "Unit_Change_Result_App3.csv"
           openfile = open(file_1,'wt') 
           writer = csv.writer(openfile)
           writer.writerow(["ParameterName", "App3_C_Default", "App3_F_Default", "Result_App3_Default", "App3_C_Min", "App3_F_Min", "Result_App3_Min", "App3_C_Max", "App3_F_Max", "Result_App3_Max", "Unit"])
       elif (Application == "SV: App4"):
           #Default = testData.field(rec, 6)
           file_1 = "Unit_Change_Result_App4.csv"
           openfile = open(file_1,'wt') 
           writer = csv.writer(openfile)
           writer.writerow(["ParameterName", "App4_C_Default", "App4_F_Default", "Result_App4_Default", "App4_C_Min", "App4_F_Min", "Result_App4_Min", "App4_C_Max", "App4_F_Max", "Result_App4_Max", "Unit"])
       elif (Application == "SV: App5"):
           #Default = testData.field(rec, 7)
           file_1 = "Unit_Change_Result_App5.csv"
           openfile = open(file_1,'wt') 
           writer = csv.writer(openfile)
           writer.writerow(["ParameterName", "App5_C_Default", "App5_F_Default", "Result_App5_Default", "App5_C_Min", "App5_F_Min", "Result_App5_Min", "App5_C_Max", "App5_F_Max", "Result_App5_Max", "Unit"])
       elif (Application == "SV: App6"):
           #Default = testData.field(rec, 8)
           file_1 = "Unit_Change_Result_App6.csv"
           openfile = open(file_1,'wt') 
           writer = csv.writer(openfile)
           writer.writerow(["ParameterName", "App6_C_Default", "App6_F_Default", "Result_App6_Default", "App6_C_Min", "App6_F_Min", "Result_App6_Min", "App6_C_Max", "App6_F_Max", "Result_App6_Max", "Unit"])
       else: 
           print "ERROR"
#     file_1 = "Result_Sheet.csv"
#     openfile = open(file_1,'wt') 
#     writer = csv.writer(openfile)
#     writer.writerow(["ParameterName", "DB_Menucode","KP_Menucode","Result" ,"DB_DefaultValue", "KP_DefaultValue", "Result", "DB_MinValue", "KP_MinValue", "Result" ,"DB_MaxValue", "KP_MaxValue", "Result", "DB_Unit", "KP_Unit", "Result"])
   records = testData.dataset(file)
   for rec in records:
       id = testData.field(rec, 0)
       name = testData.field(rec, 1)
       if (Application == "SV: App0"):
           Default_C = testData.field(rec, 2)
           Default_F = testData.field(rec, 3) 
       elif (Application == "SV: App1"):
           Default_C = testData.field(rec, 4)
           Default_F = testData.field(rec, 5)
       elif (Application == "SV: App2"):
           Default_C = testData.field(rec, 6)
           Default_F = testData.field(rec, 7)
       elif (Application == "SV: App3"):
           Default_C = testData.field(rec, 8)
           Default_F = testData.field(rec, 9)
       elif (Application == "SV: App4"):
           Default_C = testData.field(rec, 10)
           Default_F = testData.field(rec, 11)
       elif (Application == "SV: App5"):
           Default_C = testData.field(rec, 12)
           Default_F = testData.field(rec, 13)
       elif (Application == "SV: App6"):
           Default_C = testData.field(rec, 14)
           Default_F = testData.field(rec, 15)
       
       #Default = testData.field(rec, 2)
       Min_C = testData.field(rec, 16)
       Min_F = testData.field(rec, 17)
       Max_C = testData.field(rec, 18)
       Max_F = testData.field(rec, 19) 
       Unit = testData.field(rec, 20) 
       
       for i in range (0, items.Count-1):
           item=items.at(i)
           #test.log(" MenuCode:"+item.MenuCode+" ParameterName:"+item.ParameterName+" DefaultValue:"+ item.DefaultValue + " Minvalue:"+item.Minvalue+" Maxvalue:"+item.Maxvalue+" Unit:"+item.Unit)
           #test.log("Minvalue of is "+getMinvalue(items, "Differential")
           if ((Unit == "°C") & (item.Unit == "°C")):
               
               parameter_Name = test.compare(name, item.ParameterName)
               Default_Unit_C = test.compare(Default_C, item.DefaultValue)
               Min_Unit_C = test.compare(Min_C, item.Minvalue)
               Max_Unit_C = test.compare(Max_C, item.Maxvalue)
               Unit_Result = test.compare(Unit, item.Unit)
               Help_Result = test.compare(Info_Help, item.Description)
               writer.writerow([item.ParameterName, MenuCode_Result, Default, item.DefaultValue, DefaultValue_Result, Min, item.Minvalue, MinValue_Result, Max, item.Maxvalue, MaxValue_Result, Unit, item.Unit, Unit_Result, Info_Help, item.Description, Help_Result])            
          
               
def DB_Verification():
   KP_DB = "AK_CC_KP_DB.csv"
   Squish_DB = "Squish_DB_AK_CC.csv"
   
   file= "Result_Sheet_"
   file = file + Timestr
   file = file + ".csv"
   
   openfile = open(file,'wt') 
   writer = csv.writer(openfile)
   writer.writerow(["KP_DB_GrpCode", "Squish_DB_GrpCode","Result", "KP_DB_Menucode","Squish_DB_Menucode", "Result" ,"KP_DB_Groupname", "Squish_DB_Groupname", "Result", "KP_DB_Name", "Squish_DB_Name", "Result", "KP_DB_PNU", "Squish_DB_PNU", "Result", "KP_DB_DefaultValue", "Squish_DB_DefaultValue", "Result", "KP_DB_MinValue", "Squish_DB_MinValue", "Result" ,"KP_DB_MaxValue", "Squish_DB_MaxValue", "Result", "KP_DB_Unit", "Squish_DB_Unit", "Result", "KP_DB_Scale", "Squish_DB_Scale", "Result", "KP_DB_Datatype", "Squish_DB_Datatype", "Result", "KP_DB_Enum", "Squish_DB_Enum", "Result", "KP_DB_ReadOnly", "Squish_DB_ReadOnly", "Result", "KP_DB_VN", "Squish_DB_VN", "Result"])
   
   
   records = testData.dataset(KP_DB)
   records_1 = testData.dataset(Squish_DB)
   for rec in records:
       KP_groupCode = testData.field(rec, 0)
       KP_Menu_Code = testData.field(rec, 1)
       KP_Group_Name = testData.field(rec, 2)
       KP_Parameter_Name = testData.field(rec, 3)
       KP_PNU = testData.field(rec, 4)
       KP_Default = testData.field(rec, 5)
       KP_Min = testData.field(rec, 6)
       KP_Max = testData.field(rec, 7)
       KP_Unit = testData.field(rec, 8)
       KP_Scaling = testData.field(rec, 9)
       KP_Datatype = testData.field(rec, 10)
       KP_Enum = testData.field(rec, 11)
       KP_Read_Only =  testData.field(rec, 12)
       #Info_Help = testData.field(rec, 13)
       #Decimals = testData.field(rec, 14)
       KP_Variable_Name= testData.field(rec, 13)
       mylist=[]
       if(KP_Enum != ""):
           for x in KP_Enum.split(','):
               for y in x.split(':'): 
                   if(y == KP_Default):                        
                       for z in x.split(':'):
                           mylist.append(z)
                           KP_Default = z
      
       for rec_1 in records_1:
           groupCode = testData.field(rec_1, 0)
           Menu_Code = testData.field(rec_1, 1)
           Group_Name = testData.field(rec_1, 2)
           Parameter_Name = testData.field(rec_1, 3)
           PNU = testData.field(rec_1, 4)
           Default = testData.field(rec_1, 5)
           Min = testData.field(rec_1, 6)
           Max = testData.field(rec_1, 7)
           Unit = testData.field(rec_1, 8)
           Scaling = testData.field(rec_1, 9)
           Datatype = testData.field(rec_1, 10)
           Enum = testData.field(rec_1, 11)
           Read_Only =  testData.field(rec_1, 12)
   #         Info_Help = testData.field(rec, 13)
   #         Decimals = testData.field(rec, 14)
           Variable_Name= testData.field(rec_1, 15)
           mylist=[]
           if(Enum != ""):
               for x in Enum.split(','):
                   for y in x.split(':'): 
                       if(y == Default):                        
                           for z in x.split(':'):
                               mylist.append(z)
                               Default = z
                               
           if((Parameter_Name == KP_Parameter_Name) & (Group_Name == KP_Group_Name)):
               Group_Code_Result = test.compare(groupCode, KP_groupCode)      
               MenuCode_Result = test.compare(Menu_Code, KP_Menu_Code)
               GroupName_Result = test.compare(Group_Name, KP_Group_Name)
               Parameter_Name_Result = test.compare(Parameter_Name, KP_Parameter_Name)
               PNU_Result = test.compare(PNU, KP_PNU)
               DefaultValue_Result = test.compare(Default, KP_Default)
               MinValue_Result = test.compare(Min, KP_Min)
               MaxValue_Result = test.compare(Max, KP_Max)
               Unit_Result = test.compare(Unit, KP_Unit)
               Scaling_Result = test.compare(Scaling, KP_Scaling)
               Datatype_Result = test.compare(Datatype, KP_Datatype)
               Enum_Result = test.compare(Enum, KP_Enum)
               ReadOnly_Result = test.compare(Read_Only, KP_Read_Only)
               VN_Result = test.compare(Variable_Name, KP_Variable_Name)
               
               writer.writerow([KP_groupCode, groupCode, Group_Code_Result, KP_Menu_Code, Menu_Code, MenuCode_Result, KP_Group_Name, Group_Name, GroupName_Result, KP_Parameter_Name, Parameter_Name, Parameter_Name_Result, KP_PNU, PNU, PNU_Result, KP_Default, Default, DefaultValue_Result, KP_Min, Min, MinValue_Result, KP_Max, Max, MaxValue_Result, KP_Unit, Unit, Unit_Result, KP_Scaling, Scaling, Scaling_Result, KP_Datatype, Datatype, Datatype_Result, KP_Enum, Enum, Enum_Result, KP_Read_Only, Read_Only, Read_Only, KP_Variable_Name, Variable_Name, VN_Result])                                      
          
                  
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
                               if((object.properties(row)["type"] == "TableRow") and (row.nativeObject.IsVisible == True)):
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
#                                                    test.log("Parsing:%s" % (fieldName))                                                
                                                   fieldsTable[fieldName]=edit
                                                                                                                                                     
           return fieldsTable


def setParameterValue(fieldsTable, parameterName, value):
   test.log(str(parameterName) + " 's value is "+ (str(value)))
   #test.log(str(value))
   found = False
   if(fieldsTable != None):                            
       if(parameterName in fieldsTable):
           found=True
           edit=fieldsTable[parameterName]  
           if (value != ""):  
               mouseClick(waitForObject(edit))
               type(waitForObject(edit), value)
               type(waitForObject(edit), "<Tab>") 
#             try:
#                 mouseClick(":MessageBoxDisplay.OK_Button"), MouseButton.PrimaryButton
#             except:                    
#                 snooze(0.1)
       else:
           test.log(str(parameterName)+" :Is hidden under visibility rules")                                                                                               
   return found


def setInvalidValue(fieldsTable, parameterName, value):
   print parameterName
   print value
   found = False
   if(fieldsTable != None):                            
       if(parameterName in fieldsTable):
           found=True
           edit=fieldsTable[parameterName]  
           if (value != ""):  
               mouseClick(waitForObject(edit))
               type(waitForObject(edit), value)
               type(waitForObject(edit), "<Tab>") 
               snooze(2)
               try:
                    mouseClick(":MessageBoxDisplay.OK_Button"), MouseButton.PrimaryButton
               except:                    
                    test.log(parameterName+" is accepting values beyond boundary values. Please check!!!!")
       else:
           test.log(str(parameterName)+" :Is hidden under visibility rules")                                                                                               
   return found


def setParameterEnumValue(fieldsTable, parameterName, value):
   found = False    
   if(fieldsTable != None):   
       if parameterName in visibleParamName:
           test.log(parameterName)
                                
           if(fieldsTable[parameterName] != None):
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
                                                                                                           
   return found


def parseAppFields(tbl):
           fieldsTable={}    
           items_1=object.children(tbl)
           for item_1 in items_1:        
               if(object.properties(item_1)["type"] ==  "WPFControl"):
                   expander=object.children(item_1)
                   for child in expander:                
                       if(object.properties(child)["type"] ==  "Expander"):
                           rows=object.children(child)
                           for row in rows:
                               if(object.properties(row)["type"] == "TableRow"):
                                   fields=object.children(row)
                                   fieldName=None        
                                   for field in fields:                                                                
                                       if(object.properties(field)["type"] == "TableCell" and object.properties(field)["column"] == 4):
                                           fieldName=object.properties(field)["text"]                            
                                       if(object.properties(field)["type"] == "TableCell" and object.properties(field)["column"] == 7 and fieldName != None):
                                           edits=object.children(field)                                    
                                           for edit in edits:
                                               if(object.properties(edit)["type"] == "ComboBox" and object.properties(edit)["name"] == "cmbEnums"):
                                                   #if (fieldName != None):
                                                   test.log("Parsing:%s" % (fieldName))                                                
                                                   fieldsTable[fieldName]=edit
                                                                                                                                                     
           return fieldsTable

       
def setAppValue(fieldsTable, parameterName, app_value):
   tbl=waitForObjectExists(":KoolProg_Table")    
   Object=tbl.nativeObject
   items=tbl.nativeObject.Items
   print parameterName
   print app_value
   found = False
   if(fieldsTable != None):                            
       if(fieldsTable[parameterName] != None):            
           edit=fieldsTable[parameterName]
           test.log("%s" % edit)
           test.log("%s" % edit.type)
           test.log("%s" % app_value) 
           mouseClick(waitForObject(edit), MouseButton.PrimaryButton)
           snooze(2)          
           type(waitForObject(edit), app_value)
           snooze(2)
                
           try:
                #waitForObject(":MessageBoxDisplay_Window")
                mouseClick(":MessageBoxDisplay.OK_Button"), MouseButton.PrimaryButton
           except:
                snooze(5)   
           found=True                                                                                 
   return found


def File_Generation():
    test.log("inside file generation")
    result = False
    waitForObject(":KoolProg.System.Windows.Controls.Image_Button"),2000
    window=waitForObject(":KoolProg_Window")
    print("count:%s"% len(window))
    
    name1_cont=getControl(window,"Label","txtProuctName")  
    if(name1_cont == None):
        test.log("inside if")
        print "None"
        result = False
    else:  
        test.log("inside else")  
        test.log("type:%s "% name1_cont["type"])
        test.log("name:%s "% name1_cont["name"])
        test.log("text:%s "% name1_cont["text"])
        Controller_cont = (name1_cont["text"])
        Controller_Name = Controller_cont
        
#         if(Controller_Name[0:5] == "AK-CC"):
#             Controller_Name = Controller_Name[8::]
#         else:
#             snooze(2)
        
        #result = True
    
    
    if ((Controller_Name[0:4] == "ERC1")|(Controller_Name [0:3]== "EET")):
        test.log("inside if")
        name1_cont=getControl(window,"Label","txtCodeNumber")  
        if(name1_cont == None):
            print "None"
            result = False
        else:    
            test.log("type:%s "% name1_cont["type"])
            test.log("name:%s "% name1_cont["name"])
            test.log("text:%s "% name1_cont["text"])
            Code_Num = (name1_cont["text"])
            Code_Number = Code_Num[0:8]
            
    
              
    else:
        test.log("inside else")
        name2_cont=getControl(window,"Label","txtApp")  
        if(name2_cont == None):
            print "None"
            result = False
        else:    
            test.log("type:%s "% name2_cont["type"])
            test.log("name:%s "% name2_cont["name"])
            test.log("text:%s "% name2_cont["text"])
                    
            if (Controller_Name[0:3] == "EKE"):
                EKE_List = ['1A', '1B', '1C']
                count_EKE = len(EKE_List)
                for i in range (0, count_EKE):
                    Application = (name2_cont["text"])
                    Application_cont = Application[4:8]   
            else:    
                Application_cont = (name2_cont["text"])
            
#     if (((":KoolProg.BROWSE_Button").enabled, True) == "true"):
#         print ("YES!")
#         #result = True
        
    try:
        mouseClick(":KoolProg.BROWSE_Button"), MouseButton.PrimaryButton 
        test.log(Controller_Name)
#         test.log(Code_Number)
        if ((Controller_Name[0:4] == "ERC1")|(Controller_Name[0:3] == "EET")):
            project = Controller_Name+"-"+Code_Number+".xml"
            
        elif(Controller_Name[0:5] == "AK-CC"):
            mouseClick("{container=':Open_Dialog' mode='dropdownlist' type='ComboBox'}")
            type(waitForObject("{container=':Open_Dialog' mode='dropdownlist' type='ComboBox'}"), "C")
            snooze(2)
            type(waitForObject("{container=':Open_Dialog' mode='dropdownlist' type='ComboBox'}"), "<Return>")  
            project = Controller_Name[8::]+"-"+Application_cont+".cbk"
        
        else:    
            test.log(Application_cont)
            project = Controller_Name+"-"+Application_cont+".xml"
        type(waitForObject(":Open_Edit"), project)
        type(waitForObject(":Open_Edit"), "<Return>")
        result = True
        
                
    except:     
        test.compare(waitForObjectExists(":KoolProg_Table").type, "Table") 
        test.compare(waitForObjectExists(":KoolProg_Table").name, "datagridParameters")
        mouseClick(waitForObject(":KoolProg.System.Windows.Controls.Image_Button_11"), MouseButton.PrimaryButton)
        if ((Controller_Name[0:4] == "ERC1")| (Controller_Name[0:3] == "EET")):
            project = Controller_Name+"-"+Code_Number+".xml"
        else:    
            project = Controller_Name+"_"+Application_cont+".xml"
        type(waitForObject(":Open_Edit"), project)
        type(waitForObject(":Open_Edit"), "<Return>")
        result = True
        
    return result

                           
def Value_Verification():
   test.log("inside value verification")
#    result = False
   tbl=waitForObjectExists(":KoolProg_Table")
   items=tbl.nativeObject.Items
   file_1 = "AKCC-ValueGeneration.csv"
   records = testData.dataset(file_1)
   file_2 = "AKCC-ValueVerification-Result.csv"
   openfile = open(file_2,'wt')
   writer = csv.writer(openfile)
   writer.writerow(["Idx", "Parameter_Name", "Random_value", "KP_value", "Result"])
   for rec in records:
#         Unique_ID = testData.field(rec, 0)
       id= testData.field(rec, 0)
       name = testData.field(rec, 1)
       random_value = testData.field(rec, 2)
       print random_value
       for i in range (0, items.Count-1):
           item=items.at(i)
           if(item.Key==id):
               if ((item.Datatype == "Enum")|(item.Datatype == "BIT")):
                   result = test.compare(str(random_value).strip(), str(item.Value).strip())
                   writer.writerow([id , name, random_value, item.Value, result])
               else:
                   result = test.compare(str(random_value).strip(), str(item.Value).strip())
                   writer.writerow([id, name, str(random_value), str(item.Value), result])

                   
def Factory_Reset():
   mouseClick(waitForObject(":KoolProg.System.Windows.Controls.Image_Button_8"), MouseButton.PrimaryButton)
   waitForObject(":Factory Reset_Window")
   test.compare(":Factory Reset.Do you want to change to factory settings?_Label", ":Factory Reset.Do you want to change to factory settings?_Label", "True")
   mouseClick(waitForObject(":Factory Reset.Cancel_Button"), MouseButton.PrimaryButton)
   snooze(2)
   mouseClick(waitForObject(":KoolProg.System.Windows.Controls.Image_Button_8"), MouseButton.PrimaryButton)
   waitForObject(":Factory Reset_Window")
   test.compare(":Factory Reset.Do you want to change to factory settings?_Label", ":Factory Reset.Do you want to change to factory settings?_Label", "True")
   mouseClick(waitForObject(":Factory Reset.In Project_Button"), MouseButton.PrimaryButton)
   waitForObject(":MessageBoxDisplay_Window")
   mouseClick(waitForObject(":MessageBoxDisplay.OK_Button"), MouseButton.PrimaryButton)
   
   file = "Parsed_Json.csv"
   file_1= "Factory_Reset_Result_Sheet_"
   file_1 = file_1 + Timestr
   file_1 = file_1 + ".csv"
   tbl=waitForObjectExists(":KoolProg_Table")
   items=tbl.nativeObject.Items
  
   openfile = open(file_1,'wt') 
   writer = csv.writer(openfile)
   writer.writerow(["ParameterName", "KP_Default","DB_Default","Result"])
   records = testData.dataset(file)
   for rec in records:
      #id = testData.field(rec, 5)
      name = testData.field(rec, 2)
      Default = testData.field(rec, 5)
#        Min = testData.field(rec, 7)
#        Max = testData.field(rec, 6)
#        Unit = testData.field(rec, 9) 
#        Enum = testData.field(rec, 8)
#        #Info_Help = testData.field(rec, 7)
#        mylist=[]
#        if(Enum != ""):
#            for x in Enum.split(','):
#                for y in x.split(':'): 
#                    if(y == Default):                        
#                        for z in x.split(':'):
#                            mylist.append(z)
#                            Default = z 
      
      for i in range (0, items.Count-1):
          item=items.at(i)
          if (name == item.ParameterName):        
              DefaultValue_Result = test.compare(Default, item.DefaultValue)
              writer.writerow([item.ParameterName, item.DefaultValue,Default,DefaultValue_Result])            
   

def testRandomPlot():
   result = False
   resultList = []
   tbl=waitForObjectExists(":KoolProg_Table")  
   fieldsTable=parseFieldsForPlot(tbl)
   #IsSelectedForPlotting
   Object=tbl.nativeObject
   items=tbl.nativeObject.Items
   for i in range (0,10):        
       num = random.randint(0, items.Count-1)
       while num in resultList:
           num = random.randint(0, items.Count-1)
       resultList.append(num)
   count = len(resultList)
   for i in range(0,count-1): 
       item=items.at(resultList[i])
       name = item.ParameterName           
       test.log("Plot: %s" % setParameterPlotAndFav(fieldsTable, name))
   result = True
   return  result   

       
def parseFieldsForPlot(tbl):
           fieldsTable={}    
           items_1=object.children(tbl)
           for item_1 in items_1:        
               if(object.properties(item_1)["type"] ==  "WPFControl"):
                   expander=object.children(item_1)
                   for child in expander:                
                       if(object.properties(child)["type"] ==  "Expander"):
                           rows=object.children(child)
                           for row in rows:
                               if(object.properties(row)["type"] == "TableRow"):
                                   fields=object.children(row)
                                   fieldName=None    
                                                                   
                                   for field in fields: 
                                       if(object.properties(field)["type"] == "TableCell" and object.properties(field)["column"] == 2):                                               
                                           edits=object.children(field)
                                               
                                       if(object.properties(field)["type"] == "TableCell" and object.properties(field)["column"] == 4):
                                               fieldName=object.properties(field)["text"] 
                                                            
                                               for edit in edits:
                                                   if(object.properties(edit)["type"] == "CheckBox" and object.properties(edit)["name"] == "chkService"):
                                                   #if (fieldName != None):                                                   
                                                       test.log("Parsing:%s" % (fieldName))                                                
                                                       fieldsTable[fieldName]=edit 
                                      
                                           
                                                                                                                                           
           return fieldsTable

       
def parseFieldsForFavorites(tbl):
           fieldsTable={}    
           items_1=object.children(tbl)
           for item_1 in items_1:        
               if(object.properties(item_1)["type"] ==  "WPFControl"):
                   expander=object.children(item_1)
                   for child in expander:                
                       if(object.properties(child)["type"] ==  "Expander"):
                           rows=object.children(child)
                           for row in rows:
                               if((object.properties(row)["type"] == "TableRow") and (row.nativeObject.IsVisible == True) and (row.nativeObject.DataContext.IsEnabled == True)):
                                   fields=object.children(row)
                                   fieldName=None                                                                
                                   for field in fields:  
                                       if(object.properties(field)["type"] == "TableCell" and object.properties(field)["column"] == 1 and field.nativeObject.IsVisible == True):
                                               edits=object.children(field)
                                               
                                       if(object.properties(field)["type"] == "TableCell" and object.properties(field)["column"] == 4 and field.nativeObject.IsVisible == True):
                                               fieldName=object.properties(field)["text"] 
                                                            
                                               for edit in edits:
                                                   if(object.properties(edit)["type"] == "CheckBox" and object.properties(edit)["name"] == "chkFavourites"):
                                                       images = object.children(edit)
                                                       for image in images:
                                                           test.log("Parsing:%s" % (fieldName))                                                
                                                           fieldsTable[fieldName]=image
                                                           test.log("KEY:"+str(fieldName)+"--- VALUE"+ str(image))
                                                                                                                         
           return fieldsTable

   
def setParameterPlotAndFav(fieldsTable, parameterName):
   found = False
   if(fieldsTable != None):                            
       if(fieldsTable[parameterName] != None):
           found=True
           edit=fieldsTable[parameterName]   
           snooze(1) 
           mouseClick(waitForObject(edit))
           #clickButton(waitForObject(edit))
           #type(waitForObject(edit), "<Tab>")                                                                                                     
   return found


def setParameterFav(fieldsTable, parameterName):
   found = False
   test.log("PN:"+str(parameterName))
   if(fieldsTable != None):                            
       if(fieldsTable[parameterName] != None):
           found=True
           edit=fieldsTable[parameterName]   
           snooze(1) 
           print edit
           mouseClick(waitForObject(edit))
           #clickButton(waitForObject(edit))
           #type(waitForObject(edit), "<Tab>")                                                                                                     
   return found   


def verifyActiveAlarm():
   result = False
   alarmTable = []
   tbl=waitForObjectExists(":KoolProg_Table")
   tblActiveAlarm=waitForObjectExists(":KoolProg_Table_2")
   items_1=object.children(tblActiveAlarm)
   for item_1 in items_1:        
       if(object.properties(item_1)["type"] ==  "TableRow"):
           fields=object.children(item_1)
           for field in fields: 
               if(object.properties(field)["type"] == "TableCell" and object.properties(field)["column"] == 1):
                   if(field != None):
                       alarmName=object.properties(field)["text"]
                       alarmTable.append(alarmName)
   activeAlarmsCount = len(alarmTable)
   test.log(alarmName)
   Object=tbl.nativeObject
   items=tbl.nativeObject.Items
#     for i in range (0, items.Count-1):
#         item=items.at(i)
   for i in range (0,activeAlarmsCount):        
       name = alarmTable[i]
       for j in range (0, items.Count-1):
           item=items.at(j)
           if(name == item.ParameterName):
               test.compare(item.Value, "On", "Alarm: "+ name)
   result = True
   return result
                          
               
def checkFavorites():
    result = False
    resultList = []
    tbl=waitForObjectExists(":KoolProg_Table")  
    fieldsTable=parseFieldsForFavorites(tbl)
    Object=tbl.nativeObject
    items=tbl.nativeObject.Items
    for i in range (0,10):        
        num = random.randint(0, items.Count-1)
        while num in resultList:
            num = random.randint(0, items.Count-1)
        resultList.append(num) 
    count = len(resultList)    
    test.log(str(count))
    for i in range(0,count): 
        item=items.at(resultList[i])
        name = item.ParameterName 
        test.log(str(name))
        for key in fieldsTable.keys():
            if (str(key) == str(name)):                          
                test.log("Favourite: %s" % setParameterFav(fieldsTable, name))
            result = True
    return result 

       
def unCheckFavourites():
   result = False
   favouriteList = []
   tbl=waitForObjectExists(":KoolProg_Table")
   fieldsTable=parseFieldsForFavorites(tbl)
   items=tbl.nativeObject.Items
   for i in range (0,items.Count-1):
       item=items.at(i)
       if(item.FavouritesValue == True):
           favouriteList.append(item.ParameterName)
   
   favCount = len(favouriteList)   
   test.log(str(favCount))
   for i in range (0, favCount):
       test.log("UnCheck Favourite: %s" % setParameterFav(fieldsTable, favouriteList[i]))
       result = True
   return result


def verifySearchParameters_AK_CC():
   result = False
   tbl=waitForObjectExists(":KoolProg_Table")    
   items=tbl.nativeObject.Items
   randomIndex = random.randint(0,items.Count-1)
   item = items.at(randomIndex)
   searchText = item.ParameterName[:3]
   print (searchText)
   mouseClick(waitForObject(":KoolProg_Edit"), MouseButton.PrimaryButton)
   type(waitForObject(":KoolProg_Edit"), searchText)
   snooze(2)
   mouseClick(waitForObject(":KoolProg.System.Windows.Controls.Image_Button_3"), MouseButton.PrimaryButton)
   searchListExcel = []
   searchListKoolProg = []
   fieldsTable=parseVisibleRow(tbl)
   for key,value in fieldsTable.items():
       if key != "":
           test.log("%s" % key)
           searchListKoolProg.append(key)
   searchKoolProgCount = len(searchListKoolProg)
   window=waitForObject(":KoolProg_Window")
   
   
   name1=getControl(window,"Label","tbProductInfoValue0")
   if(name1 == None):
       print "None"
   else:    
       test.log("type:%s "% name1["type"])
       test.log("name:%s "% name1["name"])
       test.log("text:%s "% name1["text"])
       Product = (name1["text"])
       Product_Name = Product[0:9]
       print (Product_Name)
   if (Product_Name == "AK-CC 550"):
       file = "Danfoss."+Product_Name+".search.csv"
       records = testData.dataset(file) 
       for rec in records:
           groupName = testData.field(rec, 0)
           name = testData.field(rec, 1)
           menuCode = testData.field(rec, 2)
           if((name.find(searchText) == -1)&(menuCode.find(searchText) == -1)&(groupName.find(searchText) == -1)):
               snooze(0.2)
           else:
               searchListExcel.append(name)
               test.log(name)
       searchExcelCount = len(searchListExcel)
       result = test.compare(searchKoolProgCount, searchExcelCount, "Search Result")
   mouseClick(":KoolProg.System.Windows.Controls.Image_Button_3"), MouseButton.PrimaryButton
   return result  

   
def verifySearchParameters():
   result = False
   tbl=waitForObjectExists(":KoolProg_Table")    
   items=tbl.nativeObject.Items
   randomIndex = random.randint(0,items.Count-1)
   item = items.at(randomIndex)
   searchText = item.ParameterName[:3]
   mouseClick(waitForObject(":KoolProg_Edit"), MouseButton.PrimaryButton)
   type(waitForObject(":KoolProg_Edit"), searchText)
   snooze(2)
   mouseClick(waitForObject(":KoolProg.System.Windows.Controls.Image_Button_3"), MouseButton.PrimaryButton)
   searchListExcel = []
   searchListKoolProg = []
   fieldsTable=parseVisibleRow(tbl)
   for key,value in fieldsTable.items():
       if key != "":
           test.log("%s" % key)
           searchListKoolProg.append(key)
   searchKoolProgCount = len(searchListKoolProg)
   window=waitForObject(":KoolProg_Window")
   
   
   name1=getControl(window,"Label","txtProuctName")
   if(name1 == None):
       print "None"
   else:    
       test.log("type:%s "% name1["type"])
       test.log("name:%s "% name1["name"])
       test.log("text:%s "% name1["text"])
       Product = (name1["text"])
       Product_Name = Product
   
   if (Product_Name[0:4] == "ERC1"):
       name1=getControl(window,"Label","txtCodeNumber")  
       if(name1 == None):
           print "None"
       else:    
           test.log("type:%s "% name1["type"])
           test.log("name:%s "% name1["name"])
           test.log("text:%s "% name1["text"])
           Code_Num = (name1["text"])
           Code_Number = Code_Num[0:8]
                  
   else:
       name1=getControl(window,"Label","txtApp")
       if(name1 == None):
           print "None"
       else:    
           test.log("type:%s "% name1["type"])
           test.log("name:%s "% name1["name"])
           test.log("text:%s "% name1["text"])
           Application = (name1["text"]) 
   if (Product_Name[0:4] == "ETC1"):
       file = Global_Scripts_Path+"\Danfoss.ETC1H."+Application+"_search.csv"
       snooze(3)
   elif (Product_Name [0:4] == "ERC2"):
       file = Global_Scripts_Path+"\ERC21x_search.csv"
       snooze(3)
   elif (Product_Name[0:6] == "ERC111"):
       if ((Code_Number == "080G3237")| (Code_Number == "080G3247")):
           file = Global_Scripts_Path+Product_Name[0:6]+"_"+Code_Number+"_search.csv"
           snooze(3)
       else: 
           file = Global_Scripts_Path+Product_Name[3:6]+"_std_search.csv"
           snooze(3)
   elif (Product_Name[0:6] == "ERC112"):
       if ((Code_Number == "080G3220")| (Code_Number == "080G3221")|(Code_Number == "080G3229")|(Code_Number == "080G3248") ):
           file = Global_Scripts_Path+"\ERC"+Product_Name[3:6]+"_"+Code_Number+"_search.csv"
           snooze(3)
       else: 
           file = Global_Scripts_Path+"\ERC"+Product_Name[3:6]+"_std_search.csv"
           snooze(3)
   elif (Product_Name[0:6] == "ERC113"):
       file = Global_Scripts_Path+"\ERC"+Product_Name[3:6]+"_std_search.csv"
       snooze(3)
           
   snooze(3)
   records = testData.dataset(file) 
   for rec in records:
       name = testData.field(rec, 0)
       menuCode = testData.field(rec, 1)
       groupName = testData.field(rec, 2)
       if((name.find(searchText) == -1)&(menuCode.find(searchText) == -1)&(groupName.find(searchText) == -1)):
           snooze(0.2)
       else:
           searchListExcel.append(name)
           test.log(name)
   searchExcelCount = len(searchListExcel)
   result = test.compare(searchKoolProgCount, searchExcelCount, "Search Result")
   #result = True
   return result    

      
def parseVisibleRow(tbl):
   fieldsTable={}    
   items=object.children(tbl)
   for item in items:        
       if(object.properties(item)["type"] ==  "WPFControl"):
           expander=object.children(item)
           for child in expander:                
               if(object.properties(child)["type"] ==  "Expander"):
                   rows=object.children(child)
                   for row in rows:
                       if((object.properties(row)["type"] == "TableRow") and (row.nativeObject.IsVisible == True) and (row.nativeObject.DataContext.IsEnabled == True)):
                           fields=object.children(row)
                           fieldName=None        
                           for field in fields:                                                                
                               if(object.properties(field)["type"] == "TableCell" and object.properties(field)["column"] == 4):
                                   fieldName=object.properties(field)["text"]                            
                               if(object.properties(field)["type"] == "TableCell" and object.properties(field)["column"] == 7 and fieldName != ""):
                                   edits=object.children(field)                                    
                                   for edit in edits:
                                       if((object.properties(edit)["type"] == "Edit" and object.properties(edit)["name"] == "txtValue")) or( (object.properties(edit)["type"] == "ComboBox" and object.properties(edit)["name"] == "cmbEnums")):
                                           #if (fieldName != None):
                                               #test.log("Parsing:%s" % (fieldName))                                                
                                           fieldsTable[fieldName]=edit
                                                                                                                                             
   return fieldsTable


def checkEnableVisibleEKE():
   global checkParameters
   checkParameters = []
   file = Global_Scripts_Path+"\EKE_Visibility.csv"   
   VisibilityList = []
   visibleSet = set()
   records = testData.dataset(file)
   for rec in records:
       name = testData.field(rec, 0)
       visibility = testData.field(rec,2)
       variableName = testData.field(rec,3)
#         if(visibility != None):
       if(visibility != ""):
           for x in visibility.split(' '):
                       isText = hasTexts(x)
                       if(isText == True):
                           test.log(x)
                           if x not in visibleSet:
                               x = x.replace("(", "")
                               VisibilityList.append(x)
                               visibleSet.add(x)
   
   
   count = len(VisibilityList)
   test.log(str(count), "VariableNames")
   records = testData.dataset(file)
   for rec in records:
       name = testData.field(rec, 0)        
       variableName = testData.field(rec,3)
       for i in range (0, count-1):
           variable = VisibilityList[i]
           if(variable == variableName):
               checkParameters.append(name)
                                                  
                          
   print (checkParameters) 


def CountDownrange(value):
   result = False
   type(waitForObject(":KoolProg_Edit"), "<Right>")
   type(waitForObject(":KoolProg_Edit"), "<Backspace>")
   type(waitForObject(":KoolProg_Edit"), value)

   n = __builtin__.int(value)
   for i in range(0, n):
       mouseClick(waitForObject(":KoolProg.START_Label"))
       clickButton(waitForObject(":MessageBoxDisplay.OK_Button"))  
       result = True
   return result
       
         
def CountUprange(value):
  result = False
  type(waitForObject(":KoolProg_Edit"), "<Right>")
  type(waitForObject(":KoolProg_Edit"), "<Backspace>")
  type(waitForObject(":KoolProg_Edit"), value)

  n = __builtin__.int(value)
  for i in range(0, n):
       mouseClick(waitForObject(":KoolProg.START_Label"))
       clickButton(waitForObject(":MessageBoxDisplay.OK_Button"))
       result = True
  return result

       
def Edit(symbolicname, value):
   test.log("inside edit")
   result = False 
   type(waitForObject(symbolicname), "<Right>")
   type(waitForObject(symbolicname), "<Backspace>")
   type(waitForObject(symbolicname), value)
   result = True
   return result
   

def Max_Length(symbolicname, value):
   test.log("inside max length")
   result = False
   tbl=waitForObjectExists(symbolicname)  
   test.compare(value ,(tbl.maxlength))
   result = True 
   return result 


###AK CC #####


def DB_Verification():
   KP_DB = "AK_CC_KP_DB.csv"
   Squish_DB = "Squish_DB_AK_CC.csv"
   
   file= "Result_Sheet_"
#     file = file + Timestr
   file = file + ".csv"
   
   openfile = open(file,'wt') 
   writer = csv.writer(openfile)
   writer.writerow(["KP_DB_GrpCode", "Squish_DB_GrpCode","Result", "KP_DB_Menucode","Squish_DB_Menucode", "Result" ,"KP_DB_Groupname", "Squish_DB_Groupname", "Result", "KP_DB_Name", "Squish_DB_Name", "Result", "KP_DB_PNU", "Squish_DB_PNU", "Result", "KP_DB_DefaultValue", "Squish_DB_DefaultValue", "Result", "KP_DB_MinValue", "Squish_DB_MinValue", "Result" ,"KP_DB_MaxValue", "Squish_DB_MaxValue", "Result", "KP_DB_Unit", "Squish_DB_Unit", "Result", "KP_DB_Scale", "Squish_DB_Scale", "Result", "KP_DB_Datatype", "Squish_DB_Datatype", "Result", "KP_DB_Enum", "Squish_DB_Enum", "Result", "KP_DB_ReadOnly", "Squish_DB_ReadOnly", "Result", "KP_DB_VN", "Squish_DB_VN", "Result"])
   
   
   records = testData.dataset(KP_DB)
   records_1 = testData.dataset(Squish_DB)
   for rec in records:
       KP_groupCode = testData.field(rec, 0)
       KP_Menu_Code = testData.field(rec, 1)
       KP_Group_Name = testData.field(rec, 2)
       KP_Parameter_Name = testData.field(rec, 3)
       KP_PNU = testData.field(rec, 4)
       KP_Default = testData.field(rec, 5)
       KP_Min = testData.field(rec, 6)
       KP_Max = testData.field(rec, 7)
       KP_Unit = testData.field(rec, 8)
       KP_Scaling = testData.field(rec, 9)
       KP_Datatype = testData.field(rec, 10)
       KP_Enum = testData.field(rec, 11)
       KP_Read_Only =  testData.field(rec, 12)
       #Info_Help = testData.field(rec, 13)
       #Decimals = testData.field(rec, 14)
       KP_Variable_Name= testData.field(rec, 13)
       mylist=[]
       if(KP_Enum != ""):
           for x in KP_Enum.split(','):
               for y in x.split(':'): 
                   if(y == KP_Default):                        
                       for z in x.split(':'):
                           mylist.append(z)
                           KP_Default = z
      
       for rec_1 in records_1:
           groupCode = testData.field(rec_1, 0)
           Menu_Code = testData.field(rec_1, 1)
           Group_Name = testData.field(rec_1, 2)
           Parameter_Name = testData.field(rec_1, 3)
           PNU = testData.field(rec_1, 4)
           Default = testData.field(rec_1, 5)
           Min = testData.field(rec_1, 6)
           Max = testData.field(rec_1, 7)
           Unit = testData.field(rec_1, 8)
           Scaling = testData.field(rec_1, 9)
           Datatype = testData.field(rec_1, 10)
           Enum = testData.field(rec_1, 11)
           Read_Only =  testData.field(rec_1, 12)
   #         Info_Help = testData.field(rec, 13)
   #         Decimals = testData.field(rec, 14)
           Variable_Name= testData.field(rec_1, 15)
           mylist=[]
           if(Enum != ""):
               for x in Enum.split(','):
                   for y in x.split(':'): 
                       if(y == Default):                        
                           for z in x.split(':'):
                               mylist.append(z)
                               Default = z
                               
           if((Parameter_Name == KP_Parameter_Name) & (Group_Name == KP_Group_Name)):
               Group_Code_Result = test.compare(groupCode, KP_groupCode)      
               MenuCode_Result = test.compare(Menu_Code, KP_Menu_Code)
               GroupName_Result = test.compare(Group_Name, KP_Group_Name)
               Parameter_Name_Result = test.compare(Parameter_Name, KP_Parameter_Name)
               PNU_Result = test.compare(PNU, KP_PNU)
               DefaultValue_Result = test.compare(Default, KP_Default)
               MinValue_Result = test.compare(Min, KP_Min)
               MaxValue_Result = test.compare(Max, KP_Max)
               Unit_Result = test.compare(Unit, KP_Unit)
               Scaling_Result = test.compare(Scaling, KP_Scaling)
               Datatype_Result = test.compare(Datatype, KP_Datatype)
               Enum_Result = test.compare(Enum, KP_Enum)
               ReadOnly_Result = test.compare(Read_Only, KP_Read_Only)
               VN_Result = test.compare(Variable_Name, KP_Variable_Name)
               
               writer.writerow([KP_groupCode, groupCode, Group_Code_Result, KP_Menu_Code, Menu_Code, MenuCode_Result, KP_Group_Name, Group_Name, GroupName_Result, KP_Parameter_Name, Parameter_Name, Parameter_Name_Result, KP_PNU, PNU, PNU_Result, KP_Default, Default, DefaultValue_Result, KP_Min, Min, MinValue_Result, KP_Max, Max, MaxValue_Result, KP_Unit, Unit, Unit_Result, KP_Scaling, Scaling, Scaling_Result, KP_Datatype, Datatype, Datatype_Result, KP_Enum, Enum, Enum_Result, KP_Read_Only, Read_Only, Read_Only, KP_Variable_Name, Variable_Name, VN_Result])                                      


File_Path = None

def clickAll(symbolicname):
    test.log("Inside Click All Function")
    snooze(10)
    WPF_Control = waitForObject(symbolicname)
#     mouseClick(WPF_Control), MouseButton.PrimaryButton
    if (WPF_Control != None):
        children=object.children(WPF_Control)
        if(children != None):
            for child in children:
                if ((child["class"] == "System.Windows.Controls.TreeView") and child["name"] == "treeViewParameters" and child.nativeObject.IsVisible == True):
                    grandchild = object.children(child)
                    if (grandchild != None):
                        for subgroup in grandchild:
                            if ((subgroup["class"] == "System.Windows.Controls.TreeViewItem") and (subgroup.nativeObject.DataContext.AllMenu == "All")):
                                test.log("All-Click")
                                mouseClick(subgroup), MouseButton.PrimaryButton
#                             else :
#                                 test.log("All could not be clicked on")
                elif ((child["class"] == "System.Windows.Controls.TreeView") and child["name"] != "treeViewParameters" and child.nativeObject.IsVisible == True):
                    grandchild = object.children(child)
                    if (grandchild != None):
                        for subgroup in grandchild:
                            if ((subgroup["class"] == "System.Windows.Controls.TreeViewItem") and (subgroup.nativeObject.Header == "All")):
                                test.log("All-Click")
                                mouseClick(subgroup), MouseButton.PrimaryButton
#                             else :
#                                 test.log("All could not be clicked on")
                                            
def AKCC_Product_Variant(): ## Not used currently in AKCC. Kindly refer "selectControllerparse" function##
   global File_Path
   result= False
   
   tb_folder_Name =waitForObject(":Newproject_TabFolder")
   tb_folder = getControl(tb_folder_Name, "TabFolder", "tabNewproject")
   
   
   
   with codecs.open(findFile("testdata", r"\Latest_CDF\device.jso"),encoding='utf-8') as data_file:
       content = data_file.read()
       content = content.replace(u'\ufeff','') 
       data = json.loads(content)
       
       Parameter_Count = len(data["Parameters"])
       
       Headers = len(data["Header"])
       
       Description = data["Header"]["Description"]
       Product_Variant =str(Description)
       test.log(str(Product_Variant))
 
   fieldsTable = {}    
   items_1=object.children(tb_folder)
   for item_1 in items_1:        
       if(object.properties(item_1)["type"] ==  "TabItem"):
           expander=object.children(item_1)
           for child in expander:                
               if(object.properties(child)["type"] ==  "Table"):
                   rows=object.children(child)
                   for row in rows:
                       if(object.properties(row)["type"] == "WPFControl"):
                           fields=object.children(row)        
                           for field in fields:                                                                
                               if(object.properties(field)["type"] == "Expander"):
                                   Expander_Name = field.nativeObject.DataContext.Name
                                   if (str(Product_Variant[0:7].strip()) == str(Expander_Name.strip())):
                                       test.log("****CDF and Expander names match****")
#                                         mouseClick(field), MouseButton.PrimaryButton
                                   edits = object.children(field)
                                   for edit in edits:                               
                                       if(object.properties(edit)["type"] == "TableRow"):
                                           cells = object.children(edit)
                                           for cell in cells:
                                               if(object.properties(cell)["type"] == "TableCell"):
                                                   fieldName=object.properties(cell)["text"] 
                                                   if (str(fieldName) == str(Product_Variant)) :
                                                       test.log("ExpanderNames: " +str (fieldName))   
                                                       mouseClick(cell), MouseButton.PrimaryButton 
                                                                                                                          

def AKCC_Application_Wizard():
   global File_Path
   window_comboBox = waitForObject(":Product Name.Code Number:_ComboBox")
   window_SWversion = waitForObject(":Product Name_ComboBox")
   
   with codecs.open(findFile("testdata", r"\Latest_CDF\device.jso"),encoding='utf-8') as data_file:
       content = data_file.read()
       content = content.replace(u'\ufeff','') 
       data = json.loads(content)
       
       Parameter_Count = len(data["Parameters"])
       
       Headers = len(data["Header"])
                               
       Code_Number = data["Header"]["Name"]
       Code_Number = str(Code_Number)
       
       SW_Version = data["Header"]["SWVersion"]
       SW_Version = str(SW_Version)
   
#     
#     name1_cont=getControl(window_path,"Edit","txtCDF")  
#     if(name1_cont == None):
#         print "None"
#         result = False 
#     else:    
#         test.log("type:%s "% name1_cont["type"])
#         test.log("name:%s "% name1_cont["name"])
#         test.log("text:%s "% name1_cont["text"])
#         File_Path = (name1_cont["text"])
       
   name2_cont=getControl(window_comboBox,"ComboBox","cmbCodeNumber")  
   if(name2_cont == None):
       print "None"
       result = False
   else:    
       test.log("type:%s "% name2_cont["type"])
       test.log("name:%s "% name2_cont["name"])
       test.log("text:%s "% name2_cont["nativeObject"]["Text"])
       WizardCodeNumber = (name2_cont["nativeObject"]["Text"])
       WizardCodeNumber = str(WizardCodeNumber)
#         print (WizardCodeNumber)
       
   name3_cont=getControl(window_SWversion,"ComboBox","cmbSWversion")  
   if(name3_cont == None):
       print "None"
       result = False
   else:    
       test.log("type:%s "% name3_cont["type"])
       test.log("name:%s "% name3_cont["name"])
       test.log("text:%s "% name3_cont["nativeObject"]["Text"])
       WizardSWVersion = (name3_cont["nativeObject"]["Text"])
       WizardSWVersion = str(WizardSWVersion)
   
   result = test.compare(Code_Number, WizardCodeNumber)
   result1 = test.compare(SW_Version, WizardSWVersion)
   test.log("CodeNumber comparison is:"+ str(result))
   test.log("SW comparison is:"+ str(result1))
      
               
def AK_CC_SW_Code():
   result = False
   waitForObject(":KoolProg.System.Windows.Controls.Image_Button"),2000
   window=waitForObject(":KoolProg_Window")
   #print("count:%s"% len(window))
   
   name1_cont=getControl(window,"Label","tbProductInfoValue1")  
   if(name1_cont == None):
       print "None"
       result = False
   else:    
       test.log("type:%s "% name1_cont["type"])
       test.log("name:%s "% name1_cont["name"])
       test.log("text:%s "% name1_cont["text"])
       CodeNumber_file = (name1_cont["text"])
       CodeNumber_file = str(CodeNumber_file)
#         print (CodeNumber_file)
   
   name3_cont=getControl(window,"Label","tbProductInfoValue0")  
   if(name3_cont == None):
       print "None"
       result = False
   else:    
       test.log("type:%s "% name3_cont["type"])
       test.log("name:%s "% name3_cont["name"])
       test.log("text:%s "% name3_cont["text"])
       Product_Name_file = (name3_cont["text"])
       Product_Name_file = str(Product_Name_file)
   
       
   name2_cont=getControl(window,"Label","tbProductInfoValue3")  
   if(name1_cont == None):
       print "None"
       result = False
   else:    
       test.log("type:%s "% name2_cont["type"])
       test.log("name:%s "% name2_cont["name"])
       test.log("text:%s "% name2_cont["text"])
       SWVersion_file = (name2_cont["text"])
       SWVersion_file = str(SWVersion_file)
#         print (SWVersion_file)
   
   with codecs.open(findFile("testdata", r"\Latest_CDF\device.jso"),encoding='utf-8') as data_file:
       content = data_file.read()
       content = content.replace(u'\ufeff','') 
       data = json.loads(content)
       
       Parameter_Count = len(data["Parameters"])
       
       Headers = len(data["Header"])
                               
       Code_Number = data["Header"]["Name"]
       Code_Number = str(Code_Number)
       Product_Variant = data["Header"]["Description"]
       Product_Variant = str(Product_Variant)
       SW_Version = data["Header"]["SWVersion"]
       SW_Version = str(SW_Version)

#         print(Code_Number)
#         print(SW_Version)
       
       result = test.compare(CodeNumber_file, Code_Number)
       result1 = test.compare(Product_Name_file, Product_Variant)
       result2 = test.compare(SWVersion_file, SW_Version)
       
       test.log("CodeNumber comparison is:"+ str(result))
       test.log("ProductName comparison is:"+ str(result1))
       test.log("SW comparison is:"+ str(result2))


gExpanderList=[]
gParamList=[]

def AKCC_SG():
   result = False
   waitForObject(":KoolProg.System.Windows.Controls.Image_Button")

   window=waitForObject(":KoolProg_Window")
   tbl = getControl(window, "Table" , "datagridParameters")

#     doubleClick(waitForObject(":Danfoss.T4CClient.TreeViewParameters.Danfoss.T4CClient.TreeViewParameters_TreeItem_3"), MouseButton.PrimaryButton)
   
   tv=getControl(window, "Tree", "treeViewParameters")
   test.log("tv is:"+ str(tv))
   
#    print("Expander length"+str(len(gExpanderList)))
#    print("Parameter length"+str(len(gParamList)))
   
#    if(tv != ""):
#        if (tv != None):
#            children=object.children(tv)
#            if(children != None):
#                for child in children:
#                    if (child["class"] == "System.Windows.Controls.TreeViewItem"):
#                        if((child.nativeObject.Header.AllMenu != "Main menu") & (child.itemCount != 0)):
#                            doubleClick(child)
              
   AKCCparseTreeView(tv, tbl)  
     
#    print("Expander length"+str(len(gExpanderList)))
#    print("Parameter length"+str(len(gParamList)))
   
   for expander in gExpanderList:
       print ("Expander:" + expander)
   for param in gParamList:
       print ("Parameters:" + param)   

gExpanderList = []
gParamList = []

def AKCCparseIOTreeView(parent, tbl):    
   if (parent != None):
       children=object.children(parent)
       if(children != None):
           for child in children:
               if (child["class"] == "System.Windows.Controls.TreeViewItem"):
                   if((child.nativeObject.Header.AllMenu != "Favourites") & (child.itemCount == 0)):
                       #gHeader_List.append(child.nativeObject.Header.AllMenu)                       
                       
                       doubleClick(child)
                       #print("Expander:" + child.nativeObject.Header.AllMenu)
                       Expander, Expander_Name, ItemCount = parseAKCCVisibleExpander(tbl)
                        
                       #print (Expander)
                       
                       if(Expander != None):
#                             gExpanderList.append(Expander_Name+":"+str(ItemCount))
                           Parameters = parseAKCCVisibleRows(Expander)                            
                           for param in Parameters:
                               AKCC_IO_SG_Comparison(Expander_Name, param)                           
                   else:
                       if((child.nativeObject.Header.AllMenu != "Favourites")&(child.nativeObject.Header.AllMenu != "All")):
                           doubleClick(child)
                           AKCCparseIOTreeView(child, tbl)
                       else:
                           AKCCparseIOTreeView(child, tbl)
                       #print (child.nativeObject.Header.AllMenu)
   return

gExpanderList = []
gParamList = []

def AKCCparseTreeView(parent, tbl):    
   global gExpanderList
   global gParamList
    
   if (parent != None):
       children=object.children(parent)
#         test.log("children are: "+ str(children))
       if(children != None):
           for child in children:
#                 test.log ("child is:" + str(child))
               if (child["class"] == "System.Windows.Controls.TreeViewItem"):
#                     test.log("first IF") 
                   
                   if((child.nativeObject.Header.AllMenu != "Favourites") and (child.nativeObject.Header.AllMenu != "Main menu")and (child.nativeObject.Header.AllMenu != "All")):
                       #gHeader_List.append(child.nativeObject.Header.AllMenu)  
#                         test.log("it is"+child.nativeObject.Header.IsVisibleItem)                    
                       if (child.nativeObject.Header.IsVisibleItem == True):##Added to check visibility of Expanders##
                           if(child.itemCount == 0):
                               doubleClick(child)
                               #print("Expander:" + child.nativeObject.Header.AllMenu)
                               Expander, Expander_Name, ItemCount = parseAKCCVisibleExpander(tbl)
                               test.log(str(Expander)+","+ str(Expander_Name)+","+str(ItemCount))
                               #print (Expander)
                                
                               if(Expander != None):
       #                             gExpanderList.append(Expander_Name+":"+str(ItemCount))
                                   Parameters = parseAKCCVisibleRows(Expander)  
                                   test.log("AKCCparseTreeView parameters: " +str(Parameters))                          
                                   for param in Parameters:
                                       AKCC_SG_Comparison(Expander_Name, param)
       #                                 gParamList.append(Expander_Name+":"+param)
                               else: 
                                   test.log("Expander does not exist") 
                                   
                           else:
                               doubleClick(child)
                               AKCCparseTreeView(child, tbl)
                       else:
                           test.log(child.nativeObject.Header.AllMenu+" is invisible expander")
                                                             
#                     else:
#                         test.log("Can not click on treeview groups")
                       
   return

gHeader_List = []
def parseAKCCVisibleExpander(tbl):
   Expander_Name = None
   Item_Count = None
   Expander = None
   fieldsTable={}    
   items=object.children(tbl)
   for item in items:        
       if(object.properties(item)["type"] ==  "WPFControl"):
           expander=object.children(item)
           for child in expander:                
               if(object.properties(child)["type"] ==  "Expander" and child.nativeObject.IsExpanded == True):
                   Expander_Name = child.nativeObject.DataContext.Name
                   Item_Count = child.nativeObject.DataContext.ItemCount
#                     print ("Expander:%s "% Expander_Name)
#                     print ("Items:%s "% Item_Count)
                   Expander = child
                   return (Expander, Expander_Name, Item_Count)
#                     rows=object.children(child)
#                     for row in rows:
#                         if(object.properties(row)["type"] == "TableRow" and row.nativeObject.IsVisible == True and row.nativeObject.DataContext.IsEnabled == True):
#                             fields=object.children(row)
#                             fieldName=None        
#                             for field in fields:                                                                
#                                 if(object.properties(field)["type"] == "TableCell" and object.properties(field)["column"] == 4):
#                                     fieldName=object.properties(field)["text"]                            
#                                 if(object.properties(field)["type"] == "TableCell" and object.properties(field)["column"] == 7 and fieldName != ""):
#                                     edits=object.children(field)                                    
#                                     for edit in edits:
#                                         if((object.properties(edit)["type"] == "Edit" and object.properties(edit)["name"] == "txtValue")) or( (object.properties(edit)["type"] == "ComboBox" and object.properties(edit)["name"] == "cmbEnums")):
#                                             #if (fieldName != None):
#                                                 #test.log("Parsing:%s" % (fieldName))                                                
#                                             fieldsTable[fieldName]=edit
                                                                                                                                             
   return None, None, None

def parseAKCCVisibleRows(child):
   fieldNames = []
   rows=object.children(child)
   for row in rows:
       if(object.properties(row)["type"] == "TableRow"):
           fields=object.children(row)
           fieldName=None 
           for field in fields:                                                                
               if(object.properties(field)["type"] == "TableCell" and object.properties(field)["column"] == 4):
                   fieldName=object.properties(field)["text"]   
                   fieldNames.append(fieldName)
                    
   return (fieldNames)  


def AKCC_SG_Comparison(Expander_Name, param):
   SG_Comparison_File = Output_Global_Path+"\SGParameters"
   SG_Comparison_File = SG_Comparison_File + Timestr
   SG_Comparison_File = SG_Comparison_File + ".csv"
   openfile = open(SG_Comparison_File,'wt') 
   writer = csv.writer(openfile)
   writer.writerow(["GroupNameKP","GroupNameDB", "ParameterNameKP", "ParameterNameDB", "Result_SG", "Result_PN"]) 
   
   file = Global_Scripts_Path+"\AK_CC_DB_Squish.csv"
     
   records = testData.dataset(file)
   for rec in records: 
       GroupName = testData.field(rec, 2)
       ParameterName = testData.field(rec, 3)
       for item in ParameterName: 
           if (param == ParameterName):
                Result_1 = test.compare(GroupName,Expander_Name)
                Result_2 = test.compare(param, ParameterName)
                writer.writerow([Expander_Name,GroupName,Result_1, param, ParameterName, Result_2])
                break
#     print (Expander_Name)
#     print (param)

def verifySearchParameters_AK_CC():
   with codecs.open(findFile("testdata", r"\Latest_CDF\device.jso"),encoding='utf-8') as data_file:
       content = data_file.read()
       content = content.replace(u'\ufeff','') 
       data = json.loads(content)
       
       Code_Number = data["Header"]["Name"]
       Code_Number = str(Code_Number)
       Product_Variant = data["Header"]["Description"]
       Product_Variant = str(Product_Variant)
       SW_Version = data["Header"]["SWVersion"]
       SW_Version = str(SW_Version)
       
   result = False
   tbl=waitForObjectExists(":KoolProg_Table")    
   items=tbl.nativeObject.Items
   randomIndex = random.randint(0,items.Count-1)
   item = items.at(randomIndex)
   searchText = item.ParameterName[:3]
   print (searchText)
   mouseClick(waitForObject(":KoolProg_Edit"), MouseButton.PrimaryButton)
   type(waitForObject(":KoolProg_Edit"), searchText)
   snooze(2)
   mouseClick(waitForObject(":KoolProg.System.Windows.Controls.Image_Button_8"), MouseButton.PrimaryButton)
   searchListExcel = []
   searchListKoolProg = []
   fieldsTable=parseVisibleRow(tbl)
   for key,value in fieldsTable.items():
       if key != "":
           test.log("%s" % key)
           searchListKoolProg.append(key)
   searchKoolProgCount = len(searchListKoolProg)
   window=waitForObject(":KoolProg_Window")
   
   
   
   name1=getControl(window,"Label","tbProductInfoValue0")
   if(name1 == None):
       print "None"
   else:    
       test.log("type:%s "% name1["type"])
       test.log("name:%s "% name1["name"])
       test.log("text:%s "% name1["text"])
       Product = (name1["text"])
       Product_Name = Product[0:7]
       print (Product_Name)
   if (Product_Name == Product_Variant[0:7]):
       file = Global_Scripts_Path+"\Danfoss."+Product_Name+"_Search.csv"
       records = testData.dataset(file) 
       for rec in records:
           groupName = testData.field(rec, 0)
           name = testData.field(rec, 1)
           menuCode = testData.field(rec, 2)
           if((name.find(searchText) == -1)&(menuCode.find(searchText) == -1)&(groupName.find(searchText) == -1)):
               snooze(0.2)
           else:
               searchListExcel.append(name)
               test.log(name)
       searchExcelCount = len(searchListExcel)
       result = test.compare(searchKoolProgCount, searchExcelCount, "Search Result")
   mouseClick(":KoolProg.System.Windows.Controls.Image_Button_8"), MouseButton.PrimaryButton
   return result
 
# def Service_New_UI():


def AKCC_Readouts():
    result = False
    
    window=waitForObject(":KoolProg_Window")
    tbl = getControl(window, "Table" , "dataGridInput")
    tbl_1 = getControl(window, "Table" , "datagridParameters")
     
    #    test.log ("table is:" +str(tbl))
    
    Readout_Dict ={}
    Datagrid_Readouts = {}
    
    Readout_Dict = AKCC_Readouts_parse(tbl)
    Datagrid_Readouts = AKCC_parseFields(tbl_1)
    
    for key in Readout_Dict:
        for key_1 in Datagrid_Readouts:
            if (str(key) == str(key_1)):
                test.compare (str(Readout_Dict[key]), str(Datagrid_Readouts[key_1]))
     
#     for i in range (0, len(Readout_Dict)):
#          Param = Readout_Dict[i]
#          test.log("Readouts "+str(i)+" is:"+str(Param))
   
def AKCC_Readouts_parse(tbl):
    list = []
    Readouts_fieldsTable={}    
    items=object.children(tbl)
    test.log ("items are:" + str(items))
    for item in items:        
        if (object.properties(item)["type"] ==  "TableRow" and object.properties(item)["class"] ==  "System.Windows.Controls.DataGridRow" ):
           fields = object.children(item)
           for field in fields:
               if (object.properties(field)["type"] ==  "TableCell" and object.properties(field)["class"] ==  "System.Windows.Controls.DataGridCell" and object.properties(field)["column"] == 1 ):
                   Readout_Param = field.nativeObject.DataContext.Name
                   Readout_Value = field.nativeObject.DataContext.Value
    #                    test.log ("Readout parameters are:" +str(Readout_Param)+"___" +str(Readout_Value))
#                    list.append(Readout_Param +":"+ Readout_Value)
                   test.log ("Readout parameters are:" +str(Readout_Param)+",," +str(Readout_Value))  
                   Readouts_fieldsTable[Readout_Param] = Readout_Value
    return Readouts_fieldsTable


def AKCC_IO_ManualOverride():
   result = False
   waitForObject(":KoolProg.System.Windows.Controls.Image_Button")

   window=waitForObject(":KoolProg_Window")
   tbl = getControl(window, "Table" , "datagridInputOutput")

#     doubleClick(waitForObject(":Danfoss.T4CClient.TreeViewParameters.Danfoss.T4CClient.TreeViewParameters_TreeItem_3"), MouseButton.PrimaryButton)
   
   tv=getControl(window, "Tree", "treeViewManualIO")
   test.log("tv is:"+ str(tv))
   
   print("Expander length"+str(len(gExpanderList)))
   print("Parameter length"+str(len(gParamList)))
   
   if(tv != None):
       AKCCparseIOTreeView(tv, tbl)  
       
       
       print("Expander length"+str(len(gExpanderList)))
       print("Parameter length"+str(len(gParamList)))
       
       for expander in gExpanderList:
           print ("Expander:" + expander)
       for param in gParamList:
           print ("Parameters:" + param)
           
#         if ((Expander_Name != None) & (Parameter_Names != None)):
#             count = len(Parameter_Names)  
#         print ("Header Name:" + Expander_Name)
#         print ("Parameters:" + Parameter_Names ) 
#         print ("No.of Parameters:" + str(Item_Count))
#         else:
#             print ("False")
   else:
       test.log("Treeview not found")     
   snooze(1)
       

def AKCC_IO_SG_Comparison(Expander_Name, param):
   SG_Comparison_File = Output_Global_Path+"\IO_SGParameters"
   SG_Comparison_File = SG_Comparison_File + Timestr
   SG_Comparison_File = SG_Comparison_File + ".csv"
   openfile = open(SG_Comparison_File,'wt') 
   writer = csv.writer(openfile)
   writer.writerow(["GroupNameKP","GroupNameDB", "ParameterNameKP", "ParameterNameDB", "Result_SG", "Result_PN"]) 
   
   file = "C:\gitworkspace\TestAutomation-AKCC5XX\Test_Automation\SourceCode\Global_scripts\AK_CC_DB_Squish.csv"
     
   records = testData.dataset(file)
   for rec in records: 
       GroupName = testData.field(rec, 2)
       ParameterName = testData.field(rec, 3)
       for item in ParameterName: 
           if (param == ParameterName):
                Result_1 = test.compare(GroupName,Expander_Name)
                Result_2 = test.compare(param, ParameterName)
                writer.writerow([Expander_Name,GroupName,Result_1, param, ParameterName, Result_2])
                break
            
                result = True
#     print (Expander_Name)
#     print (param)


def AKCC_QW():
   result = False
   Unique_ID_List =[]
   
   with codecs.open(findFile("testdata", r"\Latest_CDF\device.jso"),encoding='utf-8') as data_file:
       content = data_file.read()
       content = content.replace(u'\ufeff','') 
       data = json.loads(content)
       Parameter_Count = len(data["Parameters"])
       
       Enum_Index = data["Enumerations"]
       Enum_Index_Count = str(data ["Enumerations"])
       
       QW_Group_ID = data["Header"]["QuickSetupMenuIdx"]
       QW_Parameters = data["Groups"][QW_Group_ID]["Items"]
#         test.log(str(QW_Parameters))
       
       for i in range (0, len(QW_Parameters)):
           Index = data["Groups"][QW_Group_ID]["Items"][i]["Index"]
#             test.log("Blah  "+str(Index))
           
           for j in range (0, Parameter_Count):
               if (str(Index) == str(j)):
                   Unique_ID = data["Parameters"][j]["UniqueID"]
                   Param_Name = data["Parameters"][j]["Text"]
                   Unique_ID_List.append(Unique_ID) 
#                     test.log(str(Index)+".."+str(Unique_ID)+".."+str(Param_Name))
           
   
   New_Wizard_Window = waitForObject(":NewWizard_Window")
   QW_List = getControl(New_Wizard_Window, "ListView", "lstQuickWizardSetting")
   DB_file = Global_Scripts_Path+"\AK_CC_DB_Squish.csv"
   records = testData.dataset(DB_file)
   
   fieldsList = []    
   items =object.children(QW_List)
   for item in items:        
       if(object.properties(item)["type"] ==  "ListViewItem"):
           expander=object.children(item)
           for child in expander:             
#                 if(object.properties(child)["type"] ==  "Edit"):  
               if (object.properties(child)["type"] == "ComboBox" and child.nativeObject.DataContext.IsParameterVisible == True):
                   UniqueID = child.nativeObject.DataContext.UniqueID
                   ParamName = child.nativeObject.DataContext.ParameterName
                   test.log(str(ParamName))
#                     test.log("Parameter Name is " +str(ParamName))
                   for var in range (0, len(Unique_ID_List)):
                       if (str(UniqueID) == "Id_"+str(Unique_ID_List[var])):
                           for m in range (0, Parameter_Count):
                               if (str(UniqueID) == "Id_"+str(data["Parameters"][m]["UniqueID"])):
                                   Idx = data["Parameters"][m]["Idx"]
                                   Enum_Idx = data["Parameters"][Idx]["EnumIdx"]
                                   if (Enum_Idx == -1):
                                       Min_Value = data["Parameters"][Idx]["Min"]
                                       Max_Value = data["Parameters"][Idx]["Max"]
                                       test.log("NO EnumIDX")
                                       child.nativeObject.DataContext.Value = random.randint(Min_Value, Max_Value)
#                                         snooze(5)
                                       test.log(str(child.nativeObject.DataContext.Value))
                                   else:
                                       Enum_Values = data["Enumerations"][Enum_Idx]["Values"] 
                                       Enum_Values_count = len(Enum_Values)                               
                                       Random_Enum_Idx = random.randint(0, Enum_Values_count-1)
                                       test.log(str(Random_Enum_Idx))
#                                         for k in range (0, Enum_Values_count-1):
                                       Enum_Value = Enum_Values[Random_Enum_Idx]["Value"]
                                       Enum_String = Enum_Values[Random_Enum_Idx]["Text"]
                                       test.log(str(Enum_String))
                                       mouseClick(child, MouseButton.PrimaryButton)
                                       snooze(2)
                                       type(child, str(Enum_String))
                                       snooze(2)
                                       type(child, "<Return>")
#                                         child.nativeObject.DataContext.Value = Enum_String
#                                         snooze(5)
                                       break                                       
   result = True

QW_fieldsTable = {}

def AKCC_QW_Verify():
   global QW_fieldsTable
   
   window=waitForObject(":KoolProg_Window")
   tbl = getControl(window, "Table" , "datagridParameters")
   QW_fieldsTable = AKCC_parseFields(tbl)
   test.log("hd:"+str(QW_fieldsTable))
   
   #Getting all parameters to be read ##
   Param_List = ['184', '200', '185', '186', '188', '187', '193', '213', '194', '195', '196']
   
   for ParamIdx in Param_List:
       ParamIdx = cast(ParamIdx, int) ##casting paramidx to int from string##
       test.log("ParamIdx is:"+str(ParamIdx))

       if (ParamIdx == 184):
               P1 = GetVar(184)
               
               test.log("P1 is : "+str(P1))
               if (P1 == 1):
                       SetVar(293, 1);
                       SetVar(75, 6);
                       SetVar(76, 9);
                       SetVar(77, 4);
                       SetVar(78, 7);
                       SetVar(79, 2);
                       SetVar(299, 30);
                       SetVar(300, 31);
                       SetVar(301, 32);
                       SetVar(302, 33);
                       SetVar(303, 34);
                       SetVar(304, 35);
                       SetVar(305, 0)
                         
               elif (P1 == 2):
                       SetVar(293, 1);
                       SetVar(75, 5);
                       SetVar(76, 9);
                       SetVar(77, 4);
                       SetVar(78, 7);
                       SetVar(79, 2);
                       SetVar(299, 30);
                       SetVar(300, 31);
                       SetVar(301, 32);
                       SetVar(302, 33);
                       SetVar(303, 34);
                       SetVar(304, 35);
                       SetVar(305, 0);
                         
     
               elif (P1 == 3):
                       SetVar(293, 1);
                       SetVar(75, 6);
                       SetVar(76, 9);
                       SetVar(77, 4);
                       SetVar(78, 5);
                       SetVar(79, 2);
                       SetVar(299, 30);
                       SetVar(300, 31);
                       SetVar(301, 32);
                       SetVar(302, 33);
                       SetVar(303, 34);
                       SetVar(304, 35);
                       SetVar(305, 0);
                         
     
               elif (P1 == 4):
                       SetVar(293, 1);
                       SetVar(75, 6);
                       SetVar(76, 5);
                       SetVar(77, 4);
                       SetVar(78, 7);
                       SetVar(79, 2);
                       SetVar(299, 30);
                       SetVar(300, 31);
                       SetVar(301, 32);
                       SetVar(302, 33);
                       SetVar(303, 34);
                       SetVar(304, 35);
                       SetVar(305, 0);
                         
     
               elif (P1 == 5):
                       SetVar(293, 1);
                       SetVar(75, 13);
                       SetVar(76, 12);
                       SetVar(77, 14);
                       SetVar(78, 7);
                       SetVar(79, 2);
                       SetVar(299, 30);
                       SetVar(300, 31);
                       SetVar(301, 32);
                       SetVar(302, 33);
                       SetVar(303, 34);
                       SetVar(304, 35);
                       SetVar(25, 2);
                       SetVar(305, 0);
                         
     
               elif (P1 == 6):
                       SetVar(293, 1);
                       SetVar(75, 6);
                       SetVar(76, 5);
                       SetVar(77, 4);
                       SetVar(78, 7);
                       SetVar(79, 2);
                       SetVar(299, 30);
                       SetVar(300, 31);
                       SetVar(301, 32);
                       SetVar(302, 33);
                       SetVar(303, 34);
                       SetVar(304, 36);
                       SetVar(305, 0);
                         
     
               elif (P1 == 7):
                       SetVar(293, 1);
                       SetVar(75, 6);
                       SetVar(76, 15);
                       SetVar(77, 4);
                       SetVar(78, 7);
                       SetVar(79, 2);
                       SetVar(299, 30);
                       SetVar(300, 31);
                       SetVar(301, 32);
                       SetVar(302, 33);
                       SetVar(303, 34);
                       SetVar(304, 36);
                       SetVar(305, 37);
                       SetVar(194, 0);
     
               elif (P1 == 8):
                       SetVar(293, 1);
                       SetVar(75, 6);
                       SetVar(76, 16);
                       SetVar(77, 4);
                       SetVar(78, 7);
                       SetVar(79, 2);
                       SetVar(299, 30);
                       SetVar(300, 31);
                       SetVar(301, 32);
                       SetVar(302, 33);
                       SetVar(303, 34);
                       SetVar(304, 35);
                       SetVar(305, 38);
                       SetVar(194, 0);
                         
     
               elif (P1 == 9):
                       SetVar(293, 1);
                       SetVar(299, 30);
                       SetVar(300, 31);
                       SetVar(301, 32);
                       SetVar(302, 33);
                       SetVar(303, 34);
                       SetVar(304, 35);
                       SetVar(305, 0);
                         
                 
     
       elif (ParamIdx == 200):
               P2 = GetVar(200)
                 
               if (P2 == 1):
                       SetVar(2, 8);
                       SetVar(4, 10);
                       SetVar(5, 4);
                       SetVar(124, 14);
                       SetVar(125, 0);
                       SetVar(128, 14);
                       SetVar(129, 0);
                         
     
               elif (P2 == 2):
                       SetVar(2, 0)
                       SetVar(4, 4)
                       SetVar(5, -4)
                       SetVar(124, 8)
                       SetVar(125, -5)
                       SetVar(128, 8)
                       SetVar(129, -5)
                         
     
               elif (P2 == 3):
                       SetVar(2, -2)
                       SetVar(4, 2)
                       SetVar(5, -6)
                       SetVar(124, 8)
                       SetVar(125, -5)
                       SetVar(128, 8)
                       SetVar(129, -5)
                         
     
               elif (P2 == 4):
                       SetVar(2, -20)
                       SetVar(4, -16)
                       SetVar(5, -24)
                       SetVar(124, -15)
                       SetVar(125, -30)
                       SetVar(128, -15)
                       SetVar(129, -30)
                         
     
               elif (P2 == 5):
                       SetVar(2, -24)
                       SetVar(4, -20)
                       SetVar(5, -28)
                       SetVar(124, -15)
                       SetVar(125, -30)
                       SetVar(128, -15)
                       SetVar(129, -30)
                         
       elif(ParamIdx == 185):
               P3 = GetVar(185)
               if (P3 == 0):
                       SetVar(75, 0)
                         
     
               elif (P3 == 1):
                       SetVar(75, 2)
                         
     
               elif (P3 == 2):
                       SetVar(75, 3)
                         
     
               elif (P3 == 3):
                       SetVar(75, 4)
                         
     
               elif (P3 == 4):
                       SetVar(75, 5)
                         
     
               elif (P3 == 5):
                       SetVar(75, 6)
                         
     
               elif (P3 == 6):
                       SetVar(75, 7)
                         
     
               elif (P3 == 7):
                       SetVar(75, 8)
                         
     
               elif (P3 == 8):
                       SetVar(75, 9)
                         
     
               elif (P3 == 9):
                       SetVar(75, 10)
                         
     
               elif (P3 == 10):
                       SetVar(75, 11)
                         
     
       elif (ParamIdx == 186):
               P4 = GetVar(186)
               if (P4 == 0):
                       SetVar(76, 0)
                         
     
               elif (P4 == 1):
                       SetVar(76, 2)
                         
     
               elif (P4 == 2):
                       SetVar(76, 3)
                         
     
               elif (P4 == 3):
                       SetVar(76, 4)
                         
     
               elif (P4 == 4):
                       SetVar(76, 5)
                         
     
               elif (P4 == 5):
                       SetVar(76, 6)
                         
     
               elif (P4 == 6):
                       SetVar(76, 7)
                         
     
               elif (P4 == 7):
                       SetVar(76, 8)
                         
     
               elif (P4 == 8):
                       SetVar(76, 9)
                         
     
               elif (P4 == 9):
                       SetVar(76, 10)
                         
     
               elif (P4 == 10):
                       SetVar(76, 11)
                         
     
       elif (ParamIdx == 188):
               P5 = GetVar(188)
               if (P5 == 0):
                       SetVar(77, 0)
                         
     
               elif (P5 == 1):
                       SetVar(77, 2)
                         
     
               elif (P5 == 2):
                       SetVar(77, 3)
                         
     
               elif (P5 == 3):
                       SetVar(77, 4)
                         
     
               elif (P5 == 4):
                       SetVar(77, 5)
                         
     
               elif (P5 == 5):
                       SetVar(77, 6)
                         
     
               elif (P5 == 6):
                       SetVar(77, 7)
                         
     
               elif (P5 == 7):
                       SetVar(77, 8)
                         
     
               elif (P5 == 8):
                       SetVar(77, 9)
                         
     
               elif (P5 == 9):
                       SetVar(77, 10)
                         
     
               elif (P5 == 10):
                       SetVar(77, 11)
                         
     
       elif (ParamIdx == 187):
               P6 = GetVar(187)
               if (P6 == 0):
                       SetVar(78, 0)
                         
     
               elif (P6 ==1):
                       SetVar(78, 2)
                         
     
               elif (P6 ==2):
                       SetVar(78, 3)
                         
     
               elif (P6 ==3):
                       SetVar(78, 4)
                         
     
               elif (P6 ==4):
                       SetVar(78, 5)
                         
     
               elif (P6 ==5):
                       SetVar(78, 6)
                         
     
               elif (P6 ==6):
                       SetVar(78, 7)
                         
     
               elif (P6 ==7):
                       SetVar(78, 8)
                         
     
               elif (P6 ==8):
                       SetVar(78, 9)
                         
     
               elif (P6 ==9):
                       SetVar(78, 10)
                         
     
               elif (P6 ==10):
                       SetVar(78, 11)
                         
       elif (ParamIdx == 193):
               P7 = GetVar(193)
                 
               if (P7 == 0):
                       SetVar(79, 0)
                         
     
               elif (P7 == 1):
                       SetVar(79, 2)
                         
     
               elif (P7 == 2):
                       SetVar(79, 3)
                         
     
               elif (P7 == 3):
                       SetVar(79, 4)
                         
     
               elif (P7 == 4):
                       SetVar(79, 5)
                         
     
               elif (P7 == 5):
                       SetVar(79, 6)
                         
     
               elif (P7 == 6):
                       SetVar(79, 7)
                         
     
               elif (P7 == 7):
                       SetVar(79, 8)
                         
     
               elif (P7 == 8):
                       SetVar(79, 9)
                         
     
               elif (P7 == 9):
                       SetVar(79, 10)
                         
     
               elif (P7 == 10):
                       SetVar(79, 11)
                         
       elif (ParamIdx == 213):
               P8 = GetVar(213)
               if (P8 == 0):
                       SetVar(80, 0)
                         
     
               elif (P8 == 1):
                       SetVar(80, 90)
     
       elif (ParamIdx == 194):
               P9 = GetVar(194)
               if (P9 == 0):
                       SetVar(296, 0)
                         
     
               elif (P9 == 1):
                       SetVar(296, 60)
                         
     
               elif (P9 == 2):
                       SetVar(296, 61)
                         
     
               elif (P9 == 3):
                       SetVar(296, 62)
                         
     
               elif (P9 == 4):
                       SetVar(296, 63)
                         
     
               elif (P9 == 5):
                       SetVar(296, 64)
                         
     
               elif (P9 == 6):
                       SetVar(296, 65)
                         
     
               elif (P9 == 7):
                       SetVar(296, 66)
                         
     
               elif (P9 == 8):
                       SetVar(296, 67)
                         
     
               elif (P9 == 9):
                       SetVar(296, 68)
                         
     
               elif (P9 == 10):
                       SetVar(296, 69)
                         
     
               elif (P9 == 11):
                       SetVar(296, 70)
                         
     
               elif (P9 == 12):
                       SetVar(296, 71)
                         
     
               elif (P9 == 13):
                       SetVar(296, 0)
                         
     
               elif (P9 == 14):
                       SetVar(296, 73)
                         
     
               elif (P9 == 15):
                       SetVar(296, 74)
                         
     
               elif (P9 == 16):
                       SetVar(296, 75)
                         
     
               elif (P9 == 20):
                       SetVar(296, 76)
                         
     
               elif (P9 == 21):
                       SetVar(296, 77)
             
     
       elif (ParamIdx == 195):
               P10 = GetVar(195)
               if (P10 == 0):
                       SetVar(297, 0)
                         
     
               elif(P10 == 1):
                       SetVar(297, 60)
                         
     
               elif(P10 == 2):
                       SetVar(297, 61)
                         
     
               elif(P10 == 3):
                       SetVar(297, 62)
                         
     
               elif(P10 == 4):
                       SetVar(297, 63)
                         
     
               elif(P10 == 5):
                       SetVar(297, 64)
                         
     
               elif(P10 == 6):
                       SetVar(297, 65)
                         
     
               elif(P10 == 7):
                       SetVar(297, 66)
                         
     
               elif(P10 == 8):
                       SetVar(297, 67)
                         
     
               elif(P10 == 9):
                       SetVar(297, 68)
                         
     
               elif(P10 == 10):
                       SetVar(297, 69)
                         
     
               elif(P10 == 11):
                       SetVar(297, 70)
                         
     
               elif(P10 == 12):
                       SetVar(297, 71)
                         
     
               elif(P10 == 13):
                       SetVar(297, 72)
                         
     
               elif(P10 == 14):
                       SetVar(297, 73)
                         
     
               elif(P10 == 15):
                       SetVar(297, 74)
                         
     
               elif(P10 == 16):
                       SetVar(297, 75)
                         
     
               elif(P10 == 20):
                       SetVar(297, 76)
                         
     
               elif(P10 == 21):
                       SetVar(297, 77)
                         
     
                 
                 
     
       elif (ParamIdx == 196):
               P11 = GetVar(196)
               if (P11 == 0):
                       SetVar(298, 0)
                         
     
               elif (P11 ==1):
                       SetVar(298, 60)
                         
     
               elif (P11 ==2):
                       SetVar(298, 61)
                         
     
               elif (P11 ==3):
                       SetVar(298, 62)
                         
     
               elif (P11 ==4):
                       SetVar(298, 63)
                         
     
               elif (P11 ==5):
                       SetVar(298, 64)
                         
     
               elif (P11 ==6):
                       SetVar(298, 65)
                         
     
               elif (P11 == 7):
                       SetVar(298, 66)
                         
     
               elif (P11 ==8):
                       SetVar(298, 0)
                         
     
               elif (P11 ==9):
                       SetVar(298, 0)
                         
     
               elif (P11 ==10):
                       SetVar(298, 69)
                         
     
               elif (P11 ==11):
                       SetVar(298, 70)
                         
     
               elif (P11 ==12):
                       SetVar(298, 71)
                         
     
               elif (P11 ==13):
                       SetVar(298, 0)
                         
     
               elif (P11 ==14):
                       SetVar(298, 73)
                         
     
               elif (P11 ==15):
                       SetVar(298, 74)
                         
     
               elif (P11 ==16):
                       SetVar(298, 75)
                         
     
               elif (P11 ==20):
                       SetVar(298, 76)
                         
     
               elif (P11 ==21):
                       SetVar(298, 77)

def GetVar(Idx): ##Getting UniqueID for paramIdx and checking it's value in KP grid##
   window=waitForObject(":KoolProg_Window")
#     tbl = getControl(window, "Table" , "datagridParameters")
    
   with codecs.open(findFile("testdata", r"\Latest_CDF\device.jso"),encoding='utf-8') as data_file:
       content = data_file.read()
       content = content.replace(u'\ufeff','') 
       data = json.loads(content)
        
       Parameter_Count = len(data["Parameters"])
       Enum_Count = len(data["Enumerations"])
       ##Get parameter list## 
       for i in range (0, Parameter_Count):
           CDF_Idx = data["Parameters"][i]["Idx"]
           if (CDF_Idx == Idx): ##CHeck if ParamIdx is the same as Idx in CDF file##
               Unique_ID = data["Parameters"][Idx]["UniqueID"]
               Parameter_Name = data["Parameters"][Idx]["Text"]
               
               for key, value in QW_fieldsTable.items():
                   if (str(key) == str(Parameter_Name)):
                       Enum_Idx = data["Parameters"][Idx]["EnumIdx"]
                       for j in range (0, Enum_Count):
                           Enum_Index = data["Enumerations"][j]["Idx"]
                           Enum_Val = data["Enumerations"][j]["Values"]
                           Enum_Val_Limit = len(data["Enumerations"][j]["Values"])
                           
                           if (str(Enum_Idx) == str(Enum_Index)):
                               for k in range (0, Enum_Val_Limit):                                    
                                   if (str(value) == str(Enum_Val[k]["Text"])):
                                       Enum_Pos = Enum_Val[k]["Value"]
                                       test.log("Enum_Pos:  "+str(Enum_Pos))
                                       
                                       return Enum_Pos
                                         
def SetVar(Idx, Val):
   
   with codecs.open(findFile("testdata", r"\Latest_CDF\device.jso"),encoding='utf-8') as data_file:
       content = data_file.read()
       content = content.replace(u'\ufeff','') 
       data = json.loads(content)
       
       Parameter_Count = len(data["Parameters"])
       Enum_Count = len(data["Enumerations"])
       
       for i in range (0, Parameter_Count):
           CDF_Idx = data["Parameters"][i]["Idx"]
           if (CDF_Idx == Idx):
               Unique_ID = data["Parameters"][i]["UniqueID"]
               Unique_ID = "Id_"+str(Unique_ID)
               
               Parameter_Name = data["Parameters"][i]["Text"]
               Enum_Idx = data["Parameters"][i]["EnumIdx"]
               if (Enum_Idx == -1):
                   for key, value in QW_fieldsTable.items(): 
                       if (str(key) == str(Parameter_Name)):
                           test.compare (str(Val), str(value))
               else:
                   for key, value in QW_fieldsTable.items(): 
                       if (str(key) == str(Parameter_Name)):
                           for i in range (0, Enum_Count):
                               Enum_Index = data["Enumerations"][i]["Idx"]
                               Enum_Val = data["Enumerations"][i]["Values"]
                               Enum_Val_Limit = len(data["Enumerations"][i]["Values"])
                               
                               if (str(Enum_Idx) == str(Enum_Index)):
                                   for k in range (0, Enum_Val_Limit):                                    
                                       if (str(value) == str(Enum_Val[k]["Text"])):
                                           Enum_Pos = Enum_Val[k]["Value"]
                                           test.compare(str(Val), str(Enum_Pos))            
            
###IO PARAMETER FUNCTIONS###

def Check_IO_Parameters():
   waitForObject(":KoolProg.System.Windows.Controls.Image_Button")
   snooze(30)
   
   window=waitForObject(":KoolProg_Window")
   tbl = getControl(window, "Table" , "datagridParameters")
   items=tbl.nativeObject.Items
    
   file = Output_Global_Path+"\Input_Output.csv"
   file = file + Timestr
   file = file + ".csv"
   openfile = open(file,'wt') 
   writer = csv.writer(openfile)
   writer.writerow(["ParameterName", "KP_ParameterName", "Result", "IO_Value", "KP_IO_Value", "IO_Result"])
   
#     a = "Id_1053441 > 0 && Id_1053441 != 7 && Id_1053441 != 8"

   with codecs.open(findFile("testdata", r"\Latest_CDF\device.jso"),encoding='utf-8') as data_file:
       content = data_file.read()
       content = content.replace(u'\ufeff','') 
       data = json.loads(content)
       
       Parameters = data["Parameters"]
       Parameters_Count = len(data["Parameters"])
       
       Virtual_IO = data["VirtualIO"]
       Virtual_IO_Count = len(data["VirtualIO"])
       
       IO_Config = data["IOConfig"]
       
       IO_Config_count = len(data["IOConfig"])
       for i in range (0, IO_Config_count):
           IOFuncVarIDX = data["IOConfig"][i]["IOFunctionVarIdx"]
#             test.log("is:" +str(IOFuncVarIDX))
           OverRideIDX = data["IOConfig"][i]["OverrideVarIdx"]
#             test.log("ORIDX is-" +str(OverRideIDX))
           
           
           IO_Parameter = data["Parameters"][IOFuncVarIDX]["Text"]
           test.log("IO_Parameter is:" +str(IO_Parameter))
           
           IO_Unique_ID = data["Parameters"][IOFuncVarIDX]["UniqueID"]
           IO_Parameter_Label = data["Parameters"][IOFuncVarIDX]["Label"]
           
           doubleClick(waitForObject(":KoolProg_Edit"), MouseButton.PrimaryButton)
           type(waitForObject(":KoolProg_Edit"), str(IO_Parameter_Label))
           type(waitForObject(":KoolProg_Edit"), "<Return>")
           
           try:
#                 waitForObjectExists(":MessageBoxDisplay.OK_Button")
               mouseClick(":MessageBoxDisplay.OK_Button"), MouseButton.PrimaryButton
           except:
               snooze(2)
           
           IO_Param, IO_Value = parseIOVisibleRow(tbl) ##IO Param is AI1 Function. IO Value is Pe Evap Pressure##
           
           for i in range (0, Parameters_Count):
               if (data["Parameters"][i]["Text"] == str(IO_Value)):
                   IO_Value_IDX = data["Parameters"][i]["Idx"]
                   IO_Value_Label = data["Parameters"][i]["Label"]
#                     test.log ("Idx is:" +str(IO_Value_IDX))
                   
                   for j in range (0, Virtual_IO_Count):
#                         test.log ("it is"+str(data["VirtualIO"][j]["ParamIdx"]))
                       if (data["VirtualIO"][j]["ParamIdx"] == IO_Value_IDX):
                           Override_IDX = data["VirtualIO"][j]["OverrideVarIdx"]
                           test.log("Override is:" +str(Override_IDX))
         
                           if (Override_IDX != -1):
                               for k in range(0, Parameters_Count):
                                   if (data["Parameters"][k]["Idx"] == Override_IDX):
                                       Manual_IO_Param = data["Parameters"][k]["Text"]
                                       Manual_IO_Label = data["Parameters"][k]["Label"]
#                                         Dummy_Name, IO_Status = parseVisibleRow(tbl)
#                                         test.log("IO_Status is"+str(IO_Status))
                                               
                           else: 
                               Manual_IO_Label = str(IO_Value_Label)
#                                 test.log("IO_Status is"+str(IO_Status))
                           
                           doubleClick(waitForObject(":KoolProg_Edit"), MouseButton.PrimaryButton)
                           type(waitForObject(":KoolProg_Edit"), str(Manual_IO_Label))
                           type(waitForObject(":KoolProg_Edit"), "<Return>")
                           
                           try:
#                                 waitForObjectExists(":MessageBoxDisplay.OK_Button")
                               mouseClick(":MessageBoxDisplay.OK_Button"), MouseButton.PrimaryButton
                               
                           except:
                               snooze(2)
                           
                           Input_Output_Param , Input_Output_Value = parseIOVisibleRow(tbl)
                           writer.writerow([Input_Output_Param, "","", Input_Output_Value, "", ""])
   
   
   
       mouseClick(waitForObject(":KoolProg.Input/Output_TabItem"), MouseButton.PrimaryButton)
       snooze(20)
       
       IO_tbl = getControl(window, "Table" , "datagridInputOutput")
       items=IO_tbl.nativeObject.Items
       
       openfile = open(file,'wt') 
       writer = csv.writer(openfile)
   #     writer.writerow(["ParameterName", "DB_Menucode","KP_Menucode","Result" ,"DB_DefaultValue", "KP_DefaultValue", "Result", "DB_MinValue", "KP_MinValue", "Result" ,"DB_MaxValue", "KP_MaxValue", "Result", "DB_Unit", "KP_Unit", "Result", "DB_Info", "KP_Info", "Result"])
       records = testData.dataset(file)
       for rec in records:
           Param_Name = testData.field(rec, 0)
           IO_Value = testData.field(rec, 3)
           for i in range (0, items.Count-1):
               item=items.at(i)
#                 test.log("PN:" +str(item.ParameterName))
               if (Param_Name == item.ParameterName): 
                   test.log("PN:" +str(item.ParameterName))
                   result_1 = test.compare(str(IO_Value), str(item.Value))
                   result_2 = test.compare(str(Param_Name), str(item.ParameterName))
                   
                   writer.writerow(["", item.ParameterName, result_1, "", item.Value, result_2])   
                                 
def AKCC_Active_Alarms():
   waitForObject(":KoolProg.System.Windows.Controls.Image_Button")
   
   test.compare(waitForObjectExists(":KoolProg_Table").type, "Table")
   test.compare(waitForObjectExists(":KoolProg_Table").name, "datagridParameters")
  
   window=waitForObject(":KoolProg_Window")
#     waitForObject(":KoolProg_Table_5")
   
#     print("count:%s"% len(window))
   tbl=waitForObjectExists(":KoolProg_Table")
   
   items_1=object.children(window)
   for item_1 in items_1:        
       if(object.properties(item_1)["type"] ==  "WPFControl"):
           expander=object.children(item_1)
           for child in expander:                
               if(object.properties(child)["type"] ==  "Label" and object.properties(child)["name"] ==  "txtApplicationManual"):
                 Par_App_Name=object.properties(child)["text"]   
                 test.log("ParamAN:"+str(Par_App_Name)) ##Get app name in S&T window##     
   
   MainSwitch_List = ['Start', 'Stop', 'Manual']
   MainSwitch_List_Count = len(MainSwitch_List) ##Change the Main switch value to see difference in alarms##
   
   for i in range (0, MainSwitch_List_Count):
       if (MainSwitch_List[i] == 'Manual'):
           MSValue = "Manual"
       elif (MainSwitch_List[i] == 'Stop'):
           MSValue = "Stop"
       elif (MainSwitch_List[i] == 'Start'):
           MSValue = "Start"
       
       mouseClick(":KoolProg.Parameters_TabItem"), MouseButton.PrimaryButton
       fieldsTable = AKCC_ActiveAlarms_parseFields(tbl, MSValue)
       test.log("Main Switch Value: "+str(MSValue))##GET MS VALUE FROM TABLE##
       
       verifyActiveAlarm_AKCC(Par_App_Name)##GET ALARMS FROM RPC ALARMS__TAB##
    
       ActiveAlarm_tbl = getControl(window, "Table" , "dataGridActiveAlarm")
       Active_Alarm_List =[]    
       Active_Alarm_List = AKCC_ActiveAlarms_parse(ActiveAlarm_tbl) ##GET ALARMS FROM ALARMS TABLE IN S&T##

   
def verifyActiveAlarm_AKCC(Par_App_Name):
   result = False
   alarmTable = []
   tbl=waitForObjectExists(":KoolProg_Table")
   mouseClick(":KoolProg.Alarms_TabItem"), MouseButton.PrimaryButton
   
   window=waitForObject(":KoolProg_Window")
   
#     waitForObject(":KoolProg_Table_4")
   tblActiveAlarm=getControl(window, "Table" , "datagridRPCAlarms")
   
   items=object.children(window)
   for item in items:        
       if(object.properties(item)["type"] ==  "WPFControl"):
           expander=object.children(item)
           for child in expander:                
               if(object.properties(child)["type"] ==  "Label" and object.properties(child)["name"] ==  "txtApplicationManual"):
                 Alarm_App_Name=object.properties(child)["text"]
                 test.log("AlarmAN:"+str(Alarm_App_Name))
   
   if (Par_App_Name == Alarm_App_Name):
   
       items_1=object.children(tblActiveAlarm)
       
       for WPF_obj in items_1:    
           if(object.properties(WPF_obj)["type"] =="WPFControl"):
               item_2 = object.children(WPF_obj)
               for Exp_obj in item_2:
                   if (object.properties(Exp_obj)["type"] =="Expander"):
                       item_3 = object.children(Exp_obj)
                       for TblRw_obj in item_3:
                            if(object.properties(TblRw_obj)["type"] =="TableRow"):
                               fields=object.children(TblRw_obj)
                               for field in fields: 
   #                                 test.log("Field 1 is: "+str(field))
                                   if(object.properties(field)["type"] =="TableCell" and object.properties(field)["column"] == 2):
                                       ##COLUMN IS 2 because 1 NOT AVAILABLE##
   #                                     test.log("Field 2 is: "+str(field))
                                       if(field != None):
                                           alarmName=object.properties(field)["text"]
                                           test.log ("Active RPC alarm: "+str(alarmName))
                                           alarmTable.append(alarmName)
                       activeAlarmsCount = len(alarmTable)
#                         test.log(alarmName)
                       mouseClick(":KoolProg.Parameters_TabItem"), MouseButton.PrimaryButton
                       Object=tbl.nativeObject
                       items=tbl.nativeObject.Items
                   #     for i in range (0, items.Count-1):
                   #         item=items.at(i)
                       for i in range (0,activeAlarmsCount):        
                           name = alarmTable[i]
                           for j in range (0, items.Count-1):
                               item=items.at(j)
                               if((item.Value == "On") and (str(item.ParameterName) == str(name))):
                                   test.compare(item.ParameterName, name)
   #                             if(name == item.ParameterName):
   #                                 test.compare(item.Value, "Alarm: "+ name)
                       result = True
                       return result
   else:
       test.log ("APPLICATIONS DO NOT MATCH")
       result = False
       
           
def AKCC_ActiveAlarms_parseFields(tbl, MSValue):
   fieldsTable={}        
   items_1=object.children(tbl)
   for item_1 in items_1:        
       if(object.properties(item_1)["type"] ==  "WPFControl"):
           expander=object.children(item_1)
           for child in expander:                
               if(object.properties(child)["type"] ==  "Expander"):
                   rows=object.children(child)
                   for row in rows:
                       if((object.properties(row)["type"] == "TableRow") and (row.nativeObject.IsVisible == True)):
                           fields=object.children(row)
                           fieldName=None        
                           for field in fields:                                                                
                               if(object.properties(field)["type"] == "TableCell" and object.properties(field)["column"] == 4):
                                   fieldName=object.properties(field)["text"]                        
                               if(object.properties(field)["type"] == "TableCell" and object.properties(field)["column"] == 7 and fieldName == "Main switch"):
                                   edits=object.children(field)                                    
                                   for edit in edits:
                                       if(object.properties(edit)["type"] == "ComboBox" and object.properties(edit)["name"] == "cmbEnums"):
                                           #if (fieldName != None):                                               
                                           fieldsTable[fieldName]=edit
                                           edit.nativeObject.DataContext.Value = MSValue
                                           break
                           break
                   break
                                           
                                                                                                                                                                         
   return fieldsTable

def AKCC_ActiveAlarms_parse(ActiveAlarm_tbl):
   List =[]
   fieldsTable={}
   tbl=waitForObjectExists(":KoolProg_Table")    
   items=object.children(ActiveAlarm_tbl)
#     test.log ("items are:" + str(items))
   for item in items:        
      if (object.properties(item)["type"] ==  "TableRow" and object.properties(item)["class"] ==  "System.Windows.Controls.DataGridRow" ):
          fields = object.children(item)
          for field in fields:
              if (object.properties(field)["type"] ==  "TableCell" and object.properties(field)["class"] ==  "System.Windows.Controls.DataGridCell" and object.properties(field)["column"] == 1 ):
#                            mouseClick(field)  #******NOT WORKING BECAUSE TAB FUNCTION TO CLICK ON PARAMETERS NOT IMPLEMENTED*****
                  
                  Active_Alarm = field.nativeObject.DataContext.Name
                  Active_Alarm_Status = field.nativeObject.DataContext.Value
                  test.log ("Active_Alarms are:" +str(Active_Alarm)+"___" +str(Active_Alarm_Status))
                  
                  List.append(Active_Alarm)
  
   ListCount = len(List)
#     test.log(alarmName)
   Object=tbl.nativeObject
   items=tbl.nativeObject.Items
   #     for i in range (0, items.Count-1):
   #         item=items.at(i)
   for i in range (0,ListCount):        
       name = List[i]
       for j in range (0, items.Count-1):
           item=items.at(j)
           if(item.Value == "On" and name == item.ParameterName):
               test.compare(item.ParameterName, name)
               
   #                             if(name == item.ParameterName):
   #                                 test.compare(item.Value, "Alarm: "+ name)
   result = True
   return result


##GET PARAMETERS WITH A SPECIFIC STORAGE TYPE##
def StorageType_Parameters():
   StorageType_List=[]
   enum_counter =0

   with codecs.open(findFile("testdata", r"\Latest_CDF\device.jso"),encoding='utf-8') as data_file:
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
       
def parseIOVisibleRow(tbl):
   fieldsTable={}    
   items=object.children(tbl)
   for item in items:        
       if(object.properties(item)["type"] ==  "WPFControl"):
           expander=object.children(item)
           for child in expander:                
               if(object.properties(child)["type"] ==  "Expander"):
                   rows=object.children(child)
                   for row in rows:
                       if(object.properties(row)["type"] == "TableRow" and row.nativeObject.IsVisible == True):
                           fields=object.children(row)
                           fieldName=None        
                           for field in fields:                                                                
                               if(object.properties(field)["type"] == "TableCell" and object.properties(field)["column"] == 4):
                                   fieldName=object.properties(field)["text"]                            
                               if(object.properties(field)["type"] == "TableCell" and object.properties(field)["column"] == 7): #and fieldName != ""):
                                   edits=object.children(field)                                    
                                   for edit in edits:
                                       if(object.properties(edit)["type"] == "Edit" and object.properties(edit)["name"] == "txtValue"):
                                           #if (fieldName != None):
                                               #test.log("Parsing:%s" % (fieldName))                                                
                                           ParameterName = edit.nativeObject.DataContext.ParameterName
#                                             test.log("Param is:"+str(ParameterName))
                                           
                                           Value = edit.nativeObject.DataContext.Value
#                                             test.log("Value is:"+str(Value))
                                           
                                       
                                       elif(object.properties(edit)["type"] == "ComboBox" and object.properties(edit)["name"] == "cmbEnums"):
                                           ParameterName = edit.nativeObject.DataContext.ParameterName
#                                             test.log("Param is:"+str(ParameterName))
                                           
                                           Value = edit.nativeObject.DataContext.Value
#                                             test.log("Value is:"+str(Value))
                                           
                                       
                                       elif(object.properties(edit)["type"] == "Label" and object.properties(edit)["name"] == "txtReadOnly"):
                                           ParameterName = edit.nativeObject.DataContext.ParameterName
#                                             test.log("Param is:"+str(ParameterName))
                                           
                                           Value = edit.nativeObject.DataContext.Value
#                                             test.log("Value is:"+str(Value))
                                           
   return ParameterName, Value    

def Value_Generation_AK_CC():
   result = False
   test.compare(waitForObjectExists(":KoolProg_Table").type, "Table")
   test.compare(waitForObjectExists(":KoolProg_Table").name, "datagridParameters")
  
   window=waitForObject(":KoolProg_Window")
   print("count:%s"% len(window))  
   
     
   tbl=waitForObjectExists(":KoolProg_Table")
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
       
   fieldsTable=parseVisibleRow(tbl)
   print(fieldsTable)
   Object=tbl.nativeObject
   items=tbl.nativeObject.Items
   file = Global_Scripts_Path+"\Danfoss."+Controller_file[8::]+"_Parameters.csv"
   
   file_1 = "AKCC-ValueGeneration.csv"
   openfile = open(file_1,'wt') 
   writer = csv.writer(openfile)
   writer.writerow(["Idx","Parameter_Name", "Random_Value", "", ""])
   enumList = []
   test1 = []
   functions = ['Min', 'Max', 'Val']
   records = testData.dataset(file)
   minVal = None
   maxVal = None
#     functions.append("Min")
#     functions.append("Max")
#     functions.append("Val")
   count = len(functions)
   for j in range(0,count):
       for rec in records:
           Unique_ID = testData.field(rec, 0)
           name = testData.field(rec, 1)
           enum = testData.field(rec,2)
           for i in range (0, items.Count-1):
           #for i in range (0, 5):
               item=items.at(i) 
               if ((Unique_ID == item.Key)&(item.Datatype == "Float")&(item.ReadOnly == False)&(item.IsEnabled == True)):
                   #Object.SelectedIndex = i
                   minVal = float(item.Minvalue)
                   #print ("min_value"+str(minVal))
                   maxVal = float(item.Maxvalue) 
                   #print ("max_value"+str(maxVal))  
#                    if(functions[j] == 'Min'):
#                        test.log("Result:%s" % setParameterValue(fieldsTable,item.ParameterName, str(minVal)))
#                    elif(functions[j] == 'Max'):
#                        test.log("Result:%s" % setParameterValue(fieldsTable,item.ParameterName, str(maxVal)))
#                    else:
                   item_Val = random.uniform(minVal, maxVal)
                   #print ("0_"+str(item_Val))
                   itemVal = float(item_Val)
                   #print ("1_"+str(itemVal))
                   itemVal = round(item_Val,2)
                   #print ("2_"+str(itemVal))
                   if(functions[j] == 'Min'):
#                         test.log("Min Result:%s" % setParameterValue(fieldsTable,item.ParameterName, str(minVal)))
                        setInvalidValue(fieldsTable,item.ParameterName, random.uniform(-32767, minVal))
                        
                   elif(functions[j] == 'Max'):
#                         test.log("Max Result:%s" % setParameterValue(fieldsTable,item.ParameterName, str(maxVal)))
                        setInvalidValue(fieldsTable,item.ParameterName, random.uniform(maxVal, 32767))
                        
                   else:
#                        test.log("Result:%s" % setParameterValue(fieldsTable,item.ParameterName, str(itemVal)))
                       writer.writerow([item.Key, item.ParameterName, itemVal])  
                    
               elif ((Unique_ID == item.Key)&(item.Datatype == "INT")&(item.ReadOnly == False)&(item.IsEnabled == True)&(item.ParameterName != "Delay of outputs at power up")):
                   #Object.SelectedIndex = i
                   minVal = float(item.Minvalue)
                   maxVal = float(item.Maxvalue)          
                   itemVal = random.uniform(minVal, maxVal)
                   
                   itemVal = int(itemVal)
                   minVal = int(minVal)
                   maxVal = int(maxVal)
                   try:
                        if(functions[j] == 'Min'):
#                            test.log("Min Result:%s" % setParameterValue(fieldsTable,item.ParameterName, str(minVal)))
                           setInvalidValue(fieldsTable,item.ParameterName, random.randint(-32767, minVal))
                           
                        elif(functions[j] == 'Max'):
#                             test.log("Max Result:%s" % setParameterValue(fieldsTable,item.ParameterName, str(maxVal)))
                            setInvalidValue(fieldsTable,item.ParameterName, random.randint(maxVal, 32767))
                            
                        else:
#                            test.log("Result:%s" % setParameterValue(fieldsTable,item.ParameterName, itemVal))
                           writer.writerow([item.Key, item.ParameterName, itemVal])
                   except:
                       snooze(1)
                   
               elif ((Unique_ID == item.Key)&((item.Datatype == "Enum") | (item.Datatype == "BIT"))&(item.ReadOnly == False)&(item.IsEnabled == True)):              
                   if(enum != ""):
                       #print("Raja"+item.ParameterName+"-"+enum)
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
                       if (name != "Application mode"):
                           enumValue = enumList[i]
                           if (enumValue != None):
                               item.Value = enumValue
                               #test.log("Result:%s" % setParameterValue(fieldsTable,item.ParameterName, enumValue))
                               writer.writerow([item.Key, item.ParameterName, enumValue])  
                           else:
                               snooze(1)
                       else:
                           snooze(1)                 
                   enumList = []
       result = True
   return result

def AKCC_parseFields(tbl):
   fieldsTable={}        
   items_1=object.children(tbl)
   for item_1 in items_1:        
       if(object.properties(item_1)["type"] ==  "WPFControl"):
           expander=object.children(item_1)
           for child in expander:                
               if(object.properties(child)["type"] ==  "Expander"):
                   rows=object.children(child)
                   for row in rows:
                       if((object.properties(row)["type"] == "TableRow") and (row.nativeObject.IsVisible == True)):
                           fields=object.children(row)
                           fieldName=None        
                           for field in fields:                                                                
                               if(object.properties(field)["type"] == "TableCell" and object.properties(field)["column"] == 4):
                                   fieldName=object.properties(field)["text"]                            
                               if(object.properties(field)["type"] == "TableCell" and object.properties(field)["column"] == 7 and fieldName != None):
                                   edits=object.children(field)                                    
                                   for edit in edits: ## FOR ENUMS AND FOR FLOAT VALUES, SEPERATE COMPARISON CASES ARE USED. Edit-> Txtvalue and Edit->Part_editabletextbor or ComboBox->cmbEnums##
                                       if((object.properties(edit)["type"] == "Edit" and object.properties(edit)["name"] == "txtValue") or (object.properties(edit)["type"] == "ComboBox" and object.properties(edit)["name"] == "cmbEnums")):
                                           #if (fieldName != None):
                                           val = edit.nativeObject.DataContext.Value
                                           
#                                                     test.log("Parsing:%s" % (fieldName))
#                                                     test.log("Value:%s" % (val))
                                                                                           
                                           fieldsTable[fieldName]=val
                                                                                                                                             
   return fieldsTable
		   
def selectControllerparse(symbolicname, fam, val): ##While creating a project, to dynamically click on expander and controller name as per the input from excel sheet##
   test.log("inside select controller")
   tbl = waitForObjectExists(symbolicname)
   try:
       with codecs.open(findFile("testdata", r"\Latest_CDF\device.jso"),encoding='utf-8') as data_file:
           content = data_file.read()
           content = content.replace(u'\ufeff','') 
           data = json.loads(content)
           
           Parameter_Count = len(data["Parameters"])
           
           Headers = len(data["Header"])
           
           Description = data["Header"]["Description"]
           Product_Variant =str(Description)
           test.log("Product Variant from CDF file is: " +str(Product_Variant))
   except:
        test.log("not akcc controller")
        
   ControllerTable={}        
   items_1=object.children(tbl)
   for item_1 in items_1:        
       if((object.properties(item_1)["type"] ==  "TabItem")and(object.properties(item_1)["name"] ==  "tabController")) :
           TableItem=object.children(item_1)
           for table in TableItem:
               if((object.properties(table)["type"] == "Table") and (object.properties(table)["name"] == "datagridProducts")):
                   childs = object.children(table)
                   for child in childs:                
                       if((object.properties(child)["type"] ==  "WPFControl") and (object.properties(child)["class"] ==  "System.Windows.Controls.GroupItem")):
                           expander=object.children(child)
                           for exp in expander:
                               if(object.properties(exp)["type"] == "Expander"):
                                   ExpanderName = None
                                   ExpanderName = exp.nativeObject.DataContext.Name
                                   if (str(ExpanderName).strip() == str(fam).strip()):
                                       mouseClick(exp), MouseButton.PrimaryButton
                                       test.log("Expander name in KoolProg is "+ str(ExpanderName))
                                   rows=object.children(exp)
                                   for row in rows:                                                               
                                       if(object.properties(row)["type"] == "TableRow"):
                                           cells = object.children(row)
                                           for cell in cells:
                                               if (object.properties(cell)["type"] == "TableCell"):
                                                   CellName = None
                                                   CellName = object.properties(cell)["text"]
                                                   if (str(CellName).strip() == str(val).strip()):
                                                       mouseClick(cell), MouseButton.PrimaryButton
                                                       test.log("Controller name in KoolProg is: "+ str(CellName)) 


def Maxlength(symbolicname, value):
    result = False
    test.verify(findObject(symbolicname).maxlength, value) 
    result = True
    return result
	
def App_Change(symbolicname):
    result = False
    tbl=waitForObjectExists(":KoolProg_Table") 
    fieldsTable=parseAppFields(tbl)
    window=waitForObject(":KoolProg_Window_0")
    name1_cont=getControl(window,"Label","txtProuctName")  #can change. right now App not displayed
    if(name1_cont == None):
        print "None"
        result = False
    else:    
        test.log("type:%s "% name1_cont["type"])
        test.log("name:%s "% name1_cont["name"])
        test.log("text:%s "% name1_cont["text"])
        Controller_Name = (name1_cont["text"])
        if (Controller_Name == "ERC211"):
            App_List = []
            App_List = ['App0', 'App1', 'App2', 'App3', 'App4', 'App5']
            countApp = len(App_List)
            randomIndex = random.randint(0,countApp-1)
            app = App_List[randomIndex]
            result = True
        else:
            App_List = []
            App_List = ['App0', 'App1', 'App2', 'App3', 'App4', 'App5', 'App6']
            countApp = len(App_List)
            randomIndex = random.randint(0,countApp-1)
            app = App_List[randomIndex]  
            result = True
        test.log("Result:%s" % setAppValue(fieldsTable,"Predefined applications", app))
    return result

### NOT CHECKED ####


def Checked(symbolicname, value):
   test.log("inside checked")
   result = False
   test.log("this function check label is checked or not.")
   tbl=waitForObjectExists(symbolicname)   
   test.compare(bool(strtobool(value)),(tbl.checked))
   result = True
   return result

def ClickButton(symbolicname):
   test.log("inside click button")
   result = False
   snooze(5)
   mouseClick(waitForObject(symbolicname), MouseButton.PrimaryButton)
   snooze(2) 
   result = True
   return result 

def Close():
   test.log("inside close the application")
   result = False
   Snooze()
   os.popen(r"Taskkill /IM KoolProg.exe /F")
   Snooze()
   result = True
   return result
def Code_Msg():
   test.log("inside code message")
   result = False
   waitForObject(":KoolProg.System.Windows.Controls.Image_Button"),2000
   tbl=waitForObjectExists(":KoolProg.Code Number Mismatch_Label")   
   Object=tbl.nativeObject
   test.compare("Code Number Mismatch", Object.Text)    
   result = True
   return result

def ComboBox_Edit(symbolicname, value):
       test.log("inside combo box")
       result = False
       mouseClick(waitForObject(symbolicname), MouseButton.PrimaryButton)
       snooze(2) 
       type(waitForObject(symbolicname), value)
       snooze(2)
       type(waitForObject(symbolicname), "<Return>")  
       result = True
       return result

def DataGrid_Verification_Offline_Unit_C():
   test.log("inside datagrid verification offline unit c ")
   result = False
   test.compare(waitForObjectExists(":KoolProg_Table").type, "Table")
   test.compare(waitForObjectExists(":KoolProg_Table").name, "datagridParameters")
  
   window=waitForObject(":KoolProg_Window")
   print("count:%s"% len(window))
   
   #### left side controller name
   
   name1=getControl(window,"Label","tbProductInfoValue0")  
   if(name1 == None):
       print "None"
       #result = False
   else:
       #test.log("type:%s "% name1["type"])
       #test.log("name:%s "% name1["name"])
       #test.log("text:%s "% name1["text"])
       test.log("left side controller name is " +name1["text"] )
       Controller_Name = (name1["text"])
       test.log(Controller_Name[0:9])
       #result = True   
     
   ##### left side code number
       
   name2=getControl(window,"Label","tbProductInfoValue1")  
   if(name2 == None):
       print "None"
       #result = False
   else:    
       #test.log("type:%s "% name2["type"])
       #test.log("name:%s "% name2["name"])
       #test.log("text:%s "% name2["text"])
       test.log("lyt side code number is " +name2["text"] )
       Code_Number = (name2["text"])
       #print (Application)
       #result = True
            
       if (Controller_Name[0:3] == "EET"):
           #test.log("inside controller family selection")
           file = Global_Scripts_Path+"\Danfoss."+Controller_Name[0:7]+"_"+Code_Number[0:8]+"_DB.csv"
           file_1= Output_Global_Path+"\C_Unit_Verification_"+Code_Number[0:8]+".csv"  
#            else:
#                test.log("error")
#                file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_std_DB.csv"
#                file_1= "C_Unit_Verification_"+Code_Number[0:8]+".csv"
 
 
     #test.log("outside of controller selection") 
       tbl=waitForObjectExists(":KoolProg_Table")
       items=tbl.nativeObject.Items    
       openfile = open(file_1,'wt') 
       writer = csv.writer(openfile)
       writer.writerow(["DB_Parameter_Name", "KP_Parameter_Name", "Result", "DB_Menucode","KP_Menucode","Result" ,"DB_DefaultValue", "KP_DefaultValue", "Result", "DB_MinValue", "KP_MinValue", "Result" ,"DB_MaxValue", "KP_MaxValue", "Result", "DB_Unit", "KP_Unit", "Result","DB_Help", "KP_Help", "Result"])
       
       #test.log("created result file") 

       records = testData.dataset(file)
       for rec in records:
           #test.log("inside for loop 1")
           Menu_Code = testData.field(rec,0)
           Parameter_Name = testData.field(rec, 1)
           #test.log(Parameter_Name)
           #test.log(Menu_Code)
           Default = testData.field(rec, 2)
           #test.log(Default)
           Min = testData.field(rec, 3)
           #test.log(Min)
           Max = testData.field(rec, 4)
           #test.log(Max)
           Unit = testData.field(rec, 5) 
           #test.log(Unit)
           Help = testData.field(rec, 6)
           #test.log(Help)
           #test.log("outside for loop 1")
                        
           for i in range (0, items.Count-1):
               #test.log("inside for loop 2")
               item=items.at(i)
               #test.log(str(Unit))
               #test.log("unit in db is "+ Unit)
               #test.log("unit in kp is "+ item.Unit)
               #test.log("unit in kp is "+ item.Unit[2:])
               #test.log("unit in kp is "+ item.Unit[1:])
               #test.log("parameter name in db is "+Parameter_Name)
               #test.log("parameter name in kp is "+item.ParameterName)
               if ( (Parameter_Name == item.ParameterName) & ( (item.Unit == "°C") | (item.Unit == "K") ) ): 
                   #test.log("parameter is matching with DB")
                   if ((item.Unit == "°C") | (item.Unit == "K")):   
                       test.log(item.ParameterName+" parameter have "+ item.Unit+" unit")
                       Parameter_Name_Result = test.compare((Parameter_Name).strip(), (item.ParameterName).strip())
                       MenuCode_Result = test.compare((Menu_Code).strip(), (item.MenuCode).strip())
                       if '.00' in item.DefaultValue:
                           num,dec=item.DefaultValue.split(".")
                           Default_Value_Result = test.compare((Default).strip(), (num).strip())
                       else:
                           Default_Value_Result = test.compare((Default).strip(), (item.DefaultValue).strip()) 
                       if '.00' in item.Minvalue:
                           num,dec=item.Minvalue.split(".")
                           Min_Value_Result = test.compare((Min).strip(), (num).strip())
                       else:
                           Min_Value_Result = test.compare((Min).strip(), (item.Minvalue).strip())
                       if '.00' in item.Maxvalue:
                           num,dec=item.Maxvalue.split(".")
                           Max_Value_Result = test.compare((Max).strip(), (num).strip())
                       else:
                           Max_Value_Result = test.compare((Max).strip(), (item.Maxvalue).strip())
               
                       #Default_Value_Result = test.compare((Default).strip(), (item.DefaultValue).strip())
                       #Min_Value_Result = test.compare((Min).strip(), (item.Minvalue).strip())
                       #Max_Value_Result = test.compare((Max).strip(), (item.Maxvalue).strip())
                       Unit_Result = test.compare((Unit).strip(), (item.Unit).strip())
                       Help_Result = test.compare((Help).strip(), (item.Description).strip())
                       writer.writerow([Parameter_Name, item.ParameterName,Parameter_Name_Result, Menu_Code, item.MenuCode, MenuCode_Result, Default, item.DefaultValue, Default_Value_Result, Min, item.Minvalue, Min_Value_Result, Max, item.Maxvalue, Max_Value_Result, Unit, item.Unit, Unit_Result, Help, item.Description, Help_Result])            
                       
                   else:
                       test.log("unit is not matching")
               #else:
                   #test.log(item.ParameterName+" parameter is not having c and k units")
   result = True
   return result

def DataGrid_Verification_Offline_Unit_F():
   test.log("inside datagrid verification offline unit F")
   result = False
   test.compare(waitForObjectExists(":KoolProg_Table").type, "Table")
   test.compare(waitForObjectExists(":KoolProg_Table").name, "datagridParameters")
  
   window=waitForObject(":KoolProg_Window")
   print("count:%s"% len(window))
   
   ####### left side controller name 
   
   name1=getControl(window,"Label","tbProductInfoValue0")  
   if(name1 == None):
       print "None"
       #result = False
   else:
       #test.log("type:%s "% name1["type"])
       #test.log("name:%s "% name1["name"])
       #test.log("text:%s "% name1["text"])
       test.log("left side controller name is " +name1["text"] )
       Controller_Name = (name1["text"])
       #print (Controller[0:9])
       #result = True   
       
     ####### left side code number    
       
   name2=getControl(window,"Label","tbProductInfoValue1")  
   if(name2 == None):
       print "None"
       #result = False
   else:    
       #test.log("type:%s "% name2["type"])
       #test.log("name:%s "% name2["name"])
       #test.log("text:%s "% name2["text"])
       test.log("left side code number is " +name2["text"] )
       Code_Number = (name2["text"])
       #print (Application)
       #result = True
              
   if (Controller_Name[0:3] == "EET"):
       #test.log("1")
       #test.log(Controller[0:6])
       file = Global_Scripts_Path+"\Danfoss."+Controller_Name[0:7]+"_"+Code_Number[0:8]+"_DB_F.csv"
       file_1= Output_Global_Path+"\F_Unit_Verification_"+Code_Number[0:8]+".csv"  
#            else:
#                file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_std_DB.csv"
#                file_1= "C_Unit_Verification_"+Code_Number[0:8]+"_std.csv"
#        else:
#            test.log("error")
       
       
       tbl=waitForObjectExists(":KoolProg_Table")
       items=tbl.nativeObject.Items
           
       openfile = open(file_1,'wt') 
       writer = csv.writer(openfile)
       #writer.writerow(["ParameterName", "DB_Menucode","KP_Menucode","Result" ,"DB_DefaultValue", "KP_DefaultValue", "Result", "DB_MinValue", "KP_MinValue", "Result" ,"DB_MaxValue", "KP_MaxValue", "Result", "DB_Unit", "KP_Unit", "Result"])
       writer.writerow(["DB_Parameter_Name", "KP_Parameter_Name", "Result", "DB_Menucode","KP_Menucode","Result" ,"DB_DefaultValue", "KP_DefaultValue", "Result", "DB_MinValue", "KP_MinValue", "Result" ,"DB_MaxValue", "KP_MaxValue", "Result", "DB_Unit", "KP_Unit", "Result","DB_Help", "KP_Help", "Result"])
       
       
       records = testData.dataset(file)
       for rec in records:
           #test.log("inside for loop 1")
           Menu_Code = testData.field(rec, 0)
           #test.log(id)
           #Group_Name = testData.field(rec, 1)
           #test.log(Group_Name)
           Parameter_Name = testData.field(rec, 1)
           #test.log(Parameter_Name)
           #Menu_Code = testData.field(rec,3)
           #test.log(Menu_Code)
           Default = testData.field(rec, 3)
           #test.log(Default)
           Min = testData.field(rec, 5)
           #test.log(Min)
           Max = testData.field(rec, 7)
           #test.log(Max)
           Unit = testData.field(rec, 9) 
           #test.log(Unit)
           #test.log(str(Unit))
           #Enum = testData.field(rec, 8)
           #test.log(Enum)
           Help = testData.field(rec, 10)
           #test.log(Hel
           #test.log("outside for loop 1")
                        
           for i in range (0, items.Count-1):
               ##test.log("inside for loop 2")
               item=items.at(i)
               #test.log(str(Unit))
               #test.log("unit in db is "+ Unit)
               #test.log("unit in kp is "+ item.Unit)
               #test.log("unit in kp is "+ item.Unit[2:])
               #test.log("unit in kp is "+ item.Unit[1:])
               #test.log("parameter name in db is "+Parameter_Name)
               #test.log("parameter name in kp is "+item.ParameterName)
               if  ( (Parameter_Name == item.ParameterName) & (item.Unit == "°F") ) :   
                   test.log(item.ParameterName+" have "+ item.Unit)
                   #Group_Name_Result = test.compare((Group_Name).strip(), (item.GroupName).strip())
                   Parameter_Name_Result = test.compare((Parameter_Name).strip(), (item.ParameterName).strip())
                   MenuCode_Result = test.compare((Menu_Code).strip(), (item.MenuCode).strip())
                   if '.00' in item.DefaultValue:
                       num,dec=item.DefaultValue.split(".")
                       Default_Value_Result = test.compare((Default).strip(), (num).strip())
                   else:
                       Default_Value_Result = test.compare((Default).strip(), (item.DefaultValue).strip()) 
                   if '.00' in item.Minvalue:
                       num,dec=item.Minvalue.split(".")
                       Min_Value_Result = test.compare((Min).strip(), (num).strip())
                   else:
                       Min_Value_Result = test.compare((Min).strip(), (item.Minvalue).strip())
                   if '.00' in item.Maxvalue:
                       num,dec=item.Maxvalue.split(".")
                       Max_Value_Result = test.compare((Max).strip(), (num).strip())
                   else:
                       Max_Value_Result = test.compare((Max).strip(), (item.Maxvalue).strip())
                   
                       #Default_Value_Result = test.compare((Default).strip(), (item.DefaultValue).strip())
                       #Min_Value_Result = test.compare((Min).strip(), (item.Minvalue).strip())
                       #Max_Value_Result = test.compare((Max).strip(), (item.Maxvalue).strip())
                   Unit_Result = test.compare((Unit).strip(), (item.Unit).strip())
                   Help_Result = test.compare((Help).strip(), (item.Description).strip())
                   writer.writerow([ Parameter_Name, item.ParameterName,Parameter_Name_Result, Menu_Code, item.MenuCode, MenuCode_Result, Default, item.DefaultValue, Default_Value_Result, Min, item.Minvalue, Min_Value_Result, Max, item.Maxvalue, Max_Value_Result, Unit, item.Unit, Unit_Result,Help,item.Description,Help_Result])            
                   #result = True
               #else:
                   #test.log("parameter name is not matching")
                   #test.log("parameter name in DB is "+ Parameter_Name)
   result = True
   return result
	
def Delete_File():        
   test.log("inside the delete file")
   result = False
   dirPath = "C:/KoolProg/Configurations"
   fileList = os.listdir(dirPath)
   for fileName in fileList:
       os.remove(dirPath+ "/"+fileName)
       result = True
   return result

def Delete_Folder():        
   test.log("inside the delete folder")
   result = False
   try:  
        shutil.rmtree('C:/KoolProg/Configurations/New folder')
   except OSError:  
        test.log ("Deletion of the directory %s failed" % str('C:/KoolProg/Configurations/New folder'))
   else:  
        test.log ("Successfully deleted the directory %s" % str('C:/KoolProg/Configurations/New folder'))
   result = True
   return result

def Enable_F(symbolicname, value): 
   test.log("inside enable_f function")
   result = False 
   tbl=waitForObjectExists(symbolicname)  
   Object=tbl.nativeObject
   test.compare(value, Object.IsEnabled)
   result = True
   return result  
   
def Enable_Popup(symbolicname, value):
   test.log("inside enable popup menubar")
   result = False
   test.log("this function check buttons are enable or disable during popup window")
   tbl=waitForObjectExists(symbolicname)  
   Object=tbl.nativeObject 
   test.compare(bool(strtobool(value)),(Object.IsFocused))
   result = True
   return result 

def Enable_S(symbolicname, value): 
   test.log("inside enable_s function")
   result = False
   tbl=waitForObjectExists(symbolicname)  
   test.compare(bool(value), tbl.enabled)  
   result = True
   return result

def testRandomPlot_11():
    test.log("inside random plot 11")
    result = False
    resultList = []
    tbl=waitForObjectExists(":KoolProg_Table")  
    fieldsTable=parseFieldsForPlot(tbl)
    #IsSelectedForPlotting
    Object=tbl.nativeObject
    items=tbl.nativeObject.Items
    for i in range (0,12):        
        num = random.randint(0, items.Count-1)
        while num in resultList:
            num = random.randint(0, items.Count-1)
        resultList.append(num)
    count = len(resultList) 
    for i in range(0,count-1): 
        item=items.at(resultList[i])
        name = item.ParameterName           
        test.log("Plot: %s" % setParameterPlotAndFav(fieldsTable, name))
    result = True
    return  result

def testRandomPlot_checking():
    test.log("inside random plot checking")
    result = False
    resultList = []
    tbl=waitForObjectExists(":KoolProg_Table")  
    fieldsTable=parseFieldsForPlot(tbl)
    Object=tbl.nativeObject
    items=tbl.nativeObject.Items
    for i in range (0,10):        
        num = random.randint(0, items.Count-1)
        while num in resultList:
            num = random.randint(0, items.Count-1)
        resultList.append(num)
    count = len(resultList)
    for i in range(0,count-1): 
        item=items.at(resultList[i])
        name = item.ParameterName           
        test.log("Plot: %s" % setParameterPlotAndFav(fieldsTable, name))
    result = True
    return  result

def Value_Generation_Offline():
    test.log("inside value generation offline")
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
    
    ###### left side controller name 
    
    name1=getControl(window,"Label","tbProductInfoValue0")  
    if(name1 == None):
        print "None"
        #result = False
    else:    
        #test.log("type:%s "% name1["type"])
        #test.log("name:%s "% name1["name"])
        #test.log("text:%s "% name1["text"])
        Controller = (name1["text"])
        test.log("left side controller name is "+Controller)
        #result = True
        
    ############ left side code number 
        
    name3_cont=getControl(window,"Label","tbProductInfoValue1")
    if(name3_cont == None):
        print "None"
        #result = False
    else:    
        #test.log("type:%s "% name3_cont["type"])
        #test.log("name:%s "% name3_cont["name"])
        #test.log("text:%s "% name3_cont["text"])
        Application = (name3_cont["text"])
        Code_Number = Application[0:8]
        test.log("left side code number is "+Code_Number)
        
    ##ERCWS##  
     
    if ((Controller[0:4] == "ERC2")):
       fieldsTable=parseFields(tbl)
       Object=tbl.nativeObject
       items=tbl.nativeObject.Items
       file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_Parameters.csv"
        
    ##ERCV2##    
    
    elif (Controller[0:4] == "ERC1"):
        name2_cont=getControl(window,"Label","txtApp")
        if(name2_cont == None):
            print "None"
            result = False
        else:    
#             test.log("type:%s "% name2_cont["type"])
#             test.log("name:%s "% name2_cont["name"])
#             test.log("text:%s "% name2_cont["text"])
            Product_Version = (name2_cont["text"])
        
        fieldsTable=parseFields(tbl)
        Object=tbl.nativeObject
        items=tbl.nativeObject.Items
                    
        if (Controller[0:6] == "ERC111"):
           if (Code_Number == "080G3237")| (Code_Number == "080G3247")|(Code_Number == "080G3234"):
               file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_"+Code_Number+"_"+Product_Version+"_Parameters.csv"
           else:
               file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_std_Parameters.csv"
               
        elif(Controller[0:6] == "ERC112"):
           if ((Code_Number == "080G3202")|(Code_Number == "080G3203")|(Code_Number == "080G3206")|(Code_Number == "080G3207")|(Code_Number == "080G3212")|(Code_Number == "080G3213")|(Code_Number == "080G3216")|(Code_Number == "080G3217"))&(Product_Version == "PV03"):##ALL STD CODE NUMBERS WITH MAINTENANCE DATABSE##
               file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_M_"+Product_Version+"_Parameters.csv"
               
           elif (Code_Number == "080G3221")|(Code_Number == "080G3248")|(Code_Number == "080G3276")|(Code_Number == "080G3259"):
               file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_"+Code_Number+"_"+Product_Version+"_Parameters.csv"
           
           elif (Code_Number == "080G3408")|(Code_Number == "080G3409")|(Code_Number == "080G3410")|(Code_Number == "080G3414")|(Code_Number == "080G3413")|(Code_Number == "080G3419"): ##SPECIAL CODE NUMBERS##, ##3408 uses 112M DB, but PV version is PV01, hence added here##
               file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_"+Code_Number+"_"+Product_Version+"_Parameters.csv"
           
           elif (Code_Number == "080G3220")|(Code_Number == "080G3243"):##COMMON DB_3220##
               file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_080G3220_Parameters.csv"
               
           elif (Code_Number == "080G3229")|(Code_Number == "080G3274"):##COMMON DB_3229##
               file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_080G3229_Parameters.csv"
               
           elif (Code_Number == "080G3275")|(Code_Number == "080G3239"):##COMMON DB_3275##
               file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_080G3275_Parameters.csv"
               
           else:##ALL CODE NUMBERS WITH STANDARD DATABASE##
               file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_std_Parameters.csv"
       
        elif (Controller[0:6]== "ERC113"):##ALL STD CODES FOR MAINTENANCE##
           if ((Code_Number == "080G3252")|(Code_Number == "080G3253")|(Code_Number == "080G3406")|(Code_Number == "080G3407"))&(Product_Version == "PV02"):
               file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_M_"+Product_Version+"_Parameters.csv"
           
           elif (Code_Number == "080G0993"): ##ADDED FOR TRUE - Aashika##
               file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_"+Code_Number+"_"+Product_Version+"_Parameters.csv"
                      
           else:##ALL CODE NUMBERS WITH STANDARD DATABASE##
               file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_std_Parameters.csv"
        
    ##ETC##   
    
    elif ((Controller[0:3] == "ETC")):
        fieldsTable=parseFields(tbl)
        Object=tbl.nativeObject
        items=tbl.nativeObject.Items
        name2_cont=getControl(window,"Label","txtApp")
        if(name2_cont == None):
            print "None"
            result = False
        else:    
            test.log("type:%s "% name2_cont["type"])
            test.log("name:%s "% name2_cont["name"])
            test.log("text:%s "% name2_cont["text"])
            ETC_Application = (name2_cont["text"])
            print ETC_Application
            file = Global_Scripts_Path+"\Danfoss.ETC1H."+ETC_Application+"_Parameters.csv" 
            
    ##EKE##
    
    elif ((Controller[0:3] == "EKE")):
        checkEnableVisibleEKE()
        fieldsTable=parseVisibleRow(tbl)
        Object=tbl.nativeObject
        items=tbl.nativeObject.Items
        
        name3_cont=getControl(window,"Label","txtApp")
        if(name2_cont == None):
            print "None"
            result = False
        else:    
            test.log("type:%s "% name3_cont["type"])
            test.log("name:%s "% name3_cont["name"])
            test.log("text:%s "% name3_cont["text"])
            PV = (name3_cont["text"])
            EKE_PV = PV[4:8] 
            print EKE_PV
            file = "EKE1C_"+EKE_PV+"_DB.csv"
        
                    
    ##EET##
        
    elif (Controller[0:3] == "EET"):
        test.log("inside EET controller")
        fieldsTable=parseFields(tbl)
        test.log("outside of parsing")
        Object=tbl.nativeObject
        #test.log("1")
        items=tbl.nativeObject.Items
        #test.log("2")
        file = Global_Scripts_Path+"\Danfoss."+Controller[0:7]+"_"+Code_Number[0:8]+"_Parameters.csv" 
#         else:
#             test.log("inside else")
#             file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_std_Parameters.csv"   
    
    #test.log("4")
    file_1 = "Value_Generation_Offline.csv"
    openfile = open(file_1,'wt') 
    writer = csv.writer(openfile)
    writer.writerow(["DB_Parameter_Name","KP_Parameter_Name", "KP_Random_Value"])
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
            Parameter_Name = testData.field(rec, 0)
            enum = testData.field(rec,1)
            for i in range (0, items.Count):
                item=items.at(i) 
                #test.log("database parameter name is "+ Parameter_Name+" and koolprog's parameter name is " +item.ParameterName)
                if ((Parameter_Name == item.ParameterName) & (item.Datatype == "Float") & (item.ReadOnly == False)&(item.IsEnabled == True) & (Parameter_Name != "Lowest Temperature Limit") & (Parameter_Name != "Highest Temperature Limit") & (Parameter_Name != "Low temp Alarm limit") & (Parameter_Name != "High temp Alarm limit") & (Parameter_Name != "Condenser Alarm Limit" ) & (Parameter_Name != "Condenser Block Limit") & (Parameter_Name != "Condenser OK Limit")):
                    test.log(item.ParameterName+" is float")
                    #Object.SelectedIndex = i
                    minVal = float(item.Minvalue)
                    #print ("min_value"+str(minVal))
                    maxVal = float(item.Maxvalue) 
                    #print ("max_value"+str(maxVal))  
                    if(functions[j] == 'Min'):
                        test.log("Min Result:%s" % setParameterValue(fieldsTable,item.ParameterName, str(minVal)))
                    elif(functions[j] == 'Max'):
                        test.log("Max Result:%s" % setParameterValue(fieldsTable,item.ParameterName, str(maxVal)))
                    else:
                        item_Val = random.uniform(minVal, maxVal)
                        #print ("0_"+str(item_Val))
                        itemVal = float(item_Val)
                        #print ("1_"+str(itemVal))
                        itemVal = round(item_Val,2)
                        #print ("2_"+str(itemVal))
                        test.log("Random Result of float:%s" % setParameterValue(fieldsTable,item.ParameterName, str(itemVal)))
                        test.log("random value of "+str(item.ParameterName)+" parameter is "+str(itemVal))
                        test.log(item.Key)
                        writer.writerow([item.Key,item.ParameterName,itemVal])   
                         
                elif ((Parameter_Name == item.ParameterName) & (item.Datatype == "INT") & (item.ReadOnly == False) & (item.IsEnabled == True) & (Parameter_Name != "Minimum defrost Interval") & (Parameter_Name != "Maximum defrost Interval") & (Parameter_Name != "Minimum Cut-in Voltage") & (Parameter_Name != "Minimum Cut out Voltage")):
                    test.log(item.ParameterName+" is int")
                    #Object.SelectedIndex = i
                    minVal = float(item.Minvalue)
                    maxVal = float(item.Maxvalue)  
                    if(functions[j] == 'Min'):
                        #test.log(item.ParameterName)
                        test.log("Min Result:%s" % setParameterValue(fieldsTable,item.ParameterName, minVal))
                    elif(functions[j] == 'Max'):
                        #test.log(item.ParameterName)
                        test.log("Max Result:%s" % setParameterValue(fieldsTable,item.ParameterName, maxVal))
                    else:
                        itemVal = random.randint(minVal, maxVal)
                    try:
                        #test.log(item.ParameterName)
                        test.log("Ranom Result of int:%s" % setParameterValue(fieldsTable,item.ParameterName, itemVal))
                        #Group_Name_Result = test.compare((Group_Name).strip(), (item.GroupName).strip())
                            #GroupCode_Result = test.compare((Group_Code).strip(), (item.GroupCode).strip())
                            #Parameter_Name_Result = test.compare((Parameter_Name).strip(), (item.ParameterName).strip())
                            #Menu_Code_Result = test.compare((Menu_Code).strip(), (item.MenuCode).strip())
                        test.log("random value of "+str(item.ParameterName)+" parameter is "+str(itemVal))
                        writer.writerow([item.Key,item.ParameterName,itemVal])
                    except:
                       snooze(1)
                    
                elif ((Parameter_Name == item.ParameterName)&((item.Datatype == "enum") | (item.Datatype == "BIT"))&(item.ReadOnly == False)&(item.IsEnabled == True)):              
                    test.log(item.ParameterName+" is enum")
                    if(enum != ""):
                        for x in enum.split(','):
                            test1 = x.split(':')
                            val = test1[1].strip()                       
                            enumList.append(val)
    #                         for y in x.split(':'):
    #                             isText = hasTexts(y)
    #                             if(isText):
    #                                 enumList.append(y)
                        enumList_count = len(enumList) 
                        #test.log("Count is "+str(enumList_count))                   
                        rand_enum = random.randint(0,enumList_count-1)
                        #test.log(str(i)) 
                        if ((Parameter_Name != "Predefined applications" )  & (Parameter_Name != "Sensor Error Type")):
                            #test.log(Parameter_Name)
                            enumValue = enumList[rand_enum]
                            #test.log(Controller[0:3])
                            #test.log(enumValue)
                            #test.log(Controller[0:3])
                            if (enumValue != None):
                                #test.log("2")
                                #item.Value = enumValue
                                #test.log(Controller[0:3])
                                if (Controller[0:3] == "EKE"):
                                    test.log("Result:%s" % setParameterEnumValue(fieldsTable,item.ParameterName, enumValue))
                                    writer.writerow([item.ParameterName, enumValue])
                                    if ((item.ParameterName in checkParameters)):
                                        # | (item.ParameterName == "AuH")):
                                        visibleParamName = []
                                        test.log(item.ParameterName,"Check")
                                        fieldsTable = parseVisibleRow(tbl)
                                        test.log("random value of "+str(item.ParameterName)+" parameter is "+str(item.Val))
                                        writer.writerow([item.Key,item.ParameterName,enumValue])
                                    else:
                                        snooze(1)
                                else: 
                                    #test.log(item.ParameterName)
                                    item.Value = enumValue
                                    #test.log(str(fieldsTable))
                                    #test.log(str(item.ParameterName))
                                    #test.log(enumValue)
                                    #test.log(item.ParameterName)
                                    #Group_Name_Result = test.compare((Group_Name).strip(), (item.GroupName).strip())
                                    #GroupCode_Result = test.compare((Group_Code).strip(), (item.GroupCode).strip())
                                    #Parameter_Name_Result = test.compare((Parameter_Name).strip(), (item.ParameterName).strip())
                                    #Menu_Code_Result = test.compare((Menu_Code).strip(), (item.MenuCode).strip())
                                    test.log("random value of "+str(item.ParameterName)+" parameter is "+str(enumValue))
                                    writer.writerow([Parameter_Name,item.ParameterName,enumValue])  
                            else:
                                test.log("error")
                                snooze(1)
                        else:
                            test.log("error")
                            snooze(1)                 
                    enumList = []
                #else:
                    #test.log("db parameter "+str(Parameter_Name)+" is not matching with koolprog db "+str(item.ParameterName))
                    #test.log("parameter is "+Parameter_Name)
        
        result = True
    return result

def Value_Generation_Online():
    test.log("inside value generation online")
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
    #waitForObject(":KoolProg_Image_7", 20000)
    
    ###### left side controller name 
    
    name1=getControl(window,"Label","tbProductInfoValue0")  
    if(name1 == None):
        print "None"
        #result = False
    else:    
        #test.log("type:%s "% name1["type"])
        #test.log("name:%s "% name1["name"])
        #test.log("text:%s "% name1["text"])
        Controller = (name1["text"])
        test.log("left side controller name is "+ Controller )
        #result = True
        
    ###### right side controller name 
      
    name2_cont=getControl(window,"Label","txtProuctName")  
    if(name2_cont == None):
        print "None"
        #result = False
    else:    
        #test.log("type:%s "% name2_cont["type"])
        #test.log("name:%s "% name2_cont["name"])
        #test.log("text:%s "% name2_cont["text"])
        Controller_Name = (name2_cont["text"])
        test.log("right side controller name is "+ Controller_Name )
        #result = True
        
    ############ right side code number 
        
    name3_cont=getControl(window,"Label","txtCodeNumber")
    if(name3_cont == None):
        print "None"
        #result = False
    else:    
        #test.log("type:%s "% name3_cont["type"])
        #test.log("name:%s "% name3_cont["name"])
        #test.log("text:%s "% name3_cont["text"])
        Code_Number = (name3_cont["text"])
        #Code_Number = Application
        test.log("right side code number is "+ Code_Number)
        
    ##ERCWS##  
     
    if ((Controller_Name[0:4] == "ERC2")):
       fieldsTable=parseFields(tbl)
       Object=tbl.nativeObject
       items=tbl.nativeObject.Items
       file = Global_Scripts_Path+"\Danfoss."+Controller_Name[0:6]+"_Parameters.csv"
        
    ##ERCV2##    
    
    elif (Controller_Name[0:4] == "ERC1"):
        test.log("inside ERC1 controller")
        fieldsTable=parseFields(tbl)
        Object=tbl.nativeObject
        items=tbl.nativeObject.Items
        
        name2_cont=getControl(window,"Label","txtApp")
        if(name2_cont == None):
            print "None"
            result = False
        else:    
#             test.log("type:%s "% name2_cont["type"])
#             test.log("name:%s "% name2_cont["name"])
#             test.log("text:%s "% name2_cont["text"])
            Product_Version = (name2_cont["text"])
            test.log(str(Product_Version))
                    
        if (Controller_Name[0:6] == "ERC111"):
           if (Code_Number == "080G3237")| (Code_Number == "080G3247")|(Code_Number == "080G3234"):
               file = Global_Scripts_Path+"\Danfoss."+Controller_Name[0:6]+"_"+Code_Number+"_"+Product_Version+"_Parameters.csv"
           else:
               file = Global_Scripts_Path+"\Danfoss."+Controller_Name[0:6]+"_std_Parameters.csv"
               
        elif(Controller_Name[0:6] == "ERC112"):
           if ((Code_Number == "080G3202")|(Code_Number == "080G3203")|(Code_Number == "080G3206")|(Code_Number == "080G3207")|(Code_Number == "080G3212")|(Code_Number == "080G3213")|(Code_Number == "080G3216")|(Code_Number == "080G3217"))&(Product_Version == "PV03"):##ALL STD CODE NUMBERS WITH MAINTENANCE DATABSE##
               file = Global_Scripts_Path+"\Danfoss."+Controller_Name[0:6]+"_M_"+Product_Version+"_Parameters.csv"
               
           elif (Code_Number == "080G3221")|(Code_Number == "080G3248")|(Code_Number == "080G3276")|(Code_Number == "080G3259"):
               file = Global_Scripts_Path+"\Danfoss."+Controller_Name[0:6]+"_"+Code_Number+"_"+Product_Version+"_Parameters.csv"
           
           elif (Code_Number == "080G3408")|(Code_Number == "080G3409")|(Code_Number == "080G3410")|(Code_Number == "080G3414")|(Code_Number == "080G3413")|(Code_Number == "080G3419"): ##SPECIAL CODE NUMBERS##, ##3408 uses 112M DB, but PV version is PV01, hence added here##
               file = Global_Scripts_Path+"\Danfoss."+Controller_Name[0:6]+"_"+Code_Number+"_"+Product_Version+"_Parameters.csv"
           
           elif (Code_Number == "080G3220")|(Code_Number == "080G3243"):##COMMON DB_3220##
               file = Global_Scripts_Path+"\Danfoss."+Controller_Name[0:6]+"_080G3220_Parameters.csv"
               
           elif (Code_Number == "080G3229")|(Code_Number == "080G3274"):##COMMON DB_3229##
               file = Global_Scripts_Path+"\Danfoss."+Controller_Name[0:6]+"_080G3229_Parameters.csv"
               
           elif (Code_Number == "080G3275")|(Code_Number == "080G3239"):##COMMON DB_3275##
               file = Global_Scripts_Path+"\Danfoss."+Controller_Name[0:6]+"_080G3275_Parameters.csv"
               
           else:##ALL CODE NUMBERS WITH STANDARD DATABASE##
               file = Global_Scripts_Path+"\Danfoss."+Controller_Name[0:6]+"_std_Parameters.csv"
       
        elif (Controller_Name[0:6]== "ERC113"):##ALL STD CODES FOR MAINTENANCE##
           if ((Code_Number == "080G3252")|(Code_Number == "080G3253")|(Code_Number == "080G3406")|(Code_Number == "080G3407"))&(Product_Version == "PV02"):
               file = Global_Scripts_Path+"\Danfoss."+Controller_Name[0:6]+"_M_"+Product_Version+"_Parameters.csv"
           
           elif ((Code_Number == "080G0993")):##ADDED FOR True - Aashika##
               file = Global_Scripts_Path+"\Danfoss."+Controller_Name[0:6]+"_"+Code_Number+"_"+Product_Version+"_Parameters.csv"
           
           else:##ALL CODE NUMBERS WITH STANDARD DATABASE##
               file = Global_Scripts_Path+"\Danfoss."+Controller_Name[0:6]+"_std_Parameters.csv"
       
    ##ETC##   
    
    elif ((Controller_Name[0:3] == "ETC")):
        test.log("inside ETC controller")
        fieldsTable=parseFields(tbl)
        Object=tbl.nativeObject
        items=tbl.nativeObject.Items
        name2_cont=getControl(window,"Label","txtApp")
        if(name2_cont == None):
            print "None"
            #result = False
        else:    
            test.log("type:%s "% name2_cont["type"])
            test.log("name:%s "% name2_cont["name"])
            test.log("text:%s "% name2_cont["text"])
            ETC_Application = (name2_cont["text"])
            print ETC_Application
            file = Global_Scripts_Path+"\Danfoss.ETC1H."+ETC_Application+"_Parameters.csv"         
    ##EKE##
    elif ((Controller_Name[0:3] == "EKE")):
        test.log("inside EKE controller")
        checkEnableVisibleEKE()
        fieldsTable=parseVisibleRow(tbl)
        Object=tbl.nativeObject
        items=tbl.nativeObject.Items
        
        name3_cont=getControl(window,"Label","txtApp")
        if(name2_cont == None):
            print "None"
            #result = False
        else:    
            test.log("type:%s "% name3_cont["type"])
            test.log("name:%s "% name3_cont["name"])
            test.log("text:%s "% name3_cont["text"])
            PV = (name3_cont["text"])
            EKE_PV = PV[4:8] 
            print EKE_PV
            file = "EKE1C_"+EKE_PV+"_DB.csv"
        
    ##EET##    
    
    elif (Controller_Name[0:3] == "EET"):
        test.log("inside EET controller")
        fieldsTable=parseFields(tbl)
        test.log("after parsing the parameters")
        Object=tbl.nativeObject
        items=tbl.nativeObject.Items
            
        file = Global_Objects_Path+"\Danfoss."+Controller_Name[0:7]+"_"+Code_Number[0:8]+"_Parameters.csv"
        test.log(str(file))
    else:
        test.log("not support controller is connected with KoolProg")
    #file_2 = "Online_Value_Generation_Comparison_Sheet.csv"
    
    test.log("outside controller slection");
    file_1 = "Value_Generation_Online.csv"
    #file_1 = file_1 + Timestr
    #file_1 = file_1 + ".csv"

    openfile = open(file_1,'wt') 
    writer = csv.writer(openfile)
    writer.writerow(["DB_Parameter_Name","KP_Parameter_Name", "KP_Random_Value"])
    enumList = []
    test1 = []
    functions = ['Min', 'Max', 'Val']
    #test.log(str(file))
    records = testData.dataset(file)
#     functions.append("Min")
#     functions.append("Max")
#     functions.append("Val")
    count = len(functions)
    for j in range(0,count):
        for rec in records:
            #test.log("inside loop")
            Parameter_Name= testData.field(rec, 0)
            #Group_Name = testData.field(rec,1)
            #Group_Code = testData.field(rec,2)
            #Parameter_Name = testData.field(rec,3)
            #Menu_Code = testData.field(rec, 4)
            enum = testData.field(rec,1)
            for i in range (0, items.Count):
                item=items.at(i) 
                #test.log(Parameter_Name)
                #test.log(Parameter_Name+" is writing and datatype is "+str(item.Datatype)+" read only is "+str(item.ReadOnly)+" enable is "+str(item.IsEnabled))
                #test.log("database parameter name is "+ Parameter_Name+" and koolprog's parameter name is " +item.ParameterName)
                if ((Parameter_Name == item.ParameterName) & (item.Datatype == "Float") & (item.ReadOnly == False)&(item.IsEnabled == True) & (Parameter_Name != "Lowest Temperature Limit") & (Parameter_Name != "Highest Temperature Limit") & (Parameter_Name != "Low temp Alarm limit") & (Parameter_Name != "High temp Alarm limit")  & (Parameter_Name != "Condenser Alarm Limit" ) & (Parameter_Name != "Condenser Block Limit" ) & (Parameter_Name != "Condenser OK Limit") ):
                    # & (Parameter_Name != "Lowest Temperature Limit") & (Parameter_Name != "Highest Temperature Limit") & (Parameter_Name != "Low temp Alarm limit") & (Parameter_Name != "High temp Alarm limit") & (Parameter_Name != "Condenser Alarm Limit" ) & (Parameter_Name != "Condenser Block Limit") & (Parameter_Name != "Condenser OK Limit")):
                    #test.log(item.ParameterName+" is float")
                    #Object.SelectedIndex = i
                    minVal = float(item.Minvalue)
                    #print ("min_value"+str(minVal))
                    maxVal = float(item.Maxvalue) 
                    #print ("max_value"+str(maxVal))  
                    if(functions[j] == 'Min'):
                        test.log(" Min Result of float:%s" % setParameterValue(fieldsTable,item.ParameterName, str(minVal))+ " for " + Parameter_Name + "parameter")
                    elif(functions[j] == 'Max'):
                        test.log("Max Result of float:%s" % setParameterValue(fieldsTable,item.ParameterName, str(maxVal))+ " for " + Parameter_Name + "parameter")
                    else:
                        item_Val = random.uniform(minVal, maxVal)
                        #print ("0_"+str(item_Val))
                        itemVal = float(item_Val)
                        #print ("1_"+str(itemVal))
                        itemVal = round(item_Val,2)
                        #print ("2_"+str(itemVal))
                        test.log("Random Result of float:%s" % setParameterValue(fieldsTable,item.ParameterName, str(itemVal)))
                        #Group_Name_Result = test.compare((Group_Name).strip(), (item.GroupName).strip())
                        #GroupCode_Result = test.compare((Group_Code).strip(), (item.GroupCode).strip())
                        #Parameter_Name_Result = test.compare((Parameter_Name).strip(), (item.ParameterName).strip())
                        #Menu_Code_Result = test.compare((Menu_Code).strip(), (item.MenuCode).strip())
                        test.log("random value of "+str(item.ParameterName)+" parameter is "+str(itemVal))
                        #writer.writerow([id,Group_Name,item.GroupName,Menu_Code,item.MenuCode,Parameter_Name,item.ParameterName,itemVal]) 
                        #writer.writerow([item.Key,item.ParameterName,enumValue])
                        writer.writerow([Parameter_Name, item.ParameterName,itemVal]) 
                         
                elif ((Parameter_Name == item.ParameterName) & (item.Datatype == "INT") & (item.ReadOnly == False) & (item.IsEnabled == True) & (Parameter_Name != "Minimum defrost Interval") & (Parameter_Name != "Maximum defrost Interval") & (Parameter_Name != "Minimum Cut-in Voltage") & (Parameter_Name != "Minimum Cut out Voltage") ):
                    
                    #test.log(item.ParameterName+" is int")
                    #Object.SelectedIndex = i
                    minVal = float(item.Minvalue)
                    maxVal = float(item.Maxvalue)  
                    if(functions[j] == 'Min'):
                        #test.log(item.ParameterName)
                        test.log("Min Result of int:%s" % setParameterValue(fieldsTable,item.ParameterName, minVal) + " for " + Parameter_Name + "parameter" )
                    elif(functions[j] == 'Max'):
                        #test.log(item.ParameterName)
                        test.log("Max Result of int:%s" % setParameterValue(fieldsTable,item.ParameterName, maxVal) + " for " + Parameter_Name + "parameter" )
                    else:
                        itemVal = random.randint(minVal, maxVal)
                    try:
                        #test.log(item.ParameterName)
                        test.log("Ranom Result of int:%s" % setParameterValue(fieldsTable,item.ParameterName, itemVal) + " for " + Parameter_Name + "parameter")
                        #Group_Name_Result = test.compare((Group_Name).strip(), (item.GroupName).strip())
                            #GroupCode_Result = test.compare((Group_Code).strip(), (item.GroupCode).strip())
                            #Parameter_Name_Result = test.compare((Parameter_Name).strip(), (item.ParameterName).strip())
                            #Menu_Code_Result = test.compare((Menu_Code).strip(), (item.MenuCode).strip())
                        #test.log("random value of "+str(item.ParameterName)+" parameter is "+str(itemVal) )
                        #writer.writerow([id,Group_Name,item.GroupName,Menu_Code,item.MenuCode,Parameter_Name,item.ParameterName,itemVal])
                        writer.writerow([Parameter_Name, item.ParameterName,itemVal]) 
                    except:
                       snooze(1)
                    
                elif ((Parameter_Name == item.ParameterName)&((item.Datatype == "enum") | (item.Datatype == "BIT"))&(item.ReadOnly == False)&(item.IsEnabled == True)):              
                    #test.log(item.ParameterName+" is enum")
                    if(enum != ""):
                        for x in enum.split(','):
                            test1 = x.split(':')
                            val = test1[1].strip()                       
                            enumList.append(val)
    #                         for y in x.split(':'):
    #                             isText = hasTexts(y)
    #                             if(isText):
    #                                 enumList.append(y)
                        #test.log(str(enumList))
                        enumList_count = len(enumList) 
                        #test.log("Count is "+str(enumList_count))                   
                        rand_enum = random.randint(0,enumList_count-1)
                        #test.log(str(rand_enum)) 
                        if ((Parameter_Name != "Predefined applications" ) & (Parameter_Name != "Zero crossing") & (Parameter_Name != "Sensor Error Type")):
                            #test.log("value of rand_enum is: " +str(rand_enum))
                            enumValue = enumList[rand_enum]
                            #test.log(enumValue)
                            if (enumValue != None):
                                #item.Value = enumValue
                                if (Controller_Name[0:3] == "EKE"):
                                    test.log("Result:%s" % setParameterEnumValue(fieldsTable,item.ParameterName, enumValue))
                                    writer.writerow([item.ParameterName, enumValue])
                                    if ((item.ParameterName in checkParameters)):
                                        # | (item.ParameterName == "AuH")):
                                        visibleParamName = []
                                        test.log(item.ParameterName,"Check")
                                        fieldsTable = parseVisibleRow(tbl)
                                        test.log("random value of "+str(item.ParameterName)+" parameter is "+str(item.Val))
                                        #writer.writerow([id,Group_Name,item.GroupName,Menu_Code,item.MenuCode,Parameter_Name,item.ParameterName,enumValue])
                                        writer.writerow([Parameter_Nam, item.ParameterName,itemVal]) 
                                    else:
                                        snooze(1)
                                else: 
                                    #test.log(item.ParameterName)
                                    item.Value = enumValue
                                    #test.log(str(fieldsTable))
                                    #test.log(str(item.ParameterName))
                                    #test.log(enumValue)
                                    #test.log("Random Result of enum:%s" % setParameterValue(fieldsTable,item.ParameterName, enumValue))
                                    #test.log(item.ParameterName)
                                    #Group_Name_Result = test.compare((Group_Name).strip(), (item.GroupName).strip())
                                    #GroupCode_Result = test.compare((Group_Code).strip(), (item.GroupCode).strip())
                                    #Parameter_Name_Result = test.compare((Parameter_Name).strip(), (item.ParameterName).strip())
                                    #Menu_Code_Result = test.compare((Menu_Code).strip(), (item.MenuCode).strip())
                                    test.log("random value of "+str(item.ParameterName)+" parameter is "+str(enumValue))
                                    #writer.writerow([id,Group_Name,item.GroupName,Menu_Code,item.MenuCode,Parameter_Name,item.ParameterName,enumValue])  
                                    #writer.writerow([item.Key,item.ParameterName,enumValue])
                                    writer.writerow([Parameter_Name, item.ParameterName,enumValue]) 
                            else:
                                snooze(1)
                        else:
                            snooze(1)                 
                    enumList = []
                #else:
                    #test.log("db parameter "+str(Parameter_Name)+" is not matching with koolprog db "+str(item.ParameterName))
                    #test.log("parameter is "+Parameter_Name)
        
        result = True
    return result

def Value_Verification_Offline():
    test.log("inside value verfication offline")
    result = False
    tbl=waitForObjectExists(":KoolProg_Table")
    items=tbl.nativeObject.Items
    
    file = "Value_Generation_Offline.csv"
    records = testData.dataset(file)

    file_1 = "Value_Verification_Offline.csv"
    openfile = open(file_1,'wt')
    writer = csv.writer(openfile)
    writer.writerow(["DB_Parameter_Name","KP_Parameter_Name", "KP_Random_Value", "KP_Current_Value", "Result"])
    
    for rec in records:
        DB_Parameter_Name = testData.field(rec, 0)
        KP_Parameter_Name = testData.field(rec, 1)
        Random_Value = testData.field(rec, 2)
        #print Random_Value
        for i in range (0, items.Count-1):
            #test.log("inside loop")
            item=items.at(i)
            if ( (item.ParameterName == DB_Parameter_Name)  & (DB_Parameter_Name != "Lowest Temperature Limit") & (DB_Parameter_Name != "Highest Temperature Limit") & (DB_Parameter_Name != "Low temp Alarm limit") & (DB_Parameter_Name != "High temp Alarm limit") & (DB_Parameter_Name != "Condenser Alarm Limit" ) & (DB_Parameter_Name != "Condenser Block Limit") & (DB_Parameter_Name != "Condenser OK Limit") & (DB_Parameter_Name != "Minimum Defrost Interval") & (DB_Parameter_Name != "Maximum Defrost Interval")):
                #test.log("imside if condition")
                #Group_Name_Result = test.compare((Group_Name).strip(), (item.GroupName).strip())
                #GroupCode_Result = test.compare((Group_Code).strip(), (item.GroupCode).strip())
                #Parameter_Name_Result = test.compare((Parameter_Name).strip(), (item.ParameterName).strip())
                #Menu_Code_Result = test.compare((Menu_Code).strip(), (item.MenuCode).strip())
                if ((item.Datatype == "Enum")|(item.Datatype == "BIT")):
                    result = test.compare(str(Random_Value), str(item.Value))
                    writer.writerow([DB_Parameter_Name,item.ParameterName,Random_Value, item.Value, result1])
                else:
                    result1 = test.compare(str(Random_Value).strip(), str(item.Value).strip())
                    writer.writerow([DB_Parameter_Name,item.ParameterName,str(Random_Value), str(item.Value), result1])
        result = True
    return result

def Value_Verification_Online():
    test.log("inside value verfication online")
    result = False
    tbl=waitForObjectExists(":KoolProg_Table")
    items=tbl.nativeObject.Items
    file = "Value_Generation_Online.csv"
    records = testData.dataset(file)
    
    file_1 = "Value_Verification_Online.csv"
    openfile = open(file_1,'wt')
    writer = csv.writer(openfile)
    writer.writerow(["DB_Parameter_Name","KP_Parameter_Name", "KP_Random_Value", "KP_Current_Value", "Result"])
    
    
    for rec in records:
        #test.log("inside the loop")
        DB_Parameter_Name = testData.field(rec, 0)
        KP_Parameter_Name = testData.field(rec, 1)
        Random_Value = testData.field(rec, 2)
        #test.log(Random_Value)
        for i in range (0, items.Count-1):
            #test.log("inside loop")
            item=items.at(i)
            if ((item.ParameterName == DB_Parameter_Name)  & (DB_Parameter_Name != "Lowest Temperature Limit") & (DB_Parameter_Name != "Highest Temperature Limit") & (DB_Parameter_Name != "High Temp Alarm Limit") & (DB_Parameter_Name != "High Temp Alarm delay") & (DB_Parameter_Name != "Condenser Alarm Limit" ) & (DB_Parameter_Name != "Condenser Block Limit") & (DB_Parameter_Name != "Condenser OK Limit") & (DB_Parameter_Name != "Minimum Defrost Interval") & (DB_Parameter_Name != "Maximum Defrost Interval")):
                if ((item.Datatype == "Enum")|(item.Datatype == "BIT")):
                    #result = test.compare(str(Random_Value), str(item.Value))
                    writer.writerow([DB_Parameter_Name,item.ParameterName,Random_Value, item.Value, result])
                else:
                    result = test.compare(str(Random_Value).strip(), str(item.Value).strip())
                    writer.writerow([DB_Parameter_Name,item.ParameterName,str(Random_Value), str(item.Value), result])
        result = True
    return result

def Open_Path_Change():
   test.log("inside open path change")
   result = False
   
   test.log("check and compare  text of save files as")
   tbl_save_as_path=waitForObjectExists(":_Edit")
   test.compare("C:\KoolProg\Configurations",tbl_save_as_path.text)
   path_old=tbl_save_as_path.text
   
   object_save_as_path= tbl_save_as_path.text 
   
   test.log("click on browse")
   mouseClick(waitForObject(":Settings.Browse.._Button"), MouseButton.PrimaryButton)
   
   test.log("popup window")
   tbl_window=waitForObjectExists(":Browse For Folder_Dialog")   
   test.compare("Dialog", tbl_window.type)
   
   test.log("check all buttons are disable after clicking on browse button except popup's button")
   
   test.log("help is disable")
   tbl_help=waitForObjectExists(":_MenuItem")  
   Object_help=tbl_help.nativeObject 
   test.compare(bool(strtobool("False")),(Object_help.IsFocused))
   
   test.log("setting is disable")
   tbl_setting=waitForObjectExists("{container=':KoolProg_Window' name='btnSettings' text='System.Windows.Controls.Image' type='Button'}")  
   Object_setting=tbl_setting.nativeObject 
   test.compare(bool(strtobool("True")),(Object_setting.IsFocused))
          
   test.log("set parameters is disable")
   tbl_set_parameter=waitForObjectExists("{container=':KoolProg_Window' name='imgSetParams' type='Image'}")  
   Object_set_parameter=tbl_set_parameter.nativeObject 
   test.compare(bool(strtobool("False")),(Object_set_parameter.IsFocused))
   
   test.log("copy to controller is disable")
   tbl_copy_to_controller=waitForObjectExists("{container=':KoolProg_Window' name='imgCopycontroller' type='Image'}")  
   Object_copy_to_controller=tbl_copy_to_controller.nativeObject 
   test.compare(bool(strtobool("False")),(Object_copy_to_controller.IsFocused))
   
   test.log("service and test is disable")
   tbl_service_test=waitForObjectExists("{container=':KoolProg_Window' name='imgServicetest' type='Image'}")  
   Object_service_test=tbl_service_test.nativeObject 
   test.compare(bool(strtobool("False")),(Object_service_test.IsFocused))
       
   test.log("x is disable")
   tbl_save=waitForObjectExists(":Settings.X_Button")    
   test.compare(bool("True"), tbl_save.enabled)
   
   test.log("save is disable")
   tbl_save=waitForObjectExists(":Settings.Save_Button")    
   test.compare(bool("True"), tbl_save.enabled) 
   
   test.log("cancel is disable")
   tbl_cancel=waitForObjectExists(":Settings.Cancel_Button")  
   Object_cancel=tbl_cancel.nativeObject 
   test.compare(bool(strtobool("False")),(Object_cancel.IsFocused))
   
   test.log("KoolProg folder is expanded")
   tbl=waitForObjectExists(":OS (C:).KoolProg_TreeItem") 
   test.compare(bool("True"),(tbl.expanded)) 
   
   test.log("Configuration folder is expanded")
   tbl=waitForObjectExists(":KoolProg.Configurations_TreeItem")  
   test.compare(bool("False"),(tbl.expanded)) 
   
   test.log("Configuration folder is selected")
   tbl=waitForObjectExists(":KoolProg.Configurations_TreeItem")  
   test.compare(bool("True"), tbl.selected)

   test.log("make new folder is enable")
   tbl_make_new_folder=waitForObjectExists(":Browse For Folder.Make New Folder_Button")  
   test.compare(bool("True"), tbl_make_new_folder.enabled)  
   
   test.log("ok is enable")
   tbl_ok=waitForObjectExists(":Browse For Folder.OK_Button")  
   test.compare(bool("True"), tbl_ok.enabled)

   test.log("cancel is enable")
   tbl_cancel=waitForObjectExists(":Browse For Folder.Cancel_Button")  
   test.compare(bool("True"), tbl_cancel.enabled) 
   
   test.log("click on make new folder")
   mouseClick(waitForObject(":Browse For Folder.Make New Folder_Button"), MouseButton.PrimaryButton)
   
   test.log("click on new folder")
   mouseClick(waitForObject(":Configurations.New folder_TreeItem"), MouseButton.PrimaryButton)
   
   test.log("new folder is selected")
   tbl=waitForObjectExists(":Configurations.New folder_TreeItem")   
   test.compare(bool("True"), tbl.selected) 
   
   test.log("click on ok")
   mouseClick(waitForObject(":Browse For Folder.OK_Button"), MouseButton.PrimaryButton)
   
   test.log("check text of save files as")
   tbl_save_as_path_new=waitForObjectExists(":_Edit")
   test.compare("C:\KoolProg\Configurations\New folder",tbl_save_as_path_new.text)
   path_new=tbl_save_as_path_new.text
   
   if(path_old == path_new):
       test.log("same path")
   else:
       test.log("path is changed")
       test.log("old path is " +path_old)
       test.log("new path is " +path_new)
   
   result = True 
   return result 
       
def Open_Path_Change_Cancel():
   test.log("inside Open_Path_Change")
   result = False
   test.log("check and compare  text of save files as")
   tbl_save_as_path=waitForObjectExists(":_Edit")
   test.compare("C:\KoolProg\Configurations",tbl_save_as_path.text)
   path_old=tbl_save_as_path.text
   
   object_save_as_path= tbl_save_as_path.text 
   
   test.log("click on browse")
   mouseClick(waitForObject(":Settings.Browse.._Button"), MouseButton.PrimaryButton)
   
   test.log("popup window")
   tbl_window=waitForObjectExists(":Browse For Folder_Dialog")   
   test.compare("Dialog", tbl_window.type)
   
   test.log("check all buttons are disable after clicking on browse button except popup's button")
   
   test.log("help is disable")
   tbl_help=waitForObjectExists(":_MenuItem")  
   Object_help=tbl_help.nativeObject 
   test.compare(bool(strtobool("False")),(Object_help.IsFocused))
   
   test.log("setting is disable")
   tbl_setting=waitForObjectExists("{container=':KoolProg_Window' name='btnSettings' text='System.Windows.Controls.Image' type='Button'}")  
   Object_setting=tbl_setting.nativeObject 
   test.compare(bool(strtobool("True")),(Object_setting.IsFocused))
          
   test.log("set parameters is disable")
   tbl_set_parameter=waitForObjectExists("{container=':KoolProg_Window' name='imgSetParams' type='Image'}")  
   Object_set_parameter=tbl_set_parameter.nativeObject 
   test.compare(bool(strtobool("False")),(Object_set_parameter.IsFocused))
   
   test.log("copy to controller is disable")
   tbl_copy_to_controller=waitForObjectExists("{container=':KoolProg_Window' name='imgCopycontroller' type='Image'}")  
   Object_copy_to_controller=tbl_copy_to_controller.nativeObject 
   test.compare(bool(strtobool("False")),(Object_copy_to_controller.IsFocused))
   
   test.log("service and test is disable")
   tbl_service_test=waitForObjectExists("{container=':KoolProg_Window' name='imgServicetest' type='Image'}")  
   Object_service_test=tbl_service_test.nativeObject 
   test.compare(bool(strtobool("False")),(Object_service_test.IsFocused))
       
   test.log("save is disable")
   tbl_save=waitForObjectExists(":Settings.Save_Button")    
   test.compare(bool("True"), tbl_save.enabled) 
   
   test.log("cancel is disable")
   tbl_cancel=waitForObjectExists(":Settings.Cancel_Button")  
   Object_cancel=tbl_cancel.nativeObject 
   test.compare(bool(strtobool("False")),(Object_cancel.IsFocused))
   
   test.log("KoolProg folder is expanded")
   tbl=waitForObjectExists(":OS (C:).KoolProg_TreeItem")  
   test.compare(bool(True),(tbl.expanded)) 
   
   test.log("Configuration folder is expanded")
   tbl=waitForObjectExists(":KoolProg.Configurations_TreeItem")  
   test.compare(bool(False),(tbl.expanded)) 

   test.log("make new folder")
   tbl_make_new_folder=waitForObjectExists(":Browse For Folder.Make New Folder_Button")  
   test.compare(bool("True"), tbl_make_new_folder.enabled)  
   
   test.log("ok")
   tbl_ok=waitForObjectExists(":Browse For Folder.OK_Button")  
   test.compare(bool("True"), tbl_ok.enabled)

   test.log("cancel")
   tbl_cancel=waitForObjectExists(":Browse For Folder.Cancel_Button")  
   test.compare(bool("True"), tbl_cancel.enabled) 
   
   test.log("click on make new folder")
   mouseClick(waitForObject(":Browse For Folder.Make New Folder_Button"), MouseButton.PrimaryButton)
   
   test.log("click on cancel")
   mouseClick(waitForObject(":Browse For Folder.Cancel_Button"), MouseButton.PrimaryButton)
   
   test.log("check text of save files as")
   tbl_save_as_path_new=waitForObjectExists(":_Edit")
   test.compare("C:\KoolProg\Configurations",tbl_save_as_path_new.text)
   path_new=tbl_save_as_path_new.text
   
   if(path_old == path_new):
       test.log("same path")
   else:
       test.log("path is not changed")
       test.log("old path is " +path_old)
       test.log("new path is " +path_new)
       
   result = True 
   return result 

def Open_New_Path_Verification(symbolicname, value):
   test.log("inside open new path verification")
   result = True 
   tbl=waitForObjectExists(symbolicname)   
   test.compare((value[9:]),(tbl.text[9:]))
   File_Path = tbl.text
   if(File_Path[9:] == value[9:]):
       test.log("open path is same")
   else:
       test.log("open path is not same")
   
   result = True 
   return result 
          
def Open_Old_Path_Verification(symbolicname, value):
   test.log("inside save as old path verification")
   result = False
   File_Path = "C:\KoolProg\Configurations"
   test.log(value[9:])
   test.log(value)
   if(File_Path == value[9:]):
       test.log("save as path is same")
   else:
       test.log("save as path is not same")
       
   result = True 
   return result 
  
def Visible_F(symbolicname, value):
   test.log("inside visible_f") 
   result = False
   test.log("this function check textbox is visible or not")
   tbl=waitForObjectExists(symbolicname)   
   Object=tbl.nativeObject
   test.compare(bool(strtobool(value)), Object.IsVisible) 
   result = True 
   return result 

def Visible_S(symbolicname, value):
   test.log("inside visible_s") 
   result = False
   test.log("this function check textbox is visible or not")
   tbl=waitForObjectExists(symbolicname)   
   Object=tbl.nativeObject
   test.compare(bool(value), Object.IsVisible) 
   result = True 
   return result

def Edit_About(symbolicname, value):
   test.log("inside edit_about")
   result = False
   mouseClick(waitForObject(symbolicname))
   type(waitForObject(symbolicname), "<Ctrl+A>")
   type(waitForObject(symbolicname), "<Backspace>")
   type(waitForObject(symbolicname), value)     
   result = True
   return result

def Expanded(symbolicname, value):
   test.log("inside expanded")
   result = False 
   tbl=waitForObjectExists(symbolicname) 
   try: 
       test.compare(bool(value),(tbl.expanded)) 
   except:
       Exp_Recursive(tbl,value)
   result = True
   return result
       
def Exp_Recursive(tbl,value):
    
    items=object.children(tbl)
    for item_1 in items:  
        try:      
            if((object.properties(item_1)["expanded"] ==  True)):
                test.log("Expander Name is:"+str(item_1.nativeObject.DataContext.Name))
                test.compare(str(value), str(item_1.nativeObject.DataContext.Name))            
        except:
            Exp_Recursive(item_1, value)         

def Password_Verfication():
   test.log("inside password_verfication")
   result = True 
   return result 
   test.log("check password is matching ")
   tbl=waitForObjectExists(":Settings.Password:_Edit")  
   tbl_text= tbl.text
   tbl2=waitForObjectExists(":Settings.Confirm password:_Edit")  
   tbl2_text= tbl.text
   if (tbl_text == tbl2_text):
       test.log("both password is same")
   else:
       test.log("mismatch password")
       
   result = True 
   return result 

def Pdf_Verfication(symbolicname, value):
   test.log("inside pdf_verfication")
   result = False
   test.compare(waitForObjectExists(symbolicname).type, bool(value))
   result = True 
   return result
   
def Show_Password(symbolicname, value):
   test.log("inside show password")
   result = False
   return result 
   test.log("before clicking on show password, password is not showing on textbox")
   tbl=waitForObjectExists(symbolicname)   
   test.compare(value, tbl.id)
   if(value == tbl.id):
       test.log("show password is not checked")
   else:
       test.log("show password is checked")
       
   result = True 
   return result
       
def Show_Password_Show(symbolicname, value):
   test.log("inside show password show")
   result = False
   test.log("before clicking on show password, password is showing on textbox")
   tbl=waitForObjectExists(symbolicname)   
   test.compare(value, tbl.id)
   if(value == tbl.id):
       test.log("show password is checked")
   else:
       test.log("show password is not checked")
   
   result = True 
   return result

def AK_CC_TreeView():
   result = False
   test.compare(waitForObjectExists(":KoolProg_Table").type, "Table")
   test.compare(waitForObjectExists(":KoolProg_Table").name, "datagridParameters")
  
   window=waitForObject(":KoolProg_Window")
   print("count:%s"% len(window))  
    
   Tree_View = waitForObjectExists(":KoolProg_Tree")
   waitForObject(":KoolProg.System.Windows.Controls.Image_Button", 20000)
   treeview_Param =Tree_View.nativeObject
   items= treeview_Param.Header
   
   print(len(items))
   
#     for i in range 
#         print (items)


def Controller_Matching():
   test.log("inside code message 1")
   result = False
   waitForObject(":KoolProg.System.Windows.Controls.Image_Button"),2000 
   window=waitForObject(":KoolProg_Window")
   
   ###################### Controller Name Left Side
   
   name1=getControl(window,"Label","tbProductInfoValue0")  
   if(name1 == None):
       print "None"
       #result = False
   else:    
       test.log("type:%s "% name1["type"])
       test.log("name:%s "% name1["name"])
       test.log("text:%s "% name1["text"])
       Controller_Name_L = (name1["text"])
       #Controller_file = (name1["test"])
       test.log("Controller_Name_L")
       test.log(Controller_Name_L)
       #result = True

  ###################### Controller Name Right Side
      
   name2_cont=getControl(window,"Label","txtProuctName")  

   if(name2_cont == None):
       print "None"
       #result = False
   else:    
       test.log("type:%s "% name2_cont["type"])
       test.log("name:%s "% name2_cont["name"])
       test.log("text:%s "% name2_cont["text"])
       Controller_Name_R = (name2_cont["text"])
       #Controller_cont = (name2["test"])
       test.log("Controller_Name_R")
       test.log(Controller_Name_R)
       #result = True
   
   ################## Code Number on Right Side
          
   if (Controller_Name_R[0:4] == "ERC1"):
       
       name3_cont=getControl(window,"Label","txtCodeNumber")  
       if(name3_cont == None):
           print "None"
           #result = False
       else:    
           test.log("type:%s "% name3_cont["type"])
           test.log("name:%s "% name3_cont["name"])
           test.log("text:%s "% name3_cont["text"])
           Code_Number = (name3_cont["text"])
           Code_Number_R = Code_Number[0:8]
           test.log("Code_Number_R")
           test.log(Controller_Name_R[0:8])
           
   else:
       
   ################## Application on Right Side
   
       name4_cont=getControl(window,"Label","txtApp")  
       if(name4_cont == None):
           print "None"
           #result = False
       else:    
           test.log("type:%s "% name4_cont["type"])
           test.log("name:%s "% name4_cont["name"])
           test.log("text:%s "% name4_cont["text"])
           Application_Name = (name4_cont["text"])
           Application_Name_R = Application_Name[0:4]
           test.log("Application_Name_R")
           test.log(Controller_Name_R[0:8])
           
   ################## Code Number and Application on Left Side
   
   name5_cont=getControl(window,"Label","tbProductInfoValue1")  
   if(name5_cont == None):
       print "None"
       #result = False
   else:                
       test.log("type:%s "% name5_cont["type"])
       test.log("name:%s "% name5_cont["name"])
       test.log("text:%s "% name5_cont["text"])
       Code_Number = (name5_cont["text"])
           
   if (Controller_Name_R[0:4] == "ERC1"):
       Code_Number_L = Code_Number[0:8]
       test.log("Code_Number_L")
   else:           
       Application_Name_L = Code_Number[0:4]
       test.log("Application_Name_L")

           
   ###################### Code Number Mismatch Error  Left Side
   
   if(Controller_Name_R == Controller_Name_L):
           
           if(Code_Number_R != Code_Number_L):
               tbl=waitForObjectExists(":KoolProg.Code Number Mismatch_Label")   
               Object=tbl.nativeObject
               test.compare("Code Number Mismatch", Object.Text)
     
               name6_cont=getControl(window,"Label","txtStatus")  
               if(name6_cont == None):
                   print "None"
                   #result = False
               else:    
                   test.log("type:%s "% name6_cont["type"])
                   test.log("name:%s "% name6_cont["name"])
                   test.log("text:%s "% name6_cont["text"])
                   Code_Number_Mismatch = (name5_cont["text"])
               
               if (Code_Number_Mismatch == "Code Number Mismatch"):
                   test.log("change code number")
                   #result = True
               else:
                   test.log("code number and controller name is same on both side is same 1")
                   
           else:
               test.log("code number and controller name is same on both side is same")
   
   elif ( (Controller_Name_R[:6] != Controller_Name_L[:6]) & ((Controller_Name_R[0:4] == Controller_Name_L[0:4])) ):
               tbl=waitForObjectExists(":KoolProg.Relay Version Mismatch_Label")   
               Object=tbl.nativeObject
               test.compare("Relay Version Mismatch", Object.Text)
               test.log("controller family is same but connected controllre is not same")
           
   
   elif ( (Controller_Name_R[:6] == Controller_Name_L[:6]) & (Controller_Name_R[0:4] == Controller_Name_L[0:4]) & (Controller_Name_R[ :7] == Controller_Name_L[ :7]) ):
               tbl=waitForObjectExists(":KoolProg.Relay Version Mismatch_Label")   
               Object=tbl.nativeObject
               test.compare("Relay Version Mismatch", Object.Text)
               test.log("controller family is same but connected controllre is not same")
         
   else:
       tbl=waitForObjectExists(":KoolProg.Not compliant controller_Label")   
       Object=tbl.nativeObject
       test.compare("Not compliant controller", Object.Text)
       test.log("controller is not same")
   
   result = True 
   return result 

def Type(symbolicname, value):
   test.log("inside type")
   result = False
   tbl=waitForObjectExists(symbolicname)   
   test.compare(value, tbl.type)
   result = True 
   return result 

def PV_Number(symbolicname, value):
   test.log ("inside the PV_number")
   result = False 
   test.log("this function check PV during create project")
   #if(Controller_Name_L == Controller_Name_R):
   #if (Controller_Name_L == "ERC111A"):
   if (  (value == "080G3252") | (value == "080G3253") | (value == "080G3254") | (value == "080G3276") | (value == "080G3221") | (value == "080G3408") | (value == "080G3409")  | (value == "080G3410") ):
       #:Product Name_ComboBox_2 = symbolic name of PV combobox
       tbl=waitForObjectExists(":Product Name_ComboBox_2")   
       Object=tbl.nativeObject
       test.compare("PV01", Object.Text)
   elif ( (value == "080G3230") | (value == "080G3231") | (value == "080G3220")):
       tbl=waitForObjectExists(":Product Name_ComboBox_2")   
       Object=tbl.nativeObject
       test.compare("PV02", Object.Text)
   elif((value == "080G3237")):
       tbl=waitForObjectExists(":Product Name_ComboBox_2")   
       Object=tbl.nativeObject
       test.compare("PV03", Object.Text)     
           
   result = True 
   return result 
def PV_Number_Checking():
   test.log("inside pv number checking")
   result = False 
   waitForObject(":KoolProg.System.Windows.Controls.Image_Button"),2000 
   window=waitForObject(":KoolProg_Window")
   
   ###################### Controller Name Left Side
   
   name1=getControl(window,"Label","tbProductInfoValue1")  
   if(name1 == None):
       print "None"
       result = False
   else:    
       test.log("type:%s "% name1["type"])
       test.log("name:%s "% name1["name"])
       test.log("text:%s "% name1["text"])
       Code_Number_L = (name1["text"])
       value = (name1["text"])
       #Controller_file = (name1["test"])
       test.log("Code_Number_L")
       #value == Code_Number_L 
       result = True
   
   if (  (value == "080G3252") | (value == "080G3253") | (value == "080G3254") | (value == "080G3276") | (value == "080G3221") | (value == "080G3408") | (value == "080G3409") | (value == "080G3410") ):
       tbl=waitForObjectExists(":Product Name_ComboBox_2")   
       Object=tbl.nativeObject
       test.compare("PV01", Object.Text)
   elif ( (value == "080G3230") | (value == "080G3231") | (value == "080G3220")):
       tbl=waitForObjectExists(":Product Name_ComboBox_2")   
       Object=tbl.nativeObject
       test.compare("PV02", Object.Text)
   elif((value == "080G3237")):
       tbl=waitForObjectExists(":Product Name_ComboBox_2")   
       Object=tbl.nativeObject
       test.compare("PV03", Object.Text)
              
   result = True 
   return result 

def Selected(symbolicname, value):
   test.log("inside selected")
   result = False
   return result 
   tbl=waitForObjectExists(symbolicname)   
   test.compare(bool(value), tbl.selected)
   result = True 
   return result 
   
def Selected_Is(symbolicname, value):
   test.log("inside selected is ")
   result = False
   tbl=waitForObjectExists(symbolicname)  
   Object=tbl.nativeObject
   test.compare(bool(strtobool((value))), Object.IsSelected) 
   result = True
   return result 	

def Table():
   test.log("inside table")
   result = False
   test.log("this function check after creating the project table is coming.")
   waitForObject(":KoolProg.System.Windows.Controls.Image_Button"),2000 
   tbl=waitForObjectExists(":KoolProg_Table")   
   Object=tbl.nativeObject
   test.compare("True", Object.IsEnabled) 
   result = True 
   return result

def Textbox_Online(): 
   test.log("inside textbox online")
   result = False
   global File_Copy_Textbox
   test.compare(waitForObjectExists(":KoolProg_Table").type, "Table")
   test.compare(waitForObjectExists(":KoolProg_Table").name, "datagridParameters")
  
   window=waitForObject(":KoolProg_Window")
   print("count:%s"% len(window))
   
   ############### right side controller name
   
   name1=getControl(window,"Label","txtProuctName")  
   if(name1 == None):
       print "None"
   else:    
       #test.log("type:%s "% name1["type"])
       #test.log("name:%s "% name1["name"])
       #test.log("text:%s "% name1["text"])
       Controller = (name1["text"]) 
       #test.log("right side controller name is "+Controller)
       #test.log(Controller) 
       #test.log(Controller [0:3]) 
       #test.log(Controller [0:4]) 
       #test.log(Controller [0:6]) 
   
   ################### right side code number or application name
       
   if (Controller [0:3]== "EET"):
       name2=getControl(window,"Label","txtCodeNumber")  
       if(name2 == None):
           print "None"
       else:    
           #test.log("type:%s "% name2["type"])
           #test.log("name:%s "% name2["name"])
           #test.log("text:%s "% name2["text"])
           Code_Number = (name2["text"])
           test.log("right side code number is "+Code_Number)
           #test.log(Code_Number)
   elif ((Controller [0:4]== "ERC1")):
       name2=getControl(window,"Label","txtCodeNumber")  
       if(name2 == None):
           print "None"
       else:    
           #test.log("type:%s "% name2["type"])
           #test.log("name:%s "% name2["name"])
           #test.log("text:%s "% name2["text"])
           Code_Number = (name2["text"])
#            test.log("right side code number is "+Code_Number)
           
       name3=getControl(window,"Label","txtApp")  
       if(name3 == None):
           print "None"
       else:    
#            test.log("type:%s "% name2["type"])
#            test.log("name:%s "% name2["name"])
#            test.log("text:%s "% name2["text"])
           Product_Version = (name3["text"])
#            test.log("application name")
#            test.log (Application)
   else:       
       name2=getControl(window,"Label","txtApp")  
       if(name2 == None):
           print "None"
       else:    
           test.log("type:%s "% name2["type"])
           test.log("name:%s "% name2["name"])
           test.log("text:%s "% name2["text"])
           Application = (name2["text"])
           test.log("application name")
           test.log (Application)
       
   if (Controller[0:3] == "ETC"):
       ETC_App_List = ['STANDARD', 'GDM101', 'DUALBAND102', 'DOUBLEDOOR', 'WINECOOLER', 'MEDICINECOOLER', 'COND101', 'DUALDEFROST']
       count = len(ETC_App_List)
       for i in range (0, count):
           file = Global_Scripts_Path+"\Danfoss.ETC1H."+Application+"_DB.csv"
           file_1= "Result_Sheet_"+Application+".csv"
           tbl=waitForObjectExists(":KoolProg_Table")
           items=tbl.nativeObject.Items
   
           openfile = open(file_1,'wt') 
           writer = csv.writer(openfile)
           writer.writerow(["ParameterName", "DB_Menucode","KP_Menucode","Result" ,"DB_DefaultValue", "KP_DefaultValue", "Result", "DB_MinValue", "KP_MinValue", "Result" ,"DB_MaxValue", "KP_MaxValue", "Result", "DB_Unit", "KP_Unit", "Result", "DB_Info", "KP_Info", "Result"])
           records = testData.dataset(file)
           for rec in records:
               id = testData.field(rec, 0)
               name = testData.field(rec, 1)
               Default = testData.field(rec, 2)
               Min = testData.field(rec, 3)
               Max = testData.field(rec, 4)
               Unit = testData.field(rec, 5) 
               Enum = testData.field(rec, 6)
               Info_Help = testData.field(rec, 7)
               mylist=[]
               if(Enum != ""):
                   for x in Enum.split(','):
                       for y in x.split(':'): 
                           if(y == Default):                        
                               for z in x.split(':'):
                                   mylist.append(z)
                                   Default = z 
               
#                 for i in range (0, items.Count-1):
#                     item=items.at(i)
#                     if (name == item.ParameterName): 
#                         test.log(item.ParameterName)       
#                         MenuCode_Result = test.compare((id).strip(), (item.MenuCode).strip())
#                         MinValue_Result = test.compare((Min).strip(), (item.Minvalue).strip())
#                         MaxValue_Result = test.compare((Max).strip(), (item.Maxvalue).strip())
#                         Unit_Result = test.compare((Unit).strip(), (item.Unit).strip())
#                         Help_Result = test.compare((Info_Help).strip(), (item.Description).strip())
#                         writer.writerow([item.ParameterName,id, item.MenuCode, MenuCode_Result, Default, item.DefaultValue, DefaultValue_Result, Min, item.Minvalue, MinValue_Result, Max, item.Maxvalue, MaxValue_Result, Unit, item.Unit, Unit_Result, Info_Help, item.Description, Help_Result])            
# 

           for i in range (0, items.Count-1):
               item=items.at(i)
               if (name == item.ParameterName):
                   test.log(item.ParameterName)        
                   MenuCode_Result = test.compare((id).strip(), (item.MenuCode).strip())
                   if '.00' in item.DefaultValue:
                           num,dec=item.DefaultValue.split(".")
                           DefaultValue_Result = test.compare((Default).strip(), (num).strip())
                   else:
                           DefaultValue_Result = test.compare((Default).strip(), (item.DefaultValue).strip()) 
                   if '.00' in item.Minvalue:
                           num,dec=item.Minvalue.split(".")
                           MinValue_Result = test.compare((Min).strip(), (num).strip())
                   else:
                           MinValue_Result = test.compare((Min).strip(), (item.Minvalue).strip())
                   if '.00' in item.Maxvalue:
                           num,dec=item.Maxvalue.split(".")
                           MaxValue_Result = test.compare((Max).strip(), (num).strip())
                   else:
                           MaxValue_Result = test.compare((Max).strip(), (item.Maxvalue).strip())
                   Unit_Result = test.compare((Unit).strip(), (item.Unit).strip())
                   Help_Result = test.compare((Info_Help).strip(), (item.Description).strip())
                   writer.writerow([item.ParameterName,id, item.MenuCode, MenuCode_Result, Default, item.DefaultValue, DefaultValue_Result, Min, item.Minvalue, MinValue_Result, Max, item.Maxvalue, MaxValue_Result, Unit, item.Unit, Unit_Result, Info_Help, item.Description, Help_Result])            
                   break          
            
   elif (Controller[0:4] == "ERC2"):
       ERCWS_App_List = ['App0', 'App1', 'App2', 'App3', 'App4', 'App5', 'App6']
       count = len(ERCWS_App_List)
       for i in range (0, count):
           file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_DB.csv"
           file_1= "Result_Sheet_"+Application+".csv"
                   
           tbl=waitForObjectExists(":KoolProg_Table")
           items=tbl.nativeObject.Items
           
           openfile = open(file_1,'wt') 
           writer = csv.writer(openfile)
           writer.writerow(["ParameterName", "DB_Menucode","KP_Menucode","Result" ,"DB_DefaultValue", "KP_DefaultValue", "Result", "DB_MinValue", "KP_MinValue", "Result" ,"DB_MaxValue", "KP_MaxValue", "Result", "DB_Unit", "KP_Unit", "Result", "DB_Info", "KP_Info", "Result"])
   
           records = testData.dataset(file)
           for rec in records:
               id = testData.field(rec, 0)
               name = testData.field(rec, 1)
               if (Application == "App0"):
                   Default = testData.field(rec, 2)
               elif (Application == "App1"):
                   Default = testData.field(rec, 3)
               elif (Application == "App2"):
                   Default = testData.field(rec, 4)
               elif (Application == "App3"):
                   Default = testData.field(rec, 5)
               elif (Application == "App4"):
                   Default = testData.field(rec, 6)
               elif (Application == "App5"):
                   Default = testData.field(rec, 7)
               elif (Application == "App6"):
                   Default = testData.field(rec, 8)
               Min = testData.field(rec, 9)
               Max = testData.field(rec, 10)
               Unit = testData.field(rec, 11) 
               Enum = testData.field(rec, 12)
               Info_Help = testData.field(rec, 13)
               mylist=[]
               if(Enum != ""):
                   for x in Enum.split(','):
                       for y in x.split(':'): 
                           if(y == Default):                        
                               for z in x.split(':'):
                                   mylist.append(z)
                                   Default = z 
               
#                 for i in range (0, items.Count-1):
#                     item=items.at(i)
#                     if (name == item.ParameterName):    
#                         test.log(item.ParameterName)    
#                         MenuCode_Result = test.compare((id).strip(), (item.MenuCode).strip())
#                         DefaultValue_Result = test.compare((Default).strip(), (item.DefaultValue).strip())
#                         MinValue_Result = test.compare((Min).strip(), (item.Minvalue).strip())
#                         MaxValue_Result = test.compare((Max).strip(), (item.Maxvalue).strip())
#                         Unit_Result = test.compare((Unit).strip(), (item.Unit).strip())
#                         Help_Result = test.compare((Info_Help).strip(), (item.Description).strip())
#                         writer.writerow([item.ParameterName,id, item.MenuCode, MenuCode_Result, Default, item.DefaultValue, DefaultValue_Result, Min, item.Minvalue, MinValue_Result, Max, item.Maxvalue, MaxValue_Result, Unit, item.Unit, Unit_Result, Info_Help, item.Description, Help_Result])                        
#         

           for i in range (0, items.Count-1):
               item=items.at(i)
               if (name == item.ParameterName):
                   test.log(item.ParameterName)        
                   MenuCode_Result = test.compare((id).strip(), (item.MenuCode).strip())
                   if '.00' in item.DefaultValue:
                           num,dec=item.DefaultValue.split(".")
                           DefaultValue_Result = test.compare((Default).strip(), (num).strip())
                   else:
                           DefaultValue_Result = test.compare((Default).strip(), (item.DefaultValue).strip()) 
                   if '.00' in item.Minvalue:
                           num,dec=item.Minvalue.split(".")
                           MinValue_Result = test.compare((Min).strip(), (num).strip())
                   else:
                           MinValue_Result = test.compare((Min).strip(), (item.Minvalue).strip())
                   if '.00' in item.Maxvalue:
                           num,dec=item.Maxvalue.split(".")
                           MaxValue_Result = test.compare((Max).strip(), (num).strip())
                   else:
                           MaxValue_Result = test.compare((Max).strip(), (item.Maxvalue).strip())
                   Unit_Result = test.compare((Unit).strip(), (item.Unit).strip())
                   Help_Result = test.compare((Info_Help).strip(), (item.Description).strip())
                   writer.writerow([item.ParameterName,id, item.MenuCode, MenuCode_Result, Default, item.DefaultValue, DefaultValue_Result, Min, item.Minvalue, MinValue_Result, Max, item.Maxvalue, MaxValue_Result, Unit, item.Unit, Unit_Result, Info_Help, item.Description, Help_Result])            
                   break
   
   elif (Controller [0:4] == "ERC1"):
       if (Controller[0:6] == "ERC111"):
           if (Code_Number == "080G3237")| (Code_Number == "080G3247")|(Code_Number == "080G3234"):
               file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_"+Code_Number+"_"+Product_Version+"_DB.csv"
               file_1= "Result_Sheet_"+Code_Number+"-"+Product_Version+".csv"
           else:
               file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_std_DB.csv"
               file_1= "Result_Sheet_"+Code_Number+"-"+Product_Version+".csv"
               
       elif(Controller[0:6] == "ERC112"):
           if ((Code_Number == "080G3202")|(Code_Number == "080G3203")|(Code_Number == "080G3206")|(Code_Number == "080G3207")|(Code_Number == "080G3212")|(Code_Number == "080G3213")|(Code_Number == "080G3216")|(Code_Number == "080G3217"))&(Product_Version == "PV03"):##ALL STD CODE NUMBERS WITH MAINTENANCE DATABSE##
               file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_M_"+Product_Version+"_DB.csv"
               file_1= "Result_Sheet_"+Code_Number+"-"+Product_Version+".csv"
               
           elif (Code_Number == "080G3221")|(Code_Number == "080G3248")|(Code_Number == "080G3276")|(Code_Number == "080G3259"):
               file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_"+Code_Number+"_"+Product_Version+"_DB.csv"
               file_1= "Result_Sheet_"+Code_Number+"-"+Product_Version+".csv"
           
           elif (Code_Number == "080G3408")|(Code_Number == "080G3409")|(Code_Number == "080G3410")|(Code_Number == "080G3414")|(Code_Number == "080G3413")|(Code_Number == "080G3419"): ##SPECIAL CODE NUMBERS##, ##3408 uses 112M DB, but PV version is PV01, hence added here##
               file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_"+Code_Number+"_"+Product_Version+"_DB.csv"
               file_1= "Result_Sheet_"+Code_Number+"-"+Product_Version+".csv"
           
           elif (Code_Number == "080G3220")|(Code_Number == "080G3243"):##COMMON DB_3220##
               file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_080G3220_DB.csv"
               file_1= "Result_Sheet_"+Code_Number+"-"+Product_Version+".csv"
               
           elif (Code_Number == "080G3229")|(Code_Number == "080G3274"):##COMMON DB_3229##
               file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_080G3229_DB.csv"
               file_1= "Result_Sheet_"+Code_Number+"-"+Product_Version+".csv"
               
           elif (Code_Number == "080G3275")|(Code_Number == "080G3239"):##COMMON DB_3275##
               file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_080G3275_DB.csv"
               file_1= "Result_Sheet_"+Code_Number+"-"+Product_Version+".csv"
               
           else:##ALL CODE NUMBERS WITH STANDARD DATABASE##
               file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_std_DB.csv"
               file_1= "Result_Sheet_"+Code_Number+"-"+Product_Version+".csv"
       
       elif (Controller[0:6]== "ERC113"):##ALL STD CODES FOR MAINTENANCE##
           if ((Code_Number == "080G3252")|(Code_Number == "080G3253")|(Code_Number == "080G3406")|(Code_Number == "080G3407"))&(Product_Version == "PV02"):
               file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_M_"+Product_Version+"_DB.csv"
               file_1= "Result_Sheet_"+Code_Number+"-"+Product_Version+".csv"
           
           else:##ALL CODE NUMBERS WITH STANDARD DATABASE##
               file = Global_Scripts_Path+"\Danfoss."+Controller[0:6]+"_std_DB.csv"
               file_1= "Result_Sheet_"+Code_Number+"-"+Product_Version+".csv"

       
       tbl=waitForObjectExists(":KoolProg_Table_3")
       items=tbl.nativeObject.Items
           
       openfile = open(file_1,'wt') 
       writer = csv.writer(openfile)
       writer.writerow(["ParameterName", "DB_Menucode","KP_Menucode","Result" ,"DB_DefaultValue", "KP_DefaultValue", "Result", "DB_MinValue", "KP_MinValue", "Result" ,"DB_MaxValue", "KP_MaxValue", "Result", "DB_Unit", "KP_Unit", "Result", "DB_Info", "KP_Info", "Result"])

       records = testData.dataset(file)
       for rec in records:
           id = testData.field(rec, 0)
           name = testData.field(rec, 1)
           Default = testData.field(rec, 2)
           Min = testData.field(rec, 3)
           Max = testData.field(rec, 4)
           Unit = testData.field(rec, 5) 
           Enum = testData.field(rec, 6)
           Info_Help = testData.field(rec, 7)
           mylist=[]
           if(Enum != ""):
               for x in Enum.split(','):
                   for y in x.split(':'): 
                       if(y == Default):                        
                           for z in x.split(':'):
                               mylist.append(z)
                               Default = z 
           
#             for i in range (0, items.Count-1):
#                 item=items.at(i)
#                 if (name == item.ParameterName):        
#                   test.log(item.ParameterName) 
#                   MenuCode_Result = test.compare((id).strip(), (item.MenuCode).strip())
#                   DefaultValue_Result = test.compare((Default).strip(), (item.DefaultValue).strip())
#                   MinValue_Result = test.compare((Min).strip(), (item.Minvalue).strip())
#                   MaxValue_Result = test.compare((Max).strip(), (item.Maxvalue).strip())
#                   Unit_Result = test.compare((Unit).strip(), (item.Unit).strip())
#                   Help_Result = test.compare((Info_Help).strip(), (item.Description).strip())
#                   writer.writerow([item.ParameterName,id, item.MenuCode, MenuCode_Result, Default, item.DefaultValue, DefaultValue_Result, Min, item.Minvalue, MinValue_Result, Max, item.Maxvalue, MaxValue_Result, Unit, item.Unit, Unit_Result, Info_Help, item.Description, Help_Result])                  
#             

           for i in range (0, items.Count-1):
               item=items.at(i)
               if (name == item.ParameterName):
                   test.log(item.ParameterName)        
                   MenuCode_Result = test.compare((id).strip(), (item.MenuCode).strip())
                   if '.00' in item.DefaultValue:
                           num,dec=item.DefaultValue.split(".")
                           DefaultValue_Result = test.compare((Default).strip(), (num).strip())
                   else:
                           DefaultValue_Result = test.compare((Default).strip(), (item.DefaultValue).strip()) 
                   if '.00' in item.Minvalue:
                           num,dec=item.Minvalue.split(".")
                           MinValue_Result = test.compare((Min).strip(), (num).strip())
                   else:
                           MinValue_Result = test.compare((Min).strip(), (item.Minvalue).strip())
                   if '.00' in item.Maxvalue:
                           num,dec=item.Maxvalue.split(".")
                           MaxValue_Result = test.compare((Max).strip(), (num).strip())
                   else:
                           MaxValue_Result = test.compare((Max).strip(), (item.Maxvalue).strip())
                   Unit_Result = test.compare((Unit).strip(), (item.Unit).strip())
                   Help_Result = test.compare((Info_Help).strip(), (item.Description).strip())
                   writer.writerow([item.ParameterName,id, item.MenuCode, MenuCode_Result, Default, item.DefaultValue, DefaultValue_Result, Min, item.Minvalue, MinValue_Result, Max, item.Maxvalue, MaxValue_Result, Unit, item.Unit, Unit_Result, Info_Help, item.Description, Help_Result])            
                   break
               
   elif (Controller[0:3] == "EET"):
       test.log("inside EET controller")
       # == "080X4010"):
       file = Global_Objects_Path+"\Danfoss."+Controller[0:7]+"_"+Code_Number[0:8]+"_DB.csv"
       file_1= "Textbox_Value_Generation.csv"
       #else:
               #file = Controller[0:6]+"_std_DB.csv"
               #file_1= "Textbox_Value_Generation.csv"
       
       tbl=waitForObjectExists(":KoolProg_Table")
       items=tbl.nativeObject.Items
           
       openfile = open(file_1,'wt')  
       writer = csv.writer(openfile)
       writer.writerow(["ParameterName", "DB_Menucode","KP_Menucode","Result" ,"DB_DefaultValue", "KP_DefaultValue", "Result", "DB_MinValue", "KP_MinValue", "Result" ,"DB_MaxValue", "KP_MaxValue", "Result", "DB_Unit", "KP_Unit", "Result", "DB_Info", "KP_Info", "Result","KP_Text_Old_Value"])

       records = testData.dataset(file)
       for rec in records:
           Menu_Code = testData.field(rec, 0)
           Parameter_Name = testData.field(rec, 1)
           Default = testData.field(rec, 2)
           Min = testData.field(rec, 3)
           Max = testData.field(rec, 4)
           Unit = testData.field(rec, 5) 
           Enum = testData.field(rec, 6)
           Help = testData.field(rec, 7)
           mylist=[]
           if(Enum != ""):
               for x in Enum.split(','):
                   for y in x.split(':'): 
                       if(y == Default):                        
                           for z in x.split(':'):
                               mylist.append(z)
                               Default = z 
           
#             for i in range (0, items.Count-1):
#                 item=items.at(i)
#                 if (name == item.ParameterName):        
#                   test.log(item.ParameterName) 
#                   MenuCode_Result = test.compare((id).strip(), (item.MenuCode).strip())
#                   DefaultValue_Result = test.compare((Default).strip(), (item.DefaultValue).strip())
#                   MinValue_Result = test.compare((Min).strip(), (item.Minvalue).strip())
#                   MaxValue_Result = test.compare((Max).strip(), (item.Maxvalue).strip())
#                   Unit_Result = test.compare((Unit).strip(), (item.Unit).strip())
#                   Help_Result = test.compare((Info_Help).strip(), (item.Description).strip())
#                   writer.writerow([item.ParameterName,id, item.MenuCode, MenuCode_Result, Default, item.DefaultValue, DefaultValue_Result, Min, item.Minvalue, MinValue_Result, Max, item.Maxvalue, MaxValue_Result, Unit, item.Unit, Unit_Result, Info_Help, item.Description, Help_Result])                  
#
           for i in range (0, items.Count):
               item=items.at(i)
               if (Parameter_Name == item.ParameterName):
                   test.log("information of "+item.ParameterName+ " parameter") 
                   #Group_Name_Result = test.compare((Group_Name).strip(), (item.GroupName).strip())
                   #GroupCode_Result = test.compare((Group_Code).strip(), (item.GroupCode).strip())
                   Parameter_Name_Result = test.compare((Parameter_Name).strip(), (item.ParameterName).strip())
                   MenuCode_Result = test.compare((Menu_Code).strip(), (item.MenuCode).strip())
                   if '.00' in item.DefaultValue:
                           num,dec=item.DefaultValue.split(".")
                           DefaultValue_Result = test.compare((Default).strip(), (num).strip())
                   else:
                           DefaultValue_Result = test.compare((Default).strip(), (item.DefaultValue).strip()) 
                   if '.00' in item.Minvalue:
                           num,dec=item.Minvalue.split(".")
                           MinValue_Result = test.compare((Min).strip(), (num).strip())
                   else:
                           MinValue_Result = test.compare((Min).strip(), (item.Minvalue).strip())
                   if '.00' in item.Maxvalue:
                           num,dec=item.Maxvalue.split(".")
                           MaxValue_Result = test.compare((Max).strip(), (num).strip())
                   else:
                           MaxValue_Result = test.compare((Max).strip(), (item.Maxvalue).strip())
                   Unit_Result = test.compare((Unit).strip(), (item.Unit).strip())
                   Help_Result = test.compare((Help).strip(), (item.Description).strip())
                   #test.log("random value is "+str(item.Value)+" for "+item.ParameterName+" parameter" )
                   writer.writerow([Parameter_Name,Menu_Code, item.MenuCode, MenuCode_Result, Default, item.DefaultValue, DefaultValue_Result, Min, item.Minvalue, MinValue_Result, Max, item.Maxvalue, MaxValue_Result, Unit, item.Unit, Unit_Result, Help, item.Description, Help_Result,item.Value])            
               #else:
                   #test.log("DB parameter " +Parameter_Name+"  is not matching with KoolProg parameter " +item.ParameterNam
                   break    
   result = True
   return result

def Textbox_Verification_Online(): ## last function name is Value_Verification_New_ETC
   test.log("inside value verification Textbox")
   
   result = False
   tbl=waitForObjectExists(":KoolProg_Table")
   items=tbl.nativeObject.Items
   #test.log("1")
   file = "Textbox_Value_Generation.csv"
   records = testData.dataset(file)

   file_1 = "Textbox_Value_Verification.csv"
   openfile = open(file_1,'wt')
   writer = csv.writer(openfile)
   #writer.writerow(["ParameterName", "DB_Menucode","KP_Menucode","Result" ,"DB_DefaultValue", "KP_DefaultValue", "Result", "DB_MinValue", "KP_MinValue", "Result" ,"DB_MaxValue", "KP_MaxValue", "Result", "DB_Unit", "KP_Unit", "Result", "DB_Info", "KP_Info", "Result", "KP_Text_Old_Value", "KP_Text_New_Value", "Result"])
   writer.writerow(["DB_Parameter_Name","DB_Menu_Code","KP_Menu_Code","Result_Menu_Code" ,"DB_Default_Value", "KP_Default_Value", "Result_Default_Value", "DB_MinValue", "KP_MinValue", "Result" ,"DB_MaxValue", "KP_MaxValue", "Result", "DB_Unit", "KP_Unit", "Result_Unit", "DB_Info", "KP_Info", "Result","KP_Text_Old_Value", "KP_Text_New_Value","Result"])
   #writer.writerow(["ParameterName", "DB_Menucode","KP_Menucode","Result" ,"DB_DefaultValue", "KP_DefaultValue", "Result", "DB_MinValue", "KP_MinValue", "Result" ,"DB_MaxValue", "KP_MaxValue", "Result", "DB_Unit", "KP_Unit", "Result", "DB_Info", "KP_Info", "Result", "KP_Text_Old_Value", "KP_Text_New_Value","DB_DefaultValue", "Result"])
   
   
   for rec in records:
       #test.log("inside loop")
       
       DB_Parameter_Name = testData.field(rec, 0)
       DB_Menu_Code = testData.field(rec, 1)
       KP_Menu_Code = testData.field(rec, 2)
       Result_Menu_Code = testData.field(rec, 3)
       DB_Default = testData.field(rec, 4)
       KP_Default = testData.field(rec, 5)
       Result_Default = testData.field(rec, 6)
       DB_Min = testData.field(rec, 7)
       KP_Min = testData.field(rec, 8)
       Result_Min = testData.field(rec, 9)
       DB_Max = testData.field(rec, 10)
       KP_Max = testData.field(rec, 11)
       Result_Max = testData.field(rec, 12)
       DB_Unit = testData.field(rec, 13)
       KP_Unit = testData.field(rec, 14) 
       Result_Unit = testData.field(rec, 15)
       DB_Help = testData.field(rec, 16)
       KP_Help = testData.field(rec, 17)
       Result_Help = testData.field(rec, 18) 
       KP_Textbox_Value = testData.field(rec, 19)
       for i in range (0, items.Count):
           item=items.at(i)
           if(item.ParameterName == DB_Parameter_Name):
               #test.log("inside the if")
               if ((item.Datatype == "Enum")|(item.Datatype == "BIT")):
                   writer.writerow([DB_Parameter_Name,DB_Menu_Code,KP_Menu_Code, Result_Menu_Code, DB_Default, KP_Default, Result_Default, DB_Min, KP_Min, Result_Min, DB_Max, KP_Max, Result_Max, DB_Unit, KP_Unit, Result_Unit,DB_Help,KP_Help,Result_Help,KP_Textbox_Value,KP_Textbox_Value,item.Value, result])                      
                   result = True 
               else:
                   Result = test.compare(str(KP_Textbox_Value).strip(), str(item.Value).strip())
                   writer.writerow([DB_Parameter_Name,DB_Menu_Code,KP_Menu_Code, Result_Menu_Code, DB_Default,KP_Default, Result_Default,DB_Min, KP_Min, Result_Min, DB_Max, KP_Max, Result_Max,DB_Unit,KP_Unit, Result_Unit,DB_Help,KP_Help,Result_Help,KP_Textbox_Value,(item.Value), (Result)])            
                   #test.log("2")
                   result = True 

                   #writer.writerow([paramter_name, db_menucode,kp_menucode, result_menu, str(db_default), str(kp_default), result_default, str(db_min), str(kp_min), result_min, str(db_max), str(kp_max), result_max, db_unit, kp_unit, result_unit,db_help, kp_help,result_help, str(kp_textbox_value),db_default,(item.Value), (X)])             
   #if(X == True):
      #result = True
   #else:
    #   result = False
   #test.log("1")
   return result

def Visible(symbolicname, value):
   test.log("inside visible") 
   result = False
   test.log("this function check textbox is visible or not")
   tbl=waitForObjectExists(symbolicname)   
   Object=tbl.nativeObject
   test.compare(value, Object.IsVisible)
   result = True 
   return result

def Text_Checking(symbolicname, value):
   test.log("inside text checking ")
   result = False 
   test.log("check test of combo box")
   tbl=waitForObjectExists(symbolicname)   
   Object=tbl.nativeObject
   test.compare(value, Object.SelectionBoxItem)
   result = True 
   return result 

def Text_DataContext(symbolicname, value):
   test.log("inside text data context ")
   result = False
   test.log("check test of combo box")
   tbl=waitForObjectExists(symbolicname)   
   Object=tbl.nativeObject
   test.compare(value, Object.DataContext.Name) 
   result = True 
   return result 

def Verify_Metric_Unit():
    tbl=waitForObjectExists(":KoolProg_Table")
    Temp_List, Diff_List, Pressure_List = parseCDF()
    MetricCheck(tbl,Temp_List, Diff_List, Pressure_List)

def Verify_Imperial_Unit():
    tbl=waitForObjectExists(":KoolProg_Table")
    Temp_List, Diff_List, Pressure_List = parseCDF()
    ImperialCheck(tbl,Temp_List, Diff_List, Pressure_List)

def MetricCheck(tbl, Temp_List, Diff_List, Pressure_List):
    file = "Default_Unit_Comparison.csv"
    openfile = open(file,'wt') 
    writer_1 = csv.writer(openfile)
    writer_1.writerow(["ParameterName", "CDF_Min", "KP_Min", "Result", "CDF_Max", "KP_Max", "Result", "CDF_Default", "KP_Default", "Result"])       
    
    
    Visible_Param = []
    MinVal_Dict ={}
    MaxVal_Dict = {}
    DefaultVal_Dict = {}
    
    Visible_Param, MinVal_Dict, MaxVal_Dict, DefaultVal_Dict = parseForValues(tbl)
    
    for i in range (0, len(Temp_List)):
        for j in range (0, len(Visible_Param)):
            if (str(Temp_List[i]) == str(Visible_Param[j])):
                Param_Name, Cdf_Min, Min,result, Cdf_Max, Max, result_1, Cdf_Default, Default, result_2 = checkWithCDF(Temp_List[i], MinVal_Dict, MaxVal_Dict, DefaultVal_Dict)
                writer_1.writerow([Param_Name, float(Cdf_Min), float(Min), result, float(Cdf_Max), float(Max), result_1, float(Cdf_Default), float(Default), result_2])
                
    for k in range (0, len(Diff_List)):
        for l in range (0, len(Visible_Param)):
            if (str(Diff_List[k]) == str(Visible_Param[l])):
                Param_Name, Cdf_Min, Min,result, Cdf_Max, Max, result_1, Cdf_Default, Default, result_2 = checkWithCDF(Diff_List[k], MinVal_Dict, MaxVal_Dict, DefaultVal_Dict)
                writer_1.writerow([Param_Name, float(Cdf_Min), float(Min), result, float(Cdf_Max), float(Max), result_1, float(Cdf_Default), float(Default), result_2])
                
    for m in range (0, len(Pressure_List)):
        for n in range (0, len(Visible_Param)):
            if (str(Pressure_List[m]) == str(Visible_Param[n])):
                Param_Name, Cdf_Min, Min,result, Cdf_Max, Max, result_1, Cdf_Default, Default, result_2 = checkWithCDF(Pressure_List[m], MinVal_Dict, MaxVal_Dict, DefaultVal_Dict)
                writer_1.writerow([Param_Name, float(Cdf_Min), float(Min), result, float(Cdf_Max), float(Max), result_1, float(Cdf_Default), float(Default), result_2])
    
def ImperialCheck(tbl, Temp_List, Diff_List, Pressure_List): 
    file_1 = "Imperial_Unit_Comparison.csv"
    openfile = open(file_1,'wt') 
    writer_2 = csv.writer(openfile)
    writer_2.writerow(["ParameterName", "CDF_Min", "KP_Min", "Result", "CDF_Max", "KP_Max", "Result", "CDF_Default", "KP_Default", "Result"])       
    
    Visible_Param = []
    MinVal_Dict ={}
    MaxVal_Dict = {}
    DefaultVal_Dict = {}
    
    Visible_Param, MinVal_Dict, MaxVal_Dict, DefaultVal_Dict = parseForValues(tbl)
    
    for i in range (0, len(Temp_List)):
        for j in range (0, len(Visible_Param)):
            if (str(Temp_List[i]) == str(Visible_Param[j])):
                Param_Name, Cdf_Min, Min,result, Cdf_Max, Max, result_1, Cdf_Default, Default, result_2 = ConvertFromCDF(Temp_List[i], MinVal_Dict, MaxVal_Dict, DefaultVal_Dict)
                writer_2.writerow([Param_Name, float(Cdf_Min), float(Min), result, float(Cdf_Max), float(Max), result_1, float(Cdf_Default), float(Default), result_2])
                
                
    for k in range (0, len(Diff_List)):
        for l in range (0, len(Visible_Param)):
            if (str(Diff_List[k]) == str(Visible_Param[l])):
                Param_Name, Cdf_Min, Min,result, Cdf_Max, Max, result_1, Cdf_Default, Default, result_2 = ConvertFromCDF(Diff_List[k], MinVal_Dict, MaxVal_Dict, DefaultVal_Dict)
                writer_2.writerow([Param_Name, float(Cdf_Min), float(Min), result, float(Cdf_Max), float(Max), result_1, float(Cdf_Default), float(Default), result_2])
                
                
    for m in range (0, len(Pressure_List)):
        for n in range (0, len(Visible_Param)):
            if (str(Pressure_List[m]) == str(Visible_Param[n])):
                Param_Name, Cdf_Min, Min,result, Cdf_Max, Max, result_1, Cdf_Default, Default, result_2 = ConvertFromCDF(Pressure_List[m], MinVal_Dict, MaxVal_Dict, DefaultVal_Dict)
                writer_2.writerow([Param_Name, float(Cdf_Min), float(Min), result, float(Cdf_Max), float(Max), result_1, float(Cdf_Default), float(Default), result_2])
    
    
def ConvertFromCDF(Param_Name,MinVal_Dict, MaxVal_Dict, DefaultVal_Dict):                                                     ##Get CDF values and compare with KP values##
    with codecs.open(findFile("testdata", r"\Latest_CDF\device.jso"),encoding='utf-8') as data_file:
        content = data_file.read()
        content = content.replace(u'\ufeff','') 
        data = json.loads(content)
        EngUnit_Count = len(data["EngUnitTypes"])
        for i in range (0, len(data["Parameters"])):
            if (str(Param_Name) == data["Parameters"][i]["Text"]):
                Cdf_Min = data["Parameters"][i]["Min"]
                Cdf_Max = data["Parameters"][i]["Max"]
                Cdf_Default = data["Parameters"][i]["Default"]
                Unit_Idx = data["Parameters"][i]["EngUnitIdx"] 
                           
                for j in range (0, EngUnit_Count):
                    UniqueID = data["EngUnitTypes"][Unit_Idx]["UniqueID"]
                    Unit_Text = data["EngUnitTypes"][Unit_Idx]["Text"]
                    Offset = data["EngUnitTypes"][Unit_Idx]["Offset"]
                    Factor = data["EngUnitTypes"][Unit_Idx]["Factor"]
                    
                    if (UniqueID == -37):
                        New_Min = (Cdf_Min*1.8)+32
                        New_Max = (Cdf_Max*1.8)+32
                        New_Default = (Cdf_Default*1.8)+32
                        for key in MinVal_Dict:
                            if (str(Param_Name) == str(key)):
                                Min = MinVal_Dict[key]
                                result = test.compare(float(Min), float(New_Min))                            
                       
                        for key in MaxVal_Dict:
                            if (str(Param_Name) == str(key)):
                                Max = MaxVal_Dict[key]
                                result_1 = test.compare(float(Max), float(New_Max))                           
                               
                        for key in DefaultVal_Dict:
                            if (str(Param_Name) == str(key)):
                                Default = DefaultVal_Dict[key]
                                result_2 = test.compare(float(Default), float(New_Default))
                        
                    elif (UniqueID == -38):
                        New_Min = Cdf_Min*1.8
                        New_Max = Cdf_Max*1.8
                        New_Default = Cdf_Default*1.8
                        for key in MinVal_Dict:
                            if (str(Param_Name) == str(key)):
                                Min = MinVal_Dict[key]
                                result = test.compare(float(Min), float(New_Min))                            
                       
                        for key in MaxVal_Dict:
                            if (str(Param_Name) == str(key)):
                                Max = MaxVal_Dict[key]
                                result_1 = test.compare(float(Max), float(New_Max))                           
                               
                        for key in DefaultVal_Dict:
                            if (str(Param_Name) == str(key)):
                                Default = DefaultVal_Dict[key]
                                result_2 = test.compare(float(Default), float(New_Default))
                        
                    elif (UniqueID == -32):
                        New_Min = Cdf_Min*14.504
                        New_Max = Cdf_Max*14.504
                        New_Default = Cdf_Default*14.504
                        for key in MinVal_Dict:
                            if (str(Param_Name) == str(key)):
                                Min = MinVal_Dict[key]
                                result = test.compare(float(Min), float(New_Min))                            
                       
                        for key in MaxVal_Dict:
                            if (str(Param_Name) == str(key)):
                                Max = MaxVal_Dict[key]
                                result_1 = test.compare(float(Max), float(New_Max))                           
                               
                        for key in DefaultVal_Dict:
                            if (str(Param_Name) == str(key)):
                                Default = DefaultVal_Dict[key]
                                result_2 = test.compare(float(Default), float(New_Default))
                    else:
                        break
                                
        return Param_Name, New_Min, Min,result, New_Max, Max, result_1, New_Default, Default, result_2
                      
def checkWithCDF(Param_Name,MinVal_Dict, MaxVal_Dict, DefaultVal_Dict):  ##Get CDF values and compare with KP values##
    with codecs.open(findFile("testdata", r"\Latest_CDF\device.jso"),encoding='utf-8') as data_file:
        content = data_file.read()
        content = content.replace(u'\ufeff','') 
        data = json.loads(content)
        for i in range (0, len(data["Parameters"])):
            if (str(Param_Name) == data["Parameters"][i]["Text"]):
                Cdf_Min = data["Parameters"][i]["Min"]
                Cdf_Max = data["Parameters"][i]["Max"]
                Cdf_Default = data["Parameters"][i]["Default"]
                for key in MinVal_Dict:
                    if (str(Param_Name) == str(key)):
                        Min = MinVal_Dict[key]
                        result = test.compare(float(Min), float(Cdf_Min))                            
                       
                for key in MaxVal_Dict:
                    if (str(Param_Name) == str(key)):
                        Max = MaxVal_Dict[key]
                        result_1 = test.compare(float(Max), float(Cdf_Max))                           
                       
                for key in DefaultVal_Dict:
                    if (str(Param_Name) == str(key)):
                        Default = DefaultVal_Dict[key]
                        result_2 = test.compare(float(Default), float(Cdf_Default))                           
        
        return Param_Name, Cdf_Min, Min,result, Cdf_Max, Max, result_1, Cdf_Default, Default, result_2
                       
def parseForValues(tbl):                                                 ##Parse KP table to get parname, min, max and default values##
    Min_Dict={}
    Max_Dict = {}
    Default_Dict={}
    fieldsTable=[]
      
    items=object.children(tbl)
    for item in items:        
        if(object.properties(item)["type"] ==  "WPFControl"):
            expander=object.children(item)
            for child in expander:                
                if(object.properties(child)["type"] ==  "Expander"):
                    rows=object.children(child)
                    for row in rows:
                        if(object.properties(row)["type"] == "TableRow" and row.nativeObject.IsVisible == True and row.nativeObject.DataContext.IsEnabled == True):
                            fields=object.children(row)
                            fieldName=None        
                            for field in fields:                                                                
                                if(object.properties(field)["type"] == "TableCell" and object.properties(field)["column"] == 4):
                                    fieldName=object.properties(field)["text"]
                                    fieldsTable.append(fieldName) 
                                    Min_Value = field.nativeObject.DataContext.Minvalue
                                    Min_Dict[fieldName] = Min_Value
                                    Max_Value = field.nativeObject.DataContext.Maxvalue
                                    Max_Dict[fieldName] = Max_Value
                                    Def_Value = field.nativeObject.DataContext.DefaultValue
                                    Default_Dict[fieldName] = Def_Value
                                                                                                                                                                                            
    return fieldsTable, Min_Dict, Max_Dict, Default_Dict            

def parseCDF():                                                          ##Get parameters of Temp or pressure units##
    Temp_List=[] 
    Diff_List=[] 
    Pressure_List=[]
    
    with codecs.open(findFile("testdata", r"\Latest_CDF\device.jso"),encoding='utf-8') as data_file:
        content = data_file.read()
        content = content.replace(u'\ufeff','') 
        data = json.loads(content)
        Parameter_Count = len(data["Parameters"])
        EngUnit_Count = len(data["EngUnitTypes"])
        for i in range (0, Parameter_Count):
            Parameter_Name = data["Parameters"][i]["Text"]
            Unit_Idx = data["Parameters"][i]["EngUnitIdx"]
            
            for j in range (0, EngUnit_Count):
                UniqueID = data["EngUnitTypes"][Unit_Idx]["UniqueID"]
                Unit_Text = data["EngUnitTypes"][Unit_Idx]["Text"]
                
                if (UniqueID == -37):
                    Temp_List.append(Parameter_Name)
                elif (UniqueID == -38):
                    Diff_List.append(Parameter_Name)
                elif (UniqueID == -32):
                    Pressure_List.append(Parameter_Name)
                break
                    
    return Temp_List, Diff_List, Pressure_List

def Verify_Metric_Unit_M():
    result = False
    dict_C, dict_K = getTempParam()
    result = True
    
def Verify_Imperial_Unit_M():
    dict_F = getTempFParam()
    Compare (dict_C, dict_K, dict_F)  
    
def getTempFParam():
    dict_F = {}
    tbl=waitForObjectExists(":KoolProg_Table")
    tbl_items = object.children(tbl)
    for WPF in tbl_items:
       if(object.properties(WPF)["type"] == "WPFControl"):
           Expanders=object.children(WPF)
           for Expander in Expanders:                                                                
               if(object.properties(Expander)["type"] == "Expander"): 
                   Rows = object.children(Expander)
                   for Row in Rows:
                       if(object.properties(Row)["type"] == "TableRow"):
                           PValue = Row.nativeObject.DataContext.Value
                           Unit = Row.nativeObject.DataContext.Unit
                           PName = Row.nativeObject.DataContext.ParameterName
                           if ((str(Unit) == "°F")):
                               dict_F[PName] = PValue                    
    return (dict_F)


dict_C = {}
dict_K = {}
def getTempParam():
    global dict_C
    global dict_K
    tbl=waitForObjectExists(":KoolProg_Table")
    tbl_items = object.children(tbl)
    for WPF in tbl_items:
       if(object.properties(WPF)["type"] == "WPFControl"):
           Expanders=object.children(WPF)
           for Expander in Expanders:                                                                
               if(object.properties(Expander)["type"] == "Expander"): 
                   Rows = object.children(Expander)
                   for Row in Rows:
                       if(object.properties(Row)["type"] == "TableRow"):
                           PValue = Row.nativeObject.DataContext.Value
                           Unit = Row.nativeObject.DataContext.Unit
                           PName = Row.nativeObject.DataContext.ParameterName
                           if ((str(Unit) == "°C")):
                               dict_C[PName] = PValue  
                           elif ((str(Unit) == "K")):
                               dict_K[PName] = PValue
    return (dict_C, dict_K)  

def Compare(dict_C, dict_K, dict_F):
    file = "M_Unit_Comparison.csv"
        
    openfile = open(file,'wt') 
    writer = csv.writer(openfile)
    writer.writerow(["ParameterName", "CValue or K Value", "FValue", "Result"])       
    

    for i in dict_C.keys():
        for j in dict_F.keys():
#             test.log(str(dict_C[i]))
#             test.log(str(dict_F[j]))
            if (str(i) == str(j)):
                CValue = (float(dict_C[i])*1.8)+32
                result = test.compare(CValue,dict_F[j])
                writer.writerow([i,CValue, dict_F[j]], result)
    for k in dict_K.keys():
        for l in dict_F.keys():
            if (str(k) == str(l)):
                KValue = (float(dict_K[k]))*1.8
                result_1 = test.compare(KValue,dict_F[l])
                writer.writerow([k,KValue, dict_F[l], result_1])

##FW UPgrade Comparison ##
##START##

def Cbk_File_Icons():
    Home_Button_Enable = waitForObject("{container=':KoolProg_Window' name='btnHome' type='Button'}").enabled
    if (Home_Button_Enable == True):
        Browse_Button_Enabled= waitForObject("{container=':KoolProg_Window' name='btnfilebrowse' type='Button'}").enabled
        test.log("Browse button enabled? - "+str(Browse_Button_Enabled))
        Start_Enabled = waitForObjectExists("{container=':KoolProg_Window' name='btnUpdate' type='Button'}").enabled
        test.log("Start button before selecting file is? - "+str(Start_Enabled))
        Single_Multiple_Enabled = waitForObject("{container=':KoolProg_Window' text='Single or multiple controller programming:' type='Label'}").enabled
        test.log("Single or Multiple controller programming before selecting a file is? - "+str(Single_Multiple_Enabled))


def Open_File_Path(symbolicname, value):
    
    Open_File_Path = waitForObject(symbolicname).text
    Open_File_Path = Open_File_Path.replace("Address: ", "")
    path_result = test.compare(value,Open_File_Path)
    if (path_result == True):
        test.log("Path locations are displaying correctly")
    else:
        test.log("Path locations are NOT displaying correctly - Check for .cbk and .bin")
        box = waitForObject(symbolicname)
        type(box, "<F4>")
        type(box, "<Ctrl+A>")
        type(box, value)
        type(box, "<Return>")
    
def Bin_File_Icons():
    Home_Button_Enable = waitForObject("{container=':KoolProg_Window' name='btnHome' type='Button'}").enabled
    if (Home_Button_Enable == True):
        Browse_Button_Enabled= waitForObject("{container=':KoolProg_Window' name='btnfilebrowse' type='Button'}").enabled
        test.log("Browse button enabled? - "+str(Browse_Button_Enabled))
        Start_Enabled = waitForObjectExists("{container=':KoolProg_Window' name='btnUpdate' type='Button'}").enabled
        test.log("Start button before selecting file is? - "+str(Start_Enabled))
#         Single_Multiple_Enabled = waitForObject("{container=':KoolProg_Window' text='Single or multiple controller programming:' type='Label'}").enabled
#         test.log("Single or Multiple controller programming before selecting a file is? - "+str(Single_Multiple_Enabled))

def CC_Compare_Info():
    window=waitForObject(":KoolProg_Window")
    Home_Button_Enable = waitForObject("{container=':KoolProg_Window' name='btnHome' type='Button'}").enabled
    if (Home_Button_Enable == True):
        name1=getControl(window,"Label","tbProductInfoValue0")  
        if(name1 == None):
            print "None"
        else:
            test.log("Bin File Family is:- " +name1["text"])
   
        name2=getControl(window,"Label","tbProductInfoValue1")  
        if(name2 == None):
            print "None"
        else:    
            test.log("Bin File Code Number is:- " +name2["text"])
        
        name3=getControl(window,"Label","tbProductInfoValue2")  
        if(name3 == None):
            print "None"
        else:    
            test.log("Bin File SW Version is:- " +name3["text"] )

        name4=getControl(window,"Label","txtProuctName")  
        if(name4 == None):
            print "None"
        else:    
            test.log("Controller Family is:- " +name4["text"] )
        
        name5=getControl(window,"Label","txtCodeNumber")  
        if(name5 == None):
            print "None"
        else:    
            test.log("Controller Code Number is:- " +name5["text"] )
            
        name6=getControl(window,"Label","txtApp")  
        if(name6 == None):
            print "None"
        else:    
            test.log("Controller SW Version is:- " +name6["text"] )

def Import_Settings_Project_Name():
    window=waitForObject(":KoolProg_Window")
    Home_Button_Enable = waitForObject("{container=':KoolProg_Window' name='btnHome' type='Button'}").enabled
    if (Home_Button_Enable == True):
        name1=getControl(window,"Label","txtCodeNumber")  
        if(name1 == None):
            print "None"
        else:    
            test.log("Controller Code Number is:- " +name1["text"] )
            Controller_Code_Number = name1["text"]
        
        New_File_Name = waitForObject("{name='txtprojectName' type='Edit'}").text 
        result = test.compare(Controller_Code_Number,New_File_Name)   
        if (result == True):
            test.log("Code number in controller and new file name are equal - "+str(New_File_Name))
        else:
            test.log("Code number in controller and new file name are NOT equal\n Controller Code number is: "+str(Controller_Code_Number)+"\nFIle Name is :"+str(New_File_Name))
        doubleClick(waitForObject("{name='txtprojectName' type='Edit'}"),MouseButton.PrimaryButton)
        type(waitForObject("name='txtprojectName' type='Edit'}"), "This has more than 20 characters 123@#{}]")
        mouseClick(waitForObject(":NewFileName.OK_Button"),MouseButton.PrimaryButton) 
        
        try:    
            mouseClick(":MessageBoxDisplay.YES_Button"), MouseButton.PrimaryButton
            snooze(10)
        except:
           snooze(5)
           
        name2=getControl(window,"Label","txtprojectFilename")  
        if(name2 == None):
            print "None"
        else:    
            test.log("Project_File Code Number is:- " +name2["text"])
            Project_File_Code_Number = name2["text"]
            
        result_1 = test.compare("This has more than 20 characters 123@#{}]"[0:20], Project_File_Code_Number)
        if (result_1 == True):
            test.log("Both project names are equal")
        else:
            test.log("Both project names are NOT equal")

# def Controller_Image():
    
def EET_Desc_Compare(tooltip):
    window=waitForObject(":Newproject_Window")
    name1=getControl(window,"Label","txtDescriptionTemplateA")  
    if(name1 == None):
        print "None"
    else:    
#         test.log("Project_File Code Number is:- " +name1["text"])
        Description = name1["text"]
        tooltip = tooltip.replace(" ","")
        Description = Description.replace(" ", "")
        test.compare(Description, tooltip)



