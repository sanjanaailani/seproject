from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('index/', index, name='index'),
    path('nlp/', nlp, name='nlp'),
    path('oops/', oops, name='oops'),
    path('profile/', profile, name='profile'),
    path('login/', login_view, name='login'),
    path('login/myapp/dashboard/', student_dashboard, name='student_dashboard'),
    path('oops_html/',oops_html, name='oops_html'),  # Add this view
    path('logout/', logout_view, name='logout'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('python/', python, name='python'), 
    path('probability/', probability, name='probability'),
    path('regular/', regular, name='regular'),
    path('tokenization/', tokenization, name='tokenization'),
     path('object/', object, name='object'),
]