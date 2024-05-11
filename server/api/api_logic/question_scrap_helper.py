import requests
import logging
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def clean_question(question):
    question_index_start = question.find("standard output")
    question_index_later = question.find("Input")
    question_stripped = question[question_index_start+len("standard output"):question_index_later].strip()
    index = question.find("time limit")
    return index, question_stripped


def question_scrap_helper(url):
    response = {}
    try:
        logger.log(logging.INFO,"started fetching")
        page_response = requests.get(url)
        logger.log(logging.INFO,"Started souping:-   ")
        soup= BeautifulSoup(page_response.text,"html.parser")
        targetted_div = soup.find("div",class_="problem-statement")
        question = targetted_div.getText()
        index, question_stripped= clean_question(question)
        response["title"] = question[:index].strip()
        response["question"] = question_stripped
        return response
        
        
    except Exception as e:
        logger.error(e)