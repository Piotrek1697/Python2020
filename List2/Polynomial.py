def _is_polynomial(polynomial):
    """
    Check if input variable is Polynomial type
    """
    if ~ isinstance(polynomial, Polynomial):
        raise Exception('Input must be Polynomial')


class Polynomial:

    def __init__(self, coeffs):
        """
        Initialize Polynomial class

        Parameters
        -----------
        coeffs : list
                List of polynomial coefficients, where last element is free expression and first is expression next to
                the biggest degree
        """
        if len(coeffs) >= 2 and isinstance(coeffs, list) and (len(coeffs) - coeffs.count(0)) > 1:
            self.arrayOfCoeffs = coeffs
        else:
            raise Exception('Polynomial coefficients array must have at least two elements and degree must be greater '
                            'then 0')

    def polynomial_degree(self):
        if self.arrayOfCoeffs[0] == 0:
            return len(self.arrayOfCoeffs) - 2
        else:
            return len(self.arrayOfCoeffs) - 1

    def polynomial_pretty_print(self):
        l = len(self.arrayOfCoeffs)
        for i in range(1, l + 1):
            num = self.arrayOfCoeffs[i - 1]
            sign = ''
            if num < 0:
                sign = '-'
            elif num > 0 and i > 1:
                sign = '+'

            if (num == 1 or num == -1) and i != l:
                print(" %s x%d" % (sign, l - i), end='')
            elif num == 0:
                print(end="")
            elif i == l:
                print(" %s %.2f" % (sign, abs(num)), end='')
            else:
                print(" %s %.2f" % (sign, abs(num)), end='')
                print("*x%d" % (l - i), end='')

    def polynomial_value(self, x):
        """
        Calculates value polynomial value for specific x value.

        Parameters
        -----------
        x : float
            Value of variable in equation
        """
        l = len(self.arrayOfCoeffs)
        return sum([self.arrayOfCoeffs[i - 1] * pow(x, l - i) for i in range(1, l + 1)])

    def polynomial_multiply(self, polynomial):
        """
        Multiplies two polynomials

        Parameters
        ----------
        polynomial: Polynomial
                    Polynomial type variable
        """
        _is_polynomial(polynomial)

        results = [0] * (self.polynomial_degree() + polynomial.polynomial_degree() + 1)
        l = len(self.arrayOfCoeffs)
        l2 = len(polynomial.arrayOfCoeffs)
        for i in range(1, l + 1):
            for j in range(1, l2 + 1):
                num = self.arrayOfCoeffs[i - 1]
                num2 = polynomial.arrayOfCoeffs[j - 1]

                results[(l - i) + (l2 - j)] += num * num2

        results.reverse()
        return Polynomial(results)

    def polynomial_add(self, polynomial):
        """
        Adds two polynomials

        Parameters
        ----------
        polynomial: Polynomial
                    Polynomial type variable
        """
        _is_polynomial(polynomial)

        results = [0] * (max(len(self.arrayOfCoeffs), len(polynomial.arrayOfCoeffs)))
        temp1 = list(reversed(self.arrayOfCoeffs))
        temp2 = list(reversed(polynomial.arrayOfCoeffs))
        for i in range(0, len(results)):
            el1 = el2 = 0
            try:
                el1 = temp1[i]
            except IndexError:
                pass
            try:
                el2 = temp2[i]
            except IndexError:
                pass
            results[i] = el1 + el2
        results.reverse()
        return Polynomial(results)

    def polynomial_subtract(self, polynomial):
        """
        Subtracts two polynomials

        Parameters
        ----------
        polynomial: Polynomial
                    Polynomial type variable
        """
        _is_polynomial(polynomial)
        results = [0] * (max(len(self.arrayOfCoeffs), len(polynomial.arrayOfCoeffs)))
        temp1 = list(reversed(self.arrayOfCoeffs))
        temp2 = list(reversed(polynomial.arrayOfCoeffs))
        for i in range(0, len(results)):
            el1 = el2 = 0
            try:
                el1 = temp1[i]
            except IndexError:
                pass
            try:
                el2 = temp2[i]
            except IndexError:
                pass
            results[i] = el1 - el2
        results.reverse()
        return Polynomial(results)
