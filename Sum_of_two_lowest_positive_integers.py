"""

Create a function that returns the sum of the two lowest positive numbers
given an array of minimum 4 integers. No floats or empty arrays will be passed.

For example, when an array is passed like [19, 5, 42, 2, 77],
the output should be 7.

[10, 343445353, 3453445, 3453545353453] should return 3453455.

"""

num_list = [19, 5, 42, 2, 77]

def sum_two_smallest_numbers(numbers):
    sorted_numbers = sorted(numbers)
    get_two_lowest = (sorted_numbers)[:2]
    sum_two_lowest = sum(get_two_lowest)
    return sum_two_lowest


print(sum_two_smallest_numbers(num_list))