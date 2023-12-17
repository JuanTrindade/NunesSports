from django.shortcuts import render, redirect
from .models import Produto


def index(request):
    return render(request, 'login/index.html')

def cadastro_produtos(request):
    return render(request, 'cadastro/cadastro_produtos.html')

def listagem_produtos(request):
    produtos = Produto.objects.all()

    if request.method == 'POST':
        novo_produto = Produto()

        novo_produto.nome_produto = request.POST.get('nomeproduto')
        novo_produto.codigo_produto = request.POST.get('codigoproduto')
        novo_produto.descricao_produto = request.POST.get('descproduto')
        novo_produto.preco_produto = request.POST.get('precoproduto')

        novo_produto.save()

        return render(request, 'listagem/listagem_produtos.html', {'produtos': produtos})
    
    return render(request, 'listagem/listagem_produtos.html', {'produtos': produtos})

def excluir_produto(request):
    if request.method == 'POST':
        value = request.POST.get('produto')

        if value:
            Produto.objects.filter(pk=value).delete()

        return redirect('listagem_produtos')
    
def page_atualizar(request):
    produto_id = request.POST.get('produtoatualizar')

    if produto_id:
        produto = Produto.objects.get(pk=produto_id)
        return render(request, 'atualizar/atualizar.html', {'produtoid': produto_id, 'produto': produto})
    
    return redirect('listagem_produtos')

def atualizar_produto(request):
    if request.method == 'POST':
        produto_id = request.POST.get('produtoid')
        nome = request.POST.get('nomeproduto')
        codigo = request.POST.get('codproduto')
        descricao = request.POST.get('descproduto')
        preco = request.POST.get('precoproduto')

        Produto.objects.filter(pk=produto_id).update(
            nome_produto=nome, 
            codigo_produto=codigo, 
            descricao_produto=descricao, 
            preco_produto=preco
        )

        return redirect('listagem_produtos')