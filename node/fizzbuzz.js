function fizzbuzz (n) {
  // Caso especial: si el número es 0, devolvemos 0
  if (n === 0) {
    return 0
  }

  // Si es múltiplo de AMBOS 3 y 5 (múltiplo de 15)
  if (n % 3 === 0 && n % 5 === 0) {
    return 'FizzBuzz'
  } else if (n % 3 === 0) {
    // Si es múltiplo de 3 solamente
    return 'Fizz'
  } else if (n % 5 === 0) {
    // Si es múltiplo de 5 solamente
    return 'Buzz'
  } else {
    // Si no es múltiplo de ninguno, devolvemos el número
    return n
  }
}

module.exports = fizzbuzz
