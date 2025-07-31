numeros_romanos = [
    "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X",
    "IX", "V", "IV", "I"
]

numeros = [
    1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1
]

romanos = ""

n_recebido = int(input())

for i in range(13):
    j = n_recebido // numeros[i]
    for x in range(1, j + 1):
        romanos = romanos + numeros_romanos[i]
    n_recebido = n_recebido - numeros[i] * j

print(romanos)