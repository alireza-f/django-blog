from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('archive/<int:year>/', views.year_archive, name='year-archive'),
    path('archive/<int:year>/<int:month>/', views.month_archive, name='month-archive'),
    path('archive/<int:month>/<int:pk>', views.post_detail, name='post-detail'),
    path('category/<eng_title>/', views.category_posts, name='category-posts'),

]
