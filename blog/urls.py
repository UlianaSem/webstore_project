from blog.apps import BlogConfig
from django.urls import path
from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('article/<int:pk>/', BlogDetailView.as_view(), name='article'),
    path('article/create/', BlogCreateView.as_view(), name='create_article'),
    path('article/update/<int:pk>/', BlogUpdateView.as_view(), name='update_article'),
    path('article/delete/<int:pk>/', BlogDeleteView.as_view(), name='delete_article'),
]
