# Write a program that prints all the prime numbers and all the perfect squares for all numbers between 100 and 100000.

# For all numbers between 100 and 100000 test that number for whether it is prime or a perfect square. If it is a prime number, print "Foo". If it is a perfect square, print "Bar". If it is neither, print "FooBar". Do not use the python math library for this exercise. For example, if the number you are evaluating is 25, you will have to figure out if it is a perfect square. It is, so print "Bar".

# This assignment is extra challenging! Try pair programming and pulling up a whiteboard.

i = 100
prime = ['prime']
perfect_squares = ['perfect_square']

while i < 1001:
    for ints in range(2,i):
        if i % ints == 0:
            break
        elif i % ints != 0:
            if ints == i-1:
                prime.append(i)
    i+=1

print prime
    

j = 100

while j < 1001:
    for ints in range(2,j):
        if j == ints * ints:
            perfect_squares.append(j)
    j+=1

print perfect_squares