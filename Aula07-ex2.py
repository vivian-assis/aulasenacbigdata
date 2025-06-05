user=['user00']
movie=['movie00']
usuarios_filmes={}

print('\n-----Bem-vindo à Briblioteca de Filmes----\n\n')
while True:
    try:
        opcao=input(int('===Menu===\n1-Adicionar filme\n2-Remover Filme\nVer filmes de um usuário\n4-Ver todos os usuários\n0-Sair\n\nDigite a opção desejada:  '))
        if opcao in (0,1,2,3,4):
            break
        else:
            print('Opcão inválida')
    except ValueError:
        print()

if opcao == 1:
    print('Preencha os dados para adicionar um filme\n')
            
elif opcao == 2:
    print('Preencha os dados para remover um filme\n')

elif opcao == 3:
    print('Digite o nome do usuário que deseja consultar\n')

elif opcao == 4:
    print('usuarios e filmes')
                    
elif opcao == 0:
            print('Encerrando...')
                
        








