const {test, expect } = require('@jest/globals')
const fizzbuzz = require('./fizzbuzz')

test('print zero whith zero', () => {
  expect(fizzbuzz(0)).toBe(0)
});

test('print same number on 1, 2 and 4', () => {
  expect(fizzbuzz(1)).toBe(1);
  expect(fizzbuzz(2)).toBe(2);
  expect(fizzbuzz(4)).toBe(4);
});

test('print Fizz when number is multiple of 3 but not multiple of 5', () => {
  expect(fizzbuzz(3)).toBe('Fizz');
  expect('Add more expects for Fizz').toBe(false)
});

test('print Buzz when number is multiple of 5 but not multiple of 3', () => {
  expect(fizzbuzz(5)).toBe('Buzz');
  expect('Add more expects for Buzz').toBe(false);
});

test('print FizBuzz when number is multiple of 3 and 5', () => {
  expect('To be done').toBe(false);
});


