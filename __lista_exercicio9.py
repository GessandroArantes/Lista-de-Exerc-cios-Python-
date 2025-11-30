# 9) Dicionário – Crie um dicionário com 3 produtos e seus preços. Depois permita ao usuário digitar 
# o nome de um produto e mostre seu preço. Se não existir, exiba “Produto não cadastrado”.


mercado = {
    "Arroz": 5.99,
    "Feijão": 7.49,
    "Macarrão": 4.29
}

print("="*90)
print("=== Produtos do Mercado ===")
produto = input("Digite o nome do produto desejado: ").title()
if produto in mercado:
    preco = mercado[produto]
    print(f"Temos o produto: {produto} e está por: R${preco} reais.")
else:
    print("Produto nao encontrado!")