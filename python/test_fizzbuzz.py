from fizzbuzz import fizzbuzz


def test_with_zero():
    """Test that zero returns zero (edge case)"""
    assert fizzbuzz(0) == 0


def test_same_number_with_1_2_and_4():
    """Test that numbers not multiples of 3 or 5 return themselves"""
    assert fizzbuzz(1) == 1
    assert fizzbuzz(2) == 2
    assert fizzbuzz(4) == 4
    assert fizzbuzz(7) == 7
    assert fizzbuzz(8) == 8
    assert fizzbuzz(11) == 11
    assert fizzbuzz(13) == 13
    assert fizzbuzz(14) == 14


def test_print_Fizz_when_multiple_of_3_only():
    """Test that multiples of 3 (but not 5) return 'Fizz'"""
    assert fizzbuzz(3) == 'Fizz'
    assert fizzbuzz(6) == 'Fizz'
    assert fizzbuzz(9) == 'Fizz'
    assert fizzbuzz(12) == 'Fizz'
    assert fizzbuzz(18) == 'Fizz'
    assert fizzbuzz(21) == 'Fizz'
    assert fizzbuzz(24) == 'Fizz'
    assert fizzbuzz(27) == 'Fizz'
    # Verify that multiples of both 3 and 5 don't return just 'Fizz'
    assert fizzbuzz(15) != 'Fizz'
    assert fizzbuzz(30) != 'Fizz'


def test_print_Buzz_when_multiple_of_5_only():
    """Test that multiples of 5 (but not 3) return 'Buzz'"""
    assert fizzbuzz(5) == 'Buzz'
    assert fizzbuzz(10) == 'Buzz'
    assert fizzbuzz(20) == 'Buzz'
    assert fizzbuzz(25) == 'Buzz'
    assert fizzbuzz(35) == 'Buzz'
    assert fizzbuzz(40) == 'Buzz'
    assert fizzbuzz(50) == 'Buzz'
    assert fizzbuzz(55) == 'Buzz'
    # Verify that multiples of both 3 and 5 don't return just 'Buzz'
    assert fizzbuzz(15) != 'Buzz'
    assert fizzbuzz(30) != 'Buzz'


def test_print_FizzBuzz_when_multiple_of_3_and_5():
    """Test that multiples of both 3 and 5 return 'FizzBuzz'"""
    assert fizzbuzz(15) == 'FizzBuzz'
    assert fizzbuzz(30) == 'FizzBuzz'
    assert fizzbuzz(45) == 'FizzBuzz'
    assert fizzbuzz(60) == 'FizzBuzz'
    assert fizzbuzz(75) == 'FizzBuzz'
    assert fizzbuzz(90) == 'FizzBuzz'
    assert fizzbuzz(105) == 'FizzBuzz'


def test_negative_numbers():
    """Test that the function works correctly with negative numbers"""
    assert fizzbuzz(-3) == 'Fizz'
    assert fizzbuzz(-5) == 'Buzz'
    assert fizzbuzz(-15) == 'FizzBuzz'
    assert fizzbuzz(-1) == -1
    assert fizzbuzz(-2) == -2
    assert fizzbuzz(-4) == -4


def test_large_numbers():
    """Test that the function works with larger numbers"""
    assert fizzbuzz(300) == 'FizzBuzz'  # Multiple of both 3 and 5
    assert fizzbuzz(333) == 'Fizz'      # Multiple of 3 only
    assert fizzbuzz(500) == 'Buzz'      # Multiple of 5 only
    assert fizzbuzz(997) == 997         # Prime number
