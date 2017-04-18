from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Question_sessions,Question
from django.shortcuts import render, get_object_or_404
from django.views.decorators import csrf
import json
def show_questioning_session(request, pk):
    question_session = get_object_or_404(Question_sessions, pk=pk)
    question_session.question_set.all()
    last_pk = Question.objects.last().pk
    return render(request, "question/index.html", {'question_session': question_session,
                                                   "last_pk": last_pk})
@csrf.csrf_exempt
def handle_questioning_ajax(request, pk):
    question_session = get_object_or_404(Question_sessions, pk=pk),
    old_last_pk = request.POST['last_pk']
    new_last_pk = Question.objects.last().pk
    if old_last_pk != new_last_pk:
        new_questions = question_session.question.objects.filter(id__gt=new_last_pk)
        response= {'new_questions':new_questions}
    else:
        pass
    data = json.dumps(response)
    return HttpResponse(data)