from django.urls import path, re_path
from . import views

urlpatterns = [
    # path('', views.QuestionCreate.as_view(), name='questions'),
    re_path('^create/$', views.QuestionCreate.as_view(), name='question-create'),
    re_path('^pending/$', views.QuestionList.as_view(), name='question-list'),
    re_path('^details/(?P<pk>\d+)/$', views.QuestionDetails.as_view(), name='question-details'),
    re_path('^edit/(?P<pk>\d+)/$', views.QuestionUpdate.as_view(), name='question-edit'),
    re_path('^approved/$', views.QuestionApprovedList.as_view(), name='question-approved-list'),
    re_path('^rejected/$', views.QuestionRejectedList.as_view(), name='question-rejected-list'),


]