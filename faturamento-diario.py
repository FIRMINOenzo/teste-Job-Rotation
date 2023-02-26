import json

with open('teste-Job-Rotation\dados.json', 'r') as arq:
    dados = json.load(arq)
    arq.close()

def menorFaturamento(dados):
  menorFaturamento = dados[0]

  for d in dados:
    if d['valor'] == 0:
      continue
    elif (d['valor'] < menorFaturamento['valor']):
      menorFaturamento = d

  return menorFaturamento

#print(menorFaturamento(dados))

def maiorFaturamento(dados):
  maiorFaturamento = dados[0]

  for d in dados:
    if (d['valor'] > maiorFaturamento['valor']):
      maiorFaturamento = d

  return maiorFaturamento

#print(maiorFaturamento(dados))

def maiorQueMedia(dados):
  somaTot = 0
  diasMaiores = []

  for d in dados:
    somaTot += d['valor']

  mediaMensal = somaTot / len(dados)

  for d in dados:
    if d['valor'] > mediaMensal:
      diasMaiores.append(d)
  
  return diasMaiores

# maiores = maiorQueMedia(dados)
# print(maiores)
# totalDeDiasMaiores = len(maiores)
# print(totalDeDiasMaiores)