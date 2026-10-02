print('====== Cadastro De Pessoa ======')

def cadastro_pessoa():
    nome = input('Nome: ')
    resultado = cancelar_cadastro(nome)
    if resultado == None:
        return None

    sobrenome = input('Sobrenome: ')
    resultado = cancelar_cadastro(sobrenome)
    if resultado == None:
        return None

    email = input('E-mail: ')
    resultado = cancelar_cadastro(email)
    if resultado == None:
        return None

    telefone = input('Telefone: ')
    resultado = cancelar_cadastro(telefone)
    if resultado == None:
        return None

    cidade = input('Cidade: ')
    resultado = cancelar_cadastro(cidade)
    if resultado == None:
        return None

    bairro = input('Bairro: ')
    resultado = cancelar_cadastro(bairro)
    if resultado == None:
        return None

    rua = input('Rua: ')
def cadastro_pessoa():
    nome = input('Nome: ')
    resultado = cancelar_cadastro(nome)
    if resultado == None:
        return None

    sobrenome = input('Sobrenome: ')
    resultado = cancelar_cadastro(sobrenome)
    if resultado == None:
        return None

    email = input('E-mail: ')
    resultado = cancelar_cadastro(email)
    if resultado == None:
        return None

    telefone = input('Telefone: ')
    resultado = cancelar_cadastro(telefone)
    if resultado == None:
        return None

    cidade = input('Cidade: ')
    resultado = cancelar_cadastro(cidade)
    if resultado == None:
        return None

        
    bairro = input('Bairro: ')
    resultado = cancelar_cadastro(bairro)
    if resultado == None:
        return None

    rua = input('Rua: ')
    n_casa = input('N/CASA: ')
    resultado = cancelar_cadastro(rua)
    if resultado == None:
        return None

    n_casa = input('N/CASA: ')
    resultado = cancelar_cadastro(n_casa)
    if resultado == None:
        return None

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

def cancelar_cadastro(valor):
    if valor == '0':
        print('Cadasrto cancelado!')
        return None

    else:
        return valor
