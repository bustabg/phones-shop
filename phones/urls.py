from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.PhoneList.as_view(), name='phones'),
    path('mine/', views.UserPhoneList.as_view(), name='mine-phones'),
    path('brand/', views.BrandCreate.as_view(), name='brand-add'),
    re_path('^details/(?P<pk>\d+)/$', views.PhoneDetails.as_view(), name='phone-details'),
    re_path('^create/$', views.PhoneCreate.as_view(), name='phone-create'),
    re_path('^delete/(?P<pk>\d+)/$', views.PhoneDelete.as_view(), name='phone-delete'),
    re_path('^edit/(?P<pk>\d+)/$', views.PhoneEdit.as_view(), name='phone-edit'),
    re_path('^search/$', views.PhoneSearchList.as_view(), name='phone-search')

]

