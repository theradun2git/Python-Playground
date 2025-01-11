
# Eingabe der gewünschten Berechnung
berechnung = input("Bitte geben Sie die Berechnung ein (z.B. 4 - 3): ")

# Split the input into parts
aufteilung = berechnung.split()

# Extract the numbers and operator
zahl1 = float(aufteilung[0])
operator = aufteilung[1]
zahl2 = float(aufteilung[2])

# Berechnung aufgrund des Operators
if operator == '+':
    resultat = zahl1 + zahl2
elif operator == '-':
    resultat = zahl1 - zahl2
elif operator == '*':
    resultat = zahl1 * zahl2
elif operator == '/':
    resultat = zahl1 / zahl2

# Ausgabe der Lösung
if operator == '/':
    print(f"{zahl1} {operator} {zahl2} = {resultat:.5f}")
else:
    print(f"{zahl1} {operator} {zahl2} = {resultat}")
