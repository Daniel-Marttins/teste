import menu as mn
import sistema as st

nomeUsuario = mn.msg()

while(True):

    menu = mn.menu()

    if menu == 1:
        st.verProdutos()
    
    elif menu == 2:
        dadosUsuario = mn.Login(nomeUsuario)
        adminLogado = st.efetuarLogin(dadosUsuario[0], dadosUsuario[1])
        if(adminLogado == True):
            opcao = mn.menuAdmin()
            if opcao == 1:
                print(mn.cadastrarProduto())

    elif menu == 3:
        mn.sair()
        break