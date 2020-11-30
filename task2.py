my_list = []
n = (int(input("Введите количество чисел в списке: ")))
print("Количество числе в списке равно " + str(n))
for i in range(n):
    my_list.append(int(input("Введите элемент списка: ")))
if len(my_list) % 2 == 0:
    i = 0
    while i < len(my_list):
        temp = my_list[i]
        my_list[i] = my_list[i+1]
        my_list[i+1] = temp
        i += 2
else:
    i = 0
    while i < len(my_list) - 1:
        temp = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = temp
        i += 2
print(my_list)