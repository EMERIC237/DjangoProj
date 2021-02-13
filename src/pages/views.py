from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})

def inscription_view(request, *args, **kwargs):
    return render(request, 'inscription.html', {})

def about_view(request, *args, **kwargs):
    return render(request, 'about.html', {})
    
def blog_view(request, *args, **kwargs):
    return render(request, 'blog.html', {})
