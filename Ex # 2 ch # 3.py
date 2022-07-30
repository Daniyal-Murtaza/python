# define is_palindrome function that take one word in string as input
# and return true if it is palindrome else return false

# palindrome : word that reads same backwards and forwards.

# example:
# is_palindrome("madam") ----> True
# is_palindrome("horse") ----> False

# logic:
# step 1 (reverse the string)
# step 2 (compare reversed string with original string)


#(A)
def is_palindrome(word):
    rev_word = word[::-1]              # we are reversing the word with the help of string slicing!
    if rev_word == word:
        return True
    else:
        return False
print(is_palindrome("madam"))
print(is_palindrome("horse"))

#(B) now we are shrinking the above program:
def is_palindrom(word):
    if word == word[::-1]:
        return True
    return False
print(is_palindrome("madam"))
print(is_palindrome("horse"))

#(c)
def is_palindrone(word):
    return word == word[::-1]         # since == is a boolean expression therefore it provides the answer in true or false form!!
print(is_palindrome("madam"))
print(is_palindrome("horse"))


