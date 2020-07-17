import time


# Gera números primos até o limite estipulado
def infinite_prime():
    number = 2
    while True:
        if verify_prime(number) == True:
            yield number
        if number >= 1000:
            break
        number += 1


# Verifica cada número se é primo ou não
def verify_prime(num):
    if num % 2 == 0 and num > 2:
        return False
    root = int(num ** 0.5)
    for count in range(root, 1, -1):
        if num % count == 0:
            return False
    return True


def verify_prime_noroot(num):
    for count in range(num-1, 1, -1):
        if num % count == 0:
            return False
    return True


def infinite_prime2():
    number = 2
    while True:
        if verify_prime_noroot(number) == True:
            yield number
        if number >= 1000:
            break
        number += 1


t10 = time.time()
for number in infinite_prime():
    print(number)
t11 = time.time()
dif_time1 = t11 - t10
print(f'Duração do algoritmo: {dif_time1} segundos')

for count in range(5):
    print(count, end="...", flush=True)
    time.sleep(1)
    print()

t20 = time.time()
print('Iniciando o algoritmo 2')
for number in infinite_prime2():
    print(number)

t21 = time.time()
dif_time2 = t21 - t20
print(f'Duração do algoritmo: {dif_time2} segundos')
dif_algorithms = dif_time2 - dif_time1
print(f'A diferença entre os algoritmos é de: {dif_algorithms}')
