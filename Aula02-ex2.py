'''O usuário irá inserir dois números e após isso o sistema irá mostrar um menu de opções de cacordo com a opção selecionada'''
'''O resultado será exibido'''
print('\nBem vindo\n')
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
opcao = int(input('\nMenu:\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\nDigite a opção de cálculo que deseja realizar: '))

match opcao:
    case 1:
        print(f'Soma {n1} + {n2} = {n1+n2}\n')
    case 2:
        print(f'Subtração de {n1} - {n2} = {n1-n2}\n')
    case 3:
        print(f'Multiplicação {n1} x {n2} = {n1*n2}\n')
    case 4:
        print(f'Divisão {n1} : {n2} = {n1/n2} e resto = {n1%n2}\n')
    case _:
        print('Opção inválida\n')


