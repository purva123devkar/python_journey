numbers = [11, 20, 15, 8, 7, 30, 9]

sum = 0

for number in numbers:
    if number % 2 != 0:
        sum = sum + number

print(sum)
