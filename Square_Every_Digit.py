"""
For example, if we run 9119 through the function,
811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer

"""


def square_digits(num):
    square = ''
    for num in str(num):
        square += str(int(num)** 2)
        # print(square)
    return int(square)


print(square_digits(9119))