import csv

def start():
    mouseClick(waitForObject(":KoolProg_Image"), MouseButton.PrimaryButton)
    waitForObject(":SetParameters_Window")
    mouseClick(waitForObject(":System.Windows.Controls.DockPanel.New_Label"), MouseButton.PrimaryButton)
    waitForObject(":Newproject_Window")
    mouseClick(waitForObject(":System.Windows.Controls.StackPanel_Expander_2"), MouseButton.PrimaryButton)
    
def main():
    startApplication("KoolProg")
    start()
    Func112D_3409()
    Verify_Datagrid_3409()
    Service_3409()
    
    start()
    Func112D_3408()
    Verify_Datagrid_3408()
    Service_3408()
    
def Func112D_3409():
    mouseClick(waitForObject(":System.Windows.Controls.StackPanel.5_0_TableCell_2"), MouseButton.PrimaryButton)
    
    mouseClick(waitForObject(":Newproject.NEXT >_Button"), MouseButton.PrimaryButton)
    waitForObject(":Product Name.Code Number:_ComboBox")
    mouseClick(":Product Name.Code Number:_ComboBox"), MouseButton.PrimaryButton
    type(waitForObject(":Product Name.Code Number:_ComboBox"), "080G3409")
    type(waitForObject(":Product Name.Code Number:_ComboBox"), "<Return>")
    mouseClick(waitForObject(":Product Name.System.Windows.Controls.StackPanel_Edit"), MouseButton.PrimaryButton)
    type(waitForObject(":Product Name.System.Windows.Controls.StackPanel_Edit"), "112D-3409-9.25")
    mouseClick(waitForObject(":Newproject.FINISH_Button"), MouseButton.PrimaryButton)
    try:
        mouseClick(waitForObject(":MessageBoxDisplay.YES_Button"), MouseButton.PrimaryButton)
    except:
        snooze(10)
        waitForObject(":KoolProg.System.Windows.Controls.Image_Button")
        
def Service_3409():
    mouseClick(waitForObject(":KoolProg_Image_3"), MouseButton.PrimaryButton)
    waitForObject(":KoolProg.System.Windows.Controls.Image_Button")
    
    file= "112D-3409_UGUR.csv"  
    file_1 = "Online_112D-3409_UGUR_RESULT.csv"   
    tbl=waitForObjectExists(":KoolProg_Table")
    items=tbl.nativeObject.Items
       
    openfile = open(file_1,'wt') 
    writer = csv.writer(openfile)
    writer.writerow(["ParameterName", "DB_Menucode","KP_Menucode","Result" ,"DB_DefaultValue", "KP_DefaultValue", "Result", "DB_MinValue", "KP_MinValue", "Result" ,"DB_MaxValue", "KP_MaxValue", "Result", "DB_Unit", "KP_Unit", "Result", "DB_Info", "KP_Info", "Result", "Present_Value"])

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
                MenuCode_Result = test.compare(id, item.MenuCode)
                DefaultValue_Result = test.compare(Default, item.DefaultValue)
                MinValue_Result = test.compare(Min, item.Minvalue)
                MaxValue_Result = test.compare(Max, item.Maxvalue)
                Unit_Result = test.compare(Unit, item.Unit)
                Help_Result = test.compare(Info_Help, item.Description)
                writer.writerow([item.ParameterName,id, item.MenuCode, MenuCode_Result, Default, item.DefaultValue, DefaultValue_Result, Min, item.Minvalue, MinValue_Result, Max, item.Maxvalue, MaxValue_Result, Unit, item.Unit, Unit_Result, Info_Help, item.Description, Help_Result, item.Value])
                            
    mouseClick(":KoolProg.System.Windows.Controls.Image_Button"), MouseButton.PrimaryButton
    
def Verify_Datagrid_3409():
    snooze(10)
    waitForObject(":KoolProg.System.Windows.Controls.Image_Button")
    file= "112D-3409_UGUR.csv"  
    file_1 = "112D-3409_UGUR_RESULT.csv"    
    tbl=waitForObjectExists(":KoolProg_Table")
    items=tbl.nativeObject.Items
       
    openfile = open(file_1,'wt') 
    writer = csv.writer(openfile)
    writer.writerow(["ParameterName", "DB_Menucode","KP_Menucode","Result" ,"DB_DefaultValue", "KP_DefaultValue", "Result", "DB_MinValue", "KP_MinValue", "Result" ,"DB_MaxValue", "KP_MaxValue", "Result", "DB_Unit", "KP_Unit", "Result", "DB_Info", "KP_Info", "Result", "Present_Value"])

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
                MenuCode_Result = test.compare(id, item.MenuCode)
                DefaultValue_Result = test.compare(Default, item.DefaultValue)
                MinValue_Result = test.compare(Min, item.Minvalue)
                MaxValue_Result = test.compare(Max, item.Maxvalue)
                Unit_Result = test.compare(Unit, item.Unit)
                Help_Result = test.compare(Info_Help, item.Description)
                writer.writerow([item.ParameterName,id, item.MenuCode, MenuCode_Result, Default, item.DefaultValue, DefaultValue_Result, Min, item.Minvalue, MinValue_Result, Max, item.Maxvalue, MaxValue_Result, Unit, item.Unit, Unit_Result, Info_Help, item.Description, Help_Result, item.Value])
                            
    mouseClick(":KoolProg.System.Windows.Controls.Image_Button"), MouseButton.PrimaryButton
       
    
