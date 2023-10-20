import requests
from bs4 import BeautifulSoup

# Web sitesinden veriyi çekeceğimiz URL'yi belirleyin

url = 'https://example.com'


# Web sitesine GET isteği gönderin

response = requests.get(url)


# Sayfa içeriğini analiz etmek için BeautifulSoup kullanın

soup = BeautifulSoup(response.text, 'html.parser')


# Örneğin, tüm başlıkları (h1 etiketleri) çekelim

basliklar = soup.find_all('h1')


# Başlıkları ekrana yazdırın

for baslik in basliklar:
    print(baslik.text)
