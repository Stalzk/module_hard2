import random

n = random.randint(3, 20)
print("Число на камне: ", n)
print(int(input("Введите число: ")))
result = ""
for i in range(1, n):
    for j in range(i + 1, n):
        if n % (i + j) == 0:
            result += f'{i}{j}'
print("Нужный пароль: ", f'{n} - {result}')