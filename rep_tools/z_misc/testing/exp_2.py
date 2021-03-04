
def factorial(num):
    val = 1
    for i in range(num, 0, -1):
        val *= i
    return val


print("Enter a number")
num = int(input())
print(factorial(num))

