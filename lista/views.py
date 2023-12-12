from django.shortcuts import render
from .models import Item
from .forms import ItemForm
def lista(request):
    itens = Item.objects.all()
    context = {'itens': itens}
    return render(request, "index.html", context)

def add_item(request):
    if request.method == 'GET':
        form = ItemForm()
        context = {'form' : form}
        return render(request, "add_item.html", context)
   
def salvar_item(request):
    allTasks = Item.objects.all()
    context ={'sucesso': False, 'item':allTasks}
    if request.method == 'POST':
        item = request.POST.get['item']
        quantidade =request.POST.get['quantidade']
        preco =request.POST.get['preco']
        item = Item(item=item,quantidade=quantidade,preco=preco)
        item.save()
        context ={'sucesso': True,'item': allTasks}
    context={'item' : allTasks}
    return render(request, 'index.html', context)

