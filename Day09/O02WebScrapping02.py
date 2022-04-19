
from bs4 import BeautifulSoup
import requests

html_txt = requests.get("https://www.keepinspiring.me/famous-quotes/")
print(html_txt)

soup = BeautifulSoup(html_txt.text, "lxml")

res = soup.findAll("cite")
print(res)
