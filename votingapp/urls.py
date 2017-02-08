from django.conf.urls import url
from . import views

# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^quiz/(?P<digest>\w.+)/$', views.quiz_view, name='quiz_view'),
    url(r'^results/$', views.quizlist, name='quizlist'),
    url(r'^results/(?P<digest>\w.+)/$', views.results, name='results'),
]