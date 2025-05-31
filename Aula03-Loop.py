'''contador = 0

while contador <= 5:
    print(f'Nº {contador}')
    contador += 1'''

'''while True:
    senha = input('Digite a senha: ')

    if senha == 'senac@13455':
        print('Acesso permitido')
        break
    else:
        print('Senha inválida')'''

'''lista = []

while True:

    nome = input('Digite um nome\n')
    lista.append(nome)
    sair = input('Deseja adicionar mais um nome (s/n)? ').lower()
    if sair != 's':
        print('Cadastro encerrado')
        break
print(f'Nomes cadastrados:\n{lista}')'''

lista = []
while True:
    try :
        nome = input('Digite um nome\n')
        if not nome.isalpha():
            raise ValueError('Digite um nome válido sem números')
        
        lista.append(nome)

        sair = input('Deseja adicionar mais um nome (s/n)? ').lower()

        if sair != 's':
            print('Cadastro encerrado')
            break
        
    except ValueError as e:
        print(e)

print(f'Nomes cadastrados:\n{lista}')

    
