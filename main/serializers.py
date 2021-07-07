from rest_framework import serializers 
from .models import PersonQuestion, UserQuestion, SelectAnswer, FullMessages, Copy

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonQuestion 
        fields = ('id', 'name', 'how_many_years', 'male','description','begin','end',
        )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserQuestion 
        fields = ('personquestion', 'type_question', 'text_question',)
        

class SelectAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelectAnswer
        fields = ('personquestion', 'index', 'notes',)
        


class FullMessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FullMessages
        fields = ('user', 'personquestion', 'send_time',)
        

class CopySerializer(serializers.ModelSerializer):
    class Meta:
        model = Copy
        fields = ('fullmessages', 'personquestion', 'question_note', 'answer_note',)
        



