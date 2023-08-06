from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice

# Each generic view needs to know what model it will be acting upon. This is provided using the model attribute.
# The DetailView generic view expects the primary key value captured from the URL to be called "pk", so we’ve changed question_id to pk for the generic views.

# IndexView default template name <app name>/<model name>_list.html
# DetailView default template name <app name>/<model name>_detail.html

# default context_object_name is based on django's model (in my project it's "Question"), for IndexView we have to override that name


class IndexView(generic.ListView):
    model = Question
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published in the past or present questions with more than one choice."""
        queryset = super().get_queryset()
        # exclude questions with less than two choices
        for question in queryset:
            if len(question.choice_set.all()) < 2:
                queryset = queryset.exclude(pk=question.pk)
        # return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]   # order_by('field') - ascending / order_by('-field') - descending
        # __lte is to filter objects that have pub_date less or equal to timezone.now()
        queryset = queryset.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
        return queryset


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet or have less than two choices.
        """
        queryset = super().get_queryset()
        for question in queryset:
            if len(question.choice_set.all()) < 2:
                queryset = queryset.exclude(pk=question.pk)
        queryset = queryset.filter(pub_date__lte=timezone.now())
        return queryset


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        for question in queryset:
            if len(question.choice_set.all()) < 2:
                queryset = queryset.exclude(pk=question.pk)
        queryset = queryset.filter(pub_date__lte=timezone.now())
        return queryset


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))





# ----------------------------------- OLD VIEWS VERSION ------------------------------------

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]

    # context = {'latest_question_list': latest_question_list}
    # return render(request, 'polls/index.html', context)

#     # HTTPReponse without a template
#         # output = ', '.join(question_obj.question_text for question_obj in latest_question_list)

#     # Template rendering - extended version
#         # template = loader.get_template('polls/index.html')
#         # context = {
#         #     'latest_question_list': latest_question_list,
#         # }
#         # return HttpResponse(template.render(context, request))


# def detail(request, question_id):

#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})

#     # try/except for Http404 error - extended version
#             # try:
#             #     question = Question.objects.get(pk=question_id)
#             # except Question.DoesNotExist:
#             #     raise Http404("Question does not exist")

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})