from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .api_logic.question_scrap_helper import question_scrap_helper  # Assuming question_scrap_helper is a function you've defined

@csrf_exempt
def question_scrap(req):
    question_scrap_helper("https://codeforces.com/problemset/problem/1972/B")
        
    return HttpResponse("Online and up and running")