import os

from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView
from blog.models import Blog
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify
from django.core.mail import send_mail
from django.conf import settings


class BlogListView(ListView):
    model = Blog
    extra_context = {
        'title': 'Наш блог'
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)

        return queryset


class BlogDetailView(DetailView):
    model = Blog
    extra_context = {
        'title': 'Наш блог'
    }

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()

        if self.object.view_count == 100:
            send_mail(
                'Ваша статья набрала 100 просмотров!',
                'Поздравляем! Ваша статья набрала 100 просмотров! Это отличное достижение.'
                'Желаем дальнейших успехов!',
                settings.EMAIL_HOST_USER,
                [os.getenv('E1_USER')],
            )

        return self.object


class BlogCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Blog
    fields = ('title', 'content', 'preview', )
    success_url = reverse_lazy('blog:home')
    permission_required = 'blog.add_blog'

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)

        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Blog
    fields = ('title', 'content', 'preview', )
    success_url = reverse_lazy('blog:home')
    permission_required = 'blog.change_blog'

    def get_success_url(self):
        return reverse('blog:article', args=[self.object.pk])


class BlogDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:home')
    permission_required = 'blog.delete_blog'
