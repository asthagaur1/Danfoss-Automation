def main():
    excel = r"C:\gitworkspace\KoolProg-TestAutomation\Master_Functions\Test_Automation\SourceCode\CommonTestcases\shared\testdata\Upload_from_Controller_Change_Values_Home_No.xls";
    #Mapping with Global scripts for Function library and key action.
    source(findFile("scripts", "Functions.py"))
    source(findFile("scripts", "Actions.py"))
   # source(findFile("scripts", "object_id.py"))
    keyAction(excel)
    
    