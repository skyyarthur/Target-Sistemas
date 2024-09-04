import json

with open('faturamento.json', 'r') as file:
    dados = json.load(file)

faturamento_diario = dados['faturamento']

menor_faturamento = min(faturamento_diario)
maior_faturamento = max(faturamento_diario)

dias_com_faturamento = [valor for valor in faturamento_diario if valor > 0]
media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)

dias_acima_da_media = len([valor for valor in dias_com_faturamento if valor > media_mensal])

print(f"Menor valor de faturamento: R${menor_faturamento:.2f}")
print(f"Maior valor de faturamento: R${maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")