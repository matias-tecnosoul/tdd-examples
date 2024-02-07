require_relative 'fizzbuzz'
require 'minitest/autorun'

class TestFizzBuzz < Minitest::Test

  def test_with_zero
    assert_equal fizzbuzz(0), 0
  end

  def test_same_number_with_1_2_and_4
    assert_equal fizzbuzz(1), 1
    assert_equal fizzbuzz(2), 2
    assert_equal fizzbuzz(4), 4
  end

  def test_print_Fizz_when_multiple_of_3_only
      assert_equal fizzbuzz(3), 'Fizz'
      refute_equal fizzbuzz(15), 'Fizz'
      fail 'Add more tests for Fizz'
  end

  def test_print_Fizz_when_multiple_of_5_only
      assert_equal fizzbuzz(5), 'Buzz'
      refute_equal fizzbuzz(15), 'Buzz'
      fail 'Add more tests for Buzz'
  end

  def test_print_Fizz_when_multiple_of_3_and_5
      fail 'To be done'
  end
end
