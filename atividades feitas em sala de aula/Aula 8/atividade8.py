carneirinho = 0
sono = False

while sono == False:
    jadormi = input("você já dormiu?(sim/não)").strip().lower()
    if jadormi in ['não','n','nao']:
        carneirinho+=1
        print(f"{carneirinho} 🐑 1 carneirinho pulou a cerca!")
    elif jadormi in['sim','s']:
        sono = True
        print("😴 Bons sonhos, carneirinho!")

input()