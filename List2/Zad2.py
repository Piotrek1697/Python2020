import sys

from List2.Polynomial import Polynomial


def main(args):
    pol = [0,1,2]
    p = Polynomial(pol)
    p.polynomial_pretty_print()
    print()
    print(p.polynomial_value(2))
    print("Stopień wielomianu:", p.polynomial_degree())

if __name__ == '__main__':
    main(sys.argv[1:])
