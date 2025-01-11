
def Rennergebnisse():
    distanzen = []

    while True:
        eingabe_distanz = input("Bitte eine Distanz in Meter eingeben oder mittels <Enter> beenden: ")
        
        if eingabe_distanz == "":
            break
        
        try:
            distanz = float(eingabe_distanz)
            distanzen.append(distanz)
        except ValueError:
            print("Bitte eine gültige Zahl eingeben.")

    # Ausgabe der erfassten Distanzen
    print(f"Erfasste Distanzen in Meter: \n {distanzen}")

    if distanzen:
        anzahl_rennen = len(distanzen)
        kuerzeste_rennen = min(distanzen)
        laengste_rennen = max(distanzen)
        gesamt_distanz = sum(distanzen)
        durchschnitt_distanz = gesamt_distanz / anzahl_rennen

        print("\nSpannende Informationen:")
        print(f"Anzahl der Rennen: {anzahl_rennen}")
        print(f"Kürzeste Distanz: {kuerzeste_rennen} m")
        print(f"Längste Distanz: {laengste_rennen} m")
        print(f"Gesamtdistanz: {gesamt_distanz} m")
        print(f"Durchschnittliche Distanz: {durchschnitt_distanz:.2f} m")
    else:
        print("Keine Distanzen eingegeben.")

if __name__ == "__main__":
    Rennergebnisse()