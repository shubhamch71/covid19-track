from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:state_code>', views.states, name='state'),
    path('news/', views.news, name='news')
]