from bs4 import BeautifulSoup
import requests

url = "https://commerce-roan-nine-15.vercel.app/"
result = requests.get(url)

with open ("index.html", "r") as f:
  doc2 = BeautifulSoup(f, "html.parser")

text = doc2.find_all("p")

doc = BeautifulSoup(result.text, "html.parser")
prices = doc.find_all("span").encode("utf-8")
  
print(prices)