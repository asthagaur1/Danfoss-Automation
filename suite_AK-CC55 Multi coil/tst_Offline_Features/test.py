def main():
    excel = "Set_Parameters.xls";
    source(findFile("scripts", "Functions.py"));
    source(findFile("scripts", "Actions.py"));
    source(findFile("scripts", "global.py"));
    #Mapping with Global scripts for Function library and key action.
    keyAction(excel)