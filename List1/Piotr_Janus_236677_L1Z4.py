"""Multiplication table

This script prints multiplication table

"""

import sys
import numpy
from List1.Piotr_Janus_236677_L1_tasks_utils import *


def main(args):
    input_nums = args  # Get input values
    if len(input_nums) != 1:
        sys.exit("There is no input or there is too many numbers")

    try:
        input_nums = to_int(input_nums)
    except:
        sys.exit("Input argument is not integer. Please put integer number")

    print(multiplication_table(input_nums[0]))


def multiplication_table(n):
    """Create multiplication table

    Parameters
    ----------
    n : int
        Number of rows and columns

    Returns
    -------
    ndarray
        n-dimensional array
    """
    vector = numpy.arange(1, n + 1)
    return numpy.outer(vector, vector)


if __name__ == '__main__':
    main(sys.argv[1:])
