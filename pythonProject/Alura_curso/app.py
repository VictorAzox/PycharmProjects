import os

restaurantes = ['Pobres Lanches', 'Lanches Ricos']


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
    exibir_subtitulo('Finalizando o app')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def opcao_invalida():
    print('Opção invalida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de Novos Restaurantes')
  
    nome_restaurante = input("Digite o nome do Restaurante de que desaja cadastrar: ")
    categoria = input(f'Digite o nome da categoria do restaurante {nome_restaurante}: ')
    dados_do_restaurante = {'nome':nome_restaurante,'categoria':categoria, 'ativo':False}

    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso! ')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listar Todos Restaurantes')
    for restaurante in restaurantes :
        print(f'.{restaurante}')

    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))


        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3 :
            print('Ativar Restaurante')
        elif opcao_escolhida == 4 :
            finalizar_app()
        else :
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system('cls')
    exiber_nome_programa()
    exibir_opcoes()
    escolher_opcao()
    

if __name__ == '__main__':
    main()