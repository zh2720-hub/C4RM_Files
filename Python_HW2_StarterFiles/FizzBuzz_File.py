import numpy as np

def FizzBuzz(start, finish):
    nums = np.arange(start, finish + 1)
    result = nums.astype(object)

    mask_fizzbuzz = (nums % 15 == 0)
    mask_fizz = (nums % 3 == 0) & ~mask_fizzbuzz
    mask_buzz = (nums % 5 == 0) & ~mask_fizzbuzz

    result[mask_fizzbuzz] = "FizzBuzz"
    result[mask_fizz] = "Fizz"
    result[mask_buzz] = "Buzz"

    return result
