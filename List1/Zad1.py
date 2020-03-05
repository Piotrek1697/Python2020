import sys
import math
from .tasks_utils import *

def main(args):
    input_nums = args  # Get input values

    if len(input_nums) == 1:  # When input is like: 3,4,5
        input_nums = input_nums[0].split(",")
    if len(input_nums) != 3:
        print("Input must have 3 elements")
        sys.exit(0)

    try:
        input_nums = to_float(input_nums)
    except:
        print("Some input arguments are not numbers. Please put numbers")
        sys.exit(0)

    if is_any_negative(input_nums):
        print("Input arguments must be greater then 0")
        sys.exit(0)

    s = heron_area(input_nums[0], input_nums[1], input_nums[2])
    s = round(s, 3)
    print("Traingle area:", s)


def heron_area(a, b, c):
    p = 0.5 * (a + b + c)
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return S


if __name__ == '__main__':
    main(sys.argv[1:])