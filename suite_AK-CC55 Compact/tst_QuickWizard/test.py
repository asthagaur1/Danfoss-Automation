def main():
    excel = "QuickWizard_Offline.xls";
    #Mapping with Global scripts for Function library and key action.
    source(findFile("scripts", "Functions_AKCC.py"))
    source(findFile("scripts", "Actions.py"))
#     source(findFile("scripts", "object_id.py"))
    keyAction(excel)