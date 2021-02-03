numeros = []

while(len(numeros) < 10):
    numero = int(input("Digite um número: "))

    if numero not in numeros:
        numeros.append(numero)

print(f'Números: ', end='')
for numero in numeros:
    print(numero, end='; ')