"""
------------------------------------------------------------------------
Lab 8
------------------------------------------------------------------------
Author: Laith Adi 
ID:     170265190
Email:  Adix5190@mylaurier.ca
__updated__ = "2018-11-15"
------------------------------------------------------------------------
"""
import random

DAYS_OF_WEEK = ['Sunday', 'Monday', 'Tuesday',
                'Wednesday', 'Thursday', 'Friday', 'Saturday']
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
          'October', 'November', 'December']
DIGITS = ['one', 'two', 'three', 'four',
          'five', 'six', 'seven', 'eight', 'nine']


def get_weekday_name(d):
    """
    -------------------------------------------------------
    Returns the name of a day of the week given its number.
    Use: name = get_weekday_name(d)
    -------------------------------------------------------
    Parameters:
        d - day of week number (1 <= int <= 7)
    Returns:
        name - matching day of the week, 1 = "Sunday", 7 = "Saturday" (str)
    -------------------------------------------------------
    """
    return DAYS_OF_WEEK[d - 1]


def get_month_name(m):
    """
    -------------------------------------------------------
    Returns the name of a month given its number.
    Use: name = get_month_name(m)
    -------------------------------------------------------
    Parameters:
        m - month number (int 1 <= m <= 12)
    Returns:
        name - matching month, 1 = "January", 12 = "December" (str)
    -------------------------------------------------------
    """
    return MONTHS[m - 1]


def get_digit_name(n):
    """
    -------------------------------------------------------
    Returns the name of a digit given its number.
    Use: name = get_digit_name(n)
    -------------------------------------------------------
    Parameters:
        n - digit number (int 0 <= n <= 9)
    Returns:
        name - matching digit, 0 = "zero", 9 = "nine" (str)
    -------------------------------------------------------
    """
    return DIGITS[n - 1]


def generate_integer_list(n, low, high):
    """
    -------------------------------------------------------
    Generates a list of random integers.
    Requires import: from random import randint
    Use: values = generate_integer_list(n, low, high)
    -------------------------------------------------------
    Preconditions:
        n - number of values to generate (int, > 0)
        low - low value range (int)
        high - high value range (int, > low)
    Postconditions:
        values - a list of random integers (list of int)
    -------------------------------------------------------
    """
    values = []
    for i in range(n):
        num = random.randint(low, high)
        values.append(num)
        i *= 1

    return values


def get_lotto_numbers(n, low, high):
    """
    -------------------------------------------------------
    Generates a sorted list of unique lottery numbers.
    Requires import: from random import randint
    Use: numbers = get_lotto_numbers(n, low, high)
    -------------------------------------------------------
    Parameters:
        n - number of lottery numbers to generate (int > 0)
        low - low value of the lottery number range (int >= 0)
        high - high value of the lottery number range (int > low)
    Returns:
        numbers - a list of unique random lottery numbers (list of int)
    -------------------------------------------------------
    """
    numbers = []
    count = 0
    while (count < n):
        num = random.randint(low, high)
        if num not in numbers:
            numbers.append(num)
            count += 1
    numbers.sort()
    return numbers


def list_stats(values):
    """
    -------------------------------------------------------
    Returns statistics about values in a list.
    values has at least one element.
    Use: smallest, largest, total, average = list_stats(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of float)
    Returns:
        smallest - the smallest number in values (float)
        largest - the largest number in values (float)
        total - total of numbers in list (float)
        average - the average numbers in values (float)
    -------------------------------------------------------
    """
    smallest = values[0]
    largest = values[0]
    total = 0
    for i in values:
        if i > largest:
            largest = i
        elif i < smallest:
            smallest = i
        total += i
    average = total / len(values)
    return smallest, largest, total, average


def list_categorize(values):
    """
    -------------------------------------------------------
    Returns data about the categories of values in a list.
    Use: negatives, positives, zeroes, evens, odds = list_categorize(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of int)
    Returns:
        negatives - the number of negative values (int)
        positives - the number of positive values (int)
        zeroes - the number of zeroes (int)
        evens - the number of even values (int)
        odds - the number of odd values (int)
    -------------------------------------------------------
    """
    negatives = postives = zeroes = evens = odds = 0
    for i in values:
        if i < 0:
            negatives += 1
        elif i > 0:
            postives += 1
        else:
            zeroes += 1
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    return negatives, postives, zeroes, evens, odds


