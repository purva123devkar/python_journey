numbers = []

for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

minimum = numbers[0]

for num in numbers:
    if num < minimum:
        minimum = num

print("Minimum number is:", minimum)