def generar_fibonacci(n):
    """Genera la secuencia de Fibonacci hasta n términos."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    secuencia = [0, 1]
    for i in range(2, n):
        siguiente_numero = secuencia[-1] + secuencia[-2]
        secuencia.append(siguiente_numero)
        
    return secuencia

# Ejemplo de uso:
terminos = 10
resultado = generar_fibonacci(terminos)
print(f"Secuencia de Fibonacci ({terminos} términos): {resultado}")