from django.urls import path
from api.views import question_scrap
urlpatterns = [
     path("",question_scrap)
]
