# 12) Função + Dicionário + Repetição - Crie uma função cadastrar_pessoa() que: 
# • Peça nome 
# • Peça idade 
# • Peça cidade 
# • Retorne um dicionário com esses dados 
# No programa principal: 
# • Use um while para cadastrar várias pessoas 
# • Cada pessoa deve ser guardada dentro de uma lista de dicionários 
# • Pare quando o usuário digitar “sair” 
# • Ao final, exiba todos os cadastros organizados



print("="*90)
print("=== CADASTRO DE PESSOAS ===")
def cadastrar_pessoa(): # Define a função que vai cadastrar uma única pessoa
    nome = input("Digite o nome: ").title()
    idade = int(input("Digite a idade: "))
    cidade = input("Digite o nome da cidade: ").title()

    cadastro = {# Cria um dicionário para armazenar as informações da pessoa
     "nome": nome,
     "idade": idade,
     "cidade": cidade

     }
    return cadastro

lista_cadastro = [] # Lista onde todos os cadastros serão armazenados


while True:
    cadastro = cadastrar_pessoa() # Chama a função e recebe um dicionário com os dados
    lista_cadastro.append(cadastro) # Adiciona o dicionário dentro da lista de cadastros
    sair = input("Para encerrar digite a palavra (Sair) ou ENTER para continuar:").lower() 
    print("-"*90)
    if sair == 'sair':
        print("Encerrando os cadastros de nomes no sistema!\n")
        break
    print("="*90)

print("==== CADASTROS DE NOMES ====\n")
for i in range(len(lista_cadastro)): # Loop que percorre todos os índices da lista
    pessoa = lista_cadastro[i] # A variável "pessoa" recebe o dicionário correspondente ao índice atual
    print("-"*90)
    print(f"{i+1}º Cadastro:\nNome: {pessoa['nome']}. \nIdade: {pessoa['idade']}. \nCidade: {pessoa['cidade']}.\n\n")
    print("==== NOVO CADASTRO ====")








