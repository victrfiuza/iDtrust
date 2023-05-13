contador = 3
soma = 57
while contador <= 10:
    if contador < 5 or contador == 8:
        soma = soma - contador
    else:
        soma = soma + contador
    contador += 1
print("O valor da soma é", soma)