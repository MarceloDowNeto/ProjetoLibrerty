from django.shortcuts import render, redirect
from app.forms import LivrosForm
from app.models import Livros
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    data = {}
    all = Livros.objects.all()
    search = request.GET.get('search')
    if search:
        data['search'] = search
        data['db'] = Livros.objects.filter(titulo__icontains=search)   
    else:
        paginator = Paginator(all, 7)
        pages = request.GET.get('page')
        data['db'] = paginator.get_page(pages)
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = LivrosForm()
    return render(request, 'form.html', data)

def create(request):
    form = LivrosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Livros.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
     data = {}
     data['db'] = Livros.objects.get(pk=pk)
     data['form'] = LivrosForm(instance=data['db'])
     return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Livros.objects.get(pk=pk)
    form = LivrosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
    return redirect('home')

def delete(request, pk):
    db = Livros.objects.get(pk=pk)
    db.delete()
    return redirect('home')