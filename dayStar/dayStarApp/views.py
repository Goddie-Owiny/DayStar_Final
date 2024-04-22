from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'dayStarApp/index.html')

def sitter(request):
    return render(request, 'dayStarApp/sitter.html')