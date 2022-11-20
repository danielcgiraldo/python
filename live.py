import time
import math

# ========================================== PRIMOS ==========================================


def esprimo(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def filterprimo(tope):
    listaprimo = list(filter(esprimo, range(2, tope + 1)))
    listaprimos = [y for y in listaprimo]
    return listaprimos


def gen_primos(N):
    for i in range(2, N+1):
        if esprimo(i):
            yield i

# ========================================== FACTORIAL ==========================================


def tailFactorial(n, tail=1):
    if n == 1:
        return tail
    tail *= n
    return tailFactorial(n - 1, tail)

# ============= TIMER FACTORIAL ===================

# === SIMPLE FACTORIAL === #

# def factorial(n):
#  if n<=0:
#    return 1
#  else:
#    return n*factorial(n-1)

#start = time.time()
# factorial(50)
#end = time.time()
#print("Factorial Normal de 50 Elapsed time:",end - start,'seconds')

# === TAIL FACTORIAL === #

#start = time.time()
# tailFactorial(50)
#end = time.time()
#print("Factorial Cola de 50 Elapsed time:",end - start,'seconds')

# ========================================== FIBONACCI ==========================================


def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def tailfibonacci(n, a=0, b=1):
    if n == 0:
        return a
    if n == 1:
        return b
    return tailfibonacci(n - 1, b, a + b)

# ============= TIMER FIBONACCI ===================

# === SIMPLE FIBONACCI === #
#start = time.time()
# fibonacci(50)
#end = time.time()
#print("Fibonacci Normal de 50 Elapsed time:",end - start,'seconds')

# === TAIL FIBONACCI === #
#start = time.time()
# tailfibonacci(50)
#end = time.time()
#print("Fibonacci Tail de 50 Elapsed time:",end - start,'seconds')

# ========================================== DarkSouls ==========================================


def subconjuntos(pesos):
    if len(pesos) > 1:
        for item in subconjuntos(pesos[1:]):
            yield [pesos[0]]+item
            yield item
    else:
        yield pesos
        yield []

def existe(max, pesos):
    result = []
    subc = [i for i in subconjuntos(pesos) if len(i) != 0]
    
    for subconjunto in subc:
        if(sum(subconjunto) == max):
            subconjunto.sort()
            result.append(subconjunto)
    result.sort(key=lambda x: x)
    
    return sorted(result, key=len)

