from django.urls import path, include
from . import views
urlpatterns = [
    path('quotes/', views.GetPrice().as_view()),
]