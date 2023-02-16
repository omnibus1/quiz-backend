from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Quiz,Question,Answer
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import QuizSerializer,QuestionSerializer
from rest_framework import generics
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

# Create your views here.


@api_view(["GET","POST"])
def api_home(request,*args,**kwargs):
    data={}
    serializer=QuizSerializer(data=request.data)
    print(request.data)
    if serializer.is_valid(raise_exception=True):
        instance=serializer.save()
        print(instance)
        data=serializer.data
        
    
    return Response(data)


class QuizDetailAPIView(generics.RetrieveAPIView):
    queryset=Quiz.objects.all()
    serializer_class=QuizSerializer

class QuizCreateAPIView(generics.CreateAPIView):
    queryset=Quiz.objects.all()
    serializer_class=QuizSerializer

class QuizListCreateAPIView(generics.ListCreateAPIView):
    queryset=Quiz.objects.all()
    serializer_class=QuizSerializer

@api_view(["GET","POST"])
def quiz_alt_view(request,pk=None,*args,**kwargs):
    method=request.method
    if method == "GET":
        if pk is not None:
            object=get_object_or_404(Quiz,pk=pk)
            data=QuizSerializer(object).data
            return Response(data)
        else:
            queryset=Quiz.objects.all()
            data=QuizSerializer(queryset,many=True).data
            return Response(data)
    if method == "POST":
        serializer=QuizSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response({"invalid":"error when creating the object"},status=400)

@api_view(["GET"])
def test(request,*args,**kwargs):
    json=request.data
    print(json)
    quiz=Quiz.objects.order_by('?')[0]
    data=QuizSerializer(quiz).data
    return Response(data)