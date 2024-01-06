from bs4 import BeautifulSoup
import requests
import csv

relevant_info = [
    "name",
    "model",
    "rank", 
    "genzone", 
    "element",
    "image"
]

def get_table_rows():
    URL = "https://aethergazer.miraheze.org/wiki/Characters#List__View-0"
    html_doc = requests.get(URL).text
    soup = BeautifulSoup(html_doc, 'html.parser')
    table_rows = soup.find_all("tr")
    return table_rows


def get_character_pages(table_rows): 
    pages = []
    for tr in table_rows:
        td = tr.find_all("td")
        if len(td) == 4:
            pages.append(td[1].find("a")["href"])
    return pages

def get_character_info(page): 
    URL = "https://aethergazer.miraheze.org" + page + "?action=edit"
    html_doc = requests.get(URL).text
    soup = BeautifulSoup(html_doc, 'html.parser')
    textarea = soup.find("textarea")
    parsed_data = {}
    if textarea == None:
        return parsed_data
    text = textarea.text 

    # Split the data by lines and then by the pipe character
    for line in text.split('\n'):
        if '=' in line:
            key, value = line.split('=', 1)
            key = key.strip("|").strip().replace(" ", "_")
            value = value.strip().strip(":")
            if key == "image":
                value = value.replace(" ", "_")
            if key in relevant_info:
                parsed_data[key] = value
    return parsed_data 
    
def save_into_csv(filename: str): 
    data = []
    pages = get_character_pages(get_table_rows())
    for page in pages: 
        info = get_character_info(page)
        if info != {}:
            data.append(info)
            for key, value in info.items():
                print(key, value)
            print()

    csv_file_path = f'{filename}.csv'

    # Write the data to the CSV file
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        # Define the CSV header based on the keys in the dictionaries
        fieldnames = data[0].keys()
        
        # Create a CSV writer object
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write the header
        csv_writer.writeheader()
        
        # Write the data
        csv_writer.writerows(data)

    print(f"Data has been written to {csv_file_path}")


if __name__ == "__main__":
    save_into_csv("characters")
    """
    pages = get_character_pages(get_table_rows())
    for page in pages:
        info = get_character_info(page)
        if info != {}:
            for key, value in info.items():
                print(key, value)
            print()

    """