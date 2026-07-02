# Python Fundamentals – Blackjack Project

> This guide covers **only the new Python concepts** introduced in the Blackjack project. It assumes you already understand:
>
> - Variables
> - Lists
> - Dictionaries
> - Functions
> - Loops
> - Conditional Statements
> - Random Module (`choice`, `randint`)
> - Strings
> - Boolean Variables

---

# New Concepts Covered

- `random.choices()`
- `random.choice()`
- Keyword Arguments
- List Methods (`append()`)
- Built-in Function `sum()`
- Multiple Assignment Patterns
- Game State Management
- Comparing Scores
- Emoji and Unicode Strings

---

# 1. random.choice()

## What is `random.choice()`?

Returns **one random element** from a sequence.

### Syntax

```python
random.choice(sequence)
```

Example

```python
import random

numbers = [1,2,3,4,5]

card = random.choice(numbers)

print(card)
```

Possible Output

```
4
```

Only **one** value is returned.

---

# 2. random.choices()

Notice the extra **s**.

```python
random.choices()
```

returns **multiple random elements**.

---

### Syntax

```python
random.choices(sequence, k=n)
```

where

```
k
```

means

```
How many values should be selected?
```

---

Example

```python
cards = random.choices(numbers, k=2)
```

Possible Output

```python
[7, 3]
```

Another run

```python
[10, 10]
```

Unlike `choice()`, duplicates are allowed because selection is **with replacement**.

---

# 3. Keyword Arguments

Your program uses

```python
k=2
```

This is called a **keyword argument**.

Instead of

```python
random.choices(numbers, 2)
```

Python allows

```python
random.choices(numbers, k=2)
```

This makes code easier to read.

---

# 4. Difference Between choice() and choices()

| `choice()` | `choices()` |
|------------|-------------|
| Returns one item | Returns a list |
| No `k` parameter | Uses `k` |
| Result: `5` | Result: `[5, 8]` |

Example

```python
random.choice(numbers)
```

Output

```
7
```

Example

```python
random.choices(numbers, k=3)
```

Output

```
[2,7,5]
```

---

# 5. List Method – append()

Adds one item to the end of a list.

Example

```python
cards = [5,8]

cards.append(10)
```

Result

```python
[5,8,10]
```

---

### In Your Program

```python
users_cards.append(users_card)
```

Player receives another card.

---

Similarly

```python
ai_cards.append(ai_card)
```

Computer receives another card.

---

# 6. Built-in Function – sum()

Calculates the total of all numbers in a list.

---

Example

```python
numbers = [4,7,9]

print(sum(numbers))
```

Output

```
20
```

---

### In Your Program

```python
user_points = sum(users_cards)
```

Suppose

```python
users_cards = [8, 10]
```

Result

```
18
```

---

Another example

```python
sum([5,5,5])
```

Result

```
15
```

---

# 7. Score Calculation

Instead of

```python
users_cards[0] +
users_cards[1] +
users_cards[2]
```

Python calculates

```python
sum(users_cards)
```

automatically.

---

# 8. Updating a List

Initially

```
Player

↓

[8,7]
```

Player draws

```
5
```

After

```python
append()
```

Result

```
[8,7,5]
```

---

# 9. Game State

The program keeps track of:

| Variable | Purpose |
|----------|----------|
| `users_cards` | Player's cards |
| `ai_cards` | Computer's cards |
| `user_points` | Player's score |
| `ai_points` | Computer's score |
| `game_over` | Controls loop |

---

# 10. Comparing Scores

Example

```python
if user_points > ai_points:
```

Python compares two numbers.

Suppose

```
Player = 19

Computer = 17
```

Result

```
19 > 17

↓

True
```

Player wins.

---

# 11. Nested Decision Making

Example

```python
if user_points < 21:

    if user_points > ai_points:
        ...
```

Python first checks

```
Player busted?
```

If not,

then compares both scores.

---

Visualization

```
Player Score

↓

Less than 21?

↓

Yes

↓

Compare with Computer

↓

Win / Lose
```

---

# 12. Variable Reassignment

Notice

```python
user_points = sum(users_cards)
```

Every loop,

Python recalculates the score.

Example

Iteration 1

```
15
```

Iteration 2

```
20
```

Iteration 3

```
23
```

The variable gets a new value each time.

---

# 13. Emoji and Unicode Strings

Python fully supports Unicode characters.

Example

```python
print("🎉")
```

Output

```
🎉
```

Your program prints

```python
🃁🂡🂱🃑
```

These are simply Unicode characters inside a string.

---

# 14. Simulating a Deck

Your program uses

```python
numbers = [1,2,3,...,10]
```

Every random selection simulates drawing a card.

Example

```
Deck

↓

Random Choice

↓

Card
```

This is a basic simulation.

---

# 15. Program Flow

Suppose

Initial cards

```
Player

↓

[8,6]

Computer

↓

[7]
```

Player chooses

```
y
```

Flow

```
Draw Card

↓

Append Card

↓

Calculate Sum

↓

Compare Scores

↓

Repeat
```

---

# Common Beginner Mistakes

## Confusing `choice()` and `choices()`

Wrong

```python
card = random.choices(numbers)
```

Result

```python
[7]
```

It's a list.

Correct

```python
card = random.choice(numbers)
```

Result

```
7
```

---

## Forgetting `append()`

Wrong

```python
users_card = random.choice(numbers)
```

The new card is never stored.

Correct

```python
users_cards.append(users_card)
```

---

## Manually Calculating Scores

Wrong

```python
score = cards[0] + cards[1]
```

Fails if more cards are added.

Correct

```python
sum(cards)
```

Works for any number of cards.

---

## Forgetting to End the Game

Your current program never changes

```python
game_over
```

to

```python
True
```

This causes the loop to continue forever.

Later you'll learn better ways to control game loops.

---

# New Concepts Learned

| Concept | Example |
|----------|----------|
| `random.choice()` | `random.choice(numbers)` |
| `random.choices()` | `random.choices(numbers, k=2)` |
| Keyword Arguments | `k=2` |
| List `append()` | `cards.append(10)` |
| Built-in `sum()` | `sum(cards)` |
| Score Calculation | `user_points = sum(cards)` |
| Updating Lists | Add new cards dynamically |
| Variable Reassignment | Recalculate score each loop |
| Nested Comparisons | Compare player and computer scores |
| Unicode Strings | `"🎉"` |

---

# One-Line Summary

The Blackjack project introduces **drawing multiple random values, dynamically growing lists, calculating totals with `sum()`, comparing game scores, and managing an interactive game state**, demonstrating how Python combines built-in functions, list operations, and conditional logic to build simple turn-based games.