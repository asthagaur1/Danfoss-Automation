def main():
    excel = r"C:\gitworkspace\KoolProg-TestAutomation\Master_Functions\Test_Automation\SourceCode\suite_EETc 22\shared\testdata\Open_Change_Values_Factory_Reset_Import.xls";
    #Mapping with Global scripts for Function library and key action.
    source(findFile("scripts", "Functions.py"))
    source(findFile("scripts", "Actions.py"))
    #source(findFile("scripts", "object_id.py"))
    keyAction(excel)
    
    