numbers = []

for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number is:", largest)