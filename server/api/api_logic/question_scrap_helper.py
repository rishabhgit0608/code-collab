import requests
import logging
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def question_scrap_helper(url):
    response = {}
    try:
        logger.log(logging.INFO,"started fetching")
        page_response = requests.get(url)
        logger.log(logging.INFO,"Started souping:-   ")
        soup= BeautifulSoup(page_response.text,"html.parser")
        targetted_div = soup.find("div",class_="problem-statement")
        question = targetted_div.getText()
        index = question.find("time limit")
        response["title"] = question[:index].strip()
        response["question"] = question
        return response
        
        
    except Exception as e:
        logger.error(e)