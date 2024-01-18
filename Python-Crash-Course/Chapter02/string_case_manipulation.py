#!/usr/bin/env python3

print("# Case Manipulation")
name = 'ada lovelace'
# Capitalise the first letter of each word, like in a title.
print(name.title())

name = "Ada Lovelace"
print(name.lower())
print(name.upper())

first_name = 'ada'
last_name = 'lovelace'
print("Hello, " + first_name.title() + " " + last_name.title() + "!")

# Using a variable's value inside an f string
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")
