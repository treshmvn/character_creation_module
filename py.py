from math import sqrt

message = 'Добро пожаловать в самую лучшую программу для вычисления ' \
          'квадратного корня из заданного числа'


def CalculateSquareRoot(Number):
    """Вычисляет квадратный корень."""
    return sqrt(Number)


def calc(your_number):
    """Abc."""
    if your_number <= 0:
        return
    number1 = CalculateSquareRoot(your_number)
    print('Мы вычислили квадратный корень из введённого вами числа.'
          f' Это будет: {number1}')


print(message)
calc(25.5)
