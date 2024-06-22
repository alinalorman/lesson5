immutable_var = 1, "Лосось", 2, "Зеленый"
print(immutable_var)

# immutable_var[0] = 2
# print(immutable_var) - выдаст ошибку, так как кортеж - это неизменяемый объект и мы не можем менять элементы

mutable_list = [1, 'Лосось', 2, 'Зеленый']
print(mutable_list)

mutable_list[0] = 3
mutable_list[1] = 'Карась'
mutable_list[2] = 4
mutable_list[3] = 'Оранжевый'
print(mutable_list)