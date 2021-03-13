from django.urls import path

from .views import *

app_name = 'to_do_list'

urlpatterns = [
    path('task/create', TaskCreateView.as_view()),
    path('task/delete/<str:pk>', TaskDeleteView.as_view()),
    path('task/update/<str:pk>', TaskUpdateView.as_view()),
    path('task/list', TaskListView.as_view()),
]