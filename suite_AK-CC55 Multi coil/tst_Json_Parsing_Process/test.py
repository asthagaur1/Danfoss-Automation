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
    source(findFile("scripts", "global.py"));
    Parse_Json()
    Moving_Files()

def Parse_Json():
    
    with codecs.open((CDF_Path+"\Multi Coil_1.72\cdf\device.jso"),encoding='utf-8') as data_file:
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
        
        with codecs.open((CDF_Path+"\Multi Coil_1.72\cdf\help-en-GB.jso"), encoding='utf-8') as data_file:
            help_content = data_file.read()
            help_content = help_content.replace(u'\ufeff','') 
    #        
            help_file = json.loads(help_content)
            Help_Count = len(help_file["Phrases"])
            test.log("Help count is:" +str(Help_Count))
            
        
        file = "Parsed_Json.csv"
        openfile = open(file,'wt') 
        writer_1 = csv.writer(openfile)
        writer_1.writerow(["Group_Code", "Menu_Code", "Group_Name",  "Name", "PNU", "Default_Value", "Minimum_Value", "Maximum_Value", "Unit", "Scaling", "Datatype", "Enum", "Read_Only", "Help", "Decimals", "Variable_Name", "Visibility_Index", "Visibility_Rule", "Alarm_Parameter_Idx", "Unique_ID", "ItemType", "CopyType", "Enum_Vis_List_Idx", "Group_VisibilityIdx"])       
        
        
        Parameter_File = Global_Scripts_Path+"\Danfoss.Multi Coil_Parameters.csv"
        open_Parameters_File =open(Parameter_File,'wt')           
        writer_2 = csv.writer(open_Parameters_File)
        writer_2.writerow(["Parameter_Index", "ParameterName","Enum"])   
        
        Search_file = Global_Scripts_Path+"\Danfoss.Multi Coil_Search.csv"
        open_Search_file = open(Search_file,'wt')    
        writer_3 = csv.writer(open_Search_file)
        writer_3.writerow(["Group","ParameterName", "MenuCode"]) 
       

#  	INPUT_OUTPUT PARAMETERS

#     for i in range (0, IO_Config_count):
#         Manual_Param_Idx = data["IOConfig"][i]["IOFunctionVarIdx"]
#         
#         
#         Manual_Param_Text = data["Parameters"][Manual_Param_Idx]["Text"]
#         Manual_Param_Enum = data["Parameters"][Manual_Param_Idx]["EnumIdx"]
# 
#         Enum_Limit = data["Enumerations"][Manual_Param_Enum]["Values"]
#         Enum_Limit_count = len(Enum_Limit)
#         for j in range (0, Enum_Limit_count):
#             if (i ==j):
#                 Pin_Name = data["IOConfig"][j]["PinName"]
#                 Output_Func_Value = data["Enumerations"][Manual_Param_Enum]["Values"][j]["Text"]
#                 
#                 writer_1.writerow(["", Pin_Name, "", Output_Func_Value, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""])

#   ALARM PARAMETERS

