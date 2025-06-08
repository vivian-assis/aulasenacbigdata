usuarios_filmes={'user00':['filme00']}
print('\n-----Bem-vindo à Briblioteca de Filmes----')

while True:
    try:
        opcao=int(input('\n===Menu===\n1-Adicionar filme\n2-Remover Filme\n3-Ver filmes de um usuário\n4-Ver todos os usuários\n0-Sair\nDigite a opção desejada:  '))
        if opcao in [0,1,2,3,4]:
            match opcao:
                case 1:
                    while True:
                        print('\nPreencha os dados para adicionar um filme\n')
                        user=input('Nome do usuário:  ')
                        filme=input('Nome do filme:  ')
                        if user in usuarios_filmes.keys():
                            if filme not in usuarios_filmes[user]:
                                usuarios_filmes[user].append(filme)
                                print('Filme adicionado com sucesso!')
                            else:
                                print(f'Esse filme já existe na bliblioteca de {user}')
                        else:
                            usuarios_filmes[user] = [filme]               
                        
                        cont=input('\nDeseja adicionar um outro filme (s/n)?  ').strip().lower()
                        if cont=='s':
                            print('Vamos continuar')
                        elif cont=='n':
                            
                            break
                        else:
                            print('Opção inválida')
        
                case 2:
                    while True:
                        print('\nPreencha os dados para remover um filme\n')
                        user=input('Nome do usuário:  ')
                        if user in usuarios_filmes.keys():
                            remover=input('Nome do filme que deseja remover:  ')
                            if remover in usuarios_filmes[user]:
                                usuarios_filmes[user].remove(remover)
                    
                                cont=input(f'{remover} removido com sucesso!\nDeseja remover um outro filme (s/n)?  ').strip().lower()
                    
                                if cont=='s':
                                    print('Vamos continuar')
                                elif cont=='n':
                                    break
                                else:
                                    print('Opção inválida')
                    
                            else:
                                print(f'Filme não consta na biblioteca de {user} ')
                        else:
                            print('Esse nome de usuário não existe na biblioeca')
        
        
                case 3:
                    while True:
                        user=input('\nDigite o nome do usuário que deseja consultar:\n')
                        if user in usuarios_filmes.keys():
                            print(f'Usuário: {user}\nFilmes assistidos: {usuarios_filmes.get(user,'Não existe')}')
                        else:
                            print('Usuário não existe')
            
                        cont=input('\nDeseja consultar novamente (s/n)?  ')
                        if cont=='s':
                            print('Vamos continuar')
                        elif cont=='n':
                            break
                        else:
                            print('Opção inválida')

                case 4:
                    print('\nOk, ai estão todos os usuarios e filmes assistidos\n')
                    for a,b in usuarios_filmes.items():
                        print(f'{a}: {b}')
    
                case 0:
                    print('\nEncerrando...')
                    break
            
        else:
            print('\nOpcão inválida\n')
    except ValueError:
        print('Digite o número da opção\n')



