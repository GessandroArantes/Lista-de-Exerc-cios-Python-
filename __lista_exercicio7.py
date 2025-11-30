# 7) Match Case – Crie um menu usando match case: 
# 1 - Olá   
# 2 - Informações   
# 3 - Sair 
# Dependendo da escolha, exiba uma mensagem adequada. 

print("="*90)
print("=== Escolha a opção desejada ===")

def menu ():
      print("1 - Olá")
      print("2 - Informações")
      print("3 - Sair ")

menu()  
opcao = input("Digite o número da desejada: ")
while True:  
     if opcao not in ['1','2','3']:
      print("Opção invalida! Tente novamente.")
     else:
        match opcao:
           case '1':
              print("Você escolheu _Olá")
           case '2':
                print("Você escolheu _Informações")
           case '3':
                print("Você escolheu _Sair")
                break
     print("-"*90)
     menu()
     opcao = input("Digite o número da desejada: ")

    


