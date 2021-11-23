# logic to read number from user
num = int(input('Enter a number to reverse it : '))
# creating a copy to work with
temp = num

# logic to reverse a number
res = 0

while temp:
    # logic to get last digit
    last_digit = temp % 10
    # logic to remove last digit
    temp //= 10
    # store reversed number
    res = res * 10 + last_digit # multiplying by 10 to add tenses


print(f'reverse of {num} is {res}')    
