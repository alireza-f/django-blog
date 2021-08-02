from django.db import models
from blog.models import Post
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Category, ShortIntro
import datetime
from django.views.generic import DetailView


# Create your views here.

def home(request):
    posts = Post.objects.all
    categories = Category.objects.all
    a_list = Post.objects.filter(created_at__year=2021)
    intro = ShortIntro.objects.get(id=1)
    context = {
        'monthly_archive' : a_list,
        'posts': posts,
        'categories' : categories,
        'intro' : intro,
    }
    return render(request, 'blog/home.html', context)




def year_archive(request, year):
    a_list = Post.objects.filter(created_at__year=year)
    context = {
        'year' : year,
        'yearly_archive' : a_list,
    }
    return render(request, 'blog/year_archive.html', context)

def month_archive(request, year, month):
    a_list = Post.objects.filter(created_at__year=year).filter(created_at__month=month)
    datetime_object = datetime.datetime.strptime(f'{month}', "%m")
    month_name = datetime_object.strftime("%b")
    context = {
        'year' : year,
        'month': month,
        'month_archive' : a_list,
        'month_name' : month_name,
    }
    return render(request, 'blog/month_archive.html', context)

def post_detail(request):
    pass


def category_posts(request, eng_title):
    posts_in_category = Post.objects.filter(category__eng_title=eng_title)
    cat_title = posts_in_category[0].category
    context = {
        'category_posts': posts_in_category,
        'cat_title' : cat_title
    }
    return render(request, 'blog/category_posts.html', context)



class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_detail.html'