import requests
from bs4 import BeautifulSoup
import re
from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service


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
        

def grabs_page(company)->str:
    print(f"accessing {company}")
    page = requests.get(f'https://www.google.com/search?q={company}')
    response = page.text
    if page.status_code == 200:
        print("process is successful")
    elif page.status_code == 404:
        print("not found")
    return response

def all_url_links(response):
    links = []
    soup = BeautifulSoup(response,'html.parser')
    for link in soup.find_all('a'):
        links.append(link.get('href'))

    return links
            
def facebook_link(links):
    try:
        for link in links:
            if 'facebook' in link:
                slicer=slice(7,-86)
                sliced = link[slicer]
                print(f" --->   {sliced}")
                return sliced.replace('&s','')
    except Exception as e:
        print("an error occured: ",str(e))
    return 'not found'
 
def get_facebook_page(facebook_link):
    print(f'connecting to {facebook_link}')
    # options = Options()
    # options.binary_location = r'/usr/bin/firefox'
    # service = Service('/bin/firefox.geckodriver')
    # browser = webdriver.Firefox()
    browser = webdriver.Chrome()
    browser.get(facebook_link)
    browser.quit()
    # page = requests.get(facebook_link)
    # facebook_page = page.text
    # return facebook_page
    # session = HTMLSession()
    # r = session.get(facebook_link)
    # rendered = r.html.render(sleep=1,keep_page=True,scrolldown=1)
    # print(rendered)


def pick_phonenumber(facebook_page):
    phone_pattern = "\d{3}\s\d{7}"
    print(re.match(phone_pattern,facebook_page))



if __name__ == "main":
    print("Initialising")
    
    
    