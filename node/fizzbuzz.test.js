const { test, expect } = require('@jest/globals')
const fizzbuzz = require('./fizzbuzz')

test('print zero with zero', () => {
  expect(fizzbuzz(0)).toBe(0)
})

test('print same number on 1, 2 and 4', () => {
  expect(fizzbuzz(1)).toBe(1)
  expect(fizzbuzz(2)).toBe(2)
  expect(fizzbuzz(4)).toBe(4)
  // Agregamos más casos
  expect(fizzbuzz(7)).toBe(7)
  expect(fizzbuzz(8)).toBe(8)
  expect(fizzbuzz(11)).toBe(11)
})

test('print Fizz when number is multiple of 3 but not multiple of 5', () => {
  expect(fizzbuzz(3)).toBe('Fizz')
  expect(fizzbuzz(6)).toBe('Fizz')
  expect(fizzbuzz(9)).toBe('Fizz')
  expect(fizzbuzz(12)).toBe('Fizz')
  expect(fizzbuzz(18)).toBe('Fizz')
  expect(fizzbuzz(21)).toBe('Fizz')
  // Verificamos que múltiplos de ambos NO son solo 'Fizz'
  expect(fizzbuzz(15)).not.toBe('Fizz')
  expect(fizzbuzz(30)).not.toBe('Fizz')
})

test('print Buzz when number is multiple of 5 but not multiple of 3', () => {
  expect(fizzbuzz(5)).toBe('Buzz')
  expect(fizzbuzz(10)).toBe('Buzz')
  expect(fizzbuzz(20)).toBe('Buzz')
  expect(fizzbuzz(25)).toBe('Buzz')
  expect(fizzbuzz(35)).toBe('Buzz')
  expect(fizzbuzz(40)).toBe('Buzz')
  // Verificamos que múltiplos de ambos NO son solo 'Buzz'
  expect(fizzbuzz(15)).not.toBe('Buzz')
  expect(fizzbuzz(30)).not.toBe('Buzz')
})

test('print FizzBuzz when number is multiple of 3 and 5', () => {
  expect(fizzbuzz(15)).toBe('FizzBuzz')
  expect(fizzbuzz(30)).toBe('FizzBuzz')
  expect(fizzbuzz(45)).toBe('FizzBuzz')
  expect(fizzbuzz(60)).toBe('FizzBuzz')
  expect(fizzbuzz(75)).toBe('FizzBuzz')
  expect(fizzbuzz(90)).toBe('FizzBuzz')
})

// Tests adicionales
test('works with negative numbers', () => {
  expect(fizzbuzz(-3)).toBe('Fizz')
  expect(fizzbuzz(-5)).toBe('Buzz')
  expect(fizzbuzz(-15)).toBe('FizzBuzz')
  expect(fizzbuzz(-1)).toBe(-1)
  expect(fizzbuzz(-2)).toBe(-2)
})

test('works with large numbers', () => {
  expect(fizzbuzz(300)).toBe('FizzBuzz') // Multiple of both 3 and 5
  expect(fizzbuzz(333)).toBe('Fizz') // Multiple of 3 only
  expect(fizzbuzz(500)).toBe('Buzz') // Multiple of 5 only
  expect(fizzbuzz(997)).toBe(997) // Not multiple of 3 or 5
})
