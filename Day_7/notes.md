# Python Fundamentals Learned from the Hangman Project

> This guide covers **only the new Python concepts** introduced in the Hangman project. It assumes you already know:
>
> - Variables
> - Data Types
> - Input & Output
> - Strings
> - Lists
> - Random Module
> - For Loops
> - While Loops
> - Functions
> - If / Else / Elif
> - Logical Operators
> - Indentation

---

# Complete Project Concepts

This Hangman project introduces several new programming concepts:

- Multi-line Lists
- List Indexing
- String Indexing
- `len()` Function
- Boolean Variables
- Flag Variables
- Membership Operators (`in`, `not in`)
- String Methods (`lower()`, `join()`)
- List Multiplication
- Updating List Elements
- Tracking Game State
- Win/Loss Conditions

---

# 1. len() Function

## What is len()?

`len()` returns the number of items in an object.

### Syntax

```python
len(object)
```

---

### Example (String)

```python
name = "Python"

print(len(name))
```

Output

```
6
```

---

### Example (List)

```python
numbers = [10, 20, 30]

print(len(numbers))
```

Output

```
3
```

---

### In Your Program

```python
word_length = len(chosen_word)
```

If

```python
chosen_word = "python"
```

Then

```
word_length = 6
```

---

# 2. List Multiplication

Instead of manually writing:

```python
display = ["_", "_", "_", "_", "_", "_"]
```

Python can repeat values.

```python
display = ["_"] * word_length
```

Example

```python
["_"] * 5
```

Result

```python
['_', '_', '_', '_', '_']
```

---

# 3. Boolean Variables

A Boolean stores only two values.

```python
True
False
```

Example

```python
game_over = False
```

Later

```python
game_over = True
```

---

# 4. Flag Variables

A **flag** is a Boolean variable used to track the state of something.

Example

```python
game_over = False
```

The game keeps running while the flag is False.

When the player wins:

```python
game_over = True
```

The loop stops.

---

Another example:

```python
found = False
```

If the guessed letter exists:

```python
found = True
```

---

# 5. Membership Operators

Used to check if something exists inside a sequence.

## `in`

Returns True if the item exists.

Example

```python
"a" in "apple"
```

Result

```python
True
```

---

Example

```python
3 in [1,2,3]
```

Result

```python
True
```

---

## `not in`

Returns True if the item does not exist.

Example

```python
"x" not in "apple"
```

Result

```python
True
```

---

### In Your Program

```python
if guess in display:
```

Checks whether the guessed letter has already been revealed.

---

```python
if "_" not in display:
```

Checks whether all blanks have been replaced.

---

# 6. String Indexing

Strings are sequences.

Each character has an index.

```
P  y  t  h  o  n

0  1  2  3  4  5
```

Example

```python
word = "python"

print(word[0])
```

Output

```
p
```

---

### In Your Program

```python
letter = chosen_word[position]
```

Gets one character at a time.

---

# 7. List Indexing

Lists also use indexes.

Example

```python
colors = ["Red", "Blue", "Green"]
```

```
0
1
2
```

Example

```python
print(colors[1])
```

Output

```
Blue
```

---

### In Your Program

```python
gallow_steps[6 - lives]
```

Shows the correct Hangman stage.

---

# 8. Updating List Elements

Lists are mutable.

You can change an item.

Example

```python
letters = ["_", "_", "_"]

letters[1] = "A"

print(letters)
```

Output

```python
['_', 'A', '_']
```

---

### In Your Program

```python
display[position] = letter
```

Replaces

```
_
```

with

```
a
```

---

# 9. String Method: lower()

Converts text to lowercase.

Example

```python
word = "Python"

print(word.lower())
```

Output

```
python
```

---

### Why?

If the user types

```
A
```

it becomes

```
a
```

making comparisons easier.

---

# 10. String Method: join()

Combines list elements into one string.

---

Example

```python
letters = ["P", "y", "t", "h", "o", "n"]

print("".join(letters))
```

Output

```
Python
```

---

Adding spaces

```python
print(" ".join(letters))
```

Output

```
P y t h o n
```

---

### In Your Program

```python
print(" ".join(display))
```

Displays

```
_ _ _ _ _
```

instead of

```
['_', '_', '_', '_', '_']
```

---

# 11. Accessing Elements Using a Loop

Example

```python
word = "apple"

for i in range(len(word)):
    print(word[i])
```

Output

```
a
p
p
l
e
```

---

### In Your Program

```python
for position in range(word_length):

    letter = chosen_word[position]
```

Each letter is checked one by one.

---

# 12. Updating Multiple Positions

Suppose

```
chosen_word = "apple"
```

Guess

```
p
```

Loop

```
Position 0 → a

Position 1 → p ✓

Position 2 → p ✓

Position 3 → l

Position 4 → e
```

Result

```
_ p p _ _
```

---

# 13. Tracking Game State

The game stores important information in variables.

| Variable | Purpose |
|-----------|----------|
| `chosen_word` | Secret word |
| `display` | Current progress |
| `lives` | Remaining chances |
| `game_over` | End game flag |
| `found` | Letter found flag |

---

# 14. Win Condition

```python
if "_" not in display:
```

Meaning:

No blanks remain.

Player wins.

---

# 15. Lose Condition

```python
if lives == 0:
```

Meaning:

No lives remain.

Game ends.

---

# 16. Multi-line Strings

Each Hangman drawing is stored inside triple quotes.

Example

```python
'''
  O
 /|\\
 / \\
'''
```

Triple quotes preserve formatting.

---

# 17. ASCII Art

ASCII Art is text arranged to create pictures.

Example

```
 O
/|\
/ \
```

Python stores it as a normal string.

---

# 18. Game Loop

The game repeatedly performs these steps.

```
Start

↓

Show Hangman

↓

Show Word

↓

Get Guess

↓

Check Guess

↓

Correct?

↓

Yes → Reveal Letters

↓

No → Lose Life

↓

Won?

↓

Lost?

↓

Repeat
```

---

# Common Beginner Mistakes

## Forgetting `.lower()`

Wrong

```python
guess = input("Guess:")
```

User enters

```
A
```

Word contains

```
a
```

They won't match.

Correct

```python
guess = input().lower()
```

---

## Using `=` Instead of `==`

Wrong

```python
if lives = 0:
```

Correct

```python
if lives == 0:
```

---

## Using `append()` Instead of Updating

Wrong

```python
display.append(letter)
```

Correct

```python
display[position] = letter
```

---

## Forgetting to Update Flags

Wrong

```python
found = False
```

Never changed.

The program always thinks the guess is wrong.

Correct

```python
found = True
```

when the letter is found.

---

# New Concepts Learned

| Concept | Example |
|----------|----------|
| `len()` | `len(word)` |
| List Multiplication | `["_"] * 5` |
| Boolean Variables | `True`, `False` |
| Flag Variables | `game_over`, `found` |
| Membership Operator | `in`, `not in` |
| String Indexing | `word[0]` |
| List Indexing | `list[2]` |
| Updating List Items | `display[1] = "a"` |
| `lower()` | `text.lower()` |
| `join()` | `" ".join(list)` |
| Game State Tracking | `lives`, `display` |
| Win Condition | `"_" not in display` |
| Lose Condition | `lives == 0` |
| ASCII Art | Multi-line strings |

---

# One-Line Summary

The Hangman project combines previously learned Python concepts with **list manipulation, indexing, membership operators, Boolean flags, string methods, game-state management, and ASCII art**, demonstrating how multiple language features work together to build a complete interactive game.