def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num


#  Tests
assert fizz_buzz(27) is "Fizz"
assert fizz_buzz(9) is "Fizz"
assert fizz_buzz(30) is "FizzBuzz"
assert fizz_buzz(32) is 32
assert fizz_buzz(50) is "Buzz"
assert fizz_buzz(15) is "FizzBuzz"
