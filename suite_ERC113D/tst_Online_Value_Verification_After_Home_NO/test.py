def main():
    excel = r"C:\gitworkspace\TestAutomation-Maintenance\Test_Automation\SourceCode\suite_ERC113D\shared\testdata\Online_Verifying_Values_After_HOME_NO.xls";
    #Mapping with Global scripts for Function library and key action.
    source(findFile("scripts", "Functions.py"))
    source(findFile("scripts", "Actions.py"))
    source(findFile("scripts", "object_id.py"))
    keyAction(excel)