from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .api_logic.question_scrap_helper import question_scrap_helper  # Assuming question_scrap_helper is a function you've defined
import json

@csrf_exempt
def question_scrap(req):
    body = json.loads(req.body)
    response = question_scrap_helper(body["url"])
        
    return JsonResponse(response, safe=False)