#     for a in range (0, Alarm_List_count):
#         Alarm_Name = data["Alarms"][a]["Text"]
#         if (Alarm_Name[0:3] == "---"):
#             Alarm_Name = Alarm_Name.replace("---", "")
#         Alarm_Menu_Code = data["Alarms"][a]["Label"]
#         if (Alarm_Menu_Code[0:3] == "---"):
#             Alarm_Menu_Code = Alarm_Menu_Code.replace("---", "")
#         Alarm_PNU = data["Alarms"][a]["Vid"]
#         Alarm_Unique_ID = data["Alarms"][a]["UniqueID"]
# #             Alarm_Unique_ID = data["Alarms"][a]["UniqueID"]
#         Alarm_Unique_ID = "Id_" +str(Alarm_Unique_ID)+ "_Alarm"
#         
#         
#         AlarmParameter_Idx_List = []
#         AlarmParameter = data["Alarms"][a]["AlarmValuesItemIdx"]
#         AlarmParameter_Count = len(AlarmParameter)
#         for b in range(0, AlarmParameter_Count):
#             AlarmParameter_Idx = AlarmParameter[b]["Index"]  
#             AlarmParameter_Idx = "Id_"+str(AlarmParameter_Idx)
#             AlarmParameter_Idx_List.append(str(AlarmParameter_Idx))
# #                 AlarmParameter_Idx_List.append(str(AlarmParameter_UniqueID))
#         Alarm_Parameter_Id =  ','.join(AlarmParameter_Idx_List)
#         
#         Alarm_Visibility_Idx = data["Alarms"][a]["VisibilityIdx"]
#         Alarm_Visibility_Idx = str(Alarm_Visibility_Idx)
# #                                 test.log (Visibility_Idx)
# 
#         Unique_ID = data["Alarms"][a]["UniqueID"]
# 
#         ####ALARM VISIBILITY####
#         with open("C:\\gitworkspace\\KoolProg-TestAutomation\\Master_Functions\\SourceCode\\Dependent_Files\\Latest_CDF\\visib.js", "r") as visibility_file:
#             vis = visibility_file.readlines()
#             vis = str(vis)
#             array = []
#             for x in vis.split('\\n'):
#                 array.append(x)
#     #             print (x)
#                 myItem = "RuleId"
#                 if myItem in x:
#                     array_1 = []
#                     for y in x.split('return'):
#                         if "RuleId" in y: 
#                             Id = ''.join(filter(lambda x: x.isdigit(),y))
#                            
#                         if "GetVar" in y:
#                             visibleText= ""
#                             y = y.replace(";", "")
#                             for z in y.split(" "):
#                                 if "GetVar(" in z:
#                                     Rule = z.replace("GetVar(", "").replace(")", "")
# 
#                                     if "(" in Rule:
#                                         Rule = Rule.replace("(", "")
#                                         for i in range (0, Alarm_List_count):
#                                             Rule_Idx = data["Alarms"][i]["Idx"]
#                                             if (Rule == str(Rule_Idx)):
#                                                 Rule_Idx_ID = data["Alarms"][Rule_Idx]["UniqueID"]
#                                                 visibleText += "(Id_"+str(Rule_Idx_ID)+" "
#                                     else:
#                                         for i in range (0, Alarm_List_count):
#                                             Rule_Idx = data["Alarms"][i]["Idx"]
#                                             if (Rule == str(Rule_Idx)):
#                                                 Rule_Idx_ID = data["Alarms"][Rule_Idx]["UniqueID"]
#                                                 visibleText += "Id_"+str(Rule_Idx_ID)+" " 
#                                 
#                                 else:
#                                     visibleText += z+" "
#                             
#                                     
#                             Visibility =  visibleText.strip()      
#                         if "GetVar" not in y:
#                             if "0" in y:
#                                 Visibility = "0"
#                             else:
#                                 Visibility = "" 
#                             
#                     if (Id == Alarm_Visibility_Idx):
#                         Alarm_Visibility_Rule = Visibility
# 
#         writer_1.writerow(["", Alarm_Menu_Code, "", Alarm_Name, Alarm_PNU, "", "", "", "", "", "", "", "", "", "", Alarm_Unique_ID, Alarm_Visibility_Idx, Alarm_Visibility_Rule, Alarm_Parameter_Id, Unique_ID])
#         writer_2.writerow([Alarm_Unique_ID, Alarm_Name, ""])               
#         writer_3.writerow(["", Alarm_Name, Alarm_Menu_Code])      
                            
    Main_Group = data["Groups"][0]["Text"]
    Main_Items = data["Groups"][0]["Items"]
    Idx_array =[]
    Idx_counter = ""
     
    ##MAIN MENU##
    
    Main_Items_Count = len(Main_Items)   
    print ("No of parameters"+str(Main_Items_Count))          
    for i in range (0, Main_Items_Count):
         Index = Main_Items[i]["Index"]
         Item_Type = Main_Items[i]["ItemType"]
         
         ##SUB GROUP1##
         
         if (Item_Type == "G"):
                 #for Index in range (1, Groups_List_count):
            SG = data["Groups"][Index]["Text"]
            SG_Items = data["Groups"][Index]["Items"] 
            SG_Visibility_Idx = data["Groups"][Index]["VisibilityIdx"] 
            #print SG_Items
            SG_Items_count = len(SG_Items)
            #print (Main_Group+"|"+SG)
            
            for j in range (0, SG_Items_count):
                SG_Index = SG_Items[j]["Index"]
                SG_ItemType = SG_Items[j]["ItemType"]
                
                ##SUB GROUP2##
                
                if (SG_ItemType == "G"):
                    SG_2 = data["Groups"][SG_Index]["Text"]
                    SG_2_Items = data["Groups"][SG_Index]["Items"]
                    SG_2_Visibility_Idx = data["Groups"][SG_Index]["VisibilityIdx"] 
                    SG_2_Items_count = len(SG_2_Items)
                    
                    for k in range (0, SG_2_Items_count):
                        SG_2_Index = SG_2_Items[k]["Index"]
                        SG_2_ItemType = SG_2_Items[k]["ItemType"]
                        
                        ##SUB GROUP3##
                        
                        if (SG_2_ItemType == "G"):
                            SG_3 = data["Groups"][SG_2_Index]["Text"]
                            SG_3_Items = data["Groups"][SG_2_Index]["Items"]
                            SG_3_Visibility_Idx = data["Groups"][SG_2_Index]["VisibilityIdx"] 
                            SG_3_Items_count = len(SG_3_Items)
                            
                            for l in range (0, SG_3_Items_count):
                                SG_3_Index = SG_3_Items[l]["Index"]
                                SG_3_ItemType = SG_3_Items[l]["ItemType"]
                                
                                if (SG_3_ItemType == "P"):
                                    Parameter_Name = data["Parameters"][SG_3_Index]["Text"]
                                    if (Parameter_Name[0:3] == "---"):
                                        Parameter_Name = Parameter_Name.replace("---", "")
                                        
                                    Parameter_Menu_Code = data["Parameters"][SG_3_Index]["Label"]
                                    if (Parameter_Menu_Code[0:3] == "---"):
                                        Parameter_Menu_Code = Parameter_Menu_Code.replace("---", "")
                                        
                                        
                                    Decimals = data["Parameters"][SG_3_Index]["Decimals"] 
                                    Default_Value = data["Parameters"][SG_3_Index]["Default"]
                                    #MenuCode = data["Parameters"][k]["Label"]
                                    Maximum_Val = data["Parameters"][SG_3_Index]["Max"]
                                    Minimum_Val = data["Parameters"][SG_3_Index]["Min"]
                                    Enum_Index = data["Parameters"][SG_3_Index]["EnumIdx"] 
                                    AccLevel = data["Parameters"][SG_3_Index]["AccLevelR"]
                                    Storage_Type = data["Parameters"][SG_3_Index]["StorageType"]
                                    Datatype_Scaling = data["Parameters"][SG_3_Index]["Scale10E"]
                                    PNU = data["Parameters"][SG_3_Index]["Vid"]
                                    Help_Index = data["Parameters"][SG_3_Index]["HelpTextIdx"]
        #                                 Items_Unique_Idx = data["Parameters"][SG_2_Index]["UniqueID"]
                                    Unit_Type = data["Parameters"][SG_3_Index]["EngUnitIdx"]
                                    
                                    Items_Unique_Idx = data["Parameters"][SG_3_Index]["UniqueID"]
                                    Items_Unique_Idx = str(Items_Unique_Idx)
                                    Items_Unique_Idx = "Id_"+Items_Unique_Idx
                                    
                                    ItemType = data["Parameters"][SG_3_Index]["ItemType"]
                                    CopyType = data["Parameters"][SG_3_Index]["CopyType"]
                                    
                                    Unique_ID = data["Parameters"][SG_3_Index]["UniqueID"]
        
                                    Visibility_Idx = data["Parameters"][SG_3_Index]["VisibilityIdx"]
                                    Visibility_Idx = str(Visibility_Idx)
        #                                 test.log (Visibility_Idx)
        
        
                                    ####VISIBILITY####
                                    with open((CDF_Path+r"\Multi Coil_1.72\cdf\visib.js")) as visibility_file:
                                        vis = visibility_file.readlines()
                                        vis = str(vis)
                                        array = []
                                        for x in vis.split('\\n'):
                                            array.append(x)
                                            myItem = "RuleId"
                                            if myItem in x:
                                                array_1 = []
                                                for y in x.split('return'):
                                                    if "RuleId" in y: 
                                                        Id = ''.join(filter(lambda x: x.isdigit(),y))
                                                       
                                                    if "GetVar" in y:
                                                        visibleText= ""
                                                        y = y.replace(";", "").replace("&&", "and")
                                                        visibleText += y 
                                                                
                                                        Visibility =  visibleText.strip()      
                                                    if "GetVar" not in y:
                                                        y = y.replace(";", "")
                                                        if "0" in y:
                                                            Visibility = "0"
                                                        else:
                                                            Visibility = y
                                                        
                                                if (Id == Visibility_Idx):
                                                    Visibility_Rule = Visibility.strip()
                                    
                                    
                                    ####HELP#### 
                                    test.log("Parameter is: " +str(Parameter_Name))
        #                             test.log("Help_Index is: " +str(Help_Index))                                    
                                    for x in range(0,Help_Count):
                                        if (str(x) == str(Help_Index)):
        #                                     test.log("Value of x is: "+str(x))
                                            Help_Info = help_file["Phrases"][Help_Index]
        
                                        elif (Help_Index == -1) :
                                            Help_Info = ""
                                    ####DATATYPE####
                                    Data_Type = ""
                                    Enum_Value=""
                                    Enum_Vis_List = []
                                    if (((Storage_Type == 4) | (Storage_Type == 3)|(Storage_Type == 2)) & (Enum_Index == -1)):
                                        Data_Type = "INT"
                                        Maximum_Val = Maximum_Val
                                        Minimum_Val = Minimum_Val
                                        Default_Value = Default_Value
                                        
                                        
                                    elif ((Storage_Type == 7) & (Enum_Index == -1)):
                                        Data_Type = "Float"
                                        Maximum_Val = str(Maximum_Val)
                                        Minimum_Val = str(Minimum_Val)
                                        Default_Value = str(Default_Value)
                                        
                                        
                                    elif ((Storage_Type == 9) & (Enum_Index == -1)): 
                                        Data_Type = "String"
                                        Maximum_Val = str(Maximum_Val)
                                        Minimum_Val = str(Minimum_Val)
                                        Default_Value = str(Default_Value)
                                    ####ENUM#### 
                                    elif ((Enum_Index != -1)):
                                        Data_Type == "Enum" 
                                        Enum_Vis_List =[]  
                                        
                                        for j in range (0, Enum_List_count):
                                            if Enum_Index == Enum_List[j]["Idx"]:
                                                Enum_Value_List =  (Enum_List[j]["Values"])
                                                Enum_Value_List_count = len(Enum_Value_List)
                                                
                                                for num in range (0, Enum_Value_List_count):
                                                    Vis = Enum_Value_List[num]["VisibilityIdx"]
                                                    if (Vis != 0):
                                                        Enum_Val = Enum_Value_List[num]["Text"]
                                                        Enum_Vis = str(Enum_Val)+":"+str(Vis) 
                                                        Enum_Vis_List.append(Enum_Vis)                                                  
                                             
                                                Enum_Text_List = []
                                                for k in range(0,Enum_Value_List_count) :
                                                    Enum_Text = Enum_Value_List[k]["Text"]
                                                    Enum_Text = str(Enum_List[j]["Values"][k]["Value"])+":"+Enum_Text
                                                    Enum_Text_List.append(Enum_Text)
                                                Enum_Value =  ','.join(Enum_Text_List)
                                           
                                                mylist=[]
                                                if(Enum_Index != "-1"):
                                                    for x in Enum_Value.split(','):
                                                        for y in x.split(':'): 
                                                            if(y == Default_Value):                        
                                                                for z in x.split(':'):
                                                                    mylist.append(z)
                                                                    Default_Value = z
                                                if(Enum_Index != "-1"):
                                                    for x in Enum_Value.split(','):
                                                        for y in x.split(':'): 
                                                            if(y == Maximum_Val):                        
                                                                for z in x.split(':'):
                                                                    mylist.append(z)
                                                                    Maximum_Val = z
                                                if(Enum_Index != "-1"):
                                                    for x in Enum_Value.split(','):
                                                        for y in x.split(':'): 
                                                            if(y == Minimum_Val):                        
                                                                for z in x.split(':'):
                                                                    mylist.append(z)
                                                                    Minimum_Val = z
                                                        #print value                       
                                    else: 
                                        print("missing parameter-"+Parameter_Name)
            
                                     
                                    ####UNIT####          
                                    
                                    Unit_Value=""
                                    
        #                                 Unit_Value= Unit_List[i]["Text"]
                                     
                                    for l in range (0, Unit_List_count):
                                        if (Unit_Type == Unit_List[l]["Idx"]):
                                            Unit_Value = Unit_List[l]["Text"]   
                                            
                                     
                                    if (AccLevel == 0):
                                        Read_Only = "0"
                                    else:
                                        Read_Only = "1"    
                                        
                                    
                                    writer_1.writerow(["", Parameter_Menu_Code, SG+"-"+SG_2+"-"+SG_3 ,  Parameter_Name, PNU, Default_Value, Minimum_Val, Maximum_Val, Unit_Value, Datatype_Scaling, Data_Type, Enum_Value, Read_Only, Help_Info, Decimals, Items_Unique_Idx, Visibility_Idx, Visibility_Rule, "", Unique_ID, ItemType, CopyType, Enum_Vis_List, SG_3_Visibility_Idx])

                                    writer_2.writerow([Items_Unique_Idx, Parameter_Name, Enum_Value]) 
                                    
                                    writer_3.writerow([SG+"-"+SG_2+"-"+SG_3, Parameter_Name,Parameter_Menu_Code])
                      
                                
                        ##ALARM DESTINATIONS##
                        
                        elif (SG_2_ItemType == "A"):
                            Parameter_Name = data["Alarms"][SG_2_Index]["Text"]
                            if (Parameter_Name[0:3] == "---"):
                                Parameter_Name = Parameter_Name.replace("---", "")
                            Parameter_Menu_Code = data["Alarms"][SG_2_Index]["Label"]
                            if (Parameter_Menu_Code[0:3] == "---"):
                                Parameter_Menu_Code = Parameter_Menu_Code.replace("---", "")
                                
                            Decimals = "" 
                            Default_Value = ""
                            #MenuCode = data["Parameters"][k]["Label"]
                            Maximum_Val = ""
                            Minimum_Val = ""
                            Enum_Index = ""
                            AccLevel = ""
                            Datatype_Scaling = ""
                            PNU = data["Alarms"][SG_2_Index]["Vid"]
                            Help_Index = data["Alarms"][SG_2_Index]["HelpTextIdx"]
                            ###HELP####
                            test.log("Parameter is: " +str(Parameter_Name))
        #                             test.log("Help_Index is: " +str(Help_Index))                                    
                            for x in range(0,Help_Count):
                                if (str(x) == str(Help_Index)):
