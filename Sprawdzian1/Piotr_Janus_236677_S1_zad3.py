from Sprawdzian1.Piotr_Janus_236677_S1_zad3_StraightLine import StraightLine
import sys


def main():
    print()
    line1 = StraightLine(1, 2)
    line2 = StraightLine(-2, 5)
    print(line_cross(line1, line2))


def line_cross(line1, line2):
    out = []
    if isinstance(line1, StraightLine) and isinstance(line2, StraightLine):
        if line1.a == line2.a:
            sys.exit("Lines will never cross")

        a2 = line1.a - line2.a
        b2 = line2.b - line1.b
        x = b2 / a2
        y = line1.a * x + line1.b
        out.append(x)
        out.append(y)
    else:
        sys.exit("Input must be StraightLine type")
    return out


if __name__ == '__main__':
    main()
