word = input("Введите слова через пробел: ")
a = word.split(' ')
for i, element in enumerate(a, 1):
    if len(element) > 10:
        el = element[0:10]
    print(f"{i}. {element}")
