from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from .forms import SignUpForm, CommentCreateForm
from django.urls import reverse_lazy
from .models import Post, Comment

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        comment_form = CommentCreateForm()
        context['comment_form'] = comment_form
        return context
    

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('home')
    template_name = 'register.html'

class CommentCreate(CreateView):
    model = Comment
    form_class = CommentCreateForm

    def get_success_url(self):
        return reverse('post:comment', kwargs={'pk': self.object.entry.pk})

