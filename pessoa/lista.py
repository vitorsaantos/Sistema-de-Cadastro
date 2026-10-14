import json
from pessoa.cadastro import campo_obrigatorio

lista_pessoas = []

def lista_usuarios():
    for  contador, pessoa in enumerate(lista_pessoas):
        print(f'Pessoa {contador + 1}')
        print(f"Nome: {pessoa['nome']} {pessoa['sobrenome']}")
        print(f"E-mail: {pessoa['email']}")
        print(f"Telefone: {pessoa['telefone']}")
        print(f"Cidade: {pessoa['cidade']}")
        print(f"Bairro: {pessoa['bairro']}")
        print(f"Rua: {pessoa['rua']}")
        print(f"N/Casa: {pessoa['n_casa']}")
        print('----------------')


def selecionar_usuario():
    while True: 
        try:
            num_usuario = int(input('Digite o número do usuário(a) que deseja editar ou ("0" para voltar): '))
        except ValueError:
            print(f'Digite apenas número!')
            continue
            
        if num_usuario < 0:
            print('Usuário inválido!!!')
            continue

        elif num_usuario > len(lista_pessoas):
                print('Numéro de usuário inválido.')
                continue

        elif num_usuario == 0:
            return 
        
        indice = num_usuario - 1 

        pessoa_selecionada = lista_pessoas[indice]
        print(f"Usuário selecionado(a): {pessoa_selecionada['nome']}")
        print(f"Nome: {pessoa_selecionada['nome']} {pessoa_selecionada['sobrenome']}")
        print(f"E-mail: {pessoa_selecionada['email']}")
        print(f"Telefone: {pessoa_selecionada['telefone']}")
        print(f"Cidade: {pessoa_selecionada['cidade']}")
        print(f"Bairro: {pessoa_selecionada['bairro']}")
        print(f"Rua: {pessoa_selecionada['rua']}")
        print(f"Número da casa: {pessoa_selecionada['n_casa']}")
        print('\n')

        # Opções para usuário poder editar pessoa_selecionada
        print('1 - Nome')
        print('2 - Sobrenome')
        print('3 - E-mail')
        print('4 - Telefone')
        print('5 - Cidade')
        print('6 - Bairro')
        print('7 - Rua')
        print('8 - N_Casa')
        print('0 - (A qualquer momento para cancelar)')
        print('\n')


        while True:
            try:
                opcoes_pessoa_selecionada = int(input('O que você deseja alterar? '))
            except ValueError:
                print(f'Digite apenas número!')
                continue
        
            if opcoes_pessoa_selecionada < 0:
                print('Numéro inválido.')
                continue

            elif opcoes_pessoa_selecionada > 8:
                    print('Numéro inválido.')
                    continue

            elif opcoes_pessoa_selecionada == 0:
                return 

            if opcoes_pessoa_selecionada == 1 :
                novo_nome = input('Digite o nome: ').title()
                novo_nome = campo_obrigatorio(novo_nome)
                if novo_nome == '0':
                    print('Cancelado!!!')

                else:
                    pessoa_selecionada['nome'] = novo_nome
                    print("alterado com sucesso!!!")
                    salvar_usuario(lista_pessoas)
                    continue
                

            elif opcoes_pessoa_selecionada == 2:
                novo_sobrenome = input('Digite o sobrenome: ').title()
                novo_sobrenome = campo_obrigatorio(novo_sobrenome)
                if novo_sobrenome == '0':
                    print('Cancelado!!!')

                else:
                    pessoa_selecionada['sobrenome'] = novo_sobrenome
                    print("alterado com sucesso!!!")
                    salvar_usuario(lista_pessoas)
                    continue


            elif opcoes_pessoa_selecionada == 3:
                email = input('Digite o E-mail: ')
                email = campo_obrigatorio(email)
                if email == '0':
                    print('Cancelado!!!')
                    
                else:
                    pessoa_selecionada['email'] = email
                    print("alterado com sucesso!!!")
                    salvar_usuario(lista_pessoas)
                    continue

            elif opcoes_pessoa_selecionada == 4:
                novo_telefone = input('Digite o numero Telefone: ')

                if novo_telefone == '0':
                    print('Cancelado!!!')
                
                elif len(novo_telefone) != 11:
                    print('Telefone inválido!')
                
                elif not novo_telefone.isdigit():
                    print('Digite apenas números!!!')

                else:
                    pessoa_selecionada['telefone'] = novo_telefone
                    print("alterado com sucesso!!!")
                    salvar_usuario(lista_pessoas)
                    continue

            elif opcoes_pessoa_selecionada == 5:
                nova_cidade = input('Digite a Cidade: ').title()
                nova_cidade = campo_obrigatorio(nova_cidade)
                if nova_cidade == '0':
                    print('Cancelado!!!')
                
                else:
                    pessoa_selecionada['cidade'] = nova_cidade
                    print("alterado com sucesso!!!")
                    salvar_usuario(lista_pessoas)
                    continue

            elif opcoes_pessoa_selecionada == 6:
                novo_bairro = input('Digite o Bairro: ').title()
                novo_bairro = campo_obrigatorio(novo_bairro)
                if novo_bairro == '0':
                    print('Cancelado!!!')
                
                else:
                    pessoa_selecionada['bairro'] = novo_bairro
                    print("alterado com sucesso!!!")
                    salvar_usuario(lista_pessoas)
                    continue

            elif opcoes_pessoa_selecionada == 7:
                nova_rua = input('Digite a Rua: ').title()
                nova_rua = campo_obrigatorio(nova_rua)
                if nova_rua == '0':
                    print('Cancelado!!!')
                
                else:
                    pessoa_selecionada['rua'] = nova_rua
                    print("alterado com sucesso!!!")
                    salvar_usuario(lista_pessoas)
                    continue

            elif opcoes_pessoa_selecionada == 8:
                novo_n_casa = input('Digite o n/casa: ')
                novo_n_casa = campo_obrigatorio(novo_n_casa)
                if novo_n_casa == '0':
                    print('Cancelado!!!')
                
                else:
                    pessoa_selecionada['n_casa'] = novo_n_casa
                    print("alterado com sucesso!!!")
                    salvar_usuario(lista_pessoas)
                    continue

            else:
                print('Opção inválida!')

            
