import sys

from List2.Polynomial import Polynomial


def main(args):
    pol = [2, 5, 1, 1, 6.24, 2, 2.3, 5.9, 1,23,2,5,8,1,789,2]
    pol2 = [2, 4, 1,7,12,546]
    p = Polynomial(pol)
    p2 = Polynomial(pol2)
    print("Pierwszy")
    p.polynomial_pretty_print()
    print("\n*")
    p2.polynomial_pretty_print()
    print("\n||")
    a = Polynomial(p.polynomial_multiply(p2))
    a.polynomial_pretty_print()
    print("\nWartość wielomianu:", p.polynomial_value(2))
    print("Stopień wielomianu:", p.polynomial_degree())


if __name__ == '__main__':
    main(sys.argv[1:])
