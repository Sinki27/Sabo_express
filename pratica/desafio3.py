#numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#nomes = ['gabriel', 'miguel', 'milena', 'geovana']
#anos = [2005, 2024]


# teste = [2, 3, 4, 5, 6]
# for testes in teste:
#     print(f'.{testes}')


# soma_impares = 0
# for i in range(1, 11, 2):
#     soma_impares += i
# print(soma_impares)


# for i in range(0, 11, 1):
#     print(i)



numero_multipicacao = int(input('Digite o numero a ser mutlipicado: '))
for i in range(1, 11):
    resultado = numero_multipicacao * i
    print(f"{numero_multipicacao} x {i} = {resultado}")

# lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# soma = 0

# try:
#     for numero in lista_numeros:
#         soma += numero
#     print(f'Soma dos elementos: {soma}')
# except Exception as e:
#     print(f'Ocorreu um erro: {e}')

# lista_valores = [10, 7, 4]
# soma_valores = 0

# try:
#     for valor in lista_valores:
#         soma_valores += valor
#     media = soma_valores / len(lista_valores)
#     print(f'Média dos valores: {media}')
# except ZeroDivisionError:
#     print('A lista está vázia, não é possivel calcular a média.')
# except Exception as e:
#     print(f'Ocorreu um erro : {e}')