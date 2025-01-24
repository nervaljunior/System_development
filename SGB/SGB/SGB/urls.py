"""
URL configuration for SGB project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import home, cadastro, cadastros_pendentes, aprovar_cadastro, excluir_cadastro, lista_usuarios, editar_usuario, excluir_usuario, editar_usuario, cadastrar_bem, buscar_bem, solicitar_alteracao, autorizar_alteracao, page_gerente, page_colaborador, info_bem, sucesso


urlpatterns = [
        path('admin/', admin.site.urls),
    path('', home, name='login_view'),
    path('cadastro/', cadastro, name='form.html'),
    path('cadastros_pendentes/', cadastros_pendentes, name='cadastros_pendentes.html'),
    path('aprovar_cadastro/<int:user_id>/', aprovar_cadastro, name='aprovar_cadastro'),
    path('excluir_cadastro/<int:user_id>/', excluir_cadastro, name='excluir_cadastro'),
    path('lista_usuarios/', lista_usuarios, name='lista_usuarios.html'),
    path('editar_usuario/<int:user_id>/', editar_usuario, name='editar_usuario'),
    path('excluir_usuario/<int:user_id>/', excluir_usuario, name='excluir_usuario'),
    path('page_gerente/', page_gerente, name='page_gerente.html'),
    path('cadastrar_bem/', cadastrar_bem, name='cadastrar_bem'),
    path('page_colaborador/', page_colaborador, name='page_colaborador.html'),
    path('buscar_bem/', buscar_bem, name='buscar_bem'),
    path('solicitar_alteracao/', solicitar_alteracao, name='solicitar_alteracao'),
    path('info_bem/', info_bem, name='info_bem'),
    #path('alteracoes_pendentes/', alteracoes_pendentes, name='alteracoes_pendentes'),
    path('autorizar_alteracao/<int:bem_id>/', autorizar_alteracao, name='autorizar_alteracao'),
    path('sucesso/', sucesso, name='sucesso.html'),
    #path('bem_pendente/', bem_pendente, name='bem_pendente.html'),

      
]
