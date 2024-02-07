import pytest
from fizzbuzz import fizzbuzz

def test_with_zero():
    assert fizzbuzz(0) == 0

def test_same_number_with_1_2_and_4():
    assert fizzbuzz(1) == 1
    assert fizzbuzz(2) == 2
    assert fizzbuzz(4) == 4

def test_print_Fizz_when_multiple_of_3_only():
    assert fizzbuzz(3) == 'Fizz'
    assert fizzbuzz(15) != 'Fizz'
    pytest.fail('Add more tests for Fizz')

def test_print_Fizz_when_multiple_of_5_only():
    assert fizzbuzz(5) == 'Buzz'
    assert fizzbuzz(15) != 'Buzz'
    pytest.fail('Add more tests for Buzz')

def test_print_Fizz_when_multiple_of_3_and_5():
    pytest.fail('To be done')
