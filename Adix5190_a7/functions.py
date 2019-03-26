'''
[program description]

Author: Laith Adi 

ID: 170265190

Email: Adix5190@mylaurier.ca

__updated__ = "2018-11-16"

'''

# For Task 6
TWO = "ABC"
THREE = "DEF"
FOUR = "GHI"
FIVE = "JKL"
SIX = "MNO"
SEVEN = "PRS"
EIGHT = "TUV"
NINE = "WXY"


def my_isdigit(s):
    """
    -------------------------------------------------------
    Determines if all the characters is s are digits. An empty string
    has no digits.
    NOTE: must execute as the equivalent of the Python method s.isdigit()
    Use: digits = my_isdigit(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        digits - True if all of s is digits, False otherwise (boolean)
    -------------------------------------------------------
    """
    registry = '0123456789'
    digits = True
    if len(s) > 0:
        for i in range(0, len(s)):
            if s[i] not in registry:
                digits = False
    return(digits)


def my_isalpha(s):
    """
    -------------------------------------------------------
    Determines if all the characters is s are alphabetic characters.
    An empty string has no letters.
    NOTE: must execute as the equivalent of the Python method s.isalpha()
    Use: alpha = my_isalpha(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        alpha - True if all of s is letters of the alphabet,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    registry_1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    registry_2 = registry_1.lower()
    alpha = True
    if len(s) > 0:
        for i in range(0, len(s)):
            if s[i] not in registry_1 or s[i] not in registry_2:
                alpha = False
    return(alpha)


def my_find(s, r):
    """
    -------------------------------------------------------
    Returns the index of the string r in the string s.
    NOTE: must execute as the equivalent of the Python method s.find(r)
    Use: i = my_find(s, r)
    -------------------------------------------------------
    Parameters:
        s - a string to search (str)
        r - a string to search for (str)
    Returns:
        i - the index of the start of r in s, -1 if r is not in s (int)
    -------------------------------------------------------
    """
    result = ''
    j = 0
    if len(r) > 0 and len(s) > 0:
        for i in range(0, len(s)):
            if s[i] == r[j]:
                result += s[i]
                j += 1
                if len(result) == 0:
                    i = -1
                if result == r:
                    i -= len(result) - 1
                    return(i)
                    j -= 1
                    return(i)


def common_ending(s1, s2):
    """
    -------------------------------------------------------
    Returns the longest common ending of two strings.
    Use: common = common_ending(s1, s2)
    -------------------------------------------------------
    Parameters:
        s1 - first string for ending comparison (str)
        s2 - second string for ending comparison (str)
    Returns:
        common - the longest common ending of s1 and s2 (str)
    -------------------------------------------------------
    """
    common = ''
    if len(s2) >= len(s1):
        for i in range(1, len(s1) + 1):
            if s1[-i] == s2[-i]:
                common = common[:0] + s1[-i] + common
    else:
        for i in range(1, len(s2) + 1):
            if s1[-i] == s2[-i]:
                common = common[:0] + s2[-i] + common
    return(common)


def is_valid_isbn(isbn):
    """
    -------------------------------------------------------
    Determines if an ISBN string is valid. An ISBN string is valid if:
        - it consists of only digits and dashes ('-')
        - it contains 5 groups of digits separated by dashes
        - its first group of digits is either '978' or '979'
        - its final group of digits is a single digit
        - its entire length is 17 characters
    Use: valid = is_valid_isbn(isbn)
    -------------------------------------------------------
    Parameters:
        isbn - a string (str)
    Returns:
        valid - True if isbn is valid, False otherwise (boolean)
    -------------------------------------------------------
    """
    valid = True
    isbn_digitcheck = isbn.replace("-", "")
    if len(isbn) != 17:
        valid = False
    elif isbn[0:3] != "978" and isbn[0:3] != "979":
        valid = False
    elif isbn[15] != "-":
        valid = False
    elif not isbn_digitcheck.isdigit():
        valid = False
    elif isbn.count("-") != 4:
        valid = False
    elif isbn.count("-") > 0:
        valid = False
    return(valid)


def number_convert(number):
    """
    -------------------------------------------------------
    Converts a phone number character string to a string of digits.
    A telephone keypad has the following digit/letter combinations:
        2 : ABC
        3 : DEF
        4 : GHI
        5 : JKL
        6 : MNO
        7 : PRS
        8 : TUV
        9 : WXY
    ('Q' and 'Z' are not represented.) Q, Z, and non-letters are
    left unchanged.
    Use: digits = number_convert(number)
    -------------------------------------------------------
    Parameters:
        number - a phone number string (str)
    Returns:
        digits - the numeric version of number based upon a
            telephone keypad (str)
    -------------------------------------------------------
    """
    digits = ''
    i = 0
    while i < len(number):
        if number[i] in TWO:
            digits += "2"
            i += 1
        elif number[i] in THREE:
            digits += "3"
            i += 1
        elif number[i] in FOUR:
            digits += "4"
            i += 1
        elif number[i] in FIVE:
            digits += "5"
            i += 1
        elif number[i] in SIX:
            digits += "6"
            i += 1
        elif number[i] in SEVEN:
            digits += "7"
            i += 1
        elif number[i] in EIGHT:
            digits += "8"
            i += 1
        elif number[i] in NINE:
            digits += "9"
            i += 1
        else:
            digits += number[i]
            i += 1
    else:
        return(digits)


def pluralize(s):
    """
    -------------------------------------------------------
    Pluralizes a string according to the rules:
        - if s ends with 's', 'sh', or 'ch', add 'es'
        - if s ends with 'y' but not 'ay' or 'oy', add 'ies'
        - otherwise add 's'
    Use: plural = pluralize(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        plural - a plural version of s (str)
    -------------------------------------------------------
    """
    plural = ""
    # when a word ends with "x", adding "es" i also correct thing to do.
    # Ex.)Box>B
    if s.endswith(("s", "sh", "ch", "x")):
        plural = s + "es"
    elif s.endswith("y") and s[-2] != "a" and s[-2] != "y":
        plural = s.replace(s[-1], "") + "ies"
    else:
        plural = s + "s"
    return(plural)
