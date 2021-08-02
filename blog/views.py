from django.db import connection, models
from blog.models import Post
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Category, ShortIntro
import datetime
from django.views.generic import DetailView
from .forms import CommentForm


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
    # a_list = get_object_or_404(Post, created_at__year=year)
    # if not a_list:
    #     return HttpResponse('<h1>Error 404</h1>')
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



def post_detail(request, slug):
    template_name = 'blog/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(is_active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})