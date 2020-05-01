num1 = int(input()); num2 = int(input()); num3 = int(input())
result = num1 * num2 * num3

result = list(str(result))
for i in range(10):
    print(result.count(str(i)))