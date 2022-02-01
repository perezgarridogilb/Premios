import datetime

from django.db import models
from django.utils import timezone

# Hereda de models
class Question(models.Model):
    # Identificador en automático
    question_text = models.CharField(max_length=200)
    # Nombre sencillo a la lectura
    pub_date = models.DateField("date published")
    
    def __str__(self):
        return self.question_text
    
    # Fue publicada recientemente (timedelta es un objeto que define la diferencia de tiempo)
    # Le resta al tiempo actual un día
    def was_published_recently(self):
        return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
class Choice(models.Model):
    # Llave foránea de  question
    # Question (es el constructor)
    # models.CASCADE: Cada vez que borremos una pregunta se borran sus Choices de la misma
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
    
