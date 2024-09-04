def fibo(num):
    a, b = 0, 1
    while a <num:
        a, b = b, a + b
    return a == num

numero = int(input('digite um número: '))
if fibo(numero):
    print(f'O número {numero} faz parte da sequência de fibonnacci ')
else:
    print(f'O número {numero} não faz parte da sequência de fibonnacci ')
