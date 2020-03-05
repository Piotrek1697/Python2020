import sys
import math


def main(args):
    input_nums = args
    if len(input_nums) < 3:
        print("Input must have 3 elements")
        sys.exit(0)
    print(toFloat(input_nums))

    input_nums = toFloat(input_nums)

    s = heronArea(input_nums[0], input_nums[1], input_nums[2])
    s = round(s,3)
    print(s)


def heronArea(a, b, c):
    p = 0.5 * (a + b + c)
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return S


def toFloat(list):
    try:
        for i in range(len(list)):
            list[i] = float(list[i])
    except:
        print(f"{i + 1}. input argument is not a float. Please put float number")
        sys.exit(0)
    return list


if __name__ == '__main__':
    main(sys.argv[1:])

# https://en.wikipedia.org/wiki/List_comprehension