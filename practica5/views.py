from django.http import HttpResponse
from django.shortcuts import render_to_response


def index(request):
   return HttpResponse("Hello World, you are at the index of my web")

def about(request):
   return render_to_response('/static/about_us.html',{'lol'})
