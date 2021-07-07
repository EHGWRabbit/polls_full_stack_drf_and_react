from django.urls import path
from .views import ListPersonQuestion, DetailPersonQuestion 
from .views import ListUserQuestion, DetailUserQuestion
from .views import ListSelectAnswer, DetailSelectAnswer
from .views import ListFullMessages, DetailFullMessages
from .views import ListCopy, DetailCopy

urlpatterns = [
    path('<int:pk>/', DetailPersonQuestion.as_view()),
    path('', ListPersonQuestion.as_view()),
    path('', DetailUserQuestion.as_view()),
    path('', ListUserQuestion.as_view()),
    path('', DetailSelectAnswer.as_view()),
    path('', ListSelectAnswer.as_view()),
    path('', DetailFullMessages.as_view()),
    path('', DetailFullMessages.as_view()),
    path('', DetailCopy.as_view()),
    path('', DetailCopy.as_view()),
    ]