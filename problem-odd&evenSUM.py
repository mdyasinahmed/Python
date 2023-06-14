N = [int(num) for num in input("Enter numbers separated by spaces: ").split()]

oddSum = 0
evenSum = 0

for num in N:
    if num % 2 == 0:
        evenSum += num
    else:
        oddSum += num

print("Sum of Odd numbers:", oddSum)
print("Sum of Even numbers:", evenSum)
