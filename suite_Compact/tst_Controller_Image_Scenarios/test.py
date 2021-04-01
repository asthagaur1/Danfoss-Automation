def main():
    excel = "Controller_Images.xls"
    source(findFile("scripts", "Functions.py"));
    source(findFile("scripts", "Actions.py"));
    #Mapping with Global scripts for Function library and key action.
    keyAction(excel)
         