# 1 - Abre o arquivo usuario.json em modo escrita para escrever os dados no arquivo
# 2 - Pegue o conteúdo de lista_pessoas e escreva/salve no arquivo
def salvar_usuario():
    with open("usuario.json", "w") as arquivo:
        json.dump(lista_pessoas, arquivo)

# 1 - Abre o arquivo usuario.json em modo leitura
# 2 - Pega o conteúdo do arquivo e transforma em dados Python
# 3 - Retorna esses dados para quem chamou a função
def carregar_usuarios():
    with open("usuario.json", "r") as arquivo:
        dados = json.load(arquivo)
    return dados


def deletar_usuario():
    lista_usuarios = lista_pessoas

    if not lista_usuarios: 
        print('Não existe usuários.') 
        return 
    
    for  contador, pessoa in enumerate(lista_usuarios):
        print(f'Usuário: {contador + 1}')
        print(f"Nome: {pessoa['nome']} {pessoa['sobrenome']}")
        
    while True:
            try:
                delete_usuario = int(input('Digite o usuário(a) que deseja deletar ou ("0" para voltar):  '))
            except ValueError:
                print(f'Digite apenas número!')
                continue

            if delete_usuario == 0:
                return
            
            elif delete_usuario < 0:
                print('Numéro de usuário inválido.')
                continue

            elif delete_usuario > len(lista_usuarios):
                print('Numéro de usuário inválido.')
                continue

            indice = delete_usuario - 1 
            
            pessoa_selecionada = lista_usuarios[indice]
            print(f"Usuário selecionado(a): {pessoa_selecionada['nome']}")
            print(pessoa_selecionada['nome'] + " "  + pessoa_selecionada['sobrenome'])

            confirmacao = input('Deseja realmente deletar este usuário? (s/n): ')

            if confirmacao == 'n':
                print(f"Usuário(a) {pessoa_selecionada['nome']} não foi deletado.")
                break

            elif confirmacao == 's':
                lista_usuarios.pop(indice)
                print(f"Usuário(a) {pessoa_selecionada['nome']} foi deletado.")
                salvar_usuario(lista_usuarios)
                break

            else:
                print('Opeção inválida!')


def salvar_usuario(lista_pessoa):
    with open("usuario.json", "w") as arquivo:
        json.dump(lista_pessoa, arquivo)
        

    
        