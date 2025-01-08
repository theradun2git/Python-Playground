
def umsatzsteigerung2():
    try:
        # Abfrage entsprechender Werte
        previous_sales = float(input("Bitte geben Sie den Vorjahresumsatz ein: "))
        current_sales = float(input("Bitte geben Sie den aktuellen Umsatz ein: "))
        
        # Kalkulation
        change = current_sales - previous_sales
        percentage_change = (change / previous_sales) * 100
        
        # Output
        if change > 0:
            print(f"Der Umsatz hat sich um {change:.2f} Franken erhöht. Das entspricht einer Zunahme von {percentage_change:.2f}%.")
        else:
            print(f"Der Umsatz hat sich um {-change:.2f} Franken verringert. Das entspricht einem Rückgang von {-percentage_change:.2f}%.")
    
    except ValueError:
        # Error handling
        print("Ungültige Eingabe. Bitte geben Sie eine gültige Zahl ein.")

# Funktion starten
umsatzsteigerung2()

