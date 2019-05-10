from django.conf.urls import re_path
from . import views


urlpatterns = [
    re_path('^$', views.home, name='home'),
    re_path('register/', views.register_page, name='register'),
    re_path('login/', views.login_page, name='login'),
    re_path('profile/', views.profile, name='profile'),
    re_path('bank-info-add-update/', views.bank_info_add_update, name='bank_info_add_update'),
    #re_path('bank-info-add-update/', views.BankInfoFormView.as_view(), name='bank_info_add_update'),
    re_path('all-bank-account/', views.all_bank_account, name='all_bank_account'),
    re_path('bank-account/(?P<id>[0-9]+)-(?P<slug>[-\w]+)/$', views.single_bank_account_detail, name='single_bank_account_detail'),
    re_path('logout/', views.user_logout, name='logout'),
    re_path('available-organizer/', views.available_organizer, name='available_organizer'),
    re_path('organization/(?P<id>[0-9]+)-(?P<slug>[-\w]+)/$', views.single_organization_detail, name='single_organization_detail'),
]