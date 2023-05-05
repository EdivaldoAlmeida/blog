# Inicialização de uma lista com dados
dados = [
    {'nome': 'João', 'idade': 32, 'cidade': 'São Paulo'},
    {'nome': 'Maria', 'idade': 45, 'cidade': 'Rio de Janeiro'},
    {'nome': 'José', 'idade': 53, 'cidade': 'Belo Horizonte'},
    {'nome': 'Luiza', 'idade': 28, 'cidade': 'Curitiba'},
    {'nome': 'Pedro', 'idade': 41, 'cidade': 'Recife'},
    {'nome': 'Smith', 'idade': 49, 'cidade': 'São Paulo'},
]

# Filtragem de dados
idades_acima_40 = [pessoa for pessoa in dados if pessoa['idade'] > 40]

# Agrupamento de dados
cidades = {}
for pessoa in dados:
    if pessoa['cidade'] not in cidades:
        cidades[pessoa['cidade']] = []
    cidades[pessoa['cidade']].append(pessoa)

# Impressão dos resultados
print("Pessoas com idade acima de 40:")
for pessoa in idades_acima_40:
    print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}")

print("\nAgrupamento por cidade:")
for cidade, pessoas in cidades.items():
    print(f"Cidade: {cidade}")
    for pessoa in pessoas:
        print(f"  Nome: {pessoa['nome']}, Idade: {pessoa['idade']}")
