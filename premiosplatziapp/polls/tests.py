import datetime
from pickle import FALSE

from django.test import TestCase
from django.utils import timezone

from .models import Question

"""
TestCase es una clase que viene del módulo test de Django que nos
permite definir una batería de test (es un conjunto de test que se 
corresponden a un aspecto particular de nuestra aplicación).

Estos tests se van a suceder sobre el modelo Question (es por eso 
el nombre de la clase).

Generalmente cuando estemos haciendo nuestras aplicaciones vamos a
testear:
- Modelos
- Vistas
- Más cosas (menos común)

"""

# Hereda de TestCase
class QuestionModelTests(TestCase):
    
    # Método con el nombre del test que nosotros vamos a ejecutar: Tiene un nombre descriptivo 
    # (esta es la manera en que definimos test en el archivo tests.py de Django)
    def test_was_published_recently_with_future_questions(self):
        """
        was_published_recently returns False for questions whose pub_date is in the future
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text="¿Quién es el mejor Course Director de Platzi?", pub_date=time)
        # Verificar que el resultado de aplicar el método was_published_recently() sobre future_question es igual a falso
        self.assertIs(future_question.was_published_recently(), False)