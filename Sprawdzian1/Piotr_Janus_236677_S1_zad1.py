import sys


def main(args):
    input_nums = args
    if len(input_nums) == 1:  # When input is like: 3,4,5
        input_nums = args[0].split(",")
    if len(input_nums) != 3:
        sys.exit("Input must have 3 elements. Input numbers must be like: a0 q n, or a0,q,n\n"
                 "First number (a0) - First number of series\n"
                 "Second number (r) - difference\n"
                 "Third number (n) - Number of displaying elements of series")

    try:
        input_nums = to_int(input_nums)
    except:
        sys.exit("Some input arguments are not integers. Please put integer numbers")

    print("Series: ", get_math_series(input_nums[0], input_nums[1], input_nums[2]))


def get_math_series(a0, r, n):
    """Getting arithmetic series

    Parameters
    ----------
    a0 : int
        First number of series
    r : int
        difference
    n : int
        Number of displaying elements of series

    Returns
    -------
    list
        List of arithmetic series with length = n
    """
    series = [a0]
    for i in range(0, n - 1):
        series.append(series[i] + r)
    return series


def to_int(list):
    return [int(number) for number in list]


if __name__ == '__main__':
    main(sys.argv[1:])
