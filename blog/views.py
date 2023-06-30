from django.shortcuts import render
from .models import Article
# Create your views here.
def blog(request):
    articles=Article.objects.all()
    return render(request,'blog.html',context={'articles':articles})


def blog_detail(request,id):
    article=Article.objects.get(id=id)
    return render(request,'blog-detail.html',context={'blog':article})

def example(request):
    users=[
        {'name':'eli','age':'24','job':'Frontend Developer'},
        {'name':'veli','age':'30','job':'Software Developer'},
        {'name':'leyla','age':'28','job':'SQL Developer'},
        {'name':'samir','age':'22','job':'Data Analtic'}, 
        ]
    return render(request,'example.html',context={'users':users})