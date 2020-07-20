# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    ls = [a, b, c]
    ls.remove(min(a,b,c))
    return sum(ls)

print(my_func(a=int(input("Введите число а")), b=int(input("Введите число b")), c=int(input('Введите число с'))))



