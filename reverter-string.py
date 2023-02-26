frase = str(input("Digite uma frase: "))
fraseContrario = ''

for i in range(len(frase)):
  letraFim = frase[-i-1]

  fraseContrario += letraFim

print(fraseContrario) #Maneira normal de se fazer
print(frase[::-1]) #Maneira python de se fazer