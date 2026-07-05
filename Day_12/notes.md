# Python Fundamentals – Number Guessing Game Project

> This guide covers **only the new Python concepts** introduced in the Number Guessing Game project. It assumes you already understand:
>
> - Variables
> - Data Types
> - Functions
> - Loops (`for`, `while`)
> - Lists
> - Dictionaries
> - Conditional Statements
> - Random Module
> - Return Statements
> - Type Hints

---

# New Concepts Covered

- Constants
- Docstrings
- Exception Handling (`try` / `except`)
- Built-in Exceptions (`ValueError`)
- Input Validation
- Early Function Return
- The `__name__ == "__main__"` Idiom
- Program Entry Point (`main()`)
- Infinite Loops with `break`
- String Multiplication

---

# 1. Constants

## What is a Constant?

A **constant** is a variable whose value is intended **not to change** during the program.

Python doesn't enforce constants, but by convention they are written in **UPPERCASE**.

Example

```python
EASY_ATTEMPTS = 10

HARD_ATTEMPTS = 5
```

Instead of writing

```python
attempts = 10
```

everywhere, we store it once.

Benefits

- Easier to modify
- More readable
- Avoids "magic numbers"

---

# 2. Docstrings

Inside functions you wrote

```python
def choose_difficulty():
    """Returns number of attempts based on difficulty."""
```

The triple-quoted string immediately below a function is called a **docstring**.

It explains what the function does.

Example

```python
def add(a, b):
    """Returns the sum of two numbers."""
```

Docstrings are useful because tools like VS Code can display them automatically.

---

# 3. Exception Handling

One of the biggest new concepts.

Instead of letting the program crash,

Python allows us to **catch errors**.

Syntax

```python
try:
    code
except:
    code
```

---

Example

```python
try:
    number = int(input())
except:
    print("Invalid input")
```

If the user enters

```
hello
```

the program does **not** crash.

---

# 4. ValueError Exception

Your program catches

```python
except ValueError:
```

What causes a `ValueError`?

Example

```python
int("abc")
```

Python cannot convert

```
abc
```

into an integer.

Normally

```
ValueError
```

would stop the program.

Instead

```python
except ValueError:
```

handles it gracefully.

---

# 5. Input Validation

Good programs never trust user input.

Example

```python
guess = int(input())
```

The user might enter

```
150
```

or

```
-5
```

Your program checks

```python
if guess < 1 or guess > 100:
```

and rejects invalid values.

This is called **input validation**.

---

# 6. Early Return

Inside

```python
play_game()
```

you wrote

```python
if check_guess(...):
    return
```

`return`

immediately exits the current function.

Visualization

```
play_game()

↓

Correct Guess?

↓

Yes

↓

return

↓

Function Ends
```

Everything below the `return` is skipped.

---

# 7. Returning Boolean Values

Your function

```python
check_guess()
```

returns

```python
True
```

or

```python
False
```

Example

```python
if check_guess(guess, answer):
```

Python checks

```
Did the function return True?
```

If yes,

the player wins.

---

# 8. Infinite Loop with break

Your

```python
main()
```

contains

```python
while True:
```

This creates an infinite loop.

The only exit is

```python
break
```

Example

```python
while True:

    answer = input()

    if answer == "quit":
        break
```

---

# 9. break Statement

`break`

immediately exits the nearest loop.

Example

```python
for i in range(10):

    if i == 5:
        break

    print(i)
```

Output

```
0
1
2
3
4
```

Loop stops at 5.

---

# 10. Program Entry Point

One of the most important Python concepts.

```python
if __name__ == "__main__":
    main()
```

---

## What is `__name__`?

Every Python file has a built-in variable

```python
__name__
```

If the file is run directly

```
python game.py
```

then

```python
__name__
```

equals

```python
"__main__"
```

---

If the file is imported

```python
import game
```

then

```python
__name__
```

equals

```
game
```

instead.

---

This prevents code from running automatically when imported.

---

# 11. The `main()` Function

Instead of writing code directly,

professional programs usually use

```python
def main():
```

Example

```
Program Starts

↓

main()

↓

Game Logic

↓

Program Ends
```

Benefits

- Better organization
- Easier testing
- Easier importing

---

# 12. Function Composition

Functions calling other functions.

Example

```
main()

↓

play_game()

↓

choose_difficulty()

↓

check_guess()
```

Each function performs one small task.

This is called **function composition**.

---

# 13. String Multiplication

Your program prints

```python
"=" * 50
```

Result

```
==================================================
```

Python repeats strings using `*`.

Example

```python
"*"
```

×

5

↓

```
*****
```

---

# 14. Control Flow with continue

Inside

```python
except ValueError:
```

you use

```python
continue
```

Meaning

```
Skip remaining code

↓

Go to next loop iteration
```

Example

```python
while True:

    try:
        number = int(input())
    except ValueError:
        continue
```

---

# 15. Game Flow

```
Start

↓

Print Logo

↓

Choose Difficulty

↓

Generate Random Number

↓

Input Guess

↓

Valid Number?

↓

No

↓

Ask Again

↓

Yes

↓

Too High?

↓

Too Low?

↓

Correct?

↓

Win

↓

Play Again?

↓

Yes → Restart

↓

No → Exit
```

---

# 16. Defensive Programming

Your program protects against bad input.

Examples

✔ Letters

```
abc
```

✔ Numbers outside range

```
150
```

✔ Negative numbers

```
-8
```

This approach is called **defensive programming**.

---

# Common Beginner Mistakes

## Forgetting `try`

Wrong

```python
guess = int(input())
```

User enters

```
abc
```

Program crashes.

Correct

```python
try:
    guess = int(input())
except ValueError:
```

---

## Forgetting `break`

Wrong

```python
while True:
    print("Hello")
```

Runs forever.

Correct

```python
break
```

when needed.

---

## Forgetting `return`

Wrong

```python
if check_guess():
    print("Correct")
```

The game continues.

Correct

```python
return
```

to end the function immediately.

---

## Not Using Constants

Wrong

```python
attempts = 10
```

Repeated everywhere.

Better

```python
EASY_ATTEMPTS = 10
```

---

# Program Structure

```
Program Starts

│

▼

main()

│

▼

play_game()

│

├───────────────┐

▼               ▼

choose()    check_guess()

│

▼

Game Ends

│

▼

Play Again?

│

▼

Exit
```

---

# New Concepts Learned

| Concept | Example |
|----------|----------|
| Constants | `EASY_ATTEMPTS = 10` |
| Docstrings | `"""Returns attempts"""` |
| Exception Handling | `try / except` |
| `ValueError` | Invalid integer conversion |
| Input Validation | Check valid range |
| Early Return | `return` exits function |
| Boolean Return | `True` / `False` |
| Infinite Loop | `while True:` |
| `break` | Exit loop immediately |
| `continue` | Skip current iteration |
| `main()` Function | Program entry function |
| `__name__ == "__main__"` | Entry point check |
| Function Composition | Functions calling functions |
| String Multiplication | `"=" * 50` |
| Defensive Programming | Handle invalid user input |

---

# One-Line Summary

The Number Guessing Game introduces **professional Python programming practices**, including **constants, docstrings, exception handling, defensive programming, program entry points, function composition, and robust input validation**, making the application more modular, maintainable, and resilient to user errors.