#                                     test.log("Value of x is: "+str(x))
                                    Help_Info = help_file["Phrases"][Help_Index]

                                elif (Help_Index == -1) :
                                    Help_Info = ""
#                                 Items_Unique_Idx = data["Parameters"][SG_2_Index]["UniqueID"]
                            Unit_Type = ""
                            
                            Items_Unique_Idx = data["Alarms"][SG_2_Index]["UniqueID"]
                            Items_Unique_Idx = str(Items_Unique_Idx)
                            Items_Unique_Idx = "Id_"+Items_Unique_Idx
                            
                            AlarmsValuesItemIdx = data["Alarms"][SG_2_Index]["AlarmValuesItemIdx"]
#                             for av in range (0, len(AlarmsValuesItemIdx)):
#                                 ItemType = AlarmsValuesItemIdx[av]["ItemType"]
                            
                            ItemType = "R" ###BECAUSE ALARMS ARE READONLY###
                            CopyType = "N" ###BECAUSE ALARMS SHOULD NOT BE COPIED###
                            Enum_Vis_List =[]
                            
                            
                            Unique_ID = data["Alarms"][SG_2_Index]["UniqueID"]

                            Visibility_Idx = data["Alarms"][SG_2_Index]["VisibilityIdx"]
                            Visibility_Idx = str(Visibility_Idx)   
                             
                            if (AccLevel == 0):
                                Read_Only = "0"
                            else:
                                Read_Only = "1"  
                                
                            writer_1.writerow(["", Parameter_Menu_Code, SG+"-"+SG_2 ,  Parameter_Name, PNU, Default_Value, Minimum_Val, Maximum_Val, Unit_Value, Datatype_Scaling, Data_Type, Enum_Value, Read_Only, Help_Info, Decimals, Items_Unique_Idx, Visibility_Idx, Visibility_Rule, "", Unique_ID, ItemType, CopyType, Enum_Vis_List, SG_2_Visibility_Idx])

                            writer_2.writerow([Items_Unique_Idx, Parameter_Name, Enum_Value]) 
                            
                            writer_3.writerow([SG+"-"+SG_2, Parameter_Name,Parameter_Menu_Code])  
                            
                        
                        ##PARAMETERS##
                        
                        elif (SG_2_ItemType == "P"):
                            Parameter_Name = data["Parameters"][SG_2_Index]["Text"]
                            if (Parameter_Name[0:3] == "---"):
                                Parameter_Name = Parameter_Name.replace("---", "")
                                
                            Parameter_Menu_Code = data["Parameters"][SG_2_Index]["Label"]
                            if (Parameter_Menu_Code[0:3] == "---"):
                                Parameter_Menu_Code = Parameter_Menu_Code.replace("---", "")
                            
                               
                            Decimals = data["Parameters"][SG_2_Index]["Decimals"] 
                            Default_Value = data["Parameters"][SG_2_Index]["Default"]
                            #MenuCode = data["Parameters"][k]["Label"]
                            Maximum_Val = data["Parameters"][SG_2_Index]["Max"]
                            Minimum_Val = data["Parameters"][SG_2_Index]["Min"]
                            Enum_Index = data["Parameters"][SG_2_Index]["EnumIdx"] 
                            AccLevel = data["Parameters"][SG_2_Index]["AccLevelR"]
                            Storage_Type = data["Parameters"][SG_2_Index]["StorageType"]
                            Datatype_Scaling = data["Parameters"][SG_2_Index]["Scale10E"]
                            PNU = data["Parameters"][SG_2_Index]["Vid"]
                            Help_Index = data["Parameters"][SG_2_Index]["HelpTextIdx"]
