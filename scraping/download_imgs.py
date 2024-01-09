import requests 

def convert_to_url(imgs): 
    urls = []
    for img in imgs:
        urls.append("https:" + img)
    return urls

def download_imgs(img_list, name_list): 
    for i in range(len(img_list)):
        img_name = name_list[i].replace(" ", "_").lower()
        img_data = requests.get(img_list[i]).content
        directory = r"C:\Users\larac\Documents\ag-progress-tracker\app\static\images"
        with open(directory + img_name + ".png", 'wb') as handler:
            handler.write(img_data)