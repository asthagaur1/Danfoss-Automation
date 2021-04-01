def main():
    excel = "AKCC_SubGroup_Comparison.xls"
    source(findFile("scripts", "Functions.py"));
    source(findFile("scripts", "Actions.py"));
    #Mapping with Global scripts for Function library and key action.
    keyAction(excel)