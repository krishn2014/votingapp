from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

# Create your models here.
class Quizzes(models.Model):
    idquiz = models.AutoField(db_column='idQuiz', primary_key=True) # Field name made lowercase.
    quiz = models.TextField(db_column='quiz', validators=[MinLengthValidator(300)], blank=False) # Field name made lowercase.
    option_a = models.CharField(db_column='optionA', max_length=60, blank=False) # Field name made lowercase.
    option_b = models.CharField(db_column='optionB', max_length=60, blank=False) # Field name made lowercase.
    option_c = models.CharField(db_column='optionC', max_length=60, blank=False) # Field name made lowercase.
    option_d = models.CharField(db_column='optionD', max_length=60, blank=False) # Field name made lowercase.
    shareable_key = models.CharField(db_column='shareableKey', max_length=50, blank=False, unique=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'quizzes'
        verbose_name = 'Quiz'
        verbose_name_plural='Quizzes'

class Votes(models.Model):
    idvote = models.AutoField(db_column='idVote', primary_key=True)
    quiz = models.ForeignKey('Quizzes', db_column='quiz')
    option = models.CharField(db_column='option', max_length=60, blank=False)
    user = models.ForeignKey(User)