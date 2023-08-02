import pandas as pd

# ODS dosyasını okuma
dosya_yolu = "chocolate_database.ods"
df = pd.read_excel(dosya_yolu, engine='odf')

# Ülkelerin sahip olduğu bar sayılarını hesaplama
bar_sayilari = df.groupby('Company Location')['Specific Bean Origin or Bar Name'].count()

# Bar sayılarına göre büyükten küçüğe sıralama
bar_sayilari = bar_sayilari.sort_values(ascending=False)

# Sonuçları yazdırma
print(bar_sayilari)
