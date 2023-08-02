import pandas as pd

# ODS dosyasını okuma
dosya_yolu = "chocolate_database.ods"
df = pd.read_excel(dosya_yolu, engine='odf')

# Şirketlerin lokasyonlarına göre gruplama ve sayma
lokasyon_sayilari = df.groupby('Company Location')['Company Location'].count()

# Şirket sayılarına göre büyükten küçüğe sıralama
lokasyon_sayilari = lokasyon_sayilari.sort_values(ascending=False)

# Sonuçları yazdırma
print(lokasyon_sayilari)
