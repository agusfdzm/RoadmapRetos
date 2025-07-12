numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for n in range(len(numeros) + 1):
    if n % 2 == 0:
        print(n)
    else:
        print("impar")

print("separador")

for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)