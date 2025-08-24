#!/usr/bin/env python

print("Welcome to ascii encoder!")

question = input("Do you want to encode a sentence like a list? (y/n): ")


if question == "y":
    #sentence entered by user
    sentence = input("Enter your sentence: ")

    for char in sentence:
        print(f"{char} -> {ord(char)}")

else:
    
    question1 = input("Do you want to encode a sentence like a string? (y/n): ")

    if question1 =="n":
        print("Bye!")
        exit()
    
    else:

        ascii = input("Enter your sentence: ")

        ascii_str = "" # empty string to accumulate ascii codes

        for char in ascii:
            ascii_str += str(ord(char)) # add ascii code as string

        print(ascii_str)

