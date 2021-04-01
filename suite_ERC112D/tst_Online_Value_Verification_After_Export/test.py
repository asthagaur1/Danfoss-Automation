def main():
    excel = r"C:\gitworkspace\KoolProg-TestAutomation\Master_Functions\Test_Automation\SourceCode\suite_ERC112D\shared\testdata\Online_Export_Verifying_Values.xls";
    #Mapping with Global scripts for Function library and key action.
    source(findFile("scripts", "Functions.py"))
    source(findFile("scripts", "Actions.py"))
#     source(findFile("scripts", "object_id.py"))
    keyAction(excel)