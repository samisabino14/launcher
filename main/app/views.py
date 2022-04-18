
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template.defaultfilters import slugify

from .models import Category, Post, Comment

# Create your views here.

def index(request):

    if request.user.is_staff:
        if request.user.is_superuser:
            return render(request, 'manager/super_user.html')
        
        else:
            return render(request, 'admin/admin.html')

    else:
        posts = posts = Post.objects.all()

        return render(request, 'users/index.html', {

            'posts': posts
        })

    
def login_view(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('app:logout'))

    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        """ if len(username) < 3:
            error = 'O nome de utilizador deve ter no minimo 3 caracteres!'
            
        elif len(password) < 3:
            error = 'A palavra-passe deve ter no minimo 3 caracteres!'
            
        if error:    
            return render(request, 'login.html', {
                'message': error
            })

        else: """
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return HttpResponseRedirect(reverse('app:index'))

        else:
            message = 'Credenciais inválidas!'

            return render(request, 'login.html', {
                'message': message
            })

    return render(request, 'login.html')


def category(request):

    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('app:index'))

    categories = Category.objects.all()

    return render(request, 'manager/category.html', {
        "categories": categories
    })


def new_category_view(request):

    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('index'))

    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']

        category = Category.objects.filter(
            name=name, description=description).first()

        if category:
            return render(request, 'manager/new_category.html', {
                'message': 'Essa categoria já existe!'
            })

        else:
            category = Category(name=name, description=description)
            category.save()

            return HttpResponseRedirect(reverse('app:category'))

    return render(request, 'manager/new_category.html')



def edit_category_view(request, id_category):

    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('index'))

    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']

        category = Category.objects.filter(
            name=name, description=description).first()

        if category:
            return HttpResponseRedirect(reverse('app:category'))

        else:
            category = Category.objects.get(id=id_category)
            category.name = name
            category.description = description
            category.save()

            return HttpResponseRedirect(reverse('app:category'))

    category = Category.objects.get(id=id_category)

    return render(request, 'manager/edit_category.html', {

        "category": category
    })


def delete_category_view(request, id_category):

    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('app:index'))

    category = Category.objects.get(id=id_category)
    category.delete()

    return HttpResponseRedirect(reverse('app:category'))


def post(request):

    if not request.user.is_staff:
        return HttpResponseRedirect(reverse('app:index'))

    posts = Post.objects.all()

    return render(request, 'admin/post.html', {

        'posts': posts
    })


def new_post_view(request):

    if not request.user.is_staff:
        return HttpResponseRedirect(reverse('app:index'))

    if request.method == 'POST':
        
        title = request.POST['title']
        category = request.POST['category']
        content = request.POST['content']

        post = Post.objects.filter(title=title, category=category, content=content).first()

        if post:
            return render(request, 'admin/new_post.html', {
                'message': 'Esse post já existe!'
            })

        else:
            new_post = Post(title=title, category=Category.objects.get(id=category), content=content, author=request.user.username)

            new_post.save()

            return HttpResponseRedirect(reverse('app:post'))

    categories = Category.objects.all()

    return render(request, 'admin/new_post.html', {

        "categories": categories
    })


def edit_post_view(request, id_post):

    if not request.user.is_staff:
        return HttpResponseRedirect(reverse('app:index'))

    if request.method == 'POST':

        title = request.POST['title']
        category = request.POST['category']
        content = request.POST['content']

        post = Post.objects.filter(title=title, category=category, content=content).first()

        if post:
            return HttpResponseRedirect(reverse('app:post'))

        else:
            new_post = Post.objects.get(id=id_post)

            new_post.title = title
            new_post.category = Category.objects.get(id=category)
            new_post.content = content
            new_post.slug = slugify(title)

            new_post.save()

            return HttpResponseRedirect(reverse('app:post'))

    post = Post.objects.get(pk=id_post)
    categories = Category.objects.all()

    return render(request, 'admin/edit_post.html', {

        "post": post,
        "categories": categories
    })


def delete_post_view(request, id_post):

    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('app:index'))

    post = Post.objects.get(pk=id_post)
    post.delete()

    return HttpResponseRedirect(reverse('app:post'))


def logout_view(request):

    logout(request)
    return HttpResponseRedirect(reverse('app:index'))
