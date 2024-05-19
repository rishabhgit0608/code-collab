from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .api_logic.question_scrap_helper import question_scrap_helper  # Assuming question_scrap_helper is a function you've defined
import json
import logging


@csrf_exempt
def question_scrap(req):
    try:
        
        body = json.loads(req.body)
        response = question_scrap_helper(body["url"])
            
        return JsonResponse(response, safe=False)
    except Exception as e:
        logging.info("Question cannot be scraped")