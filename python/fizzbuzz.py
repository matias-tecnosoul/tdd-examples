def fizzbuzz(n):
    # Caso especial: si el número es 0, devolvemos 0
    if n == 0:
        return 0

    # Si es múltiplo de AMBOS 3 y 5 (múltiplo de 15)
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'

    # Si es múltiplo de 3 solamente
    elif n % 3 == 0:
        return 'Fizz'

    # Si es múltiplo de 5 solamente
    elif n % 5 == 0:
        return 'Buzz'

    # Si no es múltiplo de ninguno, devolvemos el número
    else:
        return n

#  if __name__ == "__main__":
#     # Probamos algunos números
#     for i in range(16):
#         print(f"{i} -> {fizzbuzz(i)}")
