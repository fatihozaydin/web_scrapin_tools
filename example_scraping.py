import requests
from bs4 import BeautifulSoup
import time


def webPriceControl():
    url = 'https://www.amazon.com.tr/HP-Diz%C3%BCst%C3%BC-Bilgisayar-i5-13500H-7N9V3EA/dp/B0BYJWZKYH/ref=pd_lpo_sccl_3/260-2542957-8791227?pd_rd_w=rbTpQ&content-id=amzn1.sym.3ccffe31-2ea8-4a71-b7f5-6a5dec6480b7&pf_rd_p=3ccffe31-2ea8-4a71-b7f5-6a5dec6480b7&pf_rd_r=6AGDGGMCWMMZX1Y7MTQ8&pd_rd_wg=ggowq&pd_rd_r=1e7ce6d9-6e84-4820-8c08-03d13e818973&pd_rd_i=B0BYJWZKYH&psc=1'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}
    page = requests.get(url, headers=headers)
    content = BeautifulSoup(page.content, 'html.parser')

    productName = content.find(id='productTitle').get_text().strip()
    productPrice = content.find(id='corePriceDisplay_desktop_feature_div').get_text().strip()
    priceChange = int(productPrice[4:10].replace('.',''))

    if(priceChange < 29000):
        print(f"{priceChange} TL {productName} fiyat dustu hemen al")
    else:
        print(f"{priceChange} TL {productName} fiyat henüz düşmedi")

webPriceControl()

while True:
    webPriceControl()
    time.sleep(5)
