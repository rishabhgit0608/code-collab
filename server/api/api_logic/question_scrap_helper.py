import requests
import logging
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def question_scrap_helper(url):
    try:
        logger.log(logging.INFO,"started fetching")
        page_response = requests.get(url)
        logger.log(logging.INFO,"Started souping:-   ")
        soup= BeautifulSoup(page_response.text,"html.parser")
        targetted_div = soup.find("div",class_="problem-statement")
        print(targetted_div)
        
    except Exception as e:
        logging.error(e)