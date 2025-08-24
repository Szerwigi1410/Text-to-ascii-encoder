#!/usr/bin/env python

# Color codes
GREEN="\033[32m" #
RED="\033[31m"   #
BLUE="\033[34m"  #
CYAN="\033[36m"  #
WHITE="\033[37m"
YELLOW="\033[33m"#
PURPLE="\033[35m"#
BOLD="\033[1m"   #
RESET="\033[0m"  #
BLACK="\033[30m" 
GRAY="\033[90m"

print("Welcome to" + BOLD + GREEN + " a" + RED + "s" + BLUE + "c" + CYAN + "i" + PURPLE + "i " + WHITE + "encoder!" + RESET)

question = input("Do you want to encode a sentence like a list? " + BOLD + "(y/n): " + RESET)


if question == "y":
    #sentence entered by user
    sentence = input(BOLD + "Enter your sentence: " + RESET)

    for char in sentence:
        print(f"{char} -> {ord(char)}")

else:
    
    question1 = input("Do you want to encode a sentence like a string? " + BOLD + "(y/n): ")

    if question1 =="n":
        print("Bye!")
        exit()
    
    else:

        ascii = input(BOLD + "Enter your sentence: " + RESET)

        ascii_str = "" # empty string to accumulate ascii codes

        for char in ascii:
            ascii_str += str(ord(char)) # add ascii code as string

        print(ascii_str)

