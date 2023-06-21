n = int(input("Enter Number: "))

if n > 1:
    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

    if prime:
        print("Prime.")
    else:
        print("Not Prime.")
else:
    print("Not Prime.")

