def Combination(listNumbers):
    for i in range(len(listNumbers)-2):
        list123 = listNumbers[i:i + 3]
        if sorted(list123) == [1,2,3]:
            print("True")
        else:
            print("False")


n = int(input("Введите длину списка n: "))
listNumbers = list(map(int, input("Введите элементы списка: ").split()))

if len(listNumbers) != n:
    print("Ошибка: количество введенных элементов не соответствует заданной длине списка.")
else:
    print("Результат:", Combination(listNumbers))

