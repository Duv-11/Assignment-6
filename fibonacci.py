"""Assignment 6 - a fibonacci series iterable
Devon Singh 2025/07/27"""

#Setup the class for fibonacci
class Fibonacci:
    #1. the below code ensures all values is an integer
    def __init__(self, n):
        if not isinstance(n, int):
            raise ValueError("Error use integer's only")
        self.int = n

#setup iterable to run the fibanacci sequence
    def __iter__(self):
        self.fib_index = 0
        self.val = 0
        self.curr_val = 1
        return self

    def __next__(self):
        # the below stops the iterable if the number is less than the value or a negative number
        if self.int < 0 or self.fib_index > self.int:
            raise StopIteration
        #the below code calculates the fibonacci sequence and returns the next value in the sequence
        if self.fib_index == 0:
            self.fib_index += 1
            return 0 #code if value is 0 return 0
        elif self.fib_index == 1:
            self.fib_index += 1
            return 1
        else:
            next_fib_val = self.val + self.curr_val
            self.val, self.curr_val = self.curr_val, next_fib_val
            self.fib_index += 1
            return next_fib_val
