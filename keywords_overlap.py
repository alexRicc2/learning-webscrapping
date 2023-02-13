import requests
from bs4 import BeautifulSoup
import collections

def search_google(keyword):
  # Faz a busca no Google e retorna o conteúdo da página
  url = f"https://www.google.com/search?q={keyword}"
  response = requests.get(url)
  return response.text

def extract_results(html):
  # Extrai os resultados da página HTML
  soup = BeautifulSoup(html, "html.parser")
  results = []
  for item in soup.find_all("div", class_="g"):
    link = item.find("a")["href"]
    results.append(link)
  return results

def calculate_overlap(results1, results2):
  # Calcula a interseção entre os resultados
  return len(set(results1) & set(results2))

def calculate_position(results, keyword):
  # Calcula a posição média dos resultados para uma keyword
  positions = [i + 1 for i, result in enumerate(results) if keyword in result]
  if positions:
    return sum(positions) / len(positions)
  else:
    return 0

def main():
  keywords = ["keyword1", "keyword2", "keyword3"]
  results = {}
  for keyword in keywords:
    html = search_google(keyword)
    results[keyword] = extract_results(html)
  overlap = {}
  for i, keyword1 in enumerate(keywords):
    for j, keyword2 in enumerate(keywords[i+1:]):
      overlap[f"{keyword1} - {keyword2}"] = calculate_overlap(results[keyword1], results[keyword2])
  positions = {}
  for keyword in keywords:
    positions[keyword] = calculate_position(results[keyword], keyword)
  print("Overlap:", overlap)
  print("Positions:", positions)

if __name__ == "__main__":
  main()
