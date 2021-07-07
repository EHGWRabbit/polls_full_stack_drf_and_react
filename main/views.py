from rest_framework import generics 
from .models import PersonQuestion, UserQuestion, SelectAnswer, FullMessages, Copy
from .serializers import PersonSerializer, UserSerializer, SelectAnswerSerializer
from .serializers import FullMessagesSerializer, CopySerializer

class ListPersonQuestion(generics.ListAPIView):
    queryset = PersonQuestion.objects.all()
    serializer_class = PersonSerializer

class DetailPersonQuestion(generics.RetrieveAPIView):
    queryset = PersonQuestion.objects.all()
    serializer_class = PersonSerializer

class ListUserQuestion(generics.ListAPIView):
    queryset = UserQuestion.objects.all()
    serializer_class = UserSerializer

class DetailUserQuestion(generics.RetrieveAPIView):
    queryset = UserQuestion.objects.all()
    serializer_class = UserSerializer


class ListSelectAnswer(generics.ListAPIView):
    queryset = SelectAnswer.objects.all()
    serializer_class = SelectAnswerSerializer

class DetailSelectAnswer(generics.RetrieveAPIView):
    queryset = SelectAnswer.objects.all()
    serializer_class = SelectAnswerSerializer

class ListFullMessages(generics.ListAPIView):
    queryset = FullMessages.objects.all()
    serializer_class = FullMessagesSerializer

class DetailFullMessages(generics.RetrieveAPIView):
    queryset = FullMessages.objects.all()
    serializer_class = FullMessagesSerializer


class ListCopy(generics.ListAPIView):
    queryset = Copy.objects.all()
    serializer_class = CopySerializer

class DetailCopy(generics.RetrieveAPIView):
    queryset = Copy.objects.all()
    serializer_class = CopySerializer