def Func112D_3408():
    mouseClick(waitForObject(":System.Windows.Controls.StackPanel.5_0_TableCell_2"), MouseButton.PrimaryButton)
    
    mouseClick(waitForObject(":Newproject.NEXT >_Button"), MouseButton.PrimaryButton)
    waitForObject(":Product Name.Code Number:_ComboBox")
    mouseClick(":Product Name.Code Number:_ComboBox"), MouseButton.PrimaryButton
    type(waitForObject(":Product Name.Code Number:_ComboBox"), "080G3408")
    type(waitForObject(":Product Name.Code Number:_ComboBox"), "<Return>")
    mouseClick(waitForObject(":Product Name.System.Windows.Controls.StackPanel_Edit"), MouseButton.PrimaryButton)
    type(waitForObject(":Product Name.System.Windows.Controls.StackPanel_Edit"), "112D-3408-9.25")
    mouseClick(waitForObject(":Newproject.FINISH_Button"), MouseButton.PrimaryButton)
    try:
        mouseClick(waitForObject(":MessageBoxDisplay.YES_Button"), MouseButton.PrimaryButton)
    except:
        snooze(10)
        waitForObject(":KoolProg.System.Windows.Controls.Image_Button")
        
def Service_3408():
    mouseClick(waitForObject(":KoolProg_Image_3"), MouseButton.PrimaryButton)
    waitForObject(":KoolProg.System.Windows.Controls.Image_Button")
    
    file= "112D-3408_ISA.csv"  
    file_1 = "Online_112D-3408_ISA_RESULT.csv"   
    tbl=waitForObjectExists(":KoolProg_Table")
    items=tbl.nativeObject.Items
       
    openfile = open(file_1,'wt') 
    writer = csv.writer(openfile)
    writer.writerow(["ParameterName", "DB_Menucode","KP_Menucode","Result" ,"DB_DefaultValue", "KP_DefaultValue", "Result", "DB_MinValue", "KP_MinValue", "Result" ,"DB_MaxValue", "KP_MaxValue", "Result", "DB_Unit", "KP_Unit", "Result", "DB_Info", "KP_Info", "Result", "Present_Value"])

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
                MenuCode_Result = test.compare(id, item.MenuCode)
                DefaultValue_Result = test.compare(Default, item.DefaultValue)
                MinValue_Result = test.compare(Min, item.Minvalue)
                MaxValue_Result = test.compare(Max, item.Maxvalue)
                Unit_Result = test.compare(Unit, item.Unit)
                Help_Result = test.compare(Info_Help, item.Description)
                writer.writerow([item.ParameterName,id, item.MenuCode, MenuCode_Result, Default, item.DefaultValue, DefaultValue_Result, Min, item.Minvalue, MinValue_Result, Max, item.Maxvalue, MaxValue_Result, Unit, item.Unit, Unit_Result, Info_Help, item.Description, Help_Result, item.Value])
                            
    mouseClick(":KoolProg.System.Windows.Controls.Image_Button"), MouseButton.PrimaryButton
    
    
def Verify_Datagrid_3408():
    snooze(10)
    waitForObject(":KoolProg.System.Windows.Controls.Image_Button")
    file= "112D-3408_ISA.csv"  
    file_1 = "112D-3408_ISA_RESULT.csv"   
    tbl=waitForObjectExists(":KoolProg_Table")
    items=tbl.nativeObject.Items
       
    openfile = open(file_1,'wt') 
    writer = csv.writer(openfile)
    writer.writerow(["ParameterName", "DB_Menucode","KP_Menucode","Result" ,"DB_DefaultValue", "KP_DefaultValue", "Result", "DB_MinValue", "KP_MinValue", "Result" ,"DB_MaxValue", "KP_MaxValue", "Result", "DB_Unit", "KP_Unit", "Result", "DB_Info", "KP_Info", "Result", "Present_Value"])

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
                MenuCode_Result = test.compare(id, item.MenuCode)
                DefaultValue_Result = test.compare(Default, item.DefaultValue)
                MinValue_Result = test.compare(Min, item.Minvalue)
                MaxValue_Result = test.compare(Max, item.Maxvalue)
                Unit_Result = test.compare(Unit, item.Unit)
                Help_Result = test.compare(Info_Help, item.Description)
                writer.writerow([item.ParameterName,id, item.MenuCode, MenuCode_Result, Default, item.DefaultValue, DefaultValue_Result, Min, item.Minvalue, MinValue_Result, Max, item.Maxvalue, MaxValue_Result, Unit, item.Unit, Unit_Result, Info_Help, item.Description, Help_Result, item.Value])
                            
    mouseClick(":KoolProg.System.Windows.Controls.Image_Button"), MouseButton.PrimaryButton
        


    
    
    
    
    
    
    
    
    