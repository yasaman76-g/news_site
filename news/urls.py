from django.urls import path
from . import views


urlpatterns = [
    path('',views.NewsApi.as_view(),name='create-news')
]
