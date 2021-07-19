from django.http import HttpResponse
from django.shortcuts import render, redirect
from posts.models import Post
from django import forms
from django.forms import ValidationError
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView


def index(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'posts/index.html', context=context)


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            p = Post(title=form.cleaned_data['title'], content=form.cleaned_data['content'])
            p.save()
            return redirect('/posts')
        else:
            return render(request, 'posts/create_post.html', context={'form': form})
    return render(request, 'posts/create_post.html')


class CreatePostView(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'posts/create_post.html')

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            p = Post(title=form.cleaned_data['title'], content=form.cleaned_data['content'])
            p.save()
            return redirect('/posts')
        else:
            return render(request, 'posts/create_post.html', context={'form': form})


class PostDetailedView(DetailView):
    model = Post
    template_name = 'posts/post_profile.html'
    context_object_name = 'posts'

    #def post_detail(self, request, request_pk):
    #    p = Post.objects.get(pk=request_pk)
    #    return render(request, 'posts/post_profile.html')


class PostListView(ListView):
    model = Post
    template_name = 'posts/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.prefetch_related('categories', 'categories__category')



class PostForm(forms.Form):
    title = forms.CharField(label='', min_length=2)
    content = forms.CharField(max_length=100)

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 5:
            raise ValidationError('Too much letters')
        return title
