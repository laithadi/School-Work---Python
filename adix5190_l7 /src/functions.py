"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Jayvinder Singh
ID:     181000220
Email:  rsha0220@mylaurier.ca
__updated__ = "2018-11-08"
------------------------------------------------------------------------
"""


def is_hydroxide(chemical):
    """
    -------------------------------------------------------
    Determines if a chemical formula is a hydroxide.
    Use: hydroxide = is_hydroxide(chemical)
    -------------------------------------------------------
    Preconditions:
        chemical - a chemical formula (str)
    Postconditions:
        hydroxide - True if chemical is a hydroxide (ends in 'OH'),
            False otherwise (boolean)
    -------------------------------------------------------
    """

    m = chemical.endswith("OH")
    if m == True:
        print("{} is a hydroxide.".format(chemical))
    else:
        print("{} is not a hydroxide.".format(chemical))


def url_categorize(url):
    """
    -------------------------------------------------------
    Returns whether a url represents a business, a non-profit, or another
    type of organization.
    Use: url_type = org_categorize(url)
    -------------------------------------------------------
    Parameters:
        url - the web address of the organization (str)
    Returns:
        url_type - the organization type (str)
            'business' if url ends with 'com'
            'non-profit' if url ends with 'org'
            'other' if url ends with something else
    ------------------------------------------------------
    """
    m = url.endswith("com")
    d = url.endswith("org")

    if m == True:
        print("business")
    elif d == True:
        print("non-profit")
    else:
        print("other")


def parse_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code. A product code has three parts:
        The first three letters describe the product category
        The next four digits are the product ID
        The remaining characters describe the product's qualifiers
    Use: pc, pi, pq = parse_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a valid product code (str)
    Returns:
        pc - the category part of product_code (str)
        pi - the id part of product_code (str)
        pq - the qualifier part of product_code (str)
    -------------------------------------------------------
    """
    pc = (product_code[0:2])
    pi = (product_code[3:6])
    pa = (product_code[7:9])
    return pc, pi, pa


def validate_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code and prints whether the various parts are valid.
    A product code has three parts: 
        The first three letters describe the product category and must 
        all be in upper case.
        The next four digits are the product ID.
        The remaining characters describe the product's qualifiers, 
        such as colour, size, etc. and always begins with an uppercase letter.
    Use: validate_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a product code (str)
    Returns:
        None
    -------------------------------------------------------
    """
    pc = product_code[0:2].isupper()
    pi = product_code[3:6].isdigit()
    pa = product_code[7].isupper()

    if pc == True:
        print("Category {} is valid.".format(product_code[0:3]))
    if pc == False:
        print("Category {} not is valid.".format(product_code[0:3]))
    if pi == True:
        print("ID {} is valid".format(product_code[3:7]))
    if pi == False:
        print("ID {} is not valid".format(product_code[3:7]))
    if pa == True:
        print("Qualifier {} is valid.".format(product_code[7:10]))
    if pa == False:
        print("Qualifier {} is not valid.".format(product_code[7:10]))


def password_strength(password):
    """
    -------------------------------------------------------
    Checks the strength of a given password. A password is
    strong if it contains at least eight characters, has a
    combination of upper-case and lower-case letters, and
    includes digits. Prints one or more of:
        not long enough - if password less than 8 characters
        no digits - if password has no digits
        no upper case - if password has no upper case letters
        no lower case - if password has no lower case letters
    Use: passwd_strength(pass)
    -------------------------------------------------------
    Parameters:
        password - the password to be checked (str)
    Returns:
        None
    ------------------------------------------------------
    """

    num = False
    isUpper = False
    isLower = False

    if len(password) < 8:
        print("not long enough")

    for i in password:
        if i.isdigit() and num == False:
            num = True
        if i.isdigit() == False:
            if i.islower() and isLower == False:
                isLower = True
            if i.isupper() and isUpper == False:
                isUpper = True

    if num == False:
        print("no digits")
    if isUpper == False:
        print("no upper")
    if isLower == False:
        print("no lower case")
    return


def is_palindrome(s):
    """
    -----------------------------------------------------------------
    Checks whether the given string is palindrome or not. A palindrome is
    a string the reads the same forwards as backwards.
    Use: palindrome = is_palindrome(s)
    -----------------------------------------------------------------
    Parameters:
        s - a string to be checked (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -----------------------------------------------------------------
    """
    out = ""
    for i in s:
        out = i + out
    if out == s:
        return True
    else:
        return False


def vowel_count(s):
    """
    -------------------------------------------------------
    Counts the number of vowels in a string. Does not include 'y'.
    Use: count = vowel_count(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        count - the number of vowels in s (int)
    -------------------------------------------------------
    """
    count = s.count("a") + s.count("e") + s.count("i") + \
        s.count("o") + s.count("u")
    return count


def count_special_chars(s):
    """
    -------------------------------------------------------
    Counts the number of special characters in s.
    The special characters are: "#", "@", "$", "%", "&", "!".
    Use: count = count_special_chars(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        count - number of special characters in s (int)
    ------------------------------------------------------
    """

    count = s.count("#") + s.count("@") + s.count("$") + \
        s.count("%") + s.count("&") + s.count("!")
    return count


def text_analyze(s):
    """
    -------------------------------------------------------
    Analyzes txt and returns the number of uppercase letters,
    lowercase letters, digits, and number of whitespaces in txt.
    Use: uppr, lowr, dgts, whtspc = text_analyze(txt)
    -------------------------------------------------------
    Parameters:
        txt - the text to be analyzed (str)
    Returns:
        uppr - number of uppercase letters in txt (int >= 0)
        lowr - number of lowercase letters in txt (int >= 0)
        dgts - number of digits in txt (int >= 0)
        whtspc - number of white spaces in the text (int >= 0)
    ------------------------------------------------------
    """

    uppr = sum(c.isupper() for c in s)
    lowr = sum(c.islower() for c in s)
    dgts = sum(c.isdigit() for c in s)
    whtspc = sum(c.isspace() for c in s)
    return uppr, lowr, dgts, whtspc


def comma_period_replace(s):
    """
    -------------------------------------------------------
    Replaces all the commas with a period in s.
    Use: out = comma_period_replace(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        out - s with all commas replaced by a period (str)
    ------------------------------------------------------
    """

    out = s.replace(",", ".")
    return out


def total_digits(s):
    """
    -------------------------------------------------------
    Extracts and calculates the total of all digits in s.
    Use: total = total_digits(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        total - total of all the digits in s (int)
    ------------------------------------------------------
    """

    total = 0
    for i in s:
        if i.isdigit():
            i = int(i)
            total = total + i

    return total


def dsmvwl(s):
    """
    -------------------------------------------------------
    Disemvowels a string. Returns a copy of s with all the vowels
    removed. Y is not treated as a vowel. Preserves case.
    Use: out = dsmvwl(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        out - s with its vowels removed (str)
    -------------------------------------------------------
    """
    out = ""
    v = ['a', 'A', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
    for i in s:
        if i not in v:
            out = out + i

    return out
