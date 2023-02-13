import requests
import re
from bs4 import BeautifulSoup

def get_results_from_google(keyword):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.3'}
    url = f"https://www.google.com/search?q={keyword}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    results = []
    for g in soup.find_all("div", class_="r"):
        anchors = g.find_all("a")
        if anchors:
            link = anchors[0]["href"]
            title = g.find("h3").text
            item = {"title": title, "link": link}
            results.append(item)
    return results

def get_keyword_overlap(keywords):
    all_results = {}
    for keyword in keywords:
        results = get_results_from_google(keyword)
        all_results[keyword] = results
    overlap = {}
    for i, keyword1 in enumerate(keywords[:-1]):
        for keyword2 in keywords[i+1:]:
            k1_results = set([r['link'] for r in all_results[keyword1]])
            k2_results = set([r['link'] for r in all_results[keyword2]])
            common_results = k1_results & k2_results
            overlap[f"{keyword1} & {keyword2}"] = list(common_results)
    return overlap

def get_average_position(keyword):
    results = get_results_from_google(keyword)
    if not results:
        return 0
    positions = [i + 1 for i in range(len(results))]
    avg_position = sum(positions) / len(positions)
    return avg_position

keywords = ["keyword1", "keyword2", "keyword3"]
overlap = get_keyword_overlap(keywords)
for keywords, links in overlap.items():
    print(f"{keywords}: {links}")

for keyword in keywords:
    avg_position = get_average_position(keyword)
    print(f"{keyword}: {avg_position}")
