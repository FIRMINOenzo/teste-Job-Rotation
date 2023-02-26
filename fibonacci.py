def fibonacci (n1=0, n2=1, nDesejado=0):
  numFibonacci = n1 + n2

  n1 = n2
  n2 = numFibonacci

  if (nDesejado == numFibonacci):
    return True
  
  elif (numFibonacci > nDesejado):
      return False
  
  else:
      return fibonacci(n1, numFibonacci, nDesejado)

resultado = fibonacci(nDesejado=5)
print(resultado)