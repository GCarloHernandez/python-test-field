from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
def hello_world(request):
    return HttpResponse("Carlo Web Dev")

def crm_test(request):
    return HttpResponse('Welcome to CRM')

class HelloCarlo(View):
    def get(self, request):
        return HttpResponse("Hey Carlo")

class HelloCrm(View):
    def get(self,request):
        return HttpResponse("This is the UI for CRM")