n = int(input("Enter the number of terms: "))
a = 0
b = 1
if n <= 0:
    print("Invalid input!")
elif n == 1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(2, n):
        c = a + b
        a = b
        b = c
        print(c)