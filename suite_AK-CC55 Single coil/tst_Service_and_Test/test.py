def main():
    excel = "Service_and_Test.xls";
    source(findFile("scripts", "Functions.py"));
    source(findFile("scripts", "Actions.py"));
    #Mapping with Global scripts for Function library and key action.
    keyAction(excel)