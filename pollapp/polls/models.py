import json
from datetime import datetime
from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # def __str__(self):
    #     return self.question_text

    @staticmethod
    def datetime_converter(o):
        if isinstance(o, datetime):
            return o.__str__()
    
    def to_json(self):
        return json.dumps(self.__dict__, default=self.datetime_converter)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
