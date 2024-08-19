#1
# homen = {'nome' : 'Gabriel', 'idade': 19, 'cidade': 'São Paulo'}
# #2
# homen['cidade'] = 'Osasco'
# homen['profissao'] = 'Encanador'
# del homen['cidade']
# print(homen)

#3
# numeros_quadrados = {x: x**2 for x in range (1, 6)}
# print(numeros_quadrados)

#4
# homen = {'nome' : 'Gabriel', 'idade': 19, 'cidade': 'São Paulo'}
# if 'data' in homen:
#     print("A chave 'data' existe no dicionário.")
# else:
#     print("A chave 'data' não existe no dicionário.")

#5

frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)