#                                 Items_Unique_Idx = data["Parameters"][SG_2_Index]["UniqueID"]
                            Unit_Type = data["Parameters"][SG_2_Index]["EngUnitIdx"]
                            
                            Items_Unique_Idx = data["Parameters"][SG_2_Index]["UniqueID"]
                            Items_Unique_Idx = str(Items_Unique_Idx)
                            Items_Unique_Idx = "Id_"+Items_Unique_Idx
                            
                            ItemType = data["Parameters"][SG_2_Index]["ItemType"]
                            CopyType = data["Parameters"][SG_2_Index]["CopyType"]
                            
                            Unique_ID = data["Parameters"][SG_2_Index]["UniqueID"]

                            Visibility_Idx = data["Parameters"][SG_2_Index]["VisibilityIdx"]
                            Visibility_Idx = str(Visibility_Idx)
#                                 test.log (Visibility_Idx)


                            ####VISIBILITY####
                            with open((CDF_Path+r"\Multi Coil_1.72\cdf\visib.js")) as visibility_file:
                                vis = visibility_file.readlines()
                                vis = str(vis)
                                array = []
                                for x in vis.split('\\n'):
                                    array.append(x)
                                    myItem = "RuleId"
                                    if myItem in x:
                                        array_1 = []
                                        for y in x.split('return'):
                                            if "RuleId" in y: 
                                                Id = ''.join(filter(lambda x: x.isdigit(),y))
                                               
                                            if "GetVar" in y:
                                                visibleText= ""
                                                y = y.replace(";", "").replace("&&", "and")
                                                visibleText += y 
                                                        
                                                Visibility =  visibleText.strip()      
                                            if "GetVar" not in y:
                                                y = y.replace(";", "")
                                                if "0" in y:
                                                    Visibility = "0"
                                                else:
                                                    Visibility = y
                                                
                                        if (Id == Visibility_Idx):
                                            Visibility_Rule = Visibility.strip()
                            
                            
                            ####HELP#### 
                            test.log("Parameter is: " +str(Parameter_Name))
