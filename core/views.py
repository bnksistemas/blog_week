from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.contrib.auth.models import User


# Create your views here.

def home(request):

    if not request.session.get('items_per_page'):
        request.session['items_per_page'] = 2

    if request.method == 'GET' and 'items_per_page' in request.GET:
        request.session['items_per_page'] = int(request.GET['items_per_page'])

    items_per_page = request.session['items_per_page']

    posts_page = Paginator(Post.objects.filter(published=True), items_per_page)
    page = request.GET.get('page')
    posts = posts_page.get_page(page)
    aux = 'x' * posts.paginator.num_pages
    data={
        'posts': posts,
        'aux': aux
    }
    return render(request, 'core/home.html', data)

#dettalle del post
def post(request, post_id):
    post=Post.objects.get(id=post_id)
    try:
        post= get_object_or_404(Post, id=post_id)
        data={
            'post': post
        }
        return render(request, 'core/detail.html', data)
    except:
        return render(request, 'core/404.html')

# Filtrado por categorua
def category(request,category_id):
    try:
        category=get_object_or_404(Category, id=category_id)
        data={
            'category' : category,
        }
        return render(request, 'core/category.html', data)
    except:
        return render(request, 'core/404.html')


# Filtrado por autor
def author(request, author_id):
    try:
        author=get_object_or_404(User, id=author_id)
        data={
            'author' : author,
        }
        return render(request, 'core/author.html', data)
    except:
        return render(request, 'core/404.html')


def dates(request, month_id, year_id):
    posts= Post.objects.filter(published = True, created__month=month_id, created__year=year_id)
    meses={
        1: 'Enero',
        2: 'Febrero',
        3: 'Marzo', 
        4: 'Abril',
        5: 'Mayo',
        6: 'Junio',
        7: 'Julio',
        8: 'Agosto',
        9: 'Septiembre',
        10: 'Octubre',
        11: 'Noviembre',
        12: 'Diciembre',
    }
    if month_id > 12 or month_id < 1:
        return render(request, 'core/404.html')
    data = {
        'posts': posts,
        'month': meses[month_id],
        'year' : year_id,
    }
    return render(request, 'core/date.html', data)