from django.shortcuts import render
from django.shortcuts import redirect, render
from cliente.forms import ClienteForm
from ..models.cliente import Cliente


def cliente_lista(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Cliente.objects.filter(nome_cliente__icontains=search)
    else:
        data['db'] = Cliente.objects.all()
    return render(request, 'cliente/lista.html', data)

def cliente_form(request):
    data = {}
    data['form'] = ClienteForm()
    return render(request, 'cliente/form.html', data)

def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST or None)        
        if form.is_valid():
            form.save()
            return redirect('clienteform')

def cliente_edit(request, pk):
    data = {'db': Cliente.objects.get(pk=pk)}
    data['form'] = ClienteForm(instance=data['db'])
    return render(request, 'cliente/form.html', data)

def cliente_update(request, pk):
    data = {}
    data['db'] = Cliente.objects.get(pk=pk)
    form = ClienteForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('clienteform')

def cliente_delete(request, pk):
    db = Cliente.objects.get(pk=pk)
    db.delete()
    return redirect('clientelista')