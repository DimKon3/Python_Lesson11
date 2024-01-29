res = []

def factorial_recursive(n, accumulator=1):
    if n == 1:
        return accumulator
    else:
        return factorial_recursive(n - 1, n * accumulator)

a = int(input("Введите целое не отрицательное число: "))
sum1 = factorial_recursive(a)
print(f"Факториал {a} равен {sum1}")
for i in range(sum1, 0, -1):
    res.append(factorial_recursive(i))
print(res)