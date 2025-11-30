# 11) Função + Lista – Crie uma função chamada calcular_media(lista_notas). A função deve 
# retornar a média dos valores. 
# No programa principal: 
# • Peça 4 notas ao usuário 
# • Coloque numa lista 
# • Use a função para calcular a média 
# • Exiba o resultado

print("="*90)
print("==== Calculando notas e mostrando a mésia ====")
lista_notas = []#lista onde irá armazenar as notas
def informa_nota():#função
  for i in range(4):#Repete o código 4 vezes, uma para cada nota
   notas = float(input(f"Didite a {i+1}ª nota: "))
   lista_notas.append(notas)#Guarda cada nota dentro da lista lista_notas.
informa_nota () #chama a funcção

def media_nota(lista_notas):
    soma = sum(lista_notas)# soma todos os valores da lista
    quantidade = len(lista_notas)# conta quantos elementos tem na lista
    media = soma / quantidade # calcula a média
    print(f"As notas digitadas foram: {lista_notas} ")
    print (f"A média das notas é: {media}.")
                
media_nota(lista_notas) # chama a função, retorna o resultado calcula e mostra a média.