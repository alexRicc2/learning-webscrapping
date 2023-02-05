from bs4 import BeautifulSoup
import requests

url = "https://commerce-roan-nine-15.vercel.app/"
result = requests.get(url)

with open ("index.html", "r") as f:
  soup = BeautifulSoup(f, "lxml")

courses_cards = soup.find_all('div', class_='card')
for card in courses_cards:
  course_name = card.h5.text
  course_price = card.button.text.split()[-1]

  print(f'{course_name} costs {course_price}')


  
