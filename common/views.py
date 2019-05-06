from django.shortcuts import render
from django.views import generic

from .forms import AddImageForm
# Create your views here.


def landing(request):
    return render(request, 'landing_page.html')


class Landing(generic.CreateView):
    model = AddImageForm
    form_class = AddImageForm
    template_name = 'landing_page.html'
    success_url = '/'
