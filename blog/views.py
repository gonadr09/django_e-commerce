from django.shortcuts import render
from blog.models import Post, Categoria

# Create your views here.

def blog(request):
    posts = Post.objects.all() #importa todos los objectos del modelo
    categorias = Categoria.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts, 'categorias': categorias})

def categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    categorias = Categoria.objects.all()
    posts = Post.objects.filter(categorias=categoria) #importa todos los objectos del modelo
    return render(request, 'blog/categoria.html', {'categoria': categoria, 'posts': posts, 'categorias': categorias})