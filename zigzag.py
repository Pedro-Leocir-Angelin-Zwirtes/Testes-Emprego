palavra = input()
numero_linhas = int(input())

if numero_linhas == 1 or numero_linhas >= len(palavra):
    print(palavra)
else:
    
    linhas = [''] * numero_linhas
    linha_atual = 0
    linha_abaixo = False

    for char in palavra:
        linhas[linha_atual] += char

        if linha_atual == 0 or linha_atual == numero_linhas - 1:
            linha_abaixo = not linha_abaixo

        linha_atual += 1 if linha_abaixo else -1

    resultado = ''.join(linhas)
    print(resultado)
