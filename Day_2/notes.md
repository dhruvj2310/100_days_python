# New Python Concepts Learned from the Bill Split Calculator

> This guide covers **only the new concepts introduced in this program**, assuming you already understand:
>
> - Comments
> - Variables
> - Strings
> - print()
> - input()
> - f-strings
> - Escape characters (`\n`)
> - Program execution flow

---

# Complete Code

```python
print("Welcome to bill split calculator!")

## Get information ##
bill_amt = int(input("\nWhat is the bill amount?: "))
tip_pc = int(input("What percent tip you would like to give?: "))
no_of_people = int(input("How many people have contributed to the bill?: "))

## Calculations ##
tip_amt = bill_amt * (tip_pc / 100)
total_bill = bill_amt + tip_amt
split_amt = total_bill / no_of_people

print(f"""
Your total bill is ${total_bill}
including a tip of ${tip_amt}.
Each person has to pay ${split_amt}
""")
```

---

# 1. Type Conversion (Type Casting)

## Concept

```python
int(input(...))
```

This is called **type conversion** or **type casting**.

It converts one data type into another.

---

## Why is it Needed?

Remember:

```python
input()
```

always returns a string.

Example:

```python
age = input("Enter age: ")
```

User enters:

```
25
```

Python stores:

```python
age = "25"
```

which is a string.

---

### Problem

```python
bill = input("Enter bill: ")
tip = bill + 10
```

Error:

```python
TypeError
```

because Python cannot add a string and a number.

---

### Solution

Convert the string to an integer.

```python
bill = int(input("Enter bill: "))
```

Now:

```python
bill = 100
```

instead of

```python
bill = "100"
```

---

## Example

```python
age = int(input("Enter age: "))
```

Input:

```
24
```

Stored as:

```python
24
```

(integer)

---

# 2. Data Types

Your program now uses multiple data types.

---

## String

```python
"Hello"
```

Stores text.

Example:

```python
name = "Dhruv"
```

---

## Integer (int)

```python
100
```

Stores whole numbers.

Examples:

```python
bill_amt = 1000
tip_pc = 10
```

---

## Float

```python
12.5
```

Stores decimal numbers.

Examples:

```python
tip_amt = 125.50
split_amt = 562.75
```

---

## Checking Data Types

```python
print(type(100))
```

Output:

```python
<class 'int'>
```

---

```python
print(type(10.5))
```

Output:

```python
<class 'float'>
```

---

```python
print(type("hello"))
```

Output:

```python
<class 'str'>
```

---

# 3. Mathematical Operators

Your calculator introduces arithmetic operations.

---

## Addition (+)

```python
total_bill = bill_amt + tip_amt
```

Example:

```python
100 + 20
```

Result:

```python
120
```

---

## Subtraction (-)

```python
100 - 20
```

Result:

```python
80
```

---

## Multiplication (*)

```python
tip_amt = bill_amt * (tip_pc / 100)
```

Example:

```python
100 * 10
```

Result:

```python
1000
```

---

## Division (/)

```python
split_amt = total_bill / no_of_people
```

Example:

```python
120 / 4
```

Result:

```python
30.0
```

Notice:

Division returns a float.

---

# 4. Percentage Calculations

---

## Formula

```python
percentage = value × (percent / 100)
```

---

## Example

10% of 500

```python
500 * (10 / 100)
```

Step 1

```python
10 / 100
```

Result:

```python
0.1
```

Step 2

```python
500 * 0.1
```

Result:

```python
50
```

---

## Applied in Program

```python
tip_amt = bill_amt * (tip_pc / 100)
```

If:

```python
bill_amt = 1000
tip_pc = 15
```

Then:

```python
tip_amt = 1000 * (15/100)
```

Result:

```python
150
```

---

# 5. Order of Operations (PEMDAS/BODMAS)

Python follows mathematical precedence rules.

---

## Example

```python
10 + 5 * 2
```

Python calculates:

```python
5 * 2 = 10
```

Then:

```python
10 + 10 = 20
```

Result:

```python
20
```

---

## Using Parentheses

```python
(10 + 5) * 2
```

Result:

```python
30
```

---

## In Your Program

```python
bill_amt * (tip_pc / 100)
```

Python first calculates:

```python
tip_pc / 100
```

Then multiplies.

---

# 6. Float Values

When calculations involve division, Python often returns floats.

---

Example

```python
10 / 2
```

Output:

```python
5.0
```

Not:

```python
5
```

---

Example

```python
1250 / 3
```

Output:

```python
416.6666666666667
```

---

# 7. Multi-Line Strings

New concept in the final print statement.

```python
print(f"""
Your total bill is ${total_bill}
including a tip of ${tip_amt}
Each person has to pay ${split_amt}
""")
```

---

## Triple Quotes

```python
"""
Text
Text
Text
"""
```

allow strings to span multiple lines.

---

### Example

```python
print("""
Hello
World
""")
```

Output

```
Hello
World
```

---

# 8. Multi-Line f-Strings

You can combine:

- Triple Quotes
- f-Strings

---

Example

```python
name = "Dhruv"

print(f"""
Hello {name}
Welcome
""")
```

Output

```
Hello Dhruv
Welcome
```

---

# 9. Real Calculation Flow

Suppose the user enters:

```text
Bill Amount = 1000
Tip % = 10
People = 4
```

---

### Step 1

```python
tip_amt = 1000 * (10/100)
```

Result:

```python
100
```

---

### Step 2

```python
total_bill = 1000 + 100
```

Result:

```python
1100
```

---

### Step 3

```python
split_amt = 1100 / 4
```

Result:

```python
275.0
```

---

### Final Output

```text
Your total bill is $1100
including a tip of $100
Each person has to pay $275.0
```

---

# Common Beginner Mistakes

## Forgetting int()

Wrong:

```python
bill_amt = input("Bill:")
```

Then:

```python
bill_amt + 10
```

Error:

```python
TypeError
```

---

## Dividing by Zero

Wrong:

```python
split_amt = total_bill / 0
```

Error:

```python
ZeroDivisionError
```

---

## Mixing Strings and Numbers

Wrong:

```python
"100" + 50
```

Error:

```python
TypeError
```

Correct:

```python
int("100") + 50
```

Result:

```python
150
```

---

# New Concepts Learned

| Concept | Example |
|----------|----------|
| Type Conversion | `int(input())` |
| Integer Data Type | `100` |
| Float Data Type | `10.5` |
| Addition | `a + b` |
| Subtraction | `a - b` |
| Multiplication | `a * b` |
| Division | `a / b` |
| Percentage Formula | `value * (percent/100)` |
| Operator Precedence | `(10 + 5) * 2` |
| Multi-line Strings | `"""text"""` |
| Multi-line f-Strings | `f"""Hello {name}"""` |

---

# One-Line Summary

This project introduces **numeric data types, type conversion, arithmetic operators, percentage calculations, operator precedence, float values, and multi-line f-strings**, turning user input into a real-world calculator.