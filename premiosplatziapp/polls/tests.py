import datetime
from pickle import FALSE
from urllib import response

from django.test import TestCase
from django.urls.base import reverse
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
        
    def test_was_published_last_time(self):
        """
        was_published_last_time returns True for questions whose pub_date is in the past time
        """
        time = timezone.now() - datetime.timedelta(days=30)
        last_question = Question(question_text="¿Quién es el mejor Course Director de Platzi?", pub_date=time)
        # Verificar que el resultado de aplicar el método was_published_last_time() sobre last_question es igual a verdad
        self.assertIs(last_question.was_published_last_time(), True)
        
def create_question(question_text, days):
    """
    Create a question with the given "question_text", and published the given
    number of days offset to now (negative for questions published in the past, 
    positive for questions that have yet to be published)
    """
    time = timezone.now() + datetime.timedelta(days=days)
    # Creamos preguntas de manera simple sin necesidad de repetir código (cumplimos con el principio "don't repeat your self")
    return Question.objects.create(question_text=question_text, pub_date=time)
        
# Hacemos una nueva batería
class QuestionIndexViewTests(TestCase):
    # reverse: equivalente a la directiva url (no hardcodear y ponerlo de manera variable)
    def test_no_questions(self):
        """If no question exist, an appropiate message is displayed""" 
        # Hacemos una petición get
        response = self.client.get(reverse("polls:index")) 
        # Se afirma que son iguales
        self.assertEqual(response.status_code, 200) 
        # Verificamos que no aparezca en la página si es que tenemos preguntas
        self.assertContains(response, "No polls are available.")
        # Verificamos que no existan respuestas, es decir, que latest_question_list sea una lista vacía
        self.assertQuerysetEqual(response.context["latest_question_list"], [])
        
    def test_future_question(self):
        """
        Questions with a pub_date in the future aren't displayed on the index page.
        """
        create_question("Future question", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])
    
    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the index page
        """
        question = create_question("Past question", days=-10)
        response = self.client.get(reverse("polls:index"))
        # Verificamos que lo que contenga adentro es a una pregunta (de create_question)
        self.assertQuerysetEqual(response.context["latest_question_list"], [question])
     
    # Funcionamiento correcto de nuestro index cuando publicamos una pregunta en el futuro y pasado    
    def test_future_question_and_past_question(self):
        """
        Event if both past and future question exist, only past questions are displayed
        """
        past_question = create_question(question_text="Past question", days=-30)
        future_question = create_question(question_text="Future question", days=30)
        response = self.client.get(reverse("polls:index")) 
        # Verificamos que también se haya publicado past_question       
        self.assertQuerysetEqual(
                response.context["latest_question_list"],
                [past_question]
            )
        
    # Verificamos el funcionamiento correcto de nuestro index cuando publicamos dos preguntas en el pasado
    def test_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        past_question1 = create_question(question_text="Past question 1", days=-30)
        past_question2 = create_question(question_text="Past question 2", days=-40)
        response = self.client.get(reverse("polls:index"))  
        # Verificamos que también se hayan publicado las past_question         
        self.assertQuerysetEqual(
                response.context["latest_question_list"],
                [past_question1, past_question2]
        )
        
    # Reto para las dos preguntas en el futuro
    def test_two_future_questions(self):
        create_question(question_text="Future question", days=30)
        create_question(question_text="Future question", days=30)
        response = self.client.get(reverse("polls:index")) 
        self.assertQuerysetEqual(
            response.context["latest_question_list"],
            []
        )
    

# Vamos a hacer tests detail view a partir del modelo question
class QuestionDetailViewTests(TestCase):
    # Dos tests para verificar
    
    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future
        returns a 404 error not found
        """
        future_question = create_question(question_text="Future question", days=30)
        # id y pk son lo mismo, además de una coma ", " para que to interprete como una tupla
        url = reverse("polls:detail", args=(future_question.pk,))
        response = self.client.get(url)
        # Si es 404 el test es aprobado
        self.assertEqual(response.status_code, 404)

        
    def past_future_question(self):
        """
        The detail view of a question with a pub_date in the future
        returns a 404 error not found
        """
        past_question = create_question(question_text="Past question", days=-30)
        # id y pk son lo mismo, además de una coma ", " para que to interprete como una tupla
        url = reverse("polls:detail", args=(past_question.pk,))
        response = self.client.get(url)
        # Verificar que en la respuesta del texto http existe el texto de la pregunta
        self.assertContains(response, past_question.question_text)
    
        
    
    