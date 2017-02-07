from django.contrib import admin
from django.conf import settings
from models import Quizzes
import hashlib
import base64

def make_digest(value):
    return base64.urlsafe_b64encode(hashlib.md5(value).digest())

# Register your models here.
class QuizzesAdmin(admin.ModelAdmin):
    
    list_display = ['idquiz', 'quiz', 'option_a', 'option_b', 'option_c', 'option_d', 'shareable_key']
    readonly_fields = ('idquiz', 'shareable_key')

    def save_model(self, request, obj, form, change):
        if change is False:
            obj.shareable_key = make_digest(settings.SALT + obj.quiz)
        super(QuizzesAdmin, self).save_model(request, obj, form, change)

admin.site.register(Quizzes, QuizzesAdmin)