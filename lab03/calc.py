first = float(input('Введите первое число: '))
second = float(input('Введите второе число: '))
op = input('Введите знак операции (+,-,*,/): ')
if op == '/' and second == 0:
    print('Делить на 0 нельзя')
elif op == '+':
    print(first + second)
elif op == '-':
    print(first - second)
elif op == '*':
    print(first * second)
elif op == '/':
    print(first / second)
else:
    print('Неизвестная команда')