from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django import forms
from posts.models import Post, Comment
from posts.forms import PostForm, CommentForm
import datetime
#import requests
from bs4 import BeautifulSoup

class PostListView(generic.ListView):
    template_name = 'posts/post-list.html'
    context_object_name = 'all_posts'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.all().order_by("-last_modified_on")

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(PostListView, self).dispatch(request, *args, **kwargs)

# class PostDetailView(generic.DetailView):
#     model = Post
#     template_name = "posts/post-detail.html"
#
#     @method_decorator(login_required)
#     def dispatch(self, request, *args, **kwargs):
#         return super(PostDetailView, self).dispatch(request, *args, **kwargs)

class PostDetailView(CreateView):
    model = Comment
    template_name = 'posts/post-detail.html'
    form_class = CommentForm
    button = 'Comment'

    def form_valid(self, form, *args, **kwargs):
        form.instance.owner = self.request.user
        form.instance.post_id = Post.objects.get(id=self.kwargs['pk'])
        form.instance.created_on = datetime.datetime.today()
        currpost=Post.objects.get(id=self.kwargs['pk'])
        currpost.numberofcomments += 1
        currpost.save()
        return super(PostDetailView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        context['button'] = self.button
        context['post'] = Post.objects.get(id=self.kwargs['pk'])
        context['all_comments'] = Comment.objects.filter(post_id=self.kwargs['pk'])
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(PostDetailView, self).dispatch(request, *args, **kwargs)

class PostCreate(CreateView):
    model = Post
    template_name = 'posts/post-form.html'
    form_class = PostForm
    title = 'New Post'
    button = 'Post'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.created_on = datetime.datetime.today()
        form.instance.last_modified_on = datetime.datetime.today()
        return super(PostCreate, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(PostCreate, self).get_context_data(*args, **kwargs)
        context['title'] = self.title
        context['button'] = self.button
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(PostCreate, self).dispatch(request, *args, **kwargs)

class PostUpdate(UpdateView):
    model = Post
    template_name = 'posts/post-form.html'
    form_class = PostForm
    title = 'Edit Post'
    button = 'Update'

    def form_valid(self, form):
        form.instance.last_modified_on = datetime.datetime.today()
        form.instance.is_modified = True
        return super(PostUpdate, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(PostUpdate, self).get_context_data(*args, **kwargs)
        context['title'] = self.title
        context['button'] = self.button
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.owner != self.request.user:
            return redirect(obj)
        return super(PostUpdate, self).dispatch(request, *args, **kwargs)

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('posts:list')
    template_name = 'posts/confirm-delete.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.owner != self.request.user:
            return redirect(obj)
        return super(PostDelete, self).dispatch(request, *args, **kwargs)

# class ProfileView(generic.ListView):
#     template_name = 'posts/profile.html'
#     context_object_name = 'posts'
#     paginate_by = 10
#
#     @method_decorator(login_required)
#     def dispatch(self, request, *args, **kwargs):
#         return super(ProfileView, self).dispatch(request, *args, **kwargs)
#
#     def get_queryset(self, *args, **kwargs):
#         qs = Post.objects.filter(owner=User.objects.get(id=self.kwargs['pk'])).order_by("-last_modified_on")
#         qs['c_user'] = User.objects.get(id=self.kwargs['pk'])
#         return qs

class ProfileView(generic.DetailView):
    model = User
    template_name = 'posts/profile.html'
    context_object_name = 'c_user'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ProfileView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileView, self).get_context_data(*args, **kwargs)
        context['posts'] = Post.objects.filter(owner = User.objects.get(id=self.kwargs['pk'])).order_by("-last_modified_on")
        # this is for the list view of the posts by current user
        return context

class Class1():
    def __init__(self):
        title=""
        content=""
        link=""
        imgurl=""


def WebmasterArticle():
    abesitwebmaster=[]
    url = 'http://www.abesit.in/author/webmaster'
    soup = BeautifulSoup(requests.get(url).text, 'lxml')
    for item in soup.findAll('article', {'class' : 'post'}):
        x=Class1()
        x.title = item.find('h2', {'class' : 'entry-title'}).contents[0].strip()
        x.content = item.find('div', {'class' : 'entry-content'}).find('p').contents[0].strip()
        x.link = (item.find('header').find('a'))['href']
        x.imgurl = (item.find('img'))['src']
        abesitwebmaster.append(x)
    return abesitwebmaster

class WebmasterListView(generic.ListView):
    template_name = 'posts/webmaster-list.html'
    context_object_name = 'articles'
    paginate_by = 10
    def get_queryset(self):
        return WebmasterArticle()

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(WebmasterListView, self).dispatch(request, *args, **kwargs)
