import sys
import numpy
from List1.tasks_utils import *


def main(args):
    input_nums = args  # Get input values
    if len(input_nums) != 1:
        print("There is no input or there is too many numbers")
        sys.exit(0)

    try:
        input_nums = to_int(input_nums)
    except:
        print("Input argument is not integer. Please put integer number")
        sys.exit(0)

    vector = numpy.arange(1, input_nums[0] + 1)
    matrix = numpy.outer(vector, vector)

    print(matrix)



if __name__ == '__main__':
    main(sys.argv[1:])
