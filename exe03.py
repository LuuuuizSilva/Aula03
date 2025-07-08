lista = []
primeiro_numero = float(input("Digite um numero: "))
lista.append (primeiro_numero)
segundo_numero = float(input("Digite o segundo número: "))
lista.append(segundo_numero)
if lista[0] >lista[1]:
    print(f"{lista[0]} é maior que {lista[1]}")
else: 
    print(f"{lista[0]} é menor que {lista[1]}")