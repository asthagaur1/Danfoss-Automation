def main():
    excel = "AKCC_Readouts.xls";     
    source(findFile("scripts", "global.py"));             
    #Mapping with Global scripts for Function library and key action.
    keyAction(excel)