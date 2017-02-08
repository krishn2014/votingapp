from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.http import Http404

from forms import *

# Create your views here.
# this login required decorator is to not allow to any  
# view without authenticating
@login_required(login_url='login/')
def home(request):
    return render(request,'home.html')

def get_quiz(digest):
    try:
        return Quizzes.objects.get(shareable_key=digest)
    except Quizzes.DoesNotExist:
        raise Http404

@login_required(login_url="/login/")
def quiz_view(request, digest):
    quiz = get_quiz(digest)
    # validate if user has already given vote
    try:
        x = Votes.objects.get(quiz=quiz, user=request.user)
        return render(request, 'votemsg.html', {'message': 'You cannot vote twice.'})
    except Votes.DoesNotExist:
        pass

    if request.method == 'POST':
        # process with the submitted data
        post = request.POST
        option = post.get('option', None)
        if option is None:
            return render(request, 'votequiz.html', {'quiz': quiz, 'error': 'Please select an option'})
        elif post.get('key') != quiz.shareable_key:
            raise Http404
        try:
            if option not in [quiz.option_a, quiz.option_b, quiz.option_c, quiz.option_d]:
                raise Http404

            # creating vote object
            vote = Votes(quiz=quiz, option=option, user=request.user)
            vote.save()
            return render(request, 'votemsg.html', {'message': 'Thank you! Your vote has been recorded.'})
        except Exception as e:
            user.delete()
            return render(request, 'timesheets/messagebox.html', {'message': 'Error: Unable to send mail. Please cross check your email.'})
    else:
        return render(request, 'votequiz.html', {'quiz': quiz})