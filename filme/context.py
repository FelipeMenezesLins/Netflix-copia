from .models import*

def filmes_destaques(request):
    lista_filme_destaque = Filme.objects.order_by('-data')
    if lista_filme_destaque:
        filme_destaque = lista_filme_destaque[0]
        return  {'filme_destaque': filme_destaque}
    else:
        filme_destaque = lista_filme_destaque[0]
        return None

def categorias_destaques(request):
    categoria = Filme.objects.filter(categoria = 'AÇÃO')
    return {'acao': categoria}

def filmes_populares(request):
    lista_filmes_populares = Filme.objects.all().order_by('-visualizacoes')[0:10]
    return {"filmes_populares": lista_filmes_populares}