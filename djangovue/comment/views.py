from django.shortcuts import render
from .models import Comment 
# Create your views here.
def index(request):
    comments = Comment.objects.all()
    return render(request,'index.html',{'comments': comments})

