def fatorial(n):
    if n == 1:
        return 1
    else:
        return n * fatorial(n-1)

# Exemplo de uso
print(fatorial(5)) # Saída: 120
