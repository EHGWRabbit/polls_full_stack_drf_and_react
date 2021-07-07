from django.db import models

#Одна моедль вопросов составления вопросов
class PersonQuestion(models.Model):
    name = models.CharField(max_length=200)
    how_many_years = models.IntegerField(default=20)
    male = models.CharField(max_length=30)
    description = models.CharField(max_length=100, default='что-то')
    begin = models.DateField(default='2015-02-12')
    end = models.DateField(default='2015-12-22')


    def __str__(self):
        return self.name

#торая модель
class UserQuestion(models.Model):
    personquestion = models.ForeignKey('PersonQuestion', on_delete=models.CASCADE)
    type_question = models.CharField(max_length=40)
    text_question = models.CharField(max_length=200) 

#answers
class SelectAnswer(models.Model):
    personquestion = models.ForeignKey('PersonQuestion', on_delete=models.CASCADE)
    index = models.IntegerField(default=0)
    notes = models.CharField(max_length=100)


#отправка
class FullMessages(models.Model):
    user = models.IntegerField(db_index=True)
    personquestion = models.ForeignKey('PersonQuestion', on_delete=models.CASCADE)
    send_time = models.DateField(auto_now_add=True)

#answerscopy
class Copy(models.Model):
    fullmessages = models.ForeignKey('FullMessages', on_delete=models.CASCADE)
    personquestion = models.ForeignKey('PersonQuestion', on_delete=models.CASCADE)
    question_note = models.CharField(max_length=200)
    answer_note = models.CharField(max_length=200)


