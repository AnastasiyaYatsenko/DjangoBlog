from django.urls import include, path
from django.conf import settings

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
    path('add', views.CreatePostView.as_view(), name='create_post'),
    #path('<>', views.CreatePostView.as_view(), name='create_post'),
]

#if settings.DEBUG:
#    import debug_toolbar
#    urlpatterns=[path('__debug__/', include(debug_toolbar.urls))]+urlpatterns