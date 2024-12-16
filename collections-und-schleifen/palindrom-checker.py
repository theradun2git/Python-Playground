
def PrüfungPalindrom(UserInput):
    # Lehrzeichen entfernen & alles in Kleinbuchstaben
    UserInput = UserInput.strip().lower()
    
    # Text umdrehen
    UserInput_reversed = UserInput[::-1]
    
    # Text prüfen
    IstPalindrom = UserInput == UserInput_reversed
    
    # Ausgabe
    print("Vorwärts: " + UserInput)
    print("Rückwärts: " + UserInput_reversed)
    print("Ist Palindrom: " + str(IstPalindrom))

# Benutzereingabe(n)
TextEingabe = input("Bitte geben Sie ein Wort ein: ")
PrüfungPalindrom(TextEingabe)
