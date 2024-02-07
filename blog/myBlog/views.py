from django.shortcuts import render
from django.views import View
from .models import Posts

# Create your views here.

class Page1(View):
    template = 'page1.html'

    def get(self, request):
        return render(request, self.template)

class Page2(View):
    template = 'page2.html'

    def get(self, request):
        posts = Posts.objects.all()
        return render(request, self.template, {'posts': posts})
    

class Page3(View):
    template = 'posted.html'

    def get(self, request, title):
        posts = Posts.objects.get(title=title)
        return render(request, self.template, {'posts': posts})