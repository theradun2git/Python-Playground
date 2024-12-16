
# f-String

# # Benutzereingabe(n)
InputAktuellerJahresUmsatz = int(input("Bitte geben Sie den aktuellen Umsatz ein: "))
InputVorJahresUmsatz = int(input("Bitte geben Sie den Vorjahresumsatz ein: "))

# Variablen
VeraenderungUmsatz = InputAktuellerJahresUmsatz - InputVorJahresUmsatz
VeraenderungInProzent = int((VeraenderungUmsatz / InputVorJahresUmsatz) * 100)

# Ausgabe
print(f"Der Umsatz hat sich um CHF {VeraenderungUmsatz:,} verändert.")
print(f"Das entspricht einer Veränderung von {VeraenderungInProzent} %.")