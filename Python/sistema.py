import bancoDados as bd

def efetuarLogin(email, senha):
    dados = bd.recuperarDadosAdm()
    dadosSeparados = dados.split(" ")
    emailBD = dadosSeparados[0]
    senhaBD = dadosSeparados[1]
    logado = False
    if email == emailBD and senha == senhaBD:
        logado = True
    return logado

def verProdutos():
    dados = bd.recuperarProdutos()
    prods = dados.split('\n')
    for produto in prods:
        dadosProdutos = produto.split(",")
        codProduto = dadosProdutos[0]
        nomeProduto = dadosProdutos[1]
        valorProduto = float(dadosProdutos[2])
        print('Código de Barras: ', codProduto)
        print('Nome do Produto: ', nomeProduto)
        print('R$', valorProduto)


def sairAdmin():
    pass

verProdutos()