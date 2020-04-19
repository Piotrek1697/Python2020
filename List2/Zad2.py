import sys

from List2.Polynomial import Polynomial


def main(args):
    pol = [0, 0, 0, 0, 0]
    pol2 = [2, 4, 1, 7, 12, 546]
    p = Polynomial(pol)
    p2 = Polynomial(pol2)

    print("Wartość wielomianu 1 (x=2):", p.polynomial_value(2))
    print("Stopień wielomianu 1:", p.polynomial_degree())

    print("\nMNOŻENIE")

    p.polynomial_pretty_print()
    print("\n*")
    p2.polynomial_pretty_print()
    print("\n||")
    p.polynomial_multiply(p2).polynomial_pretty_print()

    print("\nDODAWANIE")

    p.polynomial_pretty_print()
    print("\n+")
    p2.polynomial_pretty_print()
    print("\n||")
    p.polynomial_add(p2).polynomial_pretty_print()

    print("\n\nODEJMOWANIE")

    p.polynomial_pretty_print()
    print("\n-")
    p2.polynomial_pretty_print()
    print("\n||")
    p.polynomial_subtract(p2).polynomial_pretty_print()

    # W tych przypadkach wyrzuci błąd
    # p_error = Polynomial([0, 0, 0, 2])
    # p_error2 = Polynomial([0, 2])
    # p_error4 = p.polynomial_multiply([1, 2, 3])
    # p_error5 = p.polynomial_multiply(0)


if __name__ == '__main__':
    main(sys.argv[1:])
