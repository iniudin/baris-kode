def is_palindrome(string):
    reverse_str = string[::-1]
    if string == reverse_str:
        return True
    else:
        return False
