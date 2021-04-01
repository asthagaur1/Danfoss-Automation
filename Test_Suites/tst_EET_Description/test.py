def main():
    excel = "EET_Description.xls"
    source(findFile("scripts", "Functions.py"));
    source(findFile("scripts", "Actions.py"));
    #Mapping with Global scripts for Function library and key action.
    #source(findFile("scripts", "object_id.py"))
    keyAction(excel)