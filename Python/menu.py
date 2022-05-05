def msg():
    print('\n\nSejam Bem vindos!\n\n')
    nome = input('Por favor, insira seu nome: ')
    return nome

def Login(nome):
    print('\n----------------\n')
    print('Olá', nome, 'indentifique-se: ', '\n')
    email = input('Informe seu email: ')
    senha = input('Digite seu senha: ')
    dados = [email, senha]
    return dados

def menu():
    print("""
                Olá! Escolha uma opção: 

                1) - Visualizar Produtos
                2) - Efetuar Login
                3) - Sair

                """)

    opcao = int(input('>>>: '))
    return opcao

def cadastrarProduto():
    codProduto = int(input('Informe o codigo: '))
    nomeProduto = input('Informe o nome: ')
    valorProduto = float(input('Informe o valor: '))
    produto = [codProduto, nomeProduto,  valorProduto]
    return produto


def menuAdmin():
    print("""
    Olá Admin!

        1) - Cadastrar Produto
        2) - Ver Produto
        3) - Sair
                """)
    opcao = int(input('>>>: '))
    return opcao

def sair():
    print('Até mais, fechando essa porra! vá se foder CACHORRA(O)')