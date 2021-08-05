from .models import Category, Post, ShortIntro, Comment


def sections_processor(request):
    categories = Category.objects.all
    a_list = Post.objects.filter(created_at__year=2021)
    intro = ShortIntro.objects.all()[0]
    # comments = posts.comments.filter(is_active=True)

    return {'categories': categories, 'intro': intro, 'monthly_archive' : a_list}