import requests
from bs4 import BeautifulSoup

url="https://www.bbc.com/news"
response = requests.get(url)


Soup = BeautifulSoup(response.text, "html.parser")
headlines = []


for h in Soup.find_all("h2"):
    text = h.get_text(strip=True)
    if text:
        headlines.append(text)


Page_title = Soup.title.string if Soup.title else None

if Page_title:
    headlines.insert(0,Page_title)



with open("headlines.txt", "w", encoding= "utf-8") as f:
    for i, title in enumerate(headlines, start=1):
        f.write(f"{i}. {title}\n")


print("Headines have been saved to headlines.txt")