#                             test.log("Help_Index is: " +str(Help_Index))                                    
                            for x in range(0,Help_Count):
                                if (str(x) == str(Help_Index)):
#                                     test.log("Value of x is: "+str(x))
                                    Help_Info = help_file["Phrases"][Help_Index]

                                elif (Help_Index == -1) :
                                    Help_Info = ""
                            ####DATATYPE####
                            Data_Type = ""
                            Enum_Value=""
                            Enum_Vis_List = []
                            
                            if (((Storage_Type == 4) | (Storage_Type == 3)|(Storage_Type == 2)) & (Enum_Index == -1)):
                                Data_Type = "INT"
                                Maximum_Val = Maximum_Val
                                Minimum_Val = Minimum_Val
                                Default_Value = Default_Value
                            elif ((Storage_Type == 7) & (Enum_Index == -1)):
                                Data_Type = "Float"
                                Maximum_Val = str(Maximum_Val)
                                Minimum_Val = str(Minimum_Val)
                                Default_Value = str(Default_Value)
                                
                            elif ((Storage_Type == 9) & (Enum_Index == -1)): 
                                Data_Type = "String"
                                Maximum_Val = str(Maximum_Val)
                                Minimum_Val = str(Minimum_Val)
                                Default_Value = str(Default_Value) 
                                
                            
                            ####ENUM#### 
                            elif ((Enum_Index != -1)):
                                Data_Type == "Enum" 
                                Enum_Vis_List=[]  
                                for j in range (0, Enum_List_count):
                                    if Enum_Index == Enum_List[j]["Idx"]:
                                        Enum_Value_List =  (Enum_List[j]["Values"])
                                        Enum_Value_List_count = len(Enum_Value_List)
                                        
                                        for num in range (0, Enum_Value_List_count):
                                            Vis = Enum_Value_List[num]["VisibilityIdx"]
                                            if (Vis != 0):
                                                Enum_Val = Enum_Value_List[num]["Text"]
                                                Enum_Vis = str(Enum_Val)+":"+str(Vis)  
                                                Enum_Vis_List.append(Enum_Vis)
                                     
                                        Enum_Text_List = []
                                        for k in range(0,Enum_Value_List_count) :
                                            Enum_Text = Enum_Value_List[k]["Text"]
                                            Enum_Text = str(Enum_List[j]["Values"][k]["Value"])+":"+Enum_Text
                                            Enum_Text_List.append(Enum_Text)
                                        Enum_Value =  ','.join(Enum_Text_List)
                                   
                                        mylist=[]
                                        if(Enum_Index != "-1"):
                                            for x in Enum_Value.split(','):
                                                for y in x.split(':'): 
                                                    if(y == Default_Value):                        
                                                        for z in x.split(':'):
                                                            mylist.append(z)
                                                            Default_Value = z
                                        if(Enum_Index != "-1"):
                                            for x in Enum_Value.split(','):
                                                for y in x.split(':'): 
                                                    if(y == Maximum_Val):                        
                                                        for z in x.split(':'):
                                                            mylist.append(z)
                                                            Maximum_Val = z
                                        if(Enum_Index != "-1"):
                                            for x in Enum_Value.split(','):
                                                for y in x.split(':'): 
                                                    if(y == Minimum_Val):                        
                                                        for z in x.split(':'):
                                                            mylist.append(z)
                                                            Minimum_Val = z
                                                #print value                       
                            else: 
                                print("missing parameter-"+Parameter_Name)
    
                             
                            ####UNIT####          
                            
                            Unit_Value=""
                            
