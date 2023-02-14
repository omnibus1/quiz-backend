from django.urls import path

from . import views


urlpatterns=[
    path('',views.api_home),
    path('quizes/',views.quiz_alt_view),
    path('quizes/<int:pk>/',views.quiz_alt_view),
    path('<int:pk>/',views.QuizDetailAPIView.as_view()),
    path('create/',views.QuizCreateAPIView.as_view()),
    path('list/',views.QuizListCreateAPIView.as_view()),
]