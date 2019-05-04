from django.shortcuts import render
from django.views import generic

from .models import Phone, Brand
from .forms import CreatePhoneForm, CreateBrandForm
from accounts.models import ProfileUser
# Create your views here.


class ListPhone(generic.ListView):
    model = Phone
    template_name = "phone_list.html"
    context_object_name = 'phones'


class UserPhoneList(generic.ListView):
    pass


class PhoneDetails(generic.DetailView):
    model = Phone
    template_name = 'phone_details.html'
    context_object_name = 'phones'


class PhoneDelete(generic.DeleteView):
    model = Phone
    login_url = '/accounts/login/'
    context_object_name = 'phone'


class PhoneCreate(generic.CreateView):
    model = Phone
    template_name = 'phone_create'
    form_class = CreatePhoneForm
    success_url = '/phones/'

    def form_valid(self, form):
        user = ProfileUser.objects.all().filter(user__pk=self.request.user.id)[0]
        form.instance.user = user
        return super().form_valid(form)


class PhoneEdit(generic.UpdateView):
    model = Phone
    form_class = CreatePhoneForm
    template_name = 'phone_create.html'
    success_url = '/phones/'


class CreateBrand(generic.CreateView):
    model = Brand
    template_name = 'brand_create.html'
    form_class = CreateBrandForm
    success_url = '/phones/'