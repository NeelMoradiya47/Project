from django.urls import path
from . import views

app_name = 'fastref'

urlpatterns = [
    path('', views.index, name='home'),
    path('content/<int:lng_id>', views.content, name='content'),
    path('feedback_form', views.feedback_form, name='feedback_form'),
    path('insert_data', views.insert_data, name='insert_data'),
]
