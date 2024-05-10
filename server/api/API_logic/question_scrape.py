import requests
from bs4 import BeautifulSoup

def question_scrap_helper(url):
    response = requests.get(url)
    if response.status_code ==  200:
        soup = BeautifulSoup(response.text,'html.parser')
        targeted_div = soup.find('div',class_="problem-statement")
        print(targeted_div.getText())
    
    