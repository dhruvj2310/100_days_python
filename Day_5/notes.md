# Python Fundamentals – Random Module and For Loops

This guide covers two important Python concepts:

- The `random` module
- `for` loops

These concepts are commonly used in games, simulations, password generators, and data processing.

---

# Part 1: The Random Module

---

# 1. What is a Module?

A **module** is a file that contains pre-written Python code.

Instead of writing everything yourself, you can import modules and use their functions.

Think of a module as a **toolbox**.

```
Python
│
├── print()
├── input()
├── math
├── random
├── datetime
└── os
```

---

# 2. Importing a Module

Before using a module, you must import it.

## Syntax

```python
import random
```

Now Python knows where to find all the random functions.

---

# 3. Why Use the Random Module?

Computers normally execute predictable code.

The `random` module allows Python to generate **pseudo-random** values such as:

- Dice rolls
- Coin tosses
- Lottery numbers
- Passwords
- Random game events

---

# 4. random.randint()

Returns a random integer within a specified range.

## Syntax

```python
random.randint(start, end)
```

Both numbers are included.

---

### Example

```python
import random

number = random.randint(1, 6)

print(number)
```

Possible Output

```
4
```

or

```
1
```

or

```
6
```

---

# 5. random.random()

Returns a random floating-point number.

Range:

```
0.0 <= number < 1.0
```

---

### Example

```python
import random

print(random.random())
```

Possible Output

```
0.4726382
```

---

# 6. Creating Random Decimals

Example

```python
price = random.random() * 100

print(price)
```

Possible Output

```
74.32
```

---

# 7. random.choice()

Selects one random element from a sequence.

---

### Example

```python
import random

fruits = ["Apple", "Banana", "Mango"]

fruit = random.choice(fruits)

print(fruit)
```

Possible Output

```
Banana
```

---

# 8. random.shuffle()

Randomly rearranges a list.

---

### Example

```python
import random

cards = ["A", "K", "Q", "J"]

random.shuffle(cards)

print(cards)
```

Possible Output

```
['Q', 'A', 'J', 'K']
```

Notice:

The original list changes.

---

# 9. random.uniform()

Returns a random decimal between two numbers.

---

### Example

```python
random.uniform(10, 20)
```

Possible Output

```
16.83
```

---

# 10. Pseudo-Random Numbers

Python doesn't generate truly random numbers.

It uses mathematical formulas to generate numbers that **appear random**.

These are called **Pseudo-Random Numbers (PRNG).**

---

# Part 2: For Loops

---

# 11. What is a Loop?

A loop repeats code automatically.

Instead of writing:

```python
print("Hello")
print("Hello")
print("Hello")
```

Use:

```python
for i in range(3):
    print("Hello")
```

---

# 12. Why Use Loops?

Loops reduce repetitive code.

Without loops:

```python
print(1)
print(2)
print(3)
print(4)
print(5)
```

With loops:

```python
for number in range(1, 6):
    print(number)
```

---

# 13. for Loop Syntax

```python
for variable in sequence:
    code
```

---

### Example

```python
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)
```

Output

```
Apple
Banana
Mango
```

---

# 14. Loop Variable

```python
for fruit in fruits:
```

Here,

```python
fruit
```

is called the **loop variable**.

Each iteration stores one item.

```
Iteration 1

fruit = Apple

Iteration 2

fruit = Banana

Iteration 3

fruit = Mango
```

---

# 15. range()

`range()` generates a sequence of numbers.

---

## Syntax

```python
range(stop)
```

Example

```python
range(5)
```

Produces

```
0
1
2
3
4
```

---

## Syntax

```python
range(start, stop)
```

Example

```python
range(2, 6)
```

Produces

```
2
3
4
5
```

---

## Syntax

```python
range(start, stop, step)
```

Example

```python
range(0, 11, 2)
```

Produces

```
0
2
4
6
8
10
```

---

# 16. Iterating Through Lists

Example

```python
names = ["John", "Alice", "Bob"]

for name in names:
    print(name)
```

Output

```
John
Alice
Bob
```

---

# 17. Iterating Through Strings

Strings are sequences.

Example

```python
word = "Python"

for letter in word:
    print(letter)
```

Output

```
P
y
t
h
o
n
```

---

# 18. Loop Execution

Example

```python
for number in range(3):
    print(number)
```

Execution

```
Iteration 1

number = 0

Iteration 2

number = 1

Iteration 3

number = 2
```

---

# 19. Accumulator Pattern

Used for calculating totals.

Example

```python
total = 0

for number in range(1, 6):
    total += number

print(total)
```

Output

```
15
```

Equivalent to

```
1 + 2 + 3 + 4 + 5
```

---

# 20. Finding Maximum Value

Example

```python
numbers = [3, 8, 2, 10, 5]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print(largest)
```

Output

```
10
```

---

# 21. Nested Loops

A loop inside another loop.

Example

```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

Output

```
0 0
0 1
1 0
1 1
2 0
2 1
```

---

# 22. Using Random with Loops

Example

```python
import random

for i in range(5):
    print(random.randint(1, 6))
```

Possible Output

```
3
6
2
1
5
```

---

# 23. Common Beginner Mistakes

## Forgetting to Import

Wrong

```python
number = random.randint(1, 10)
```

Error

```
NameError
```

Correct

```python
import random

number = random.randint(1, 10)
```

---

## Forgetting Colon

Wrong

```python
for i in range(5)
```

Correct

```python
for i in range(5):
```

---

## Wrong Indentation

Wrong

```python
for i in range(3):
print(i)
```

Correct

```python
for i in range(3):
    print(i)
```

---

## Confusing range()

```python
range(5)
```

Produces

```
0
1
2
3
4
```

Not

```
1
2
3
4
5
```

---

# New Concepts Learned

| Concept | Example |
|----------|----------|
| Module | `import random` |
| Import Statement | `import random` |
| `random.randint()` | `random.randint(1, 6)` |
| `random.random()` | `random.random()` |
| `random.uniform()` | `random.uniform(10, 20)` |
| `random.choice()` | `random.choice(list)` |
| `random.shuffle()` | `random.shuffle(list)` |
| Pseudo-Random Numbers | Computer-generated randomness |
| `for` Loop | `for i in range(5):` |
| Loop Variable | `for fruit in fruits:` |
| `range(stop)` | `range(5)` |
| `range(start, stop)` | `range(2, 6)` |
| `range(start, stop, step)` | `range(0, 10, 2)` |
| Iterating Lists | `for item in list:` |
| Iterating Strings | `for char in word:` |
| Accumulator Pattern | `total += number` |
| Nested Loops | `for i:` inside `for j:` |

---

# One-Line Summary

The **random module** enables Python to generate pseudo-random numbers and selections for games, simulations, and automation, while **for loops** provide an efficient way to iterate over sequences or repeat code, making programs more concise, scalable, and easier to maintain.