n=0
itens=[]
precos=[]

nomes = []
#captar produtos
while True:
    if n <= 2:
        try :
            produto = input('Digite o nome do produto que deseja cadastrar:\n').title()
            
            if not produto.replace(' ','').isalpha():
                raise ValueError('Digite um nome de produto válido sem números ou caracteres especiais')
            else:
                itens.append
                try:
                    preco=float(input('Produto cadastrado, agora digite o seu preço:\n')
                    precos.append            
                    n+=1
                except ValueError:
                    print('Digite um valor válido')

            
            
                            
                n+=1
        except ValueError as e:
            print(e)
    else:
        break


    



    while n < len(itens):
        print (f'O produto {produto[n]} custa {precos[n]})