#                                 Unit_Value= Unit_List[i]["Text"]
                             
                            for l in range (0, Unit_List_count):
                                if (Unit_Type == Unit_List[l]["Idx"]):
                                    Unit_Value = Unit_List[l]["Text"]   
                                    
                             
                            if (AccLevel == 0):
                                Read_Only = "0"
                            else:
                                Read_Only = "1"
                            
                            
                            writer_1.writerow(["", Parameter_Menu_Code, SG+"-"+SG_2 ,  Parameter_Name, PNU, Default_Value, Minimum_Val, Maximum_Val, Unit_Value, Datatype_Scaling, Data_Type, Enum_Value, Read_Only, Help_Info, Decimals, Items_Unique_Idx, Visibility_Idx, Visibility_Rule, "", Unique_ID, ItemType, CopyType, Enum_Vis_List, SG_2_Visibility_Idx])

                            writer_2.writerow([Items_Unique_Idx, Parameter_Name, Enum_Value]) 
                            
                            writer_3.writerow([SG+"-"+SG_2, Parameter_Name,Parameter_Menu_Code])
              
                            #print (Main_Group+"|"+SG+"|"+SG_2+"|"+Parameter_Name)
                            
                elif (SG_ItemType == "P"):
                    SG_2 = ""
                    Parameter_Name = data["Parameters"][SG_Index]["Text"]
                    if (Parameter_Name[0:3] == "---"):
                        Parameter_Name = Parameter_Name.replace("---", "")
                        
                    Parameter_Menu_Code = data["Parameters"][SG_Index]["Label"]
                    if (Parameter_Menu_Code[0:3] == "---"):
                        Parameter_Menu_Code = Parameter_Menu_Code.replace("---", "") 
                                              
                    Decimals = data["Parameters"][SG_Index]["Decimals"] 
                    Default_Value = data["Parameters"][SG_Index]["Default"]
                    #MenuCode = data["Parameters"][k]["Label"]
                    Maximum_Val = data["Parameters"][SG_Index]["Max"]
                    Minimum_Val = data["Parameters"][SG_Index]["Min"]
                    Enum_Index = data["Parameters"][SG_Index]["EnumIdx"] 
                    AccLevel = data["Parameters"][SG_Index]["AccLevelR"]
                    Storage_Type = data["Parameters"][SG_Index]["StorageType"]
                    Datatype_Scaling = data["Parameters"][SG_Index]["Scale10E"]
                    PNU = data["Parameters"][SG_Index]["Vid"]
                    Help_Index = data["Parameters"][SG_Index]["HelpTextIdx"]
#                         Items_Unique_Idx = data["Parameters"][SG_Index]["UniqueID"]
                    Unit_Type = data["Parameters"][SG_Index]["EngUnitIdx"]
                    
                    Items_Unique_Idx = data["Parameters"][SG_Index]["UniqueID"]
                    Items_Unique_Idx = str(Items_Unique_Idx)
                    Items_Unique_Idx = "Id_"+Items_Unique_Idx
                    
                    ItemType = data["Parameters"][SG_Index]["ItemType"]
                    CopyType = data["Parameters"][SG_Index]["CopyType"]
                    
                    Unique_ID = data["Parameters"][SG_Index]["UniqueID"]
        
                    Visibility_Idx = data["Parameters"][SG_Index]["VisibilityIdx"]
                    Visibility_Idx = str(Visibility_Idx)
                    ####VISIBILITY####
                    with open((CDF_Path+r"\Multi Coil_1.72\cdf\visib.js")) as visibility_file:
                        vis = visibility_file.readlines()
                        vis = str(vis)
                        array = []
                        for x in vis.split('\\n'):
                            array.append(x)
                            myItem = "RuleId"
                            if myItem in x:
                                array_1 = []
                                for y in x.split('return'):
                                    if "RuleId" in y: 
                                        Id = ''.join(filter(lambda x: x.isdigit(),y))
                                       
                                    if "GetVar" in y:
                                        visibleText= ""
                                        y = y.replace(";", "").replace("&&", "and")
                                        visibleText += y 
                                                
                                        Visibility =  visibleText.strip()      
                                    if "GetVar" not in y:
                                        y = y.replace(";", "")
                                        if "0" in y:
                                            Visibility = "0"
                                        else:
                                            Visibility = y
                                        
                                if (Id == Visibility_Idx):
                                    Visibility_Rule = Visibility.strip()
                    
                    
                    ####HELP####
                    test.log("Parameter is: " +str(Parameter_Name))
#                     test.log("Help_Index is: " +str(Help_Index))                                    
                    for x in range(0,Help_Count):
                        if (str(x) == str(Help_Index)):
