"""Estruturas de decisão e operadores relacionais  """


if False:
    print('verdadeiro')
elif False:
    print('Agora verdadeiro')
elif False:
    print("Maria uma verdad")
# else:
#     print('falsa')

"""operadores relacionais  """
# num1 = 3
# num2 = 2
#
# expressao = (num1 <= num2)
# print(expressao)
#
# nome = input("Qual o seu nome?")
# idade = input("Qual a sua idade?")
# idade = int(idade)

#Limite para pegar empréstimo

# idade_menor = 20
# idade_maior = 30
#
# if idade_menor <= idade <= idade_maior:
#     print(f'{nome} pode pegar o emprestimo.')
# else:
#     print(f'{nome} Não pode pegar o empréstimo.')

"""operadores lógicos  """
a = "Achei um caractere"
b = ''

if 'b' not in a:
    print('Achei um caractere')
else:
    print("Esse caractere não existe")

usuario = input("Nome de usuário: ")
senha = input('senha do usuário;')
usuario_bd = 'luiz'
senha_bd = '12345'

if usuario_bd == usuario and senha_bd == senha:
    print('VOcê logou')
else:
    print('Usuário e senha inválidos')
