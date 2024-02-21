import sys
import time

# use of generators; elements are not stored in memory
print(sys.getsizeof(range(999999)))
g = (x*2 for x in range(999999))  # notice the parenthesis for generator
print(sys.getsizeof(g))
start = time.time()
for i in g:
    pass
print('iterating over generator took', time.time() - start)

# use of list; all elements are stored in memory
l = [x for x in range(999999)]
print(sys.getsizeof(l))  # notice the square brackets for list
start = time.time()
for i in l:
    pass
print('iterating over list took', time.time() - start)

# Conclusion
# Generators are more memory efficient than lists.
# Lists are faster iterated than generators

# tradeoff between compute and memory

# If you do not need to reuse the elements, use a generator.
# If you need to reuse the elements, use a list.

# make your generator function
# use the yield keyword to return a value


def fibonacci_generator(n):
    """Return a generator for the fibonacci sequence."""
    def fibonacci(n):
        """Return the nth value in the fibonacci sequence."""
        if n == 0:
            return 1
        elif n <= 2:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    for i in range(n):
        yield fibonacci(i)


for i in fibonacci_generator(30):
    print(i)




