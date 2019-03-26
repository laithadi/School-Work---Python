"""
------------------------------------------------------------------------
check if word is palindrome
------------------------------------------------------------------------
Author: Jayvinder Singh, Laith Adi
ID:     181000220, 170265190
Email:  rsha0220@mylaurier.ca, adix5190@mylaurier.ca
__updated__ = "2018-11-08"
------------------------------------------------------------------------
"""


from functions import is_palindrome


s = input("Enter a string: ")
palindrome = is_palindrome(s)
print()

if palindrome == True:
    print("'{}' is a palindrome".format(s))
else:
    print("'{}' is not a palindrome".format(s))
