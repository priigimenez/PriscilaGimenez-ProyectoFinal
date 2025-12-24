from codecs import register
from django.urls import path
from .views import CustomLoginView, home, posts, create_category, create_tag, registro_usuario, search_posts, about, post_detail
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name='home'),
    path("posts/", posts, name="posts"),
    path("posts/<int:post_id>/", post_detail, name="post_detail"),
    path("buscar/", search_posts, name="search_posts"),
    path("categorias/nueva/", create_category, name="create_category"),
    path("etiquetas/nueva/", create_tag, name="create_tag"),
    path("sobre-mi/", about, name="about"),

#Login / Logout / Registration
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', registro_usuario, name='register'),
]