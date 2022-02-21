from random import  random, randint, randrange

# GENERATORS

n = 10

#List generators

#n = int(input('Enter list size: '))

# my_list = []
# for el in range(1, n+1):
#     if el % 7 == 0:
#         continue
#     my_list.append(el)
#
# my_list1 = [el for el in range(1, n+1) if el % 7 != 0]
# print(my_list)
# print(my_list1)

#set generators

# my_set = {el * 2 for el in range(0, n+1) if el % 7 != 0}
# print(my_set)

#dict generators

# my_dict = {el: str(el) for el in range(0, n+1)}
# print(my_dict)

# RANDOM

# result = random()
#
# print(result * 10 + 10)


# YIELD

# def my_range(end):
#     current = 0
#     while current < end:
#         yield current           # Instead of return to continue iteration process in function
#         current += 1
#
# my_gen = my_range(10)
#
# for el in my_range(10):
#     print(el)

# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))

# from functools import reduce
#
# my_list = [1, 2, 3, 4, 5, 6]
#
# result = 1
# for i in my_list:
#     result *= i
#
# result_1 = reduce(lambda a, b: a * b, my_list)
#
# print(result)
# print(result_1)

# from itertools import count, cycle
#
# # my_object = count(1, 2)
# # for el in my_object:
# #     print(el)
#
# my_list = ['    1','   111' , '  11111', ' 1111111', '111111111']
# my_cycle = cycle(my_list)
# for el in my_cycle:
#     print(el, sep = ' ')


