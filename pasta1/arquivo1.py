lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, -10]
negativo = False

for numero in lista:
  if numero < 0:
      negativo = True
      break

  if negativo:
    print("Existe pelo menos um número negativo na lista.")
  else:
    print("Não existe número negativo na lista.")

print("Teste novo")