#                             test.log("Value of x is: "+str(x))
                            Help_Info = help_file["Phrases"][Help_Index]
                        elif (Help_Index == -1) :
                            Help_Info = ""
                     
                    ####DATATYPE####
                    Data_Type = ""
                    Enum_Value=""
                    Enum_Vis_List =[]
                    
                    if (((Storage_Type == 4) | (Storage_Type == 3)|(Storage_Type == 2)) & (Enum_Index == -1)):
                        Data_Type = "INT"
                        Maximum_Val = Maximum_Val
                        Minimum_Val = Minimum_Val
                        Default_Value = Default_Value
                    elif ((Storage_Type == 7) & (Enum_Index == -1)):
                        Data_Type = "Float"
                        Maximum_Val = str(Maximum_Val)
                        Minimum_Val = str(Minimum_Val)
                        Default_Value = str(Default_Value)
                        
                    elif ((Storage_Type == 9) & (Enum_Index == -1)): 
                        Data_Type = "String"
                        Maximum_Val = str(Maximum_Val)
                        Minimum_Val = str(Minimum_Val)
                        Default_Value = str(Default_Value) 
                        
                    elif ((Enum_Index != -1)):
                        Data_Type == "Enum"
                        Enum_Vis_List=[]
                        
                        for j in range (0, Enum_List_count):
                            if Enum_Index == Enum_List[j]["Idx"]:
                                Enum_Value_List =  (Enum_List[j]["Values"])
                                Enum_Value_List_count = len(Enum_Value_List)
                                
                                
                                for num in range (0, Enum_Value_List_count):
                                    Vis = Enum_Value_List[num]["VisibilityIdx"]
                                    if (Vis != 0):
                                        Enum_Val = Enum_Value_List[num]["Text"]
                                        Enum_Vis = str(Enum_Val)+":"+str(Vis) 
                                        Enum_Vis_List.append(Enum_Vis)
                                                    
                                                     
                                Enum_Text_List = []
                                for k in range(0, Enum_Value_List_count) :
                                    Enum_Text = Enum_Value_List[k]["Text"]
                                    Enum_Text = str(Enum_List[j]["Values"][k]["Value"])+":"+Enum_Text
                                    Enum_Text_List.append(Enum_Text)
                                Enum_Value =  ','.join(Enum_Text_List)
#                                     test.log ("enum value:"+str(Enum_Value))
                                
                                mylist=[]
                                if(Enum_Index != "-1"):
                                    for x in Enum_Value.split(','):
                                        for y in x.split(':'): 
                                            if(y == Default_Value):                        
                                                for z in x.split(':'):
                                                    mylist.append(z)
                                                    Default_Value = z
                                if(Enum_Index != "-1"):
                                    for x in Enum_Value.split(','):
                                        for y in x.split(':'): 
                                            if(y == Maximum_Val):                        
                                                for z in x.split(':'):
                                                    mylist.append(z)
                                                    Maximum_Val = z
                                if(Enum_Index != "-1"):
                                    for x in Enum_Value.split(','):
                                        for y in x.split(':'): 
                                            if(y == Minimum_Val):                        
                                                for z in x.split(':'):
                                                    mylist.append(z)
                                                    Minimum_Val = z
                                            #print value                      
                    else: 
                        print("missing parameter-"+Parameter_Name)
                     
                    ####UNIT####        
                    
                    Unit_Value=""
#                         Unit_Value= Unit_List[i]["Text"]
                     
                    for l in range (0, Unit_List_count):
                        if (Unit_Type == Unit_List[l]["Idx"]):
                            Unit_Value = Unit_List[l]["Text"]   
                            
                            
                     
                    if (AccLevel == 0):
                        Read_Only = "0"
                    else:
                        Read_Only = "1"
                   
                    writer_1.writerow(["", Parameter_Menu_Code, SG, Parameter_Name, PNU, Default_Value, Minimum_Val, Maximum_Val, Unit_Value, Datatype_Scaling, Data_Type, Enum_Value, Read_Only, Help_Info, Decimals, Items_Unique_Idx, Visibility_Idx, Visibility_Rule,"", Unique_ID, ItemType, CopyType, Enum_Vis_List, SG_Visibility_Idx])
                    
                    writer_2.writerow([Items_Unique_Idx, Parameter_Name, Enum_Value]) 
                    
                    writer_3.writerow([SG, Parameter_Name,Parameter_Menu_Code])
                                             
def Moving_Files():
    src_file = 'Parsed_Json.csv'
    dest_file = Global_Scripts_Path+'\Danfoss.Multi Coil_DB.csv'                    
    shutil.copy (src_file, dest_file)
    
    PName_Dup_List=[]
    file = Global_Scripts_Path+"\Danfoss.Multi Coil_DB.csv"
    records = testData.dataset(file)
    for rec in records:
        PName = testData.field(rec, 3)
        GName = testData.field(rec, 2)
        if ((PName != "") and (GName != "")):
            PName_Dup_List.append(PName)
    test.log("Parameter count with duplicates: "+str(len(PName_Dup_List)))
    
    x = Parameter_Count(PName_Dup_List)
    test.log("Parameter count without duplicates: "+str(x))
    
    Duplicate_Parameter_Count()
    
def Parameter_Count(PName_Dup_List):
    with codecs.open((CDF_Path+"\Multi Coil_1.72\cdf\device.jso"),encoding='utf-8') as data_file:
        content = data_file.read()
        content = content.replace(u'\ufeff','') 
        data = json.loads(content)
        Parameter_Count = len(data["Parameters"])
        
    counter = 0
    PName_List =[]
    for i in range(0, len(PName_Dup_List)):  
        for j in range (0, Parameter_Count):
            if (i==j):
                PName_Idx = data["Parameters"][i]["Idx"]
                if (PName_Idx not in PName_List):
                    counter=counter+1
                    PName_List.append(PName_Idx)
    return counter


