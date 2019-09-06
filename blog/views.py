from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

#As we shifted to class based views from function based views, home(request) got removed from above

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html --> Browser will use this naming convention for all class based views
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):  #In Class based views instead of loginrequired decorator this is used
    model = Post
    fields = ['title', 'content'] #These fields are going into crispy forms

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
