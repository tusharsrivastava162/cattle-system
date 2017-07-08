from django.conf.urls import url
from posts import views

app_name = 'posts'

urlpatterns=[
    # url(r'^/page(?P<page>[0-9]+)/$', views.PostListView.as_view(), name='list'),
    url(r'^$', views.PostListView.as_view(), name='list'),
    url(r'^abesit/$', views.WebmasterListView.as_view(), name='abesit'),
    url(r'^(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'),
    url(r'^profile/(?P<pk>[0-9]+)/$', views.ProfileView.as_view(), name='profile'),
    url(r'^newpost/$', views.PostCreate.as_view(), name='newpost'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.PostUpdate.as_view(), name='editpost'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.PostDelete.as_view(), name='deletepost'),

]
