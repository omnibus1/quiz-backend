from django.db import models

# Create your models here.
class Quiz(models.Model):
    title=models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Question(models.Model):
    question_text=models.TextField(blank=False)
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE,blank=False,related_name='questions')

    def __str__(self):
        return self.question_text

class Answer(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE,blank=False,related_name='answers')
    text=models.TextField(blank=False)
    answer=models.BooleanField(blank=False)
    def __str__(self):
        return "Pytanie: "+self.question.__str__()+", Odpowiedź "+self.text+": "+str(self.answer)