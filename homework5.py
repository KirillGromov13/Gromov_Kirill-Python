immutable_var = 1, 2, 'Kirill', True
# immutable_var.remove('Kirill')
print(immutable_var)

# Кортеж - это не изменяемый вид списка, в котором нельзя удалять и изменять существующие/добавлять новые элементы

mutable_list = [12, 15, True, False, 'Abrakadabra']
mutable_list.append('Volandemort')
mutable_list[0] = 194
mutable_list.extend(['Tvorog', 18.5])
print(mutable_list)