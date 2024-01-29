from django.urls import path
from per import views

urlpatterns = [
    path('', views.quiz, name='home'),
    path('quiz/', views.predict, name='quiz'),
]