"""Print geometric series

This script n numbers of geometric series with eq. a[n+1] = a[n] * q
Input must have 3 elements. Input numbers must be like: a0 q n, or a0,q,n
where:
First number (a0) - First number of series
Second number (q) - quotient
Third number (n) - Number of displaying elements of series
"""
import sys
from List1.Piotr_Janus_236677_L1_tasks_utils import *


def main(args):
    input_nums = args
    if len(input_nums) == 1:  # When input is like: 3,4,5
        input_nums = input_nums[0].split(",")
    if len(input_nums) != 3:
        print(
            "Input must have 3 elements. Input numbers must be like: a0 q n, or a0,q,n\n"
            "First number (a0) - First number of series\n"
            "Second number (q) - quotient\n"
            "Third number (n) - Number of displaying elements of series")
        sys.exit(0)

    try:
        input_nums = to_int(input_nums)
    except:
        sys.exit("Some input arguments are not integers. Please put integer numbers")

    print("Your series: ", get_math_series(input_nums[0], input_nums[1], input_nums[2]))


def get_math_series(a0, q, n):
    """Getting geometric series

    Parameters
    ----------
    a0 : int
        First number of series
    q : int
        quotient
    n : int
        Number of displaying elements of series

    Returns
    -------
    list
        List of geometric series with length = n
    """
    series = [a0]
    for i in range(0, n - 1):
        series.append(series[i] * q)
    return series


if __name__ == '__main__':
    main(sys.argv[1:])
