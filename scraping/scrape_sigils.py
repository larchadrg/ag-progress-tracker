from bs4 import BeautifulSoup
import requests
from download_imgs import download_imgs
import csv 
import os 

URL = "https://www.bluestacks.com/blog/game-guides/aether-gazer/azr-sigils-guide-en.html"
html_doc = requests.get(URL).text 
soup = BeautifulSoup(html_doc, 'html.parser')

sigils = soup.find_all("h4")[:-1]
sigil_names = [sigil.text for sigil in sigils]
sigil_names.insert(23, "King of Conquest’s Anabasis")
sigil_names.sort()


sigils = soup.find_all("img", {"width": "150"})
sigil_images = [sigil["src"] for sigil in sigils]
sigil_images = [name.replace(" ", "_").lower() for name in sigil_images]


directorio = r'C:\Users\larac\Documents\ag-progress-tracker\app\static\images\sigils'
img_names = os.listdir(directorio)

data = [{"name": name, "image": img} for name, img in zip(sigil_names, img_names)]
csv_file_path = 'sigils.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        # Define the CSV header based on the keys in the dictionaries
        fieldnames = ["name", "image"]
        # Create a CSV writer object
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # Write the header
        csv_writer.writeheader()
        # Write the data
        csv_writer.writerows(data)

        print(f"Data has been written to {csv_file_path}")


#print(len(sigil_images))
#print(len(sigil_names))

#download_imgs(sigil_images, sigil_names)

