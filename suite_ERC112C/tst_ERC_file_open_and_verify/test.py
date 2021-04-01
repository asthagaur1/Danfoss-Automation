def main():
    excel = r"C:\gitworkspace\KoolProg-TestAutomation\CommonTestcases\shared\testdata\Active_Alarms.xls"
    #Mapping with Global scripts for Function library and key action.
    source(findFile("scripts", "Functions.py"))
    source(findFile("scripts", "Actions.py"))
    #source(findFile("scripts", "object_id.py"))
    keyAction(excel)
        
        
        
        
        
        
        