a = int(input("Введите первое число: " ))
b = int(input("Введите второе число: "))
print("Сумма равна ", a+b)
print("Разность равна", a-b)
print("Произведение равно", a*b)
if b == 0:
    print("Делить на ноль? Мы это ещё не проходили")
if b != 0:
    print("Частное равно ", a/b)
    print("Остаток от деления: ", a%b)
