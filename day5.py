# O objetivo aqui é pegar uma palavra e separar as letras dela em dois grupos baseados na posição (índice) de cada letra
T = int(input())

for _ in range(T):
    palavra = input()
    pares = ""
    impares = ""

    for i in range(len(palavra)):
        if i % 2 == 0:
            pares += palavra[i]
        else:
            impares += palavra[i]

    print(pares, impares)