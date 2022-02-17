# def mul_nums1(num_1, num_2, num_3):
#     result = num_1 * num_2 * num_3
#    # return result
#
# print(mul_nums1(2, 2, 2))

# def mul_nums2(num_1, num_2, num_3=3, results=None):
#     if not results:
#         results = []
#     print(f'num_1={num_1}')
#     print(f'num_2={num_2}')
#     print(f'num_3={num_3}')
#     result = num_1 * num_2 * num_3
#     results.append(result)
#     return results
#
# results = [0, 0, 0, 0]
# print(mul_nums2(1, 2, results=results))

# my_lambda = lambda num_1, num_2, num_3: num_1 * num_2 * num_3
# print(my_lambda(1, 2, 3))

# for el in range(0, 100000):
#     print(el)

def mul_nums(num_1, num_2, num_3):
    """ Multiply 3 numbers

    :param num_1: int, float
    :param num_2: int, float
    :param num_3: int, float
    :return:
    """

    result = num_1 * num_2 * num_3
    return result

mul_nums(1, 2, 3)
print(mul_nums.__doc__)
