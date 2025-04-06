import pandas as pd

# Lire le fichier parquet
df = pd.read_parquet('data/yellow-taxi.parquet')

# Calculer la moyenne de la colonne 'fare_amount'
average_fare = df['fare_amount'].mean()

# Afficher la moyenne (juste pour confirmation)
print(f"Moyenne du montant de la course: {average_fare}")

# Enregistrer le résultat dans un fichier texte
with open('results/resultat_moyenne.txt', 'w') as f:
    f.write(f"Moyenne du montant de la course: {average_fare}\n")
