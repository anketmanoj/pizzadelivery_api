from django.urls import path
from authentication import views

urlpatterns = [
    path('', views.HelloAuthView.as_view(), name='hello_auth'),
]
