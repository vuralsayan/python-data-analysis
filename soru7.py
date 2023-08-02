import pandas as pd

# ODS dosyasını okuma
dosya_yolu = "chocolate_database.ods"
df = pd.read_excel(dosya_yolu, engine='odf')

# Kakao çekirdeklerinin kökenlerini ve sayılarını hesapla
kakao_koken_sayilari = df['Country of Bean Origin'].value_counts()

# Kökenler ve sayıları içeren yeni bir DataFrame oluşturma
df_koken_sayilari = pd.DataFrame({'Country of Bean Origin': kakao_koken_sayilari.index, 'Count': kakao_koken_sayilari.values})

# Kökenlerin yanına sayıları yazdırma
for i, row in df_koken_sayilari.iterrows():
    koken = row['Country of Bean Origin']
    sayi = row['Count']
    print(f"{koken}: {sayi}")
