from django.urls import path, re_path, include


from . import views

urlpatterns = [
    re_path('^profile/edit/(?P<pk>\d+)/$', views.UserProfileEdit.as_view(), name='edit_user'),
    re_path('^profile/$', views.redirect_to_user_profile, name='redirect-user-detail'),
    re_path('^password_change/$', views.change_password, name='change_password'),
    re_path('profile/(?P<pk>\d+)/', views.UserDetail.as_view(), name='user-profile'),
    path('', include('django.contrib.auth.urls')),
    path('signup/', views.SignUp.as_view(), name='signup'),


]