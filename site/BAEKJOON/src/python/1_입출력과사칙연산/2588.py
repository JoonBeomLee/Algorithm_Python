a = input(); b = input()
a = int(a); b = int(b)

num1 = a * (b % 10)
num2 = a * ((b % 100) - (b % 10)) / 10
num3 = a * ((b % 1000) - (b % 100)) / 100

print(num1)
print(int(num2))
print(int(num3))
print(int(num1 + num2*10 + num3*100))