def linear_search(a, v):
    """
    -------------------------------------------------------
    Searches through a for the value v and returns its index.
    User: index = linear_search(a, v)
    -------------------------------------------------------
    Parameters:
        a - a list of values (list of ?).
        v - can be compared to values in a (?).
    Returns:
        index - the index of the location of v in a, -1 if not found (int).
    -------------------------------------------------------
    """
    index = -1
    for i in range(len(a)):
        if a[i] == v:
            index = i
    return index


def many_search(a, v):
    """
    -------------------------------------------------------
    Searches through a for the value v and returns a list of
    all indexes of its occurrence.
    User: indexes = many_search(a, v)
    -------------------------------------------------------
    Parameters:
        a - a list of values (list of ?).
        v - can be compared to values in a (?).
    Returns:
        indexes - a list of indexes of the location of v in a,
            [] if not found (list of int).
    -------------------------------------------------------
    """
    index = []
    for i in range(len(a)):
        if a[i] == v:
            index.append(i)
    return index


def min_search(a):
    """
    -------------------------------------------------------
    Searches through a for the minimum value(s) and returns a
    list of the indexes of those values. (Assumes a has at least
    one element.)
    User: indexes = min_search(a, v)
    -------------------------------------------------------
    Parameters:
        a - a list of values (list of ?).
    Returns:
        indexes - a list of indexes of the minimum values in 
            a (list of int).
    -------------------------------------------------------
    """
    minimum = a[0]
    for i in a:
        if i < minimum:
            minimum = i
    min_index = many_search(a, minimum)
    return min_index


def dot_product(source1, source2):
    """
    -------------------------------------------------------
    Calculates a dot product of two lists. Lists must be the
    same length.
    Use: target = dot_product(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - list of numbers (list of float)
        source2 - list of numbers (list of float)
    Returns:
        target - source1 ⋅ source2 [source1 dot product source2] (list of float)
    -------------------------------------------------------
    """
    target = 0
    for i in range(len(source1)):
        target += source1[i] * source2[i]
    return target


def list_sums(source1, source2):
    """
    -------------------------------------------------------
    Calculates sums of elements of two lists. Lists must be the
    same length.
    Use: target = list_sum(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - list of numbers (list of float)
        source2 - list of numbers (list of float)
    Returns:
        target - sums of elements of source1 and source2 (list of float)
    -------------------------------------------------------
    """
    target = []
    for i in range(len(source1)):
        target.append(source1[i] + source2[i])
    return target


def union(source1, source2):
    """
    -------------------------------------------------------
    Returns a list that is the union of the contents of source1 and source2.
    Every element that appears at least once in either source1 and source2
    must appear once and only once in target.
    Use: target = union(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a list (list of ?)
        source2 - a list (list of ?)
    Returns:
        target - the union of source1 and source2 (list of ?)
    -------------------------------------------------------
    """
    target = []
    for i in source1:
        if i not in target:
            target.append(i)
    for i in source2:
        if i not in target:
            target.append(i)
    return target


def intersection(source1, source2):
    """
    -------------------------------------------------------
    Returns a list that is the intersection of the contents of source1 and source2.
    Only elements that appear in both source1 and source2
    appear once and only once in target.
    Use: target = intersection(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a list (list of ?)
        source2 - a list (list of ?)
    Returns:
        target - the intersection of source1 and source2 (list of ?)
    -------------------------------------------------------
    """
    target = []
    big_list = source1 if source1 < source2 else source2
    for i in big_list:
        if i in source1 and i in source2 and i not in target:
            target.append(i)
    return target


def symmetric_difference(source1, source2):
    """
    -------------------------------------------------------
    Returns a list that is the symmetric difference of the contents
    of source1 and source2.
    Only elements that appear in one of source1 and source2
    appear once and only once in target.
    Use: target = symmetric_difference(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a list (list of ?)
        source2 - a list (list of ?)
    Returns:
        target - the symmetric difference of source1 and source2 (list of ?)
    -------------------------------------------------------
    """
    target = []
    for i in source1:
        if i not in source2 and i not in target:
            target.append(i)
    for i in source2:
        if i not in source1 and i not in target:
            target.append(i)
    return target
