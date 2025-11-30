# 8) Dicionário – Crie um dicionário com os seguintes campos: 
# • Nome 
# • Idade 
# • Curso 
# Peça os valores ao usuário e ao final exiba o dicionário completo formatado.

print("="*90)
print("=== Preencha o formulario a seguir ===")
nome = input("Digite o nome: ").title()
idade = int(input("Digite a idade: "))
curso = input("Digite o nome da cidade: ").title()

dicionario = {
     "nome": nome,
     "idade": idade,
     "curso": curso

     }
print("="*90)
print("Dados Digitados")
print(f"Nome: {dicionario['nome']}.\nIdade: {dicionario['idade']}.\nCurso: {dicionario['curso']}")
print("="*90)
print("Dados dentro do dicionario")
print(f"{dicionario['nome']}. {dicionario['idade']}. {dicionario['curso']}")