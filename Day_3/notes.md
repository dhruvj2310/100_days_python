# Python If / Else Statements — Summary Notes

## What is an If/Else Statement?

An **if/else statement** allows a program to make decisions based on conditions.

### Logic

```text
If condition is True → Do Action A
Else → Do Action B
```

### Real-Life Example: Bathtub Overflow

- If water level > 80 cm → Drain water
- Else → Continue filling

```python
if water_level > 80:
    drain_water()
else:
    fill_water()
```

---

# Basic If Statement

```python
if condition:
    # code to execute if condition is True
```

### Example

```python
height = 130

if height > 120:
    print("You can ride the roller coaster.")
```

Output:

```text
You can ride the roller coaster.
```

---

# If / Else Statement

```python
if condition:
    # runs when condition is True
else:
    # runs when condition is False
```

### Example

```python
height = 100

if height > 120:
    print("You can ride.")
else:
    print("Sorry, you are too short.")
```

Output:

```text
Sorry, you are too short.
```

---

# Roller Coaster Example

### Requirement

A person can ride only if their height is at least 120 cm.

```python
height = int(input("Enter your height in cm: "))

if height >= 120:
    print("You can ride the roller coaster.")
else:
    print("Sorry, you have to grow taller before you can ride.")
```

---

# Importance of Indentation

Python uses indentation (spaces) to define code blocks.

### Correct

```python
if height > 120:
    print("You can ride.")
```

### Incorrect

```python
if height > 120:
print("You can ride.")
```

This will cause:

```text
IndentationError
```

### Rule

Everything indented under an `if` belongs to that block.

```python
if condition:
    statement1
    statement2
```

---

# Comparison Operators

| Operator | Meaning | Example |
|-----------|---------|---------|
| `>` | Greater Than | `height > 120` |
| `<` | Less Than | `height < 120` |
| `>=` | Greater Than or Equal To | `height >= 120` |
| `<=` | Less Than or Equal To | `height <= 120` |
| `==` | Equal To | `height == 120` |
| `!=` | Not Equal To | `height != 120` |

---

# Greater Than vs Greater Than or Equal To

### Greater Than (`>`)

```python
if height > 120:
```

| Height | Result |
|----------|--------|
| 121 | True |
| 120 | False |

### Greater Than or Equal To (`>=`)

```python
if height >= 120:
```

| Height | Result |
|----------|--------|
| 121 | True |
| 120 | True |

Use `>=` when you want to include the boundary value.

---

# Assignment (=) vs Comparison (==)

## Assignment Operator

Stores a value in a variable.

```python
height = 120
```

Meaning:

> Store 120 in the variable `height`.

---

## Equality Operator

Checks whether two values are equal.

```python
if height == 120:
```

Meaning:

> Is height exactly equal to 120?

Returns:

- True
- False

---

# Equal To Example

```python
height = 120

if height == 120:
    print("Exactly 120 cm")
else:
    print("Not 120 cm")
```

Output:

```text
Exactly 120 cm
```

---

# Not Equal To Example

```python
height = 121

if height != 120:
    print("Height is not 120")
else:
    print("Height is 120")
```

Output:

```text
Height is not 120
```

---

# Flow of an If/Else Statement

```text
Start
  |
Check Condition
  |
True? ------ No -----> Else Block
  |
 Yes
  |
If Block
  |
 End
```

---

# Key Takeaways

- `if` checks a condition.
- `else` executes when the condition is False.
- Conditions evaluate to either **True** or **False**.
- Indentation is mandatory in Python.
- `>` means greater than.
- `>=` means greater than or equal to.
- `==` checks equality.
- `=` assigns a value.
- `!=` means not equal to.

## Basic Template

```python
if condition:
    do_this
else:
    do_that
```

This is the foundation of decision-making in Python and is used in almost every real-world program.

# Python Fundamentals – Control Flow & Decision Making

Based on the topics:

- Control Flow with if / else and Conditional Operators
- Modulo Operator
- Nested if Statements and elif Statements
- Multiple if Statements in Succession
- Logical Operators
- Treasure Island Project

---

# 1. Control Flow

## What is Control Flow?

Control flow determines the order in which your program executes statements.

Until now, Python executed code from top to bottom.

```python
print("Step 1")
print("Step 2")
print("Step 3")
```

Output:

```text
Step 1
Step 2
Step 3
```

Sometimes we want Python to make decisions.

Example:

```python
if it is raining:
    take umbrella
else:
    don't take umbrella
```

This is called **Control Flow**.

---

# 2. Boolean Data Type

A Boolean can only have two values:

```python
True
False
```

Examples:

```python
is_raining = True
is_logged_in = False
```

---

# 3. Comparison Operators

Comparison operators compare values and return either:

```python
True
```

or

```python
False
```

| Operator | Meaning |
|-----------|---------|
| == | Equal To |
| != | Not Equal To |
| > | Greater Than |
| < | Less Than |
| >= | Greater Than or Equal To |
| <= | Less Than or Equal To |

---

### Example

```python
5 > 3
```

Result:

```python
True
```

---

```python
5 < 3
```

Result:

```python
False
```

---

```python
5 == 5
```

Result:

```python
True
```

---

# 4. if Statement

## Syntax

