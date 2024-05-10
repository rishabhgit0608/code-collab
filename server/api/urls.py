from django.urls import path
from api.views import question_scrap
urlpatterns = [
    path("",view=question_scrap,name="question_scrap"),
]