def rect_area(width, height):
    return width * height


def upper_first_letter(input_string):
    new_string = input_string.lower()  # make all characters lowercase
    return new_string.capitalize()


def factorial(num):
    if num > 10:
        raise ValueError("Values > 10 are not allowed!")
    if num < 0:
        raise ArithmeticError("Negative values are not allowed!")

    factorial = 1
    for x in range(1, num+1):  # num+1 here because range() STOPS when it reaches the value in the 2nd arg.
        factorial = factorial * x
    return factorial


def fibonacci(nums_to_calculate):
    nums_calculated = 0
    fibs = [1, 1]  # we already said that it starts at 1, so the second one is also one (i.e. 1 + 0 = 1)
    for index in range(2, nums_to_calculate+1):
        fib = fibs[index-1] + fibs[index-2]
        fibs.append(fib)
    return fibs


def get_list_intersection(list_a, list_b):
    intersection = []
    for item in list_a:
        if item in list_b:
            if item not in intersection:
                intersection.append(item)
    for item in list_b:
        if item in list_a:
            if item not in intersection:
                intersection.append(item)
    return intersection


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
def num_days(year1, year2):
    total = 0
    for year in range(year1, year2 + 1):
        if is_leap(year):
            total += 366
        else:
            total += 365
    return total


def double_values_in_list(list_to_double):
    new_list = []
    for item in list_to_double:
        new_list.append(item * 2)
    return new_list


def sum_lists_in_place(list_a, list_b):
    new_list = []
    if len(list_a) != len(list_b):
        raise ValueError('Lists are of different length!')
    for index , leftval in enumerate(list_a):  # NOTE we're not actually using the leftval here, we only need the index
        new_value = list_a[index] + list_b[index]
        new_list.append(new_value)
        
    return new_list


def rotate_values(x, y, z):
    return y, z, x


def split_name(fullname):
    split_string = fullname.split(' ')
    all_forenames = " ".join(split_string[:-1])  # Handle middle names e.g. Julius "Bob" Caesar
    surname = split_string[-1]
    return all_forenames, surname


def square(num):
    return num ** 2


def cube(num):
    return num ** 3


def forth_power(num):
    return num ** 4


def integer_powers(num):
    for x in range(1, num+1):
        print ("{0}: {1}, {2}, {3}".format(x, square(x), cube(x), forth_power(x)))


def tuple_from_range(lower, upper):
    my_list = []
    for x in range(lower, upper+1):
        my_list.append(x)
    return tuple(my_list)


def join_tuples(tup_a, tup_b):
    my_list = list(tup_a)
    my_list.extend(list(tup_b))
    return tuple(my_list)