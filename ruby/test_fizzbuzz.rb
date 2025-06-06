require_relative 'fizzbuzz'
require 'minitest/autorun'

class TestFizzBuzz < Minitest::Test

  def test_with_zero
    assert_equal fizzbuzz(0), 0
  end

  def test_same_number_with_one_two_and_four
    assert_equal fizzbuzz(1), 1
    assert_equal fizzbuzz(2), 2
    assert_equal fizzbuzz(4), 4
    # Agregamos más casos
    assert_equal fizzbuzz(7), 7
    assert_equal fizzbuzz(8), 8
    assert_equal fizzbuzz(11), 11
  end

  def test_print_fizz_when_multiple_of_three_only
    assert_equal fizzbuzz(3), 'Fizz'
    assert_equal fizzbuzz(6), 'Fizz'
    assert_equal fizzbuzz(9), 'Fizz'
    assert_equal fizzbuzz(12), 'Fizz'
    assert_equal fizzbuzz(18), 'Fizz'
    assert_equal fizzbuzz(21), 'Fizz'
    # Verificamos que múltiplos de ambos NO son solo 'Fizz'
    refute_equal fizzbuzz(15), 'Fizz'
    refute_equal fizzbuzz(30), 'Fizz'
  end

  def test_print_buzz_when_multiple_of_5_only
    assert_equal fizzbuzz(5), 'Buzz'
    assert_equal fizzbuzz(10), 'Buzz'
    assert_equal fizzbuzz(20), 'Buzz'
    assert_equal fizzbuzz(25), 'Buzz'
    assert_equal fizzbuzz(35), 'Buzz'
    assert_equal fizzbuzz(40), 'Buzz'
    # Verificamos que múltiplos de ambos NO son solo 'Buzz'
    refute_equal fizzbuzz(15), 'Buzz'
    refute_equal fizzbuzz(30), 'Buzz'
  end

  def test_print_fizzbuzz_when_multiple_of_3_and_5
    assert_equal fizzbuzz(15), 'FizzBuzz'
    assert_equal fizzbuzz(30), 'FizzBuzz'
    assert_equal fizzbuzz(45), 'FizzBuzz'
    assert_equal fizzbuzz(60), 'FizzBuzz'
    assert_equal fizzbuzz(75), 'FizzBuzz'
    assert_equal fizzbuzz(90), 'FizzBuzz'
  end

  # Tests adicionales
  def test_works_with_negative_numbers
    assert_equal fizzbuzz(-3), 'Fizz'
    assert_equal fizzbuzz(-5), 'Buzz'
    assert_equal fizzbuzz(-15), 'FizzBuzz'
    assert_equal fizzbuzz(-1), -1
    assert_equal fizzbuzz(-2), -2
  end

  def test_works_with_large_numbers
    assert_equal fizzbuzz(300), 'FizzBuzz'  # Multiple of both 3 and 5
    assert_equal fizzbuzz(333), 'Fizz'      # Multiple of 3 only
    assert_equal fizzbuzz(500), 'Buzz'      # Multiple of 5 only
    assert_equal fizzbuzz(997), 997         # Not multiple of 3 or 5
  end
end