# ------------------------------- Information --------------------------------- #
"""
Titel: Biblioteket
Författare:
Datum:
Det här är ett program för hantering av enklare biblioteksrutiner.
Programmet lagrar böckerna i en fil med namnet "bibliotek.txt" mellan körningarna.
"""
# ------------------------- Biblioteksimportering ----------------------------- #
import random as rand
import json
from xml.etree.ElementPath import xpath_tokenizer

# ---------------------------- Klassdefinitioner ------------------------------ #

class Bok:
    """ Bok är en klass som representerar en bok i biblioteket. Varje objekt
    som skapas ur klassen har en titel, författare och en variabel som håller
    reda på om boken är utlånad eller inte. """
    def __init__(self, författare, titel):
        self.titel = titel
        self.författare = författare
        self.utlånad = False

    # Strängrepresentation av objektet.
    def __str__(self):
        return f"Boken {self.titel}, skriven av {self.författare}."

# ------------------------- Testböcker -------------------------------------- #
Boklista = []

Boklista.append(Bok('F.Scott Fitzgerald','The great Gatsby'))
Boklista.append(Bok('Khalid Hosseini','Kite runner'))
Boklista.append(Bok('George Orwell', '1984'))
Boklista.append(Bok('Winston Groom', 'Forrest gump'))
    # ----------------------------------------------------------------------------#


class Bibliotek:
    """ Bibliotek är en klass som representerar en bibliotekskatalog. Ett objekt
    ur klassen har en lista över böcker som attribut, samt metoder för att
    modifiera katalogen. """
    def __init__(self, bookList):
        self.books = bookList

    # Sparar hela bibliotekskatalogen i en fil. 
    def spara(self, filnamn):
        return

    
    # Söker på en titel.
    def hittaTitel(self, titel):
        for number, x in enumerate(Boklista, start=1):
            print(number, x.titel)
        
     
            

    # Söker på en författare.
    def hittaFörfattare(self, författare):
        return

    # Lånar en bok.
    def lånaBok(self, bok):
        
        if self.utlånad == str(False):
            print('boken är ej utlånad')
        

        return

    # Återlämnar en bok.
    def lämnaTillbaka(self, bok):
        
        

        return

    # Lägger till en ny bok:
    def läggTill(self, bok):
        

        return

    # Tar bort en bok:
    def taBort(self, bok):
        return

    # Returnerar en lista över alla böcker:
    def listaBöcker(self):
        
        
        
        return

# ------------------------------ Huvudprogram --------------------------------- #
def main():
    


    for obj in Boklista:
        print( obj.titel, obj.författare, obj.utlånad, sep =' ' )
    
    
    menyVal = ""

    while menyVal != "q":

        print(
        """
                                          --- MENY ---
                Välkommen till biblioteks-simulatorn. Välj ett av alternativen nedan:
            1. Sök efter titel                                  2. Sök efter författare
            3. Låna bok                                         4. Återlämna bok
            5. Lägg till ny bok                                 6. Ta bort bok                                 
            7. Lista alla böcker                                8. Sortera böcker                                   
            q. Avsluta
        ---------------------------------------------------------------------------------------""")

        menyVal = input("-> ")

        if menyVal == "1":

            
        
            
            pass
        elif menyVal == "2":
            
            for number, x in enumerate(Boklista, start=1):
                print(number, x.författare)
           
            number = 1
            sök = str(input())

            if sök[-len(sök)] == Boklista[number][-len(Boklista)[number]] :
                print(Boklista[number])
                
                
        elif menyVal == "3":
            
            for number, x in enumerate(Boklista, start=1):
                 print(number,x.titel, x.författare,"utlånad:",x.utlånad)
            number = int(input())
            Boklista[number].utlånad = True


            

            
            
            
        elif menyVal == "4":
             
             for number, x in enumerate(Boklista, start=1):
                 print(number,x.titel, x.författare,"utlånad:",x.utlånad)
             number = int(input())
             Boklista[number].utlånad = False

        
            
        

        
        
            

            
        
        
        elif menyVal == "3":
            
            for number, x in enumerate(Boklista, start=1):
                 print(number,x.titel, x.författare,"utlånad:",x.utlånad)
            number = int(input())
            Boklista[number].utlånad = True


            

            
            
            
        elif menyVal == "4":
             
             for number, x in enumerate(Boklista, start=1):
                 print(number,x.titel, x.författare,"utlånad:",x.utlånad)
             number = int(input())
             Boklista[number].utlånad = False

        
            
        

        
        
            

        
            




    
        elif menyVal == "5":
            
            for number, x in enumerate(Boklista, start=1):
                print(number, x.titel, x.författare)
            print('Vad heter boken?')
            x.titel = input()
            print("vad heter förattaren")
            x.författare = input()
            Boklista.append(Bok(x.titel,x.författare))
            






           

            
        elif menyVal == "6":
            for number, x in enumerate(Boklista, start=1):
                print(number, x.titel, x.författare)
                
            print("vilken vill du ta bort")
            number = int(input())
            Boklista.pop(number)

          

           


        

        elif menyVal == "7":
            for x in Boklista:
                print(x.titel, x.författare)
            pass
        
        
        
        elif menyVal == "8":
            print("How do you want to sort")
            sortM = int(input())
            if sortM == 1 :
                Boklista.sort()
            
            pass
        
        
        
        elif menyVal == "q":
            pass

        else :
            print("Välj ett alternativ på listan")
            menyVal = input()
print(
"""
                                   .--.                   .---.
                               .---|__|           .-.     |~~~|
                            .--|===|--|_          |_|     |~~~|--.--.
                            |  |===|  |'\     .---!~|  .--|   |--|--|
                            |%%|   |  |.'\    |===| |--|%%|   |  |  |
                            |%%|   |  |\.'\   |   | |__|  |   |  |  |
                            |B | I |B | \L \  |=I=|O|T=|E | K |E |T |
                            |  |   |__|  \.'\ |   |_|__|  |~~~|__|__|
                            |  |===|--|   \.'\|===|~|--|%%|~~~|--|--|
                            ^--^---'--^    `-'`---^-^--^--^---'--'--'
""")

main()
