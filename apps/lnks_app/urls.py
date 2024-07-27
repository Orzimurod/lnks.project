from django.urls import path
from apps.lnks_app.views import home_view,redirect_view,login_view,logout_view,my_links

urlpatterns=[
    path('',home_view,name='home'),
    path('<str:short_code>/',redirect_view, name='redirect'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('links', my_links, name='links')
]