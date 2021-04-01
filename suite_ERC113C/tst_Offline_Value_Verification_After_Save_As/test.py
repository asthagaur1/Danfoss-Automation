def main():
    excel = r"C:\gitworkspace\TestAutomation-AKCC5XX\Test_Automation\SourceCode\Test_Suites\suite_ERC113C\shared\testdata\Offline_Verifying_Values_After_Save_As.xls";
    #Mapping with Global scripts for Function library and key action.
    source(findFile("scripts", "Functions.py"))
    source(findFile("scripts", "Actions.py"))
    source(findFile("scripts", "object_id.py"))
    keyAction(excel)