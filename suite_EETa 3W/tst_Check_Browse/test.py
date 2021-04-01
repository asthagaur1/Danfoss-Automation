def main():
    excel = r"C:\gitworkspace\KoolProg-TestAutomation\Master_Functions\Test_Automation\SourceCode\suite_EETa 3W\shared\testdata\Check_Browse.xls";
    #Mapping with Global scripts for Function library and key action.
    source(findFile("scripts", "Actions.py"))
    #source(findFile("scripts", "object_id.py"))
    source(findFile("scripts", "Functions.py"))
    keyAction(excel)