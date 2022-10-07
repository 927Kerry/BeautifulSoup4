from bs4 import BeautifulSoup
import requests
import re

url = "https://coinmarketcap.com/"
url2 ="https://www.scan.co.uk/shop/computer-hardware/gpu-amd-gaming/amd-radeon-rx-6700-xt-pcie-40-graphics-cards"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

tbody = doc.tbody
trs = tbody.contents

# print(list(trs[0].children))


prices = {}

for tr in trs[:10]:
    name, price = tr.contents[2:4]
    fixed_name = (name.p.string)
    fixed_price = (price.a.string)

    prices[fixed_name] = fixed_price

print(prices)
