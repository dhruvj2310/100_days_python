# Python Concepts Covered

Based on the uploaded practice files.

## 1. Importing Modules

``` python
import random
```

-   Reuse Python's standard library.
-   The `random` module generates random values.

## 2. User Input

``` python
user_choice = input("rock, paper, scissor?: ")
```

-   `input()` always returns a string.

## 3. String Methods

### `.lower()`

``` python
user_choice = input(...).lower()
```

Converts text to lowercase.

## 4. Variables

Variables store values such as strings, numbers, and lists.

## 5. Lists

``` python
choices = ["rock", "paper", "scissors"]
```

### Nested Lists

``` python
dirty_dozen = [fruits, vegetables]
print(dirty_dozen[1][1])
```

## 6. Dictionaries

``` python
choices_art = {
    "rock": rock,
    "paper": paper,
    "scissors": scissor
}
```

## 7. Multi-line Strings

Triple quotes allow multi-line text.

## 8. Random Module

### random.choice()

``` python
random.choice(choices)
```

### random.randint()

``` python
random.randint(0, 1)
```

## 9. Conditional Statements

``` python
if condition:
    ...
elif another_condition:
    ...
else:
    ...
```

## 10. Comparison Operators

-   ==

-   !=

-   

-   \<

-   =

-   \<=

## 11. Boolean Logic

Conditions evaluate to `True` or `False`.

## 12. print()

``` python
print("Hello")
```

## 13. f-Strings

``` python
print(f"You chose {user_choice}")
```

## 14. Comments

``` python
# This is a comment
```

## 15. Indexing

``` python
friends[2]
dirty_dozen[1][1]
```

## 16. Game Logic

The Rock-Paper-Scissors program combines: - User input - Random
selection - Lists - Dictionaries - Conditions - ASCII art - f-strings -
Program flow

# Summary

The uploaded programs introduce:

-   Importing modules
-   Variables
-   User input
-   Strings
-   String methods
-   Lists
-   Nested lists
-   Dictionaries
-   Indexing
-   Random module
-   Conditional statements
-   Boolean logic
-   Comparison operators
-   Printing
-   f-strings
-   Comments
-   Simple game development
