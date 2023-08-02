import pandas as pd

file_path = "chocolate_database.ods"
df = pd.read_excel(file_path, engine='odf')

df['Ingredients'].fillna('empty', inplace=True)
df.dropna(subset=['Ingredients'], inplace=True)

contains_lecithin = df[df['Ingredients'].str.contains('L')]
does_not_contain_lecithin = df[~df['Ingredients'].str.contains('L')]

mean_rating_contains_lecithin = contains_lecithin['Rating'].mean()
mean_rating_does_not_contain_lecithin = does_not_contain_lecithin['Rating'].mean()

print("Lesitin İçeren Barların Ortalama Puanı:", mean_rating_contains_lecithin)
print("Lesitin İçermeyen Barların Ortalama Puanı:", mean_rating_does_not_contain_lecithin)
