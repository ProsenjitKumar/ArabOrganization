from django.conf.urls import re_path
from . import views


urlpatterns = [
    re_path('^$', views.home, name='home'),
    re_path('register/', views.register_page, name='register'),
    re_path('login/', views.login_page, name='login'),
    re_path('profile/', views.profile, name='profile'),
    re_path('bank-info-add-update/', views.bank_info_add_update, name='bank_info_add_update'),
    re_path('logout/', views.user_logout, name='logout'),
    re_path('available-organizer/', views.available_organizer, name='available_organizer'),
    re_path('organization/(?P<id>[0-9]+)-(?P<slug>[-\w]+)/$', views.single_organization_detail, name='single_organization_detail'),
]