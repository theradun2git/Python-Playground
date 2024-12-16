
# Benutzereingabe(n)
InputAktuellerJahresUmsatz = int(input("Bitte geben Sie den aktuellen Umsatz ein: "))
InputVorJahresUmsatz = int(input("Bitte geben Sie den Vorjahresumsatz ein: "))

# Variablen
VeraenderungUmsatz = InputAktuellerJahresUmsatz - InputVorJahresUmsatz
VeraenderungInProzent = int((VeraenderungUmsatz / InputVorJahresUmsatz) * 100)

# Ausgabe
print("Der Umsatz hat sich um CHF " + str(VeraenderungUmsatz) + " verändert.")
print("Das entspricht einer Veränderung von " + str(VeraenderungInProzent) + "%.")

