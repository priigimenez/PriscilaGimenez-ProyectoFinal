from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
#authenticate
from .models import Post
from .forms import PostForm, CategoryForm, RegistroForm, TagForm
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    ultimo_post = Post.objects.order_by('-created_at').first()
    return render(request, 'entidades/index.html', {'ultimo_post': ultimo_post})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'entidades/post_detail.html', {'post': post})

@login_required
def about(request):
    return render(request, 'entidades/about.html')

@login_required
def search_posts(request):
    from .forms import PostSearchForm
    form = PostSearchForm(request.GET or None)
    results = []
    if form.is_valid() and form.cleaned_data['query']:
        q = form.cleaned_data['query']
        results = Post.objects.filter(Q(title__icontains=q) | Q(content__icontains=q))
    return render(request, 'entidades/search_posts.html', {'form': form, 'results': results})

@login_required
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            form = CategoryForm()
    else:
        form = CategoryForm()
    return render(request, 'entidades/create_category.html', {'form': form})

@login_required
def create_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            form = TagForm()
    else:
        form = TagForm()
    return render(request, 'entidades/create_tag.html', {'form': form})

@login_required
def posts(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user if request.user.is_authenticated else None
            post.save()
            form.save_m2m()
            form = PostForm()  # Limpiar el formulario tras guardar
    else:
        form = PostForm()
    contexto = {
        "Posts": Post.objects.all().order_by('-created_at'),
        "form": form
    }
    return render(request, 'entidades/posts.html', contexto)


## -- Login / Logout / Registration -- ##

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = RegistroForm()
    return render(request, 'registration/register.html', {'form': form})