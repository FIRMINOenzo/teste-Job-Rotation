faturamentoGeral = {
  'SP': 67836.43,
  'RJ': 36678.66,
  'MG': 29229.88,
  'ES': 27165.48,
  'OUTROS':  19849.53
}

totalGeral = 0
resultado = []

for key, value in faturamentoGeral.items():
    totalGeral += value

for key, value in faturamentoGeral.items():
    calc = value / totalGeral * 100
    resultado.append([key, round(calc, 2)])

print(resultado)
