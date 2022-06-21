# num1 = input('Digite um numero:')
#
# if num1.isdigit():
#      num = int(num1)
#      if num%2 == 0:
#         print("É par")
#      else:
#          print ("É impar")
# else:
#      print("informe um numero inteiro")


hora = input("Informe a hora")
if hora.isdigit():
    hora = int(hora)
    if hora < 0 or hora > 23:
        print("Horário deve esta 0 e 23")
    else:
        if hora >= 0 and hora <= 11:
            print("Bom dia")
        elif hora>11 and hora<=17:
            print("Boa tarde")
        else:
            print("Boa noite")

else:
    print("Digie um hoŕario válido")

# nome = input("inseria eu nome completo")
# tamanho = len(nome)
# if tamanho<= 4:
#     print("Nome CURTO")
# elif tamanho >= 5 and tamanho <= 6:
#     print("Ttamanho normal de nome")
# elif tamanho >6:
#     print("muito grande")