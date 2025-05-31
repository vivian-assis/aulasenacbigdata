while True:
    try:
        n1 = float(input('Digite o primeiro número:  '))
        break
    except ValueError:
        print('Dado inválido')

while True:
    try:        
        operacao = int(input('\nSelecione a operação desejada:\n 1 - Adição\n 2 - Subtração\n 3 - Multiplicação\n 4 - Divisão\n'))
        if operacao == 1 or 2 or 3 or 4:
            break
        else:
            print('Opção inválida, digite 1, 2, 3 ou 4')         
    except ValueError:
        print('Opção inválida')

while True:
    try:
        n2 = float(input('\nDigite o segundo número:  '))
        break
    except ValueError:
        print('Dado inválido')

match operacao:
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

