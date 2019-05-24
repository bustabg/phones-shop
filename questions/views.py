from django.views import generic

from .forms import CreateQuestionForm, EditQuestionForm
from .models import Question
from.enums import StatusEnum


class QuestionCreate(generic.CreateView):
    model = Question
    template_name = 'question_create.html'
    form_class = CreateQuestionForm
    success_url = '/'


class QuestionList(generic.ListView):
    model = Question
    context_object_name = 'questions'
    template_name = 'question_list.html'


class QuestionDetails(generic.DetailView):
    model = Question
    login_url = '/accounts/login/'
    context_object_name = 'question'
    template_name = 'question_details.html'


class QuestionUpdate(generic.UpdateView):
    model = Question
    form_class = EditQuestionForm
    template_name = 'question_edit.html'
    success_url = '/questions/pending/'


class QuestionApprovedList(generic.ListView):
    model = Question
    context_object_name = 'questions'
    template_name = 'questions_approved_list.html'


class QuestionRejectedList(generic.ListView):
    model = Question
    context_object_name = 'questions'
    template_name = 'questions_rejected_list.html'
