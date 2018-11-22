def sum_array(array):

    '''Return sum of all items in array'''
    return sum(array)

sum_array([0,0,1])

def fibonacci(n):

    '''Return nth term in fibonacci sequence'''
    if  n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fibonacci(5)

def factorial(n):

    '''Return n!'''
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def reverse(word):

    '''Return word in reverse'''
    if word == "":
        return word
    else:
        return reverse(word[1:]) + word[0]
