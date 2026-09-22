print('====== Cadastro De Pessoa ======')

def cadastro_pessoa():
    nome = input('Nome: ')
    sobrenome = input('Sobrenome: ')
    email = input('E-mail: ')
    telefone = input('Telefone: ')

    # Endereço
    cidade = input('Cidade: ')
    bairro = input('Bairro: ')
    rua = input('Rua: ')
    n_casa = input('N/CASA: ')


    # Dicionário

    pessoa = {
        'nome': nome,
        'sobrenome' : sobrenome,
        'email' : email,
        'telefone': telefone,
        'cidade': cidade,
        'bairro': bairro,
        'rua': rua,
        'n_casa': n_casa,
    }

    return pessoa
