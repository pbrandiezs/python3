#!/usr/bin/env python3

def print_message(message, count = 1):
    while count > 0:
        print(message)
        count -= 1


message = input("Message? ")
count = input("Count [1]? ").strip()

if count:
    count = int(count)
else:
    count = 1

print_message(message, count)

