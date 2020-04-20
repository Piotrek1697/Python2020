def _is_polynomial(polynomial):
    """
    Check if input variable is Polynomial type

    Parameters
    ----------
    polynomial : any type

    Returns
    -------
    bool
        Information (True or False) about input type.

    Raises:
        Exception: if input value type is not Polynomial.
    """
    if not isinstance(polynomial, Polynomial):
        raise Exception('Input must be Polynomial')


def _polynomial_degree_coeffs(coeffs):
    """
    Calculates degree of Polynomial based on coefficients list

    Parameters
    ----------
    coeffs : list[float]
        List of polynomial coefficients, where last element is free expression and first is expression next to
        the biggest degree

    Returns
    -------
    int
        Degree of polynomial
    """
    degree = len(coeffs) - 1
    for el in coeffs:
        if el == 0:
            degree = degree - 1
        else:
            break
    return degree


class Polynomial:

    def __init__(self, coeffs):
        """
        Initialize Polynomial class

        Parameters
        -----------
        coeffs : list[float]
                List of polynomial coefficients, where last element is free expression and first is expression next to
                the biggest degree
        """
        if isinstance(coeffs, list) and _polynomial_degree_coeffs(coeffs) > 0:
            self.arrayOfCoeffs = coeffs
        else:
            raise Exception('Polynomial coefficients array must have at least two elements and degree must be greater '
                            'then 0')

    def polynomial_degree(self):
        """
        Public method that returns polynomial degree

        See also:
            _polynomial_degree_coeffs(coeffs)
        """
        return _polynomial_degree_coeffs(self.arrayOfCoeffs)

    def polynomial_pretty_print(self):
        """
        Prints text version of polynomial like:
        an*xn + an-1*xn-1 + a1*x + a0
        """
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

        Returns
        -------
        Polynomial
            Multiplication result
        """
        _is_polynomial(polynomial)

        results = [0] * (len(self.arrayOfCoeffs) + len(polynomial.arrayOfCoeffs) + 1)
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

        Returns
        -------
        Polynomial
            Sum result
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

        Returns
        -------
        Polynomial
            Subtract result
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
