from django.contrib import admin
from api.models import Questions
# Register your models here.

class QuestionsAdmin(admin.ModelAdmin):
    list_display = ['question_title','question_description']


admin.site.register(Questions,QuestionsAdmin)