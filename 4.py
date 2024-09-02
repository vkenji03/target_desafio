FATURAMENTOS = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

total = 0
for faturamento in FATURAMENTOS.values():
    total += faturamento

print('Percentual de representação de cada estado no valor total mensal da distribuidora:')

for estado, faturamento in FATURAMENTOS.items():
    print(f'{estado}: {faturamento / total * 100:.2f}%')