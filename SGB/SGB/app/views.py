from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render, redirect
from .models import User, Bem

from .forms import UserRegistrationForm, UserLoginForm, BemForm, AlteracaoBemForm
from .forms import CustomUserChangeForm
from django.http import JsonResponse
from django.contrib.auth import authenticate, login



# Create your views here.
#def home(request):
#    return render(request, 'admin.html')


def home(request):
    data = {}
    if request.method == 'POST':
       form = UserLoginForm(request.POST)
       if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None and user.is_approved:
                login(request, user)
                if user.user_type == User.COLABORADOR:
                    return redirect('page_colaborador.html')
                elif user.user_type == User.GERENTE:
                    return redirect('page_gerente.html')
            else:
                data['msg'] = 'Login inválido ou cadastro não aprovado.'
                data['class'] = 'alert-danger'
    else:
        form = UserLoginForm()
    return render(request, 'login_view.html', {'form': form})


def cadastro(request):
    data = {}
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            confirm_password = form.cleaned_data.get('confirm_password')
            if password == confirm_password:
                user.set_password(password)
                user.save()
                data['msg'] = 'Cadastro realizado com sucesso! Aguarde a aprovação do administrador.'
                data['class'] = 'alert-success'
            else:
                data['msg'] = 'As senhas não coincidem'
                data['class'] = 'alert-danger'
        else:
            data['msg'] = 'Erro no formulário'
            data['class'] = 'alert-danger'
    else:
        form = UserRegistrationForm()
    return render(request, 'form.html', {'form': form, 'data': data})




# Caso seja um pedido GET, exibir o formulário de login
    return render(request, 'login.html')
#Formulário para cadastro de users
def form(request):
    return render(request, 'form.html')
# Get de dados dos users

#
def cadastros_pendentes(request):
    usuarios_pendentes = User.objects.filter(is_approved=False)
    return render(request, 'cadastros_pendentes.html', {'usuarios_pendentes': usuarios_pendentes})

def aprovar_cadastro(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.is_approved = True
    user.save()
    
    # Remover o usuário aprovado da lista de usuários pendentes
    usuarios_pendentes = User.objects.filter(is_approved=False).exclude(id=user_id)
    
    return render(request, 'cadastros_pendentes.html', {'usuarios_pendentes': usuarios_pendentes})




def excluir_cadastro(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('cadastros_pendentes.html')  # Corrigido o nome da rota


        
    



def lista_usuarios(request):
    usuarios_aprovados = User.objects.filter(is_approved=True)
    return render(request, 'lista_usuarios.html', {'usuarios_aprovados': usuarios_aprovados})


def editar_usuario(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios.html')
    else:
        form = CustomUserChangeForm(instance=user)
    return render(request, 'editar_usuario.html', {'form': form, 'user': user})


def excluir_usuario(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('lista_usuarios.html')


def page_gerente(request):
    bens_pendentes = Bem.objects.filter(autorizado=False)
    return render(request, 'page_gerente.html', {'bens_pendentes': bens_pendentes})


def cadastrar_bem(request):
    if request.method == 'POST':
        form = BemForm(request.POST)
        if form.is_valid():
            bem = form.save(commit=True)
            bem.autorizado = True  # Definir como False ao cadastrar um novo Bem
            bem.save()
            return redirect('page_gerente.html')
    else:
        form = BemForm()
    return render(request, 'page_gerente.html', {'form': form})



def page_colaborador(request):
    return render(request, 'page_colaborador.html')



def buscar_bem(request):
    if request.method == 'POST':
        codigo = request.POST['codigo']  # Obtém o código enviado pelo formulário de busca
        try:
            bem = Bem.objects.get(codigo=codigo)  # Tenta encontrar um bem com o código especificado
            return render(request, 'info_bem.html', {'bem': bem})
        except Bem.DoesNotExist:
            return render(request, 'page_colaborador.html', {'error_message': 'Nenhum bem encontrado com o código especificado.'})
    else:
        return render(request, 'page_colaborador.html')
    
def solicitar_alteracao(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo_bem')
        local_utilizacao = request.POST.get('novo_local')
        try:
            bem = Bem.objects.get(codigo=codigo)
            bem.local_utilizacao = local_utilizacao
            bem.autorizado = False  # Definir como False ao alterar o local de utilização
            bem.save()
            return redirect('sucesso.html')
        except Bem.DoesNotExist:
            return render(request, 'page_colaborador.html', {'message': 'Bem não encontrado.'})
    return render(request, 'page_colaborador,html')



def sucesso(request):
    return render(request, 'sucesso.html')


#def alteracoes_pendentes(request):
    bens_pendentes = Bem.objects.filter(autorizado=False)
    return render(request, 'page_gerente.html', {'bens_pendentes': bens_pendentes})


def autorizar_alteracao(request, bem_id):
    bem = Bem.objects.get(id=bem_id)
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        try:
            bem = Bem.objects.get(codigo=codigo)
            bem.autorizado = True
            bem.save()
            return redirect('sucesso.html')
        except Bem.DoesNotExist:
            return render(request, 'page_gerente.html', {'message': 'Bem não encontrado.'})
    return render(request, 'page_gerente.html')




def info_bem(request):
    codigo_bem = request.GET.get('codigo_bem')
    try:
        bem = Bem.objects.get(codigo=codigo_bem)
        data = {
            'success': True,
            'bem': {
                'local_utilizacao': bem.local_utilizacao,
            }
        }
    except Bem.DoesNotExist:
        data = {
            'success': False,
            'message': 'Bem não encontrado.',
        }
    
    return JsonResponse(data)