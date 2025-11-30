# 1) Repetição – Crie um programa que peça um número ao usuário e conte de 1 até esse número, 
# exibindo todos os valores.

print("="*90)
numero = int(input("Digite um número para fazer contagem ate ele: "))

for i in range(numero):
    print(i+1)