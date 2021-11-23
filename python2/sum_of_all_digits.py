num = int(input('Enter a number to sum it : '))
temp = num
res = 0

while temp:
    last_digit = temp % 10
    temp //= 10
    res = res + last_digit


print(f'sum of all digits {num} is {res}')
 
