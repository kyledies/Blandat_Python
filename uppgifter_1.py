#Jackor i dictionary med priser
# Recap Try-Except - När man ej vill att exceptions ska avbryta programmet
#Uppgift 1: Välj jacka/jackor, ange eventuell rea och beräkna totalt pris
def uppgift_1():

    jackor = {
        "adidas": 1200,
        "nike": 1500,
        "puma": 1300,
        "reebok": 1400,
        "under_armour": 1600,
        "lager 157": 300
        }
    print("Tillgängliga jackor och priser:")
    for key in jackor:
        print(f"--- {key.capitalize()}: {jackor[key]} kr ---")

    total = 0

    while True:
        #Välja jacka
        val = input("Vilken jacka vill du köpa? ").lower()
        if val == "klar":
            break
        if val not in jackor:
            print("Den jackan finns inte i sortimentet. Försök igen.")
            continue

        #Ange rea   
        while True: 
            try: #try except för att hantera ogiltiga inmatningar
                rea = float(input(f"Ange eventuell rea i procent för {val.capitalize()} (0-100): "))
                if 0 <= rea <= 100:
                    break
                else:
                    print("Rean måste vara mellan 0 och 100 procent. Försök igen.")
            except ValueError:
                print("Ogiltigt värde. Ange ett numeriskt värde mellan 0 och 100.")

        #Beräkna pris
        pris = jackor[val] * (1 - rea / 100)
        total += pris
        print(f"Du har valt {val.capitalize()} för {pris:.2f} kr efter rea.")

    print(f"Totalt att betala: {total:.2f} kr")

#Uppgift 2 program som tar emot 2-5 numeriska värden och skriver ut dem i storleksordning
def uppgift_2():
    print("Ange 2-5 numeriska värden.):")
    while True:
        values = input("Ange värden separerade med mellanslag (Ange 'klar' för att avbryta): ").strip().split()
        if len(values) == 1 and values[0].lower() == "klar":
            print("Avbryter uppgiften.")
            return #bryter om användaren skriver "klar"
        #Kontrollerar först att värden är numeriska
        try:
            numbers = [float(value) for value in values]
        except ValueError:
            print("Ogiltig inmatning. Se till att ange numeriska värden.")
            continue
        #Kontrollerar att antalet värden är mellan 2 och 5
        if 2 <= len(numbers) <= 5:
            numbers.sort()
            print("Värden i storleksordning:", numbers)
            fortsätt = input("Vill du ange nya värden? (j/n): ").lower()
            if fortsätt != "j":
                break
        else:
            print("Du måste ange mellan 2 och 5 värden. Försök igen.")
        
def uppgift_3():
    for i in range(3):
        print(str(i))
    i = 3
    while i > 0:
        print(str(i))
        i -= 1
def uppgift_4():
    pokemons = ["Pikachu", "Charmander", "Bulbasaur", "Squirtle", "Jigglypuff", "Meowth"]
    for pokemon in pokemons:
        print(f"Pokemon: {pokemon}")
    pokemons.insert(0, "Eevee")
    print(pokemons) 
    pokemons.insert(7, "Mew")  
    print(pokemons) 
    pokemons.insert(2, "Mewtwo")  
    print(pokemons) 
    # Lägger till Eevee i början av listan

#---Program för att köra uppgifterna---
while True:
    print("\nVälj uppgift:")
    print("1. Jackor + Rea")
    print("2. Uppgift 2")
    print("3. Uppgift 3")
    print("4. Uppgift 4")
    print("q. Avsluta")

    val = input("Ditt val: ").lower()

    if val == "1":
        uppgift_1()
    elif val == "2":
        uppgift_2()
    elif val == "3":
        uppgift_3()
    elif val == "4":
        uppgift_4()
    elif val == "q":
        print("Hejdå!")
        break
    else:
        print("Ogiltigt val, försök igen.")