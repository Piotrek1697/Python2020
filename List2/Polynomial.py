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
        l = len(self.arrayOfCoeffs)
        return sum([self.arrayOfCoeffs[i - 1] * pow(x, l - i) for i in range(1, l + 1)])

    def polynomial_multiply(self, polynomial):
        # Create list that length equals to greater degree in output polynomial
        results = [0] * (self.polynomial_degree() + polynomial.polynomial_degree() + 1)
        l = len(self.arrayOfCoeffs)
        l2 = len(polynomial.arrayOfCoeffs)
        for i in range(1, l + 1):
            for j in range(1, l2 + 1):
                num = self.arrayOfCoeffs[i - 1]
                num2 = polynomial.arrayOfCoeffs[j - 1]

                results[(l - i) + (l2 - j)] += num * num2

        results.reverse()
        return results
