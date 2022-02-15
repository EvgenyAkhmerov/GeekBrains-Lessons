my_str = 'Hello world!'
#print(my_str.replace())

my_list = []
numbers_list = []

for i in range(1, 11):
    numbers_list.append(i)

my_list.append(numbers_list)
my_list.append(True)
my_list.append('Hello world!')
my_list.insert(0, 0.5)
my_list.remove(0.5)


print(my_list)
print(my_list.count(0))

my_tuple = (1, 2, False)

my_set = {False, True, 1, 2, 3}

print(my_set)
#print(id(False), id(0))

my_dict = {
    'one': 1,
    'two': 2,
    'three': 3
}

print(my_dict['one'])
my_dict['four'] = 4
print(my_dict)
print(my_dict.get('four'))
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

for key, value in my_dict.items():
    print(f'key = {key},    value = {value}')

number = int(input('write a number: '))
result = 'even' if number % 2 == 0 else 'odd'
print(result)
