numbers = []

for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

search = int(input("Enter number to count: "))

count = 0

for num in numbers:
    if num == search:
        count = count + 1

print("Number occurs", count, "times")