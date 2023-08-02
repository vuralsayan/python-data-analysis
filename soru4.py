import pandas as pd

# ODS dosyasını okuma
dosya_yolu = "chocolate_database.ods"
df = pd.read_excel(dosya_yolu, engine='odf')

# İnceleme yılını çıkarma
df['Review Year'] = pd.to_datetime(df['Review Date'], format='%Y').dt.year

# En fazla incelemenin yapıldığı yılı bulma
en_fazla_inceleme_yili = df['Review Year'].value_counts().idxmax()
en_fazla_inceleme_sayisi = df['Review Year'].value_counts().max()

# Sonucu yazdırma
print("En fazla incelemenin yapıldığı yıl:", en_fazla_inceleme_yili)
print("En fazla inceleme sayısı:", en_fazla_inceleme_sayisi)
