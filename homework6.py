my_dict = {'Kirill': 2001, 'Julia': 2000, 'Alina': 1997, 'Inna': 1992}

print(my_dict)
print(my_dict['Kirill'])
my_dict.update({'Svetlana': 1995, 'Michael': 1999})
print(my_dict)

del my_dict['Alina']
print(my_dict.get('Alina'))
print(my_dict)

my_set = {200, 222, 200, 'Kirill', True, 222, 'Kirill'}
print(my_set)

my_set.update({'Vladimir', 428})
my_set.discard(222)
print(my_set)
