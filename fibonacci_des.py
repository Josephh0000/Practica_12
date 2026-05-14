from time import time

# --- 1. Fibonacci con memoización (diccionario) ---
memoria = {0:1, 1:1}

def fib_des(n):
    # print(memoria)
    if n in memoria:
        return memoria[n]
    
    memoria[n] = fib_des(n-1) + fib_des(n-2)
    # print("fib({}) + fib({})".format(n-1, n-2))
    return memoria[n]

# --- 2. Fibonacci recursivo simple ---
def fibonacci(n):
    if n==0 or n==1:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)

# --- 3. Fibonacci ascendente con programación dinámica (lista) ---
dp = [1, 1]

def fib_asc(n):
    if n==0 or n==1:
        return dp[n]
    
    while len(dp) <= n:
        dp.append(dp[-1] + dp[-2])
    return dp[n]

# --- Pruebas de tiempo (opcional) ---
# t0 = time()
# fib_asc(50)
# print(time()-t0)

# t0 = time()
# fibonacci(50)
# print(time()-t0)