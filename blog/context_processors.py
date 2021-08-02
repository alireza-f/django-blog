from .models import Category, Post, ShortIntro


def sections_processor(request):
    categories = Category.objects.all
    a_list = Post.objects.filter(created_at__year=2021)
    intro = ShortIntro.objects.get(id=1)
    return {'categories': categories, 'intro': intro, 'monthly_archive' : a_list}