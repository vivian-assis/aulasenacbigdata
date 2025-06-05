produto= {'nome':'Mouse', 'preco' : 49.90 , 'estoque': 25}

for chave,valor in produto.items():
    print(f"Chave: {chave} , Valor: {valor}")

while True:
    consulta=input('Digite a chave que deseja consultar: ').lower()
    if consulta in (produto.keys)():
        print(f'O valor da chave {consulta} é: {produto.get(consulta)}')
        break
    else:
        print('Essa informação não está disponível')


dados_novos={'categoria':'Informática','preco':59.90}
produto.update(dados_novos)
del produto['estoque']

print(f'--Dados atualizados--')

for chave,valor in produto.items():
    print(f'{chave} : {valor}')
    