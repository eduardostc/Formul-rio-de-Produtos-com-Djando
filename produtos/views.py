from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Produto
# Create your views here.

def cadastrar(request):    
    #return HttpResponse('Olá mundo!')
    #print(request.method)
    if request.method == "GET":
        cd_erro = request.GET.get('cd_erro')
        texto = request.GET.get('texto')

        return render(request, 'cadastrar.html', {'cd_erro': cd_erro, 'texto': texto})
    elif request.method == "POST":
        #print(request.POST)
        produto = request.POST.get('produto')
        preco = request.POST.get('preco')

        if len(produto) <= 0:
            return redirect('/produtos/cadastrar/?cd_erro=1&texto=Digite o nome completo do produto')

        produto = Produto(
            nome_produto = produto,
            preco = preco
        )

        produto.save()

        #return HttpResponse(f'O produto selecionado foi {produto} e o preço dele foi {preco} reais')
        return redirect('/produtos/listar/')
    
def listar(request):
    nome_filtrado = request.GET.get('nome_filtrar')

    if nome_filtrado:
        produtos = Produto.objects.filter(nome_produto__icontains=nome_filtrado)  #nome_produto é a variavel da models produto
    else:
        #produto = Produto.objects.filter(nome_produto='Banana')
        produtos = Produto.objects.all()
    
    return render(request, 'listar.html', {'produtos': produtos})

def deletar(request, id):
    produto = Produto.objects.get(id=id)#o primeiro id se refere a coluna do bd id, já o segundo id referece a variavel id  digitada pelo usuário "passada na url".
    produto.delete()
    return redirect('/produtos/listar')
    #return HttpResponse(f'O valor digitado foi: {id}')