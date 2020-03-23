"""Fibonacci series

This script print n of the fibonacci series numbers that begins with x and y.

Input must have 3 elements. Input numbers must be like: x y n, or x,y,n
where:
First number (x) - First number of fibonacci sequence
Second number (y) - Second number of fibonacci sequence
Third number (n) - Number of displaying elements of fibonacci sequence
"""

import math
import sys
from List1.Piotr_Janus_236677_L1_tasks_utils import *


def main(args):
    input_nums = args
    if len(input_nums) == 1:  # When input is like: 3,4,5
        input_nums = input_nums[0].split(",")
    if len(input_nums) != 3:
        print(
            "Input must have 3 elements. Input numbers must be like: x y n, or x,y,n\n"
            "First number (x) - First number of fibonacci sequence\n"
            "Second number (y) - Second number of fibonacci sequence\n"
            "Third number (n) - Number of displaying elements of fibonacci sequence")
        sys.exit(0)

    try:
        input_nums = to_int(input_nums)
    except:
        sys.exit("Some input arguments are not integers. Please put integer numbers")

    if is_any_negative(input_nums):
        sys.exit("Input arguments must be greater then 0")
    temp_inputs = input_nums.copy()
    temp_inputs.pop()  # Delete last element from list
    if not all(is_fibonacci_number(num) for num in temp_inputs):
        sys.exit("There is no proper fibonacci number in input")

    if input_nums[0] > input_nums[1]:
        sys.exit("y must be greater then x")

    sub = input_nums[1] - input_nums[0]

    if not (is_fibonacci_number(sub) and sub < input_nums[0]) and (sub != 1 and sub != 0):
        sys.exit("y must be next fibonacci number after x")

    fib = fibonacci(input_nums[0], input_nums[1], input_nums[2])
    print(fib)


def fibonacci(x, y, n):
    """Calculating fibonacci series

    This function calculates fibonacci series with length n and first numbers x and y

    Parameters
    ----------
    x : int
        Fibonacci number that begins returned series
    y : int
        Fibonacci number that is second in series
    n : int
        Length of returned series

    Returns
    -------
    list
        Part of fibonacci series that begins with x and y, it's length is n
    """
    out_list = [x, y]
    for i in range(2, n):
        out_list.append(x + y)
        x = y
        y = out_list[i]
    return out_list


def is_fibonacci_number(num):
    """Check if input number belongs to fibonacci series

    Check if 5*x^2 + 4 or 5*x^2 - 4 is square number.
    If is, this number is fibonacci number

    Parameters
    ----------
    num : int
        Number that can be fibonacci number

    Returns
    -------
    bool
        Info if input number is fibonacci number (True or False)
    """
    first = 5 * math.pow(num, 2) + 4
    second = 5 * math.pow(num, 2) - 4
    return is_square_number(first) or is_square_number(second)


def is_square_number(squared_num):
    """Check if input number is square number (perfect square)

    Get integer part of square root of input num and then compare if power of this number is equal to input.
    Square number is an integer that is the square of an integer ~https://en.wikipedia.org/wiki/Square_number

    Parameters
    ----------
    squared_num : float

    Returns
    -------
    bool
        Info if input number is perfect square
    """
    num = int(math.sqrt(squared_num))
    return math.pow(num, 2) == squared_num


if __name__ == '__main__':
    main(sys.argv[1:])
