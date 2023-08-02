import pandas as pd
import matplotlib.pyplot as plt

# ODS dosyasını okuma
dosya_yolu = "chocolate_database.ods"
df = pd.read_excel(dosya_yolu, engine='odf')

# Kakao çekirdeği kökenine göre gruplama ve ortalama puanı hesaplama
ortalama_puanlar = df.groupby('Country of Bean Origin')['Rating'].mean()

# Köken ve ortalama puanları içeren yeni bir DataFrame oluşturma
df_ortalama_puanlar = pd.DataFrame({'Country of Bean Origin': ortalama_puanlar.index, 'Average Rating': ortalama_puanlar.values})

# Görselleştirme
plt.figure(figsize=(12, 6))
plt.bar(df_ortalama_puanlar['Country of Bean Origin'], df_ortalama_puanlar['Average Rating'])
plt.xticks(rotation=90)
plt.xlabel('Country of Bean Origin')
plt.ylabel('Average Rating')
plt.title('Average Rating by Bean Origin')
plt.show()
