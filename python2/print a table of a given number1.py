num =  int(input('Enter a number to print its table -> '))
lower_limit = int(input('Enter from where you want the table to be printed -> '))
upper_limit = int(input('Enter till where you want the table to be printed -> '))

for n in range(lower_limit, upper_limit + 1):
    print('{} * {} = {}' .format(num, n, (num * n)))