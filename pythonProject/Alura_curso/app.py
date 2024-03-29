import os


#restaurantes = ['Pobres Lanches', 'Lanches Ricos']
restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False},
                {'nome':'Pizza Suprema','categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}
                ]

def exiber_nome_programa():
    'Exibe o nome estilizado do programa na tela'
    print (""" 
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
 """)

def exibir_opcoes():
    'Exibir o menu na tela'
    print ('1. Cadastrar Restaurante')
    print ('2. Listar Restaurante')
    print ('3. Alternar Status do Restaurante')
    print ('4. Sair')

def finalizar_app():
    'Responsavél por entregar a mensagem de finalização do aplicativo'
    exibir_subtitulo('Finalizando o app')

def voltar_ao_menu_principal():
    'Botão que aparece no fim de cada fluxo para voltar ao menu principal'
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def opcao_invalida():
    'Mensagem de erro que apresenta a algun processo que não foi encontrado'
    print('Opção invalida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    'Responsavél por botar os asteristicos ao redor dos titulos '
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    "Essa função é responsável por cadastrar um novo restaurante "
    exibir_subtitulo('Cadastro de Novos Restaurantes')
  
    nome_restaurante = input("Digite o nome do Restaurante de que desaja cadastrar: ")
    categoria = input(f'Digite o nome da categoria do restaurante {nome_restaurante}: ')
    dados_do_restaurante = {'nome':nome_restaurante,'categoria':categoria, 'ativo':False}

    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso! ')
    voltar_ao_menu_principal()

def listar_restaurantes():
    "Listar os restaurantes cadastrados "
    exibir_subtitulo('Listar Todos Restaurantes')

    print(f"{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status")
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    "alterar o estatos de restaurante de ativado ou desativado"
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()

def escolher_opcao():
    "Fluxo de entrada para Fazer escolhe no menú as opções 1 ao 4"
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))


        if opcao_escolhida == 1 :
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2 :
            listar_restaurantes()
        elif opcao_escolhida == 3 :
            alternar_estado_restaurante()
        elif opcao_escolhida == 4 :
            finalizar_app()
        else :
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    'Chama a tela principal do menú'
    os.system('cls')
    exiber_nome_programa()
    exibir_opcoes()
    escolher_opcao()
    

if __name__ == '__main__':
    main()