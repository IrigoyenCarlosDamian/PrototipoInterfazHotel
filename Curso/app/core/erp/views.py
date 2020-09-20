from django.shortcuts import render
from core.erp.models import Categoria
# Create your views here.
from django.contrib.auth.decorators import login_required
@login_required
def  primervista(request):

    return render(request, 'index.html')

def category_list(request):
    data= {
        'title': 'Listado De Categorias',
        'categoria': Categoria.objects.all()
    }
    return render(request, 'list.html',data)
