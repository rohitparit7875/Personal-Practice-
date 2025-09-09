def is_palindrome(s):
    s = str(s)  # convert to string (works for numbers too)
    return s == s[::-1]

# Example
print(is_palindrome("madam"))  # True
print(is_palindrome(121))      # True
print(is_palindrome("hello"))  # False
