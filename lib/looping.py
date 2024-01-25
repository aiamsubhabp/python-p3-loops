#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i < 11 and i > 0:
        print(i)
        i -= 1
        print('Happy New Year!')



def square_integers(int_list):
    square_int = [int * int for int in int_list]
    return square_int

def fizzbuzz():
    for i in range(1, 101):
        if not i % 15:
            print("FizzBuzz")
        elif not i % 5:
            print("Buzz")
        elif not i % 3:
            print("Fizz")
        else:
            print(i)
