from django.shortcuts import render
from .models import Post
def article(request):
    book = Post.objects.all()
    return render(request,'index.html', {'book':book})
