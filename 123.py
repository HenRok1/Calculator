print("Данный калькулятор позволяет делать некоторые операции над множеством")
print("% это объединение\n"
      "& это пересечение\n"
      "/ это вычитание")
print("Вы можете остановить операции командой 'stop'\n")


def input_operation(mn1, mn2, mn3):
    print('Введите знак операции над множествами')

    op1 = mn1 | mn2
    op2 = mn1 & mn2
    op3 = mn1 - mn2

    while True:
        operation1 = input("Введите один из знаков(%, &, /): ")
        if operation1 == "stop":
            break
        operation2 = input("Введите один из знаков(%, &, /): ")

        if operation1 == operation2 and operation1 == "%":
            print(op1 | mn3)
            continue

        elif operation1 == operation2 and operation1 == "&":
            print(op2 & mn3)
            continue

        elif operation1 == operation2 and operation1 == "/":
            print(op3 - mn3)
            continue

        elif operation1 == "%":
            if operation2 == "&":
                print(op1 & mn3)
                continue
            elif operation2 == "/":
                print(op1 - mn3)
                continue

        elif operation1 == "&":
            if operation2 == "%":
                print(op2 | mn3)
                continue
            elif operation2 == "/":
                print(op2 - mn3)
            continue

        elif operation1 == "/":
            if operation2 == "%":
                print(op3 | mn3)
                continue
            elif operation2 == "&":
                print(op3 & mn3)
            continue


count_el1 = int(input('Введите количество элементов в первом множестве '))
count_el2 = int(input('Введите количество элементов во втором множестве '))
count_el3 = int(input('Введите количество элементов в третьем множестве '))

my_set1 = set()
my_set2 = set()
my_set3 = set()

print('Введите элементы первого множества')
for i in range(count_el1):
    my_set1.add(input())

print('Введите элементы второго множества')
for i in range(count_el2):
    my_set2.add(input())

print('Введите элементы третьего множества')
for i in range(count_el3):
    my_set3.add(input())

print('Множество:', my_set1)
print('Множество:', my_set2)
print('Множество:', my_set3, "\n")

print(input_operation(my_set1, my_set2, my_set3))
