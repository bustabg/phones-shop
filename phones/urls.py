from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.ListPhone.as_view(), name='phone-list'),
    re_path('^details/(?P<pk>\d+)$', views.PhoneDetails.as_view(), name='phone-details'),

]

