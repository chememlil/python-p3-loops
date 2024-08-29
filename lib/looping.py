#!/usr/bin/env python3

def happy_new_year():
    # Countdown from 10 to 1, then print "Happy New Year!"
    counter = 10
    while counter > 0:
        print(counter)
        counter -= 1
    print("Happy New Year!")

def fizzbuzz(num):
    # Return "FizzBuzz" if num is divisible by 3 and 5, "Fizz" if divisible by 3, "Buzz" if divisible by 5, or the number itself.
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

def fizzbuzz_printer():
    # Print numbers from 1 to 100, replacing multiples of 3 with "Fizz", multiples of 5 with "Buzz", and multiples of both with "FizzBuzz".
    for num in range(1, 101):
        print(fizzbuzz(num))

def reverse_string(str):
    # Reverse the input string without using the built-in reverse method.
    reversed_str = ""
    for char in str:
        reversed_str = char + reversed_str
    return reversed_str

def square_integers(int_list):
    # Return a list of squared elements from the input list of integers.
    return [num ** 2 for num in int_list]

# Example usage (You can remove these or keep them for testing purposes)
if __name__ == "__main__":
    happy_new_year()
    fizzbuzz_printer()
    print(reverse_string("hello"))
    print(square_integers([1, 2, 3, 4]))
