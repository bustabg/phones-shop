from django.shortcuts import render
from django.views import generic

from .forms import AddImageForm
from .models import AddImage


class Landing(generic.CreateView):
    model = AddImage
    form_class = AddImageForm
    template_name = 'landing_page.html'
    success_url = '/'
    context_object_name = 'create'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Landing, self).get_context_data(**kwargs)
        context['image'] = AddImage.objects.latest('date_created')
        print(context)
        return context



    # def get_context_data(self, **kwargs):
    #     context = super(Landing, self).get_context_data(**kwargs)
    #     return context
#
#
# class HomePageView(generic.ListView):
#     model = AddImage
#     template_name = 'landing_page.html'
#     context_object_name = 'obj'
#
#     def get_context_data(self, **kwargs):
#         context = super(HomePageView, self).get_context_data(**kwargs)
#         return context




