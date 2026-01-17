import requests
from bs4 import BeautifulSoup
import time
import json
import csv

def scrape_headlines(url, keyword=None):
    print(f"Fetching data from {url}")
    time.sleep(2)  # Respect robots.txt rate limits

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.find_all("h3")
    results = []

    for art in articles:
        title = art.get_text(strip=True)
        link = art.find_parent('a')['href'] if art.find_parent('a') else None

        if keyword and keyword.lower() not in title.lower():
            continue

        results.append({
            "title": title,
            "url": link,
            "time": time.strftime("%Y-%m-%d %H:%M:%S")
        })

    return results

def save_json(data, file):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Saved JSON: {file}")

def save_csv(data, file):
    with open(file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "url", "time"])
        writer.writeheader()
        writer.writerows(data)
    print(f"Saved CSV: {file}")

if __name__ == "__main__":
    results = scrape_headlines("https://www.bbc.com/news", keyword=None)
    save_json(results, "headlines.json")
    save_csv(results, "headlines.csv")
