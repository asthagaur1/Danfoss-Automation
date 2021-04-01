def main():
    excel = r"C:\gitworkspace\TestAutomation-Maintenance\Test_Automation\SourceCode\suite_ETC 1H2\shared\testdata\Offline_Verifying_Values_HOME_YES.xls";
    #Mapping with Global scripts for Function library and key action.
    source(findFile("scripts", "Functions.py"))
    source(findFile("scripts", "Actions.py"))
    source(findFile("scripts", "object_id.py"))
    keyAction(excel)