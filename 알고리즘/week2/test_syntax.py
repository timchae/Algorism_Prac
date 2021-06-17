input = "abcccaba"


def is_palindrome(string):

    n = len(string)//2
    l = len(string)
    c = 0
    for a in range(n):
        
        if string[a] == string[l-1]:
            c += 1
        l = l-1 

    if c == n:
        return True
    else:
        return False


print(is_palindrome(input))


# input = "abcba"


# def is_palindrome(string):
#     if len(string) <= 1:
#         return True
#     if string[0] != string[-1]:
#         return False
#     return is_palindrome(string[1:-1])


# print(is_palindrome(input))