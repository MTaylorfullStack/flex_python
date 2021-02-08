from django.shortcuts import render

blog_posts=["Hi! This my first blog post!", "How is the weather over there?", "Seems like things are going well.", "Wow! 2021 Already!"]

def index(request):
    context={
        'name':"Michael",
        'posts':blog_posts
    }
    return render(request, 'index.html', context)

def name(request, name):
    context={
        'name':name
    }
    return render(request, "name.html", context)


