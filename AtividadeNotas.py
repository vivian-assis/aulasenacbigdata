alunos_notas={'Aluno00':[10.0,5.0,7.5]}


def cadastro():
    while True:
        print('\nPreencha os dados para cadastrar um aluno e/ou suas notas\n')
        nome=input('Nome do aluno:  ').title()
        
        while True:
            try:
                n1=float(input('Digite a primeria nota: '))
                break
            except ValueError:
                print('Nota inválida')
        while True:
            try:
                n2=float(input('Digite a segunda nota: '))
                break
            except ValueError:
                print('Nota inválida')
        while True:
            try:
                n3=float(input('Digite a terceira nota: '))
                break
            except ValueError:
                print('Nota inválida')
    
            
        if nome in alunos_notas.keys():
            alunos_notas[nome].append(n1)
            alunos_notas[nome].append(n2)
            alunos_notas[nome].append(n3)
            print(f'Notas cadastradas com sucesso.')
        
        else:
            alunos_notas[nome]= [n1,n2,n3]
            print('Aluno cadastrado com sucesso!')
        
        cont=input('Digite S para sim ou N para não:  ').strip().upper()
        if cont=='S':
            print('Vamos continuar')
        elif cont=='N':
            break
        else:
            print('Opção inválida')

def cmedia(a):
    return sum(a) / len(a)
    
def calcmedia():
    while True:
        print('\nPreencha os dados consultar a média\n')
        nome=input('Nome do aluno:  ').title()
        if nome in alunos_notas.keys():
            a=alunos_notas.get(nome)
            cmedia(a)
            print(f'O aluno {nome} possui {len(a)} notas cadastradas,sua média é: {cmedia(a)}')
            
        elif nome not in alunos_notas.keys():
            print('Nome não existe no sistema')
            
        else:
            print(f'{nome} não possui notas no sistema')
            
        print('\nDeseja consultar a média de outro aluno (s/n)?')
        cont=input('Digite S para sim ou N para não:  ').strip().upper()
        if cont=='S':
            print('Vamos continuar')
        elif cont=='N':
            break
        else:
            print('Opção inválida')
    
def situacao(a):
    if cmedia(a) >=5.0:
        print('Situação: Aprovado')
    elif cmedia(a)>3.0 and cmedia(a)<5:
        print('Situação: Recuperação')
    else:
        print('Situção: Reprovado')

def versituacao():
    while True:
        nome=input('\nDigite o nome do aluno deseja consultar:\n').title()
        a=alunos_notas.get(nome)
        if nome in alunos_notas.keys():
            situacao(a)
        else:
            print('Aluno não consta no sinema')
        print('\nDeseja consultar outro aluno?')
        cont=input('Digite S para sim ou N para não:  ').strip().upper()
        if cont=='S':
            print('Vamos continuar')
        elif cont=='N':
            break
        else:
            print('Opção inválida')
            
def boletim():
    while True:
        nome=input('\nDigite o nome do aluno deseja consultar:\n').title()
        if nome in alunos_notas.keys():
            a=alunos_notas.get(nome)
            print(f'Aluno: {nome}')
            print(f'Notas: {a}')
            print(f'Media: {cmedia(a)}')
            situacao(a)
                            
        elif nome not in alunos_notas.keys():
            print('Usuário não existe')
                        
        print('\nDeseja consultar novamente?')
        cont=input('Digite S para sim ou N para não:  ').strip().upper()
        if cont=='S':
            print('Vamos continuar')
        elif cont=='N':
            break
        else:
            print('Opção inválida')
            
def boletins():
    for a,b in alunos_notas.items():
        print(f'Aluno: {a}\nNotas: {b}\nMédia: {cmedia(b)}')
        situacao(b)
                        
        while True:
            cont=input('\nDigite R para retornar ao menu:  ').strip().upper()
            if cont=='R':
                break
            else:
                print('Opção inválida')
    

print('\n-----Bem-vindo ao Sistema Escolar----')
while True:
    try:
        opcao=int(input('\n===Menu===\n1-Cadastrar aluno\n2 –Calcular a média\n3-Verificar a situação\n4–Exibir o boletim\n5–Exibir todos os boletins\n0-Sair\nDigite a opção desejada:  '))
        if opcao in [0,1,2,3,4,5]:
            match opcao:
                case 1:
                    cadastro()
                    
                case 2:
                    calcmedia()
                    
                case 3:
                    versituacao()
                    
                case 4:
                    boletim()
                    
                case 5:
                    boletins()
                
                case 0:
                    print('\nEncerrando...')
                    break
            
        else:
            print('\nOpcão inválida\n')
    except ValueError:
        print('Digite o número da opção\n')
        


