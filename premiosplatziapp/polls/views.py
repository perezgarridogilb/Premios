import re
from django.shortcuts import render, redirect, get_object_or_404
# from django.http import HttpResponse, HttpResponseRedirect
# Utilizamos generic views / views based class
from django.views import generic

from .models import Question, Choice

# Function Based Views.


def index(request):
    latest_question_list = Question.objects.all()
    return render(request, "polls/index.html", {
        # De esta manera va a estar dispobible en el index.html
        "latest_question_list": latest_question_list
    })
"""
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {
        "question": question
    })

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {
        "question": question
    })
"""

# Con view hacemos indicar que es basado en clases
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"
    
    def get_queryset(self):
        """Return the last five publised questions"""
        # -pub_date: Ordenar desde las más recientes a las más antiguas
        return Question.objects.order_by("-pub_date")[:5]
    
    
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
    
class ResultView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    # Intentamos acceder a una llave que no existe    
    except (KeyError, Choice.DoesNotExist):
       return render(request, "polls/detail.html", {
           "question": question,
           "error_message": "No elegiste una respuesta"
       })
    else:
        # Ya era un atributo que nosotros definimos en el modelo de choices
        selected_choice.votes += 1
        selected_choice.save()
        # Redirect: se asegura que el usuario no envíe la información dos veces en el formulario
        # args: Argumentos en la URL
        # return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))
        return redirect("polls:results", question.id)
