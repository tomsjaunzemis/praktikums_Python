"""
Izveidot funkciju, kura atgriež skaitļu kvadrātus, lietotāja norādītā apgabalā.
"""
skaitlis=float(input("Ievadi skaitli:"))

def kvadrats(a):
    kvadrats=pow(a,2)
    return kvadrats
    
print(kvadrats(skaitlis))