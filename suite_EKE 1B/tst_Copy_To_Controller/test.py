def main():
    excel = r"C:\gitworkspace\TestAutomation-Maintenance\Test_Automation\SourceCode\suite_EKE 1B\shared\testdata\Check_Browse.xls"
    #Mapping with Global scripts for Function library and key action.
    source(findFile("scripts", "Functions.py"))
    source(findFile("scripts", "Actions.py"))
    source(findFile("scripts", "object_id.py"))
    keyAction(excel)