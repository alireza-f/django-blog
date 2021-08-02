from django.contrib import admin
from django.db import models
from blog.models import Post, Category, ShortIntro
from django_jalali.admin.filters import JDateFieldListFilter
import django_jalali.admin as jadmin


class PostAdmin(admin.ModelAdmin):


    list_filter = (
        ('created_at', JDateFieldListFilter),
        ('updated_at', JDateFieldListFilter),
        ('published_at', JDateFieldListFilter),
    )
    # exclude = ('author',)
    # pass
    # fields = [
    #     'title',
    #     'content',
    #     'category',
    #     'author',
    #     'is_published',

    # ]
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ShortIntro)
