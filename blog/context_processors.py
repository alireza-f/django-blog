from .models import Category, Post, ShortIntro, Comment


def sections_processor(request):
    posts = Post.objects.all
    categories = Category.objects.all
    a_list = Post.objects.filter(created_at__year=2021)
    intro = ShortIntro.objects.get(id=1)
    # comments = posts.comments.filter(is_active=True)

    return {'categories': categories, 'intro': intro, 'monthly_archive' : a_list}