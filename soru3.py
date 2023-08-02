import pandas as pd

# ODS dosyasını okuma
dosya_yolu = "chocolate_database.ods"
df = pd.read_excel(dosya_yolu, engine='odf')

# Ülke kökenine göre ortalama puanı hesaplama
ortalama_puanlar = df.groupby('Country of Bean Origin')['Rating'].mean()

# Ortalama puanlara göre büyükten küçüğe sıralama
ortalama_puanlar = ortalama_puanlar.sort_values(ascending=False)

# Sonuçları yazdırma
print(ortalama_puanlar)
