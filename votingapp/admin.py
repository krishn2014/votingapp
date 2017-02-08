from django.contrib import admin
from django.conf import settings
from models import Quizzes
import hashlib
import base64

from django.urls import reverse

def make_digest(value):
    return base64.urlsafe_b64encode(hashlib.md5(value).digest())

# Register your models here.
# provisoining admin view for creating quizess
class QuizzesAdmin(admin.ModelAdmin):
    
    list_display = ['idquiz', 'quiz', 'option_a', 'option_b', 'option_c', 'option_d', 'shareable_key', 'urllink']
    readonly_fields = ('idquiz', 'shareable_key', 'urllink')

    # urllink represents partial url
    def urllink(self, obj):
            return reverse('quiz_view', args=[obj.shareable_key]) if getattr(obj, 'shareable_key') else '' 

    def save_model(self, request, obj, form, change):
        if change is False:
            obj.shareable_key = make_digest(settings.SALT + obj.quiz)
        super(QuizzesAdmin, self).save_model(request, obj, form, change)

admin.site.register(Quizzes, QuizzesAdmin)