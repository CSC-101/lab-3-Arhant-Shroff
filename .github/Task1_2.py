def square(n:int) -> int:
    return n * n                           # Record, in order of the calls, each value of n and
                                           # the corresponding return value.
# order of n = 1, 2, 3, 4, order of return = 1, 4, 9, 16

squares = [square(x) for x in [1,2,3,4]]   # What is the value of squares and how does this relate to the
print()                                    # values recorded above?

#squares = [1, 4, 9, 16], it is the squared values of the list above
