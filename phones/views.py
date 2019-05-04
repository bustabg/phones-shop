from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect


from .models import Phone, Brand
from .forms import CreatePhoneForm, CreateBrandForm

from accounts.models import ProfileUser
# Create your views here.


def has_access_to_modify(current_user, phone):
    if current_user.is_superuser:
        return True
    elif current_user.id == phone.user.id:
        return True
    return False


class ListPhone(generic.ListView):
    model = Phone
    template_name = "phone_list.html"
    context_object_name = 'phones'


class UserPhoneList(generic.ListView):
    model = Phone
    template_name = "phone_list.html"
    context_object_name = 'phones'

    def get_queryset(self):
        user_id = int(self.request.user.id)

        try:
            user = ProfileUser.objects.all().filter(user__pk=user_id)[0]
            furniture = Phone.objects.all().filter(user=user.pk)
            return furniture
        except:
            return []


class PhoneDetails(LoginRequiredMixin, generic.DetailView):
    model = Phone
    login_url = '/accounts/login/'
    context_object_name = 'phone'
    template_name = 'phone_details.html'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(PhoneDetails, self).get_context_data(**kwargs)
    #     context['reviews'] = Review.objects.all().filter(furniture=self.get_object())
    #     context['form'] = ReviewForm()
    #     # context['form'].fields['author'].initial = self.request.user.id
    #     print(context)
    #     owner = context['object'].user
    #     current_user = self.request.user
    #     if has_access_to_modify(current_user, owner):
    #         context['is_user_furniture'] = True
    #         return context
    #     context['is_user_furniture'] = False
    #     return context
    #
    # def post(self, request, pk):
    #     url = f'/furniture/details/{self.get_object().id}/'
    #     post_values = request.POST.copy()
    #     form = ReviewForm(post_values)
    #
    #     if form.is_valid():
    #         author = ProfileUser.objects.all().filter(user__pk=request.user.id)[0]
    #         post_values['furniture'] = self.get_object()
    #         review = Review(
    #             content=post_values['content'],
    #             score=post_values['score'],
    #             furniture=self.get_object(),
    #             author=author
    #         )
    #         review.save()
    #         return HttpResponseRedirect(url)
    #     else:
    #         raise Exception(form.errors)


class PhoneDelete(LoginRequiredMixin, generic.DeleteView):
    model = Phone
    login_url = '/accounts/login/'
    context_object_name = 'phone'

    def get(self, request, pk):
        if not has_access_to_modify(self.request.user, self.get_object()):
            return render(request, 'permission_denied.html')
        return render(request, 'phone_delete.html', {'phone': self.get_object()})

    def post(self, request, pk):
        if not has_access_to_modify(self.request.user, self.get_object()):
            return render(request, 'permission_denied.html')
        phone = self.get_object()
        phone.delete()
        return HttpResponseRedirect('/phone/')


class PhoneCreate(generic.CreateView):
    model = Phone
    template_name = 'phone_create.html'
    form_class = CreatePhoneForm
    success_url = '/phones/'

    def form_valid(self, form):
        user = ProfileUser.objects.all().filter(user__pk=self.request.user.id)[0]
        form.instance.user = user
        return super().form_valid(form)


class PhoneEdit(LoginRequiredMixin, generic.UpdateView):
    model = Phone
    form_class = CreatePhoneForm
    template_name = 'phone_create.html'
    success_url = '/phone/'

    def form_valid(self, form):
        user = ProfileUser.objects.all().filter(user__pk=self.request.user.id)[0]
        form.instance.user = user
        return super().form_valid(form)

    def get(self, request, pk):
        if not has_access_to_modify(self.request.user, self.get_object()):
            return render(request, 'permission_denied.html')
        instance = Phone.objects.get(pk=pk)
        form = CreatePhoneForm(request.POST or None, instance=instance)
        return render(request, 'phone_create.html', {'form': form})


class BrandCreate(generic.CreateView):
    model = Brand
    template_name = 'brand_create.html'
    form_class = CreateBrandForm
    success_url = '/phones/'
