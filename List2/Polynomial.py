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
            self._arrayOfCoeffs = coeffs
        else:
            raise Exception('Polynomial coefficients array must have at least two elements')

    def polynomial_degree(self):
        if self._arrayOfCoeffs[0] == 0:
            return len(self._arrayOfCoeffs) - 2
        else:
            return len(self._arrayOfCoeffs) - 1

    def polynomial_pretty_print(self):
        l = len(self._arrayOfCoeffs)
        for i in range(1, l + 1):
            num = self._arrayOfCoeffs[i - 1]
            sign = ''
            if num < 0:
                sign = '-'
            elif num > 0 and i > 1:
                sign = '+'

            if num == 1 or num == -1:
                print(" %s x%d" % (sign, l - i), end='')
            elif num == 0:
                print(end="")
            elif i == l:
                print(" %s %.2f" % (sign, abs(num)), end='')
            else:
                print(" %s %.2f" % (sign, abs(num)), end='')
                print("*x%d" % (l - i), end='')

    def polynomial_value(self, x):
        l = len(self._arrayOfCoeffs)
        return sum([self._arrayOfCoeffs[i - 1] * pow(x, l - i) for i in range(1, l + 1)])
