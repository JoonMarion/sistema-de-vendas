from django.contrib import admin
from django.urls import path
from app.views import home
from produto.views.views import produto_create, produto_delete, produto_edit, produto_form, produto_lista, produto_update


urlpatterns = [
    path('admin/', admin.site.urls),
    
     # HOME
    path('', home, name='home'),

    # PRODUTOS
    path('produto_lista/', produto_lista, name='produtolista'),
    path('produto_form/', produto_form, name='produtoform'),
    path('produto_create/', produto_create, name='produtocreate'),
    path('produto_edit/<uuid:pk>/', produto_edit, name='produtoedit'),
    path('produto_update/<uuid:pk>/', produto_update, name='produtoupdate'),
    path('produto_delete/<uuid:pk>/', produto_delete, name='produtodelete'),
]
