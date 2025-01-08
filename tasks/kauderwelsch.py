
def kauderwelsch(Eingabe):
    # Konvertiere den Text in Kleinbuchstaben
    Eingabe = Eingabe.lower()
    
    # Ersetze die Vokale gemäß den Regeln
    text_kauderwelsch = Eingabe.replace('a', 'e').replace('i', 'e').replace('o', 'e').replace('u', 'e').replace('e', 'ü')
    
    # Zähle die Anzahl der ersetzten Buchstaben
    anzahl_ersetzte_buchstaben = (
        Eingabe.count('a') +
        Eingabe.count('i') +
        Eingabe.count('o') +
        Eingabe.count('u') +
        Eingabe.count('e')
    )
    
    # Ausgabe
    print(text_kauderwelsch)
    print(f"Es wurden {anzahl_ersetzte_buchstaben} Buchstaben ersetzt.")

# Benutzereingabe(n)
TextEingabe = input("Bitte geben Sie einen Text ein: ")
kauderwelsch(TextEingabe)