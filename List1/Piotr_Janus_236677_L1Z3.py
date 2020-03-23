def main():
    print("Your series: ", get_math_series(1, 2, 12))


def get_math_series(a0, q, n):
    series = [a0]
    for i in range(0, n - 1):
        series.append(series[i] * q)
    return series


if __name__ == '__main__':
    main()
