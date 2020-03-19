# Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.


def fibo_sequence(n):
    """
    Generates a fibonacci sequence with the size of n
    """
    assert n > 0

    series = [1]

    while len(series) < n:
        if len(series) == 1:
            series.append(1)
        else:
            series.append(series[-1] + series[-2])

    for i in range(len(series)):  # Convert the numbers to strings
        series[i] = str(series[i])

    return (', '.join(series))  # Return the sequence seperated by commas


def main():  # Wrapper function

    print(fibo_sequence(int(input('How many numbers of iterations you need? '))))


if __name__ == '__main__':
    main()
