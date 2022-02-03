from django.contrib import admin
from .models import Choice, Question

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

# Modelo que registramos
class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]
    # StackedInline Clases
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
