from bs4 import BeautifulSoup
import requests

URL = r"https://helbase.com/guide/insights-on-warp-enhancements/"
doc = requests.get(URL)
soup = BeautifulSoup(doc.content, "html.parser")

skill_names = soup.find_all("div", class_="etitle")
[print(name.text) for name in skill_names]