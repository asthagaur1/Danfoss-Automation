def main():
    excel = r"C:\gitworkspace\KoolProg-TestAutomation\Master_Functions\Test_Automation\SourceCode\suite_EETa-2Relay\tst_MainFunction\testdata\Open_Factory_Reset_Import.xls";
    #Mapping with Global scripts for Function library and key action.
    source(findFile("scripts", "Functions.py"))
    source(findFile("scripts", "Actions.py"))
   # source(findFile("scripts", "object_id.py"))
    keyAction(excel)
    
    