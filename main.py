import requests
from bs4 import BeautifulSoup

def company_reader(filename:str)->list:
    print(f" reading companies in {filename}")
    companies = []
    try:
        with open(filename,'r') as file:
            for item in file:
                strip = item.rstrip('\n')
                companies.append(strip)
            print(companies) 
    except Exception as e:
        print("An error occured:", str(e))
    return companies
        

def grabs_url(company_reader)->str:
    print(f"accessing {company_reader}")
    list = company_reader
    for url in list:
        print(url)
        page = requests.get(f'https://www.google.com/search?q={url}')
        print(page.status_code) 
        soup = BeautifulSoup(page.text,'html.parser')
        soup.prettify()
        # print(soup.find_all('a'))
        for link in soup.find_all('a'):
            links = (link.get('href'))
            print(links)
    return links



if __name__ == "main":
    print("Initialising")
    
    
    