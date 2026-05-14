def fibonacci_ascendente(n):
    """Genera la secuencia de Fibonacci y la devuelve en orden ascendente."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    secuencia = [0, 1]
    for i in range(2, n):
        secuencia.append(secuencia[-1] + secuencia[-2])
        
    # Aseguramos el orden ascendente (menor a mayor)
    secuencia.sort()
    return secuencia

# Ejemplo de uso:
terminos = 10
resultado = fibonacci_ascendente(terminos)
print(f"Fibonacci en orden ascendente: {resultado}")