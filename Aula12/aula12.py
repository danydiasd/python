#Estruturas de repetição


# x= 0
#
# while x<10:
#     y = 0
#     while y < 5:
#      print(f'x vale {x} e Y vale {y}1')
#      y += 1
#
#     x += 1
#
# print("Acabou!")
#
# while True:
#     print()
#     num1 = input('Digite um número:')
#     num2 = input('Digite outro número:')
#     operador = input('Digite um operador:')
#     sair = input("Deseja sair? [s] Sim ou [n] Não")
#
#     if sair == 's':
#         break
#
#     if not num1.isnumeric() or not num2.isnumeric():
#         print("Você precisa digitar")
#         continue
#
#     num1 = int(num1)
#     num2 = int(num2)
#
#     if operador == '+':
#         print(num1 + num2)
#     elif operador == '-':
#         print(num1 - num2)
#     elif operador == '/':
#         print(num1 / num2)
#     elif operador == '*':
#         print(num1 * num2)
#     else:
#         print("Operador inválido")

contador = 1
acumulador = 1

while contador <100:
    print(contador, acumulador)
    acumulador = acumulador + contador
    contador += 1
