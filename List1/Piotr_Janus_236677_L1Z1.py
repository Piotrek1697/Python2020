"""Heron triangle area

This script allows user to calculate triangle area with the Heron equation.

For input user must pass 3 numbers that are separated with comma (,) or space
"""
import sys
import math
from List1.Piotr_Janus_236677_L1_tasks_utils import *


def main(args):
    input_nums = args  # Get input values

    if len(input_nums) == 1:  # When input is like: 3,4,5
        input_nums = input_nums[0].split(",")
    if len(input_nums) != 3:
        sys.exit("Input must have 3 elements")

    try:
        input_nums = to_float(input_nums)
    except:
        sys.exit("Some input arguments are not numbers. Please put numbers")

    if is_any_negative(input_nums):
        sys.exit("Input arguments must be greater then 0")

    s = heron_area(input_nums[0], input_nums[1], input_nums[2])
    s = round(s, 3)
    print("Triangle area:", s)


def heron_area(a, b, c):
    """Calculates triangle are with heron equation

    Parameters
    ----------
    a : float
        One of the triangle edge length
    b : float
        Second of the triangle edge length
    c : float
        Third of the triangle edge length

    Returns
    -------
    float
        Area of triangle
    """
    p = 0.5 * (a + b + c)
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


if __name__ == '__main__':
    main(sys.argv[1:])
