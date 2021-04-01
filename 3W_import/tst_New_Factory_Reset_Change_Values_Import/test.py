def main():
    excel = r"C:\gitworkspace\KoolProg-TestAutomation\Master_Functions\Test_Automation\SourceCode\suite_EETa 3W\shared\testdata\New_Factory_Reset_Change_Values_Import.xls";
    #Mapping with Global scripts for Function library and key action.
    source(findFile("scripts", "Functions.py"))
    source(findFile("scripts", "Actions.py"))
    #source(findFile("scripts", "object_id.py"))
    keyAction(excel)
    
    