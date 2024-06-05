import requests
from bs4 import BeautifulSoup
import re
from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service



def company_reader(filename:str)->list:
    # print(f" reading companies in {filename}")
    companies = []
    try:
        with open(filename,'r') as file:
            for item in file:
                strip = item.rstrip('\n')
                companies.append(strip)
            # print(companies) 
    except Exception as e:
        print("An error occured:", str(e))
    return companies
        

def grabs_page(company)->str:
    try:
        page = requests.get(f'https://www.google.com/search?q={company}')
        response = page.text
        if page.status_code == 200:
            print("page found")
        elif page.status_code == 404:
            print("not found")
    except Exception as e:
        print(f'an error has occured {e}')
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
                # print(f" --->   {sliced}")
                return sliced.replace('&s','')
    except Exception as e:
        print("an error occured: ",str(e))
    return 'not found'
 
def get_facebook_page(facebook_link):
    options = Options()
    options.headless = True
    # options.binary_location = r'/usr/bin/firefox'
    # service = Service('/bin/firefox.geckodriver')
    # browser = webdriver.Firefox()
    service = Service(executable_path=r'/usr/bin/chromedriver')
    browser = webdriver.Chrome(service=service, options=options)
    browser.get(facebook_link)
    facebook_page = browser.page_source
    # print(facebook_page)
    browser.quit()
    return facebook_page
    # page = requests.get(facebook_link)
    # facebook_page = page.text
    # return facebook_page
    # session = HTMLSession()
    # r = session.get(facebook_link)
    # rendered = r.html.render(sleep=1,keep_page=True,scrolldown=1)
    # print(rendered)


def pick_phonenumber(facebook_page):
    pattern = r'\d{3,4}\s\d{6,7}'
    phonenumber = re.findall(pattern,facebook_page)
    # print(f"----> {matches}")
    return phonenumber

def formatting(matches):
    contact_value = matches[0]
    return contact_value


def result_panel(company,contact_value):
    results = {company:contact_value}
    return results


if __name__ == "main":
    print("Initialising")
    
    
    