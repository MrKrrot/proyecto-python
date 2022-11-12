def factorial(n: int): 
    if n < 0:
        raise ValueError("El numero no puede ser negativo")
    if n == 0:
        return 1
    
    return n * factorial(n - 1)
    