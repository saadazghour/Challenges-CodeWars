"""

There is an array with some numbers. All numbers are equal except for one.
Try to find it!

findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
findUniq([ 0, 0, 0.55, 0, 0 ]) === 0.55
It’s guaranteed that array contains more than 3 numbers.

The tests contain some very huge arrays, so think about performance.

This is the first kata in series:

Find the unique number (this kata)
Find the unique string
Find The Unique

"""


arr_uniq = [ 1, 1, 1, 2, 1, 1 ]
# arr_uniq = [ 0, 0, 0.55, 0, 0 ]
# arr_uniq = [ 3, 10, 3, 3, 3 ]

def find_uniq(arr):

    number1, number2 = set(arr)
    # print(arr.count(number1))

    if arr.count(number1) == 1 or arr.count(number1) == 0  or arr.count(number1) == 3:
        return number1
    return number2


print(find_uniq(arr_uniq))