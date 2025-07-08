# Criar um programa onde mostre se o usuario pode tirar CNH ou não 

idade = int(input("Qual a sua idade: "))
if idade >=18:
    print("==="*10)
    print(f"Com {idade}, você já pode tirar CNH :) ")
    print("==="*10)
else: 
    print("==="*10)
    print(f"Com {idade}, ainda não pode tirar CNH :( )")
    print("==="*10)