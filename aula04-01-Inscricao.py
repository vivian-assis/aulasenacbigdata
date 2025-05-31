
print('\n BEM VINDO AO SENAC \n')

'''while True:
    try:
        insc = input('Deseja realizar uma inscrição (s/n)?').lower()
        if insc == 's':
            break
        elif insc == 'n':
            print('ACESSO ENCERRADO, O SENAC AGRADECE SUA VISITA')
            break
    except:
        print('Digite uma opção válida: s para sim e n para não')'''
        

while True:
    try:
        nome1 = input('Digite seu primeiro nome:  ')
        if not nome1.isalpha():
            raise ValueError('Digite um nome válido sem números')
        else:
            break
    except ValueError as e:
        print(e)   

while True:
    try:
        nome2 = input('Digite seu segundo nome:  ')
        if not nome2.isalpha():
            raise ValueError('Digite um nome válido sem números')
        else:
            break
    except ValueError as e:
        print(e)   


while True:
    try:
        idade = int(input('Qual a sua idade:  '))
        break
    except ValueError:
        print('Dado inválido, somente números são aceitos para este campo')

while True:
    try:
        cpf = input('Digite o numero do cpf sem pontos ou espaços (ex: 00011100022):  ')
        if not cpf.isalpha() and len(cpf)==11:
            break
        elif not cpf.isalpha() and len(cpf)!=11:
            print('Verifique a quantidade de digitos')
        else:
            raise ValueError('Dado inválido, somente números são aceitos para este campo')
    except ValueError as e:
        print(e)          


'''while True:
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
        print(e)'''



cpf= input('Digite o numero do cpf sem pontos ou espaços (ex: 0001112233):  ')
sexo=input('Qual o seu gênero, ou qual gênero se identifica (F - Feminino, M-Masculino, X-Outro) :  ')

curso = int(input('Qual curso você deseja fazer conosco:\n1- Análise de Dados\n2- Power BI\n3- Desenvolvimento de Banco de Dados\n4- Outro\nDigite sua opção:  '))

match curso:
    case 1:
        print('Parabéns por escolher Análise de Dados\n')
    case 2:
        print('Parabéns por escolher Power BI\n')
    case 3:
        print('Parabéns por escolher Desenvolvimento de Banco de Dados\n')
    case 4:
        print('Acesse nosso site e veja outras opções\n')
    case _:
        print('Opção inválida\n')