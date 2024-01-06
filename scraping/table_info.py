from bs4 import BeautifulSoup
import requests


def get_table_rows():
    URL = "https://aethergazer.miraheze.org/wiki/Characters#List__View-0"
    html_doc = requests.get(URL).text
    soup = BeautifulSoup(html_doc, 'html.parser')
    table_rows = soup.find_all("tr")
    return table_rows

def get_character_imgs(table_rows): 
    imgs = []
    for tr in table_rows:
        if tr.find("img") != None:
            imgs.append(tr.find("img")["src"])
    return set(imgs)

def convert_to_url(imgs): 
    urls = []
    for img in imgs:
        urls.append("https:" + img)
    return urls

def download_imgs(): 
    imgs = convert_to_url(get_character_imgs())
    for img in imgs:
        img_data = requests.get(img).content
        with open('imgs/' + img.split("/")[-1], 'wb') as handler:
            handler.write(img_data)

def get_names(table_rows): 
    names = []
    for tr in table_rows:
        td = tr.find_all("td")
        if len(td) == 4:
            names.append(td[1].text.strip())
    return names

def get_ranks(table_rows): 
    ranks = []
    for tr in table_rows:
        td = tr.find_all("td")
        if len(td) == 4:
            ranks.append(td[2].find("img")["alt"])
    return ranks 

def get_factions(table_rows): 
    factions = []
    for tr in table_rows:
        td = tr.find_all("td")
        if len(td) == 4:
            if td[3].find("img") != None:
                factions.append(td[3].find("img")["alt"])
            else: 
                factions.append(td[3].text.strip())
    return factions

if __name__ == "__main__":
    table_rows = get_table_rows()
    names = get_names(table_rows)
    ranks = get_ranks(table_rows)
    factions = get_factions(table_rows)	

    for i in range(len(names)):
        print("name: ", names[i])
        print("rank: ", ranks[i])
        print("faction:",factions[i])
        print()
