from bs4 import BeautifulSoup
import requests
import re

with open("beautifulsoup4/index2.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

url = "https://www.gladiatorpc.co.uk/"

url2 ="https://www.scan.co.uk/shop/computer-hardware/gpu-amd-gaming/amd-radeon-rx-6700-xt-pcie-40-graphics-cards"


result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser") 

tags = doc.find_all(text=re.compile("\£.*"))
for tag in tags:
    print(tag.strip())
# print(tag.attrs)
