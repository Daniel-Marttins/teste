def recuperarDadosAdm():
    banco = open("bd.txt", "r")
    dados = banco.readline()
    banco.close()
    return dados

def recuperarProdutos():
    banco = open("produtos.txt", "r")
    dados = banco.read()
    banco.close()
    return dados