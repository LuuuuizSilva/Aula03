# 1 = branco 
# 2 = verde
# 3 = vermelho

print("Escolha um número: ")
print("=="*10)
print("1")
print("2")
print("3")
print("=="*10)
numero = int(input(""))

if numero == 1:
    print("=="*10)
    print(f"{numero} REPRESENTA BRANCO :) ")
    print("=="*10)
elif numero == 2:
    print("=="*10)
    print(f"{numero} REPRESENTA VERDE :) ")
    print("=="*10)
elif numero ==3:
    print("=="*10)
    print(f"{numero} REPRESENTA VERMELHO :) ")
    print("=="*10)
else: 
    print("CODIGO INVALIDO !!!")