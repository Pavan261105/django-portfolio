from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.
from .models import Project, Contact, Blog, Experience
from django.shortcuts import render
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.contrib import messages

def home(request):
    projects = Project.objects.all()[:3]
    blogs = Blog.objects.all()[:3]  # latest 3 blogs
    return render(request, 'main/home.html', {
        'projects': projects,
        'blogs': blogs,
    })


def about(request):
    return render(request, 'main/about.html')


def projects(request):
    project_list = Project.objects.all()
    paginator = Paginator(project_list, 6)  # Show 6 projects per page

    page_number = request.GET.get('page')
    projects = paginator.get_page(page_number)

    return render(request, 'main/projects.html', {'projects': projects})


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        Contact.objects.create(name=name, email=email, message=message)
        messages.success(request, "Thanks for reaching out! I'll get back to you soon.")
        return redirect('contact')
    return render(request, 'main/contact.html')

def blog_list(request):
    posts = Blog.objects.all()
    return render(request, 'main/blog_list.html', {'posts': posts})

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'main/blog_detail.html', {'blog': blog})

def about(request):
    experiences = Experience.objects.all()
    return render(request, 'main/about.html', {'experiences': experiences})
