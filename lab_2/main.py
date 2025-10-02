from random import randint
chis=[25,22,43,57,86,13,72,38,54,10]
num = 13
def bin_poick(num,chis):
    for i in range(len(chis)):  # исправляем ошибки тестов 1-5, в которых ошибка возникает из-за нецелочисленных типов переменных внутри массива
        if type(chis[i]) != int:
            return 'не верный тип данных'

    if type(chis) != list:  # исправляем ошибку теста 6, в котором ошибка возникает из-за того, что переменная nums не массив
        return 'нет массива'

    if len(chis) < 2:  # исправляем ошибку теста 7, в котором ошибка возникает из-за не верного количества переменных в массиве
        return 'не верное количество элементов'

    if type(num) != int:  # исправляем ошибки тестов 8-10, в которых ошибка возникает из-за нецелочисленных значений переменной target
        return 'не верный тип данных'

    kol=0
    low = 0
    high = len(chis)
    while high > low:
        mid= (low+high)//2
        if num == chis[mid]:
            kol+=1
            return 'Num =',num, 'Time =', kol

        elif chis[mid] < num:
            kol+=1
            low = mid + 1
        else:
            kol+=1
            high=mid
    return 'None'



print(bin_poick(num,chis))

'''chis = []
for i in range(10):
    chis.append(randint(1, 50))
chis.sort()
print(chis)'''