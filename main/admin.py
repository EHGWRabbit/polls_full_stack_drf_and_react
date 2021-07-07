from django.contrib import admin
from .models import PersonQuestion, UserQuestion, SelectAnswer, FullMessages, Copy

admin.site.register(PersonQuestion)
admin.site.register(UserQuestion)
admin.site.register(SelectAnswer)
admin.site.register(FullMessages)
admin.site.register(Copy)

