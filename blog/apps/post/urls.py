from django.urls import path
import apps.post.views as views

app_name = 'post'

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name="post_list"),
    path('posts/create', views.PostCreateView.as_view(), name="post_create"),
    path('posts/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('posts/<slug:slug>/update', views.PostDetailView.as_view(), name='post_update'),
    path('posts/<slug:slug>/delete', views.PostDetailView.as_view(), name='post_delete'),
    
]
    
#En este caso, se han definido las siguientes URLs:
#post_list: URL para listar los posts.
#post_create: URL para crear un nuevo post.
#post_detail: URL para ver un post en detalle.
#post_update: URL para actualizar un post.
#post_delete: URL para eliminar un post.