##NO OF DUPLICATE PARAMETERS, Their name and group names###
def Duplicate_Parameter_Count():
        PName_Dup_List=[]
        UniqueID_Dup_List =[]
        file = Global_Scripts_Path+"\Danfoss.Multi Coil_DB.csv"
        records = testData.dataset(file)
        for rec in records:
            PName = testData.field(rec, 3)
            GName = testData.field(rec, 2)
            UniqueID = testData.field(rec, 19)
            if ((PName != "") and (UniqueID != "")):
                PName_Dup_List.append(PName)
                UniqueID_Dup_List.append(UniqueID)
#         test.log("Parameter count with duplicates: "+str(len(PName_Dup_List)))
         
        Duplicate_List(UniqueID_Dup_List)
       
def Duplicate_List(UniqueID_Dup_List):
    with codecs.open((CDF_Path+"\Multi Coil_1.72\cdf\device.jso"),encoding='utf-8') as data_file:
        content = data_file.read()
        content = content.replace(u'\ufeff','') 
        data = json.loads(content)
        Parameter_Count = len(data["Parameters"])
    
    PName_List = []
    Occurences_List =[]
    Occurences_Dup_List =[]
    for i in range(0, len(UniqueID_Dup_List)):       
        PName_Count = UniqueID_Dup_List.count(UniqueID_Dup_List[i])
        if (PName_Count>1):
            Occurences_Dup_List.append(UniqueID_Dup_List[i])
#             Occurences_Dup_List.append(PName_Count)
#     test.log(str(Occurences_Dup_List))
#     test.log(str(len(Occurences_Dup_List))) 
    
    for k in range(0, len(Occurences_Dup_List)):
        if (Occurences_Dup_List[k] not in Occurences_List):
            Occurences_List.append(Occurences_Dup_List[k])
    test.log("Duplicate parameter count is: "+str(len(Occurences_List)))     

    Group_Count(Occurences_List)

def Group_Count(Occurences_List):
    file = Output_Global_Path+"\Multi Coil_Parameters_Groups.csv"
    openfile = open(file,'wt') 
    writer = csv.writer(openfile)
    writer.writerow(["ParameterName", "GroupName"])
    
        
    with codecs.open((CDF_Path+"\Multi Coil_1.72\cdf\device.jso"),encoding='utf-8') as data_file:
        content = data_file.read()
        content = content.replace(u'\ufeff','') 
        data = json.loads(content)
        Parameter_Count = len(data["Parameters"])
        Group_Count = len(data["Groups"])
        Group_Items_List =[]
        
        for i in range (0, len(Occurences_List)):
            for k in range (0, Parameter_Count):
                if (str(Occurences_List[i]) == str(data["Parameters"][k]["UniqueID"])):
                    Param_ID = Occurences_List[i]
                    Param_Name = data["Parameters"][k]["Text"]
                    writer.writerow([Param_Name, ""])
#             test.log("PN: "+str(Param_Name))
            
                    for j in range (0, Parameter_Count):
                        if (str(Param_Name) == str(data["Parameters"][j]["Text"])):
                            Param_Idx = data["Parameters"][j]["Idx"]
                            for k in range (0, Group_Count-1): ## -1 because QUICKSETTINGS does not come under parameter count##
                                Items = data["Groups"][k]["Items"]
        #                         Group_Items_List.append(Items)
                                for l in range (0, len(Items)):
                                    if (str(Param_Idx) == str(Items[l]["Index"]) and str(Items[l]["ItemType"]) == "P"):
                                        GroupName = data["Groups"][k]["Text"]
        #                                 test.log("GN: "+str(GroupName))
                                        writer.writerow(["", GroupName])
    
def Compare_DB():
    file = Output_Global_Path+"\Multi Coil_Database_Comparison.csv"
    openfile = open(file,'wt') 
    writer = csv.writer(openfile)
    writer.writerow(["Label","Name", "VariableName", "Sql_Visib_Rule", "Squish_Visib_Rule", "Result", "Sql_Help", "Squish_Help", "Result"])
     
    Sql_file = Global_Scripts_Path+"AK_CC_MultiCoil_DB_Sql.csv"
    param = testData.dataset(Sql_file)
    for par in param:
#         Sql_Name = testData.field(par, 0) 
        Sql_VisibilityRule = testData.field(par, 34)
        Sql_VariableName = testData.field(par, 36)
        Sql_Help_Info = testData.field(par,26)
         
 
        Squish_file = Global_Scripts_Path+"\Danfoss.Multi Coil_DB.csv"
        records = testData.dataset(Squish_file)
        for rec in records:
            Squish_Label = testData.field(rec, 1) 
            Squish_Name = testData.field(rec, 3) 
            Squish_VisibilityRule = testData.field(rec, 17)
            Squish_VariableName = testData.field(rec, 15)
            Squish_Help_Info = testData.field(rec,13)
             
            if ((str(Sql_VariableName) == str(Squish_VariableName))):
#                 test.log("parameter is: " +str(Squish_VariableName))
                test.log("PARNAME: "+str(Squish_Name))
                result = test.compare(str(Sql_VisibilityRule.strip()), str(Squish_VisibilityRule.strip()))
                result_help = test.compare(str(Sql_Help_Info.strip()), str(Squish_Help_Info.strip()))
                writer.writerow([Squish_Label, Squish_Name, Squish_VariableName, Sql_VisibilityRule, Squish_VisibilityRule, result, Sql_Help_Info, Squish_Help_Info, result_help])
                break
     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
                
