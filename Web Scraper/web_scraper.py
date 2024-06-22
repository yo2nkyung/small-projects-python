import csv
import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("The fetch was successful :)")
            return response.text
        else:
            print(f"Failed to fetch. Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    extracted_data = []
    for a_tag in soup.find_all('a', "gPFEn"):
        title = a_tag.get_text().strip()
        link = a_tag.get('href')
        if title and link:
            extracted_data.append({'title': title, 'link': link})
    
    return extracted_data

def save_to_csv(extracted_data, output_file):
    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile: #newline='' 한 줄 띄기 해제
            fieldnames = ['title', 'link']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader() #header
            for item in extracted_data:
                writer.writerow(item)
        print(f"Extracted data are saved in {output_file}.")
    except IOError as e:
        print(f"Error occurred while saving the file: {e}")



url = "https://news.google.com/home?hl=ko&gl=KR&ceid=KR%3Ako"
html_content = fetch_html(url)

if html_content:
    extracted_data = parse_html(html_content)
    for item in extracted_data:
        print(f"Title: {item['title']}, Link: {item['link']}")

save_to_csv(extracted_data, 'scraping_result.csv')