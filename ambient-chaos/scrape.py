import os
import requests
from bs4 import BeautifulSoup

def download_file(url, folder, file_name):
    response = requests.get(url)
    if response.status_code == 200:
        with open(f"{folder}/{file_name}", "wb") as f:
            f.write(response.content)
            print(f"{file_name} Downloaded 😅")
    else:
        print(f"Failed to download {file_name}")

url = "https://neal.fun/ambient-chaos/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    title_elements = soup.find_all("div", class_="title-mobile")
    titles = [element.text.strip().lower().replace(" ", "-") for element in title_elements]
else:
    print("Failed to retrieve the webpage.")

# Create the folders 
if not os.path.exists('audio'):
    os.makedirs('audio')
if not os.path.exists('svg'):
    os.makedirs('svg')

for title in titles:
    mp3_url = f"https://neal.fun/ambient-chaos/sounds/{title}.mp3"
    svg_url = f"https://neal.fun/ambient-chaos/icons/{title}.svg"

    download_file(mp3_url, 'audio', f"{title}.mp3")
    download_file(svg_url, 'svg', f"{title}.svg")
