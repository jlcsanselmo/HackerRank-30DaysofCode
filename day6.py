# utlizando o metodo slicing para inverter uma lista 

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    
    arr_invertido = arr[::-1]
    
    print(*arr_invertido)