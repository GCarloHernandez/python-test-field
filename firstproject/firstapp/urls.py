from django.urls import path
from . import views

urlpatterns = [
    path('function', views.hello_world),
    path('class', views.HelloCarlo.as_view()),
    path('function1', views.crm_test),
    path('class1', views.HelloCrm.as_view())
]