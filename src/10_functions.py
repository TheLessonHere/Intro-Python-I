# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

def is_even(number):
    if int(number) % 2 == 0:
        print("true")
    else:
        print("false")

is_even(2)
is_even(3)

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
def even_odd_checker(number):
    if number % 2 == 0:
        print("Even!")
    else:
        print("Odd!")

even_odd_checker(num)
even_odd_checker(2)
even_odd_checker(3)