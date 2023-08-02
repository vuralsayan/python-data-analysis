import pandas as pd

# ODS dosyasını okuma
dosya_yolu = "chocolate_database.ods"
df = pd.read_excel(dosya_yolu, engine='odf')

# Her bir çekirdek orijini için ortalama reytingi hesaplama
ortalama_reytingler = df.groupby('Country of Bean Origin')['Rating'].mean()

# En yüksek ve en düşük ortalama reytinge sahip çekirdek orijinlerini bulma
en_yuksek_ortalama = ortalama_reytingler.idxmax()
en_yuksek_ortalama_reyting = ortalama_reytingler.max()

en_dusuk_ortalama = ortalama_reytingler.idxmin()
en_dusuk_ortalama_reyting = ortalama_reytingler.min()

# Sonuçları ekrana yazdırma
print("En yüksek ortalama reytinge sahip çekirdek orijini:", en_yuksek_ortalama, "-", en_yuksek_ortalama_reyting)
print("En düşük ortalama reytinge sahip çekirdek orijini:", en_dusuk_ortalama, "-", en_dusuk_ortalama_reyting)
