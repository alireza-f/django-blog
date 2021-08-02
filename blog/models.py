from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
from django_jalali.db import models as jmodels
from ckeditor.fields import RichTextField
from django.utils.text import slugify



class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان دسته‌بندی")
    eng_title = models.CharField(max_length=50, verbose_name="نامک دسته‌بندی", null=True, blank=True)

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"
        ordering = ["title"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/category/{self.eng_title}/"


# class PostTag(models.Model):
#     name = models.CharField(max_length=20)

#     class Meta:
#         verbose_name = "Tag"
#         verbose_name_plural = "Tags"
#         ordering = ["name"]




class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان پست")
    slug = models.SlugField(max_length=255)
    content = RichTextField(verbose_name="محتوای پست")
    category = models.ForeignKey(Category, verbose_name="انتخاب دسته‌بندی پست", on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        default=1,
        on_delete=models.CASCADE,
    )
    created_at = jmodels.jDateTimeField(auto_now_add=True, verbose_name="ایجاد شده در تاریخ")
    updated_at = jmodels.jDateTimeField(auto_now=True, verbose_name="ویرایش شده در تاریخ")
    is_published = models.BooleanField(default= False, verbose_name="وضعیت انتشار")
    published_at = jmodels.jDateTimeField(null=True, blank=True, editable=False, verbose_name="منتشر شده در تاریخ")
    # post_tag = models.ManyToManyField(PostTag, null=True)

    def save(self, *args, **kwargs):
        self.slug = self.slug.replace(' ', '-')
        super().save(*args, **kwargs)


    class Meta:
        verbose_name = "پست"
        verbose_name_plural = "پست‌ها"
        ordering = ["-created_at"]



    def publish(self):
        self.is_published = True
        self.published_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class ShortIntro(models.Model):
    title = models.CharField(max_length=25)
    content = RichTextField(max_length=150)

    class Meta:
        verbose_name = 'درباره وبلاگ'
        verbose_name_plural = 'درباره وبلاگ'

    def __str__(self):
        return self.title
