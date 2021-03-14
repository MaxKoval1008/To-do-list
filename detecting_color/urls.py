from django.urls import path

from .views import *

app_name = 'detecting_color'

urlpatterns = [
    path('picture/post', PicturePostView.as_view()),
    path('picture/color/<str:pk>', ColorRetrieveView.as_view()),
    path('picture/delete/<str:pk>', PictureDeleteView.as_view()),
]