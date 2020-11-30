my_list = [7, 5, 3, 3, 2]
print("Список чисел: " + str(my_list))
number = int(input("Введите новое число списка: "))
c = my_list.count(number)
for element in my_list:
    if c > 0:
        i = my_list.index(number)
        my_list.insert(i+c, number)
        break
    else:
        if number > element:
            j = my_list.index(element)
            my_list.insert(j, number)
            break
        elif number < my_list[len(my_list) - 1]:
            my_list.append(number)
print("Новый список чисел: " + str(my_list))
