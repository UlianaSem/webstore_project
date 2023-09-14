from django.views.decorators.cache import never_cache

from blog.apps import BlogConfig
from django.urls import path
from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('article/<int:pk>/', BlogDetailView.as_view(), name='article'),
    path('article/create/', never_cache(BlogCreateView.as_view()), name='create_article'),
    path('article/update/<int:pk>/', never_cache(BlogUpdateView.as_view()), name='update_article'),
    path('article/delete/<int:pk>/', never_cache(BlogDeleteView.as_view()), name='delete_article'),
]
