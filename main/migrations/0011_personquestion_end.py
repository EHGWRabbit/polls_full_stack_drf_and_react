# Generated by Django 2.2.10 on 2021-07-07 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_personquestion_begin'),
    ]

    operations = [
        migrations.AddField(
            model_name='personquestion',
            name='end',
            field=models.DateField(default='2015-12-22'),
        ),
    ]
