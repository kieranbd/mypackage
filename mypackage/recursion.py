def sum_array(array):

    '''Return sum of all items in array'''
    sum[array]

def fibonacci(n):

    '''Return nth term in fibonacci sequence'''
    if  n <= 1:
        return
    else:
        return fibonacci(n-1) + fibonacci(n-2)

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
