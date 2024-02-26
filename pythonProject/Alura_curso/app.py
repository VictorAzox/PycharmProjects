import os

def exiber_nome_programa():
    print (""" 
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
 """)

def exibir_opcoes():
    print ('1. Cadastrar Restaurante')
    print ('2. Listar Restaurante')
    print ('3. Ativar Restaurante')
    print ('4. Sair')

def finalizar_app():
    os.system('cls')
    print('Finalizando o app\n')

def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))


    if opcao_escolhida == 1 :
        print('Cadastrar Restaurante')
    elif opcao_escolhida == 2 :
        print('Listar Restaurante')
    elif opcao_escolhida == 3 :
        print('Ativar Restaurante')
    else :
        finalizar_app()



def main():
    exiber_nome_programa()
    exibir_opcoes()
    escolher_opcao()
    

if __name__ == '__main__':
    main()