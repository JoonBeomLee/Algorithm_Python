num1 = int(input())
num2 = int(input())

if num1 >= 0 and num2 >= 0:
    print(1)
if num1 < 0 and num2 >= 0:
    print(2)
if num1 < 0 and num2 < 0:
    print(3)
if num1 >= 0 and num2 < 0:
    print(4)