```python
if condition:
    code
```

---

### Example

```python
age = 18

if age >= 18:
    print("You can vote")
```

Output:

```text
You can vote
```

---

## Important: Indentation

Python uses indentation to identify code blocks.

Correct:

```python
if age >= 18:
    print("You can vote")
```

Wrong:

```python
if age >= 18:
print("You can vote")
```

Produces:

```python
IndentationError
```

---

# 5. if - else Statement

## Syntax

```python
if condition:
    code
else:
    code
```

---

### Example

```python
age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Output:

```text
Minor
```

---

# 6. elif Statement

Used when there are multiple conditions.

---

## Syntax

```python
if condition1:
    code
elif condition2:
    code
else:
    code
```

---

### Example

```python
score = 75

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("Fail")
```

Output:

```text
C
```

---

# 7. Modulo Operator (%)

## What is Modulo?

Returns the remainder after division.

---

### Syntax

```python
a % b
```

---

### Example

```python
10 % 2
```

Result:

```python
0
```

Because:

```text
10 ÷ 2 = 5 remainder 0
```

---

### Example

```python
11 % 2
```

Result:

```python
1
```

Because:

```text
11 ÷ 2 = 5 remainder 1
```

---

# 8. Checking Even and Odd Numbers

### Example

```python
number = 8

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

Output:

```text
Even
```

---

# 9. Nested if Statements

An if statement inside another if statement.

---

## Syntax

```python
if condition1:
    if condition2:
        code
```

---

### Example

```python
age = 20
has_ticket = True

if age >= 18:
    if has_ticket:
        print("Enter")
```

Output:

```text
Enter
```

---

## Visualization

```text
Age >= 18?
│
├── No → Stop
│
└── Yes
      │
      ├── Has Ticket?
      │
      ├── No → Stop
      │
      └── Yes → Enter
```

---

# 10. Multiple if Statements

Unlike if-elif-else, every condition is checked.

---

### Example

```python
score = 95

if score >= 50:
    print("Pass")

if score >= 80:
    print("Good")

if score >= 90:
    print("Excellent")
```

Output:

```text
Pass
Good
Excellent
```

All three conditions are evaluated.

---

# 11. Difference Between elif and Multiple if

## Using elif

```python
score = 95

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
```

Output:

```text
A
```

Only the first matching block runs.

---

## Using Multiple if

```python
score = 95

if score >= 80:
    print("Good")

if score >= 90:
    print("Excellent")
```

Output:

```text
Good
Excellent
```

Both run.

---

# 12. Logical Operators

Used to combine conditions.

---

## AND

Both conditions must be true.

```python
and
```

### Example

```python
age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("Enter")
```

Output:

```text
Enter
```

---

## OR

At least one condition must be true.

```python
or
```

### Example

```python
is_admin = False
is_owner = True

if is_admin or is_owner:
    print("Access Granted")
```

Output:

```text
Access Granted
```

---

## NOT

Reverses a Boolean value.

---

### Example

```python
logged_in = False

if not logged_in:
    print("Login Required")
```

Output:

```text
Login Required
```

---

# 13. Truth Table

## AND

| A | B | Result |
|---|---|--------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

---

## OR

| A | B | Result |
|---|---|--------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

---

## NOT

| A | Result |
|---|--------|
| True | False |
| False | True |

---

# 14. Combining Conditions

### Example

```python
age = 25
country = "India"

if age >= 18 and country == "India":
    print("Eligible")
```

Output:

```text
Eligible
```

---

# 15. String Comparison

Strings can be compared using `==`.

---

### Example

```python
choice = "left"

if choice == "left":
    print("Move Left")
```

Output:

```text
Move Left
```

---

# 16. Treasure Island Concepts

The Treasure Island project combines:

- input()
- print()
- Variables
- Strings
- if
- elif
- else
- Nested if statements
- Logical operators

---

### Example

```python
direction = input("Left or Right? ")

if direction == "left":
    print("You survived")
else:
    print("Game Over")
```

---

# Common Beginner Mistakes

## Using = instead of ==

Wrong:

```python
if age = 18:
```

Correct:

```python
if age == 18:
```

---

## Forgetting Colon

Wrong:

```python
if age > 18
```

Correct:

```python
if age > 18:
```

---

## Wrong Indentation

Wrong:

```python
if age > 18:
print("Adult")
```

Correct:

```python
if age > 18:
    print("Adult")
```

---

# New Concepts Learned

| Concept | Example |
|----------|----------|
| Boolean | `True`, `False` |
| Comparison Operators | `==`, `!=`, `>`, `<` |
| if Statement | `if condition:` |
| else Statement | `else:` |
| elif Statement | `elif condition:` |
| Modulo Operator | `10 % 2` |
| Even/Odd Check | `number % 2 == 0` |
| Nested if | `if inside if` |
| Multiple if Statements | Independent checks |
| Logical AND | `and` |
| Logical OR | `or` |
| Logical NOT | `not` |
| String Comparison | `choice == "left"` |
| Indentation | Defines code blocks |

---

# One-Line Summary

This section introduces **decision-making in Python** using **Booleans, comparison operators, if/elif/else statements, modulo calculations, nested conditions, multiple condition checks, and logical operators**, enabling programs to react differently based on user input and data.