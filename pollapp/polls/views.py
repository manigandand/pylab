from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import JsonResponse
from django.urls import reverse
# from django.template import loader

from django.core import serializers


from polls.models import Question, Choice

# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)


def json_test_handler(request):
    return JsonResponse({
            'key1': 'value1',
            'key2': [
                {
                    'key2.1': 'val1',
                },
            ],
            })

def details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/details.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/details.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def details_json(request, question_id):
    try:
        question = Question.objects.get(pk=question_id).values()
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return JsonResponse({"data": list(question)})
    # return JsonResponse({
    #     "question_text": question.question_text,
    #     "pub_date": question.pub_date,
    # })
