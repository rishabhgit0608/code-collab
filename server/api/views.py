from django.shortcuts import render,HttpResponse
from api.API_logic.question_scrape import question_scrap_helper
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def question_scrap(req):
    print("Hello world")
    url = "https://codeforces.com/problemset/problem/1972/B"
    question_scrap_helper(url)
    return HttpResponse("Online ")
    