from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import  loader
from article.models import Article,Comments
from django.template import Context
from django.template.loader import render_to_string

# Create your views here.
def basic_one(request):
    view = "basic_one"
    html = "<html><body>This  is %s view</body></html>" % view
    return HttpResponse(html)

def template_two(request):
    view = "template_two"
    t = loader.get_template('myview.html')
    context = {'name': view}
    return HttpResponse(t.render(context, request))

def render_three(request):
    view = "render_three"
    context = {'name': view}
    return render(request, 'myview.html', context)

def articles(request):
    return render(request,'articles.html',{'articles': Article.objects.all()})

def article(request, article_id=1):
    return render(request, 'article.html', {'article': Article.objects.get(id=article_id), 'comments': Comments.objects.filter(comments_article_id=article_id)})