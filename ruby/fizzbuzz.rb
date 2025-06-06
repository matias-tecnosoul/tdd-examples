# FizzBuzz implementation
def fizzbuzz(number)
  # Caso especial: si el número es 0, devolvemos 0
  return 0 if number.zero?

  # Si es múltiplo de AMBOS 3 y 5 (múltiplo de 15)
  return 'FizzBuzz' if !number.zero? && (number % 15).zero?

  # Si es múltiplo de 3 solamente
  return 'Fizz' if !number.zero? && (number % 3).zero?

  # Si es múltiplo de 5 solamente
  return 'Buzz' if !number.zero? && (number % 5).zero?

  # Si no es múltiplo de ninguno, devolvemos el número
  number
end