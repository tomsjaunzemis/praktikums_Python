""" 
Uzrakstiet programmu, kas ielasa vienu vārdu 
un izvada uz ekrāna sveicienu sekojošā formātā:
"Labdien, vards, pimrdienā!"
Ja ievadīts nav jūsu vards, tiek izdrukāts teksts - Uzredzēšanos!
Pārbaudiet programmas darbību ar dažādiem ievaddatiem.
"""
vards=str(input("Ievadi savu vārdu: "))
if vards=="Toms":
    print("Labdien,"+vards+",pirmdienā!")
if not vards=="Toms":
    print("Uzredzēšenos!")    