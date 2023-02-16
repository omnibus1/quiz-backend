from rest_framework import serializers
from .models import Quiz,Question,Answer



class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Answer
        fields=['text','answer']

class QuestionSerializer(serializers.ModelSerializer):
    answers=AnswerSerializer(many=True,read_only=True)

    class Meta:
        model=Question
        fields=['question_text','answers']

class QuizSerializer(serializers.ModelSerializer):
    questions=QuestionSerializer(many=True,read_only=True)
    class Meta:
        model=Quiz
        fields=['title','questions']