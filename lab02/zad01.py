import pandas as pd
import numpy as np

df = pd.read_csv("/Users/adamoporski/Documents/inteligencja_obliczeniowa/lab02/iris.csv")

# A) Sprawdzanie brakujących danych
missing_values = df.isnull().sum() 
total_missing = missing_values.sum()  

print("\nA) Brakujące wartości")
print("Brakujące wartości w każdej kolumnie:\n", missing_values)
print("Łączna liczba braków w bazie:", total_missing)

# B) Sprawdzanie zakresu danych numerycznych i poprawa wartości spoza (0, 15)
def correct_values(column, method='mean'):
    valid_values = column[(column > 0) & (column < 15)]  
    replacement = valid_values.mean() if method == 'mean' else valid_values.median()
    column = column.apply(lambda x: replacement if x <= 0 or x >= 15 else x)  
    return column

for col in df.select_dtypes(include=[np.number]).columns:
    df[col] = correct_values(df[col], method='mean')  

print("\nB) Dane numeryczne zostały poprawione (wartości spoza zakresu 0-15 zastąpiono średnią)")

# C) Sprawdzanie poprawności nazw gatunków

valid_species = {"Setosa", "Versicolor", "Virginica"}

invalid_species = df[~df['variety'].isin(valid_species)]['variety'].unique()

print("\nC) Sprawdzanie poprawności gatunków")
if len(invalid_species) > 0:
    print("Niepoprawne wartości w kolumnie 'species':", invalid_species)

    # Metoda poprawiania - użycie najbliższego dopasowania (można dostosować)
    def correct_species(name):
        name = name.strip().capitalize()  # Usuwamy spacje i poprawiamy wielkość liter
        if name in valid_species:
            return name
        elif "set" in name.lower():
            return "Setosa"
        elif "ver" in name.lower():
            return "Versicolor"
        elif "vir" in name.lower():
            return "Virginica"
        else:
            return "Unknown"  # Jeśli nie da się poprawić, oznacz jako "Unknown"

    df['variety'] = df['variety'].apply(correct_species)
    print("Niepoprawne gatunki zostały poprawione.")

else:
    print("Wszystkie gatunki są poprawne.")

### **Wyświetlenie pierwszych wierszy poprawionych danych**
print("\n=== Podgląd poprawionych danych ===")
print(df.head())

# Opcjonalnie: zapis do nowego pliku
df.to_csv("iris_cleaned.csv", index=False)
