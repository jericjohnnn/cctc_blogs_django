from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Blog
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def home(request):
    latest_blogs = Blog.objects.all()[:5]
    return render(request, 'home.html', {'blogs': latest_blogs})

class BlogListView(ListView):
    model = Blog
    template_name = 'blog_list.html'
    context_object_name = 'blogs'

class BlogCreateView(CreateView):
    model = Blog
    template_name = 'blog_form.html'
    fields = ['author', 'title', 'body']
    success_url = reverse_lazy('blog-list')

    def form_valid(self, form):
        messages.success(self.request, 'Blog post created successfully!')
        return super().form_valid(form)

class BlogUpdateView(UpdateView):
    model = Blog
    template_name = 'blog_form.html'
    fields = ['author', 'title', 'body']
    success_url = reverse_lazy('blog-list')

    def form_valid(self, form):
        messages.success(self.request, 'Blog post updated successfully!')
        return super().form_valid(form)

class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog_confirm_delete.html'
    success_url = reverse_lazy('blog-list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Blog post deleted successfully!')
        return super().delete(request, *args, **kwargs)
