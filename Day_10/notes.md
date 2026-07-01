# Python Fundamentals – Calculator Project

> This guide covers **only the new Python concepts** introduced in the Calculator project. It assumes you already understand:
>
> - Variables
> - Data Types (`int`, `str`, `float`, `bool`)
> - Functions
> - Parameters & Arguments
> - Return Statements
> - Conditional Statements (`if`, `elif`, `else`)
> - Input & Output
> - Arithmetic Operators

---

# New Concepts Covered

- Functional Decomposition
- Function Reusability
- Type Hints
- Operation Dispatch
- Storing Function Results
- Division Returning Float
- Code Reusability
- Separation of Logic and User Interface

---

# 1. Functional Decomposition

## What is Functional Decomposition?

Breaking a large problem into multiple smaller functions.

Instead of writing everything inside one block,

you divide the program into small tasks.

Example

```python
def add():
```

handles addition.

```python
def subtract():
```

handles subtraction.

```python
def multiply():
```

handles multiplication.

```python
def divide():
```

handles division.

Each function has only **one responsibility**.

---

# 2. Function Reusability

One function can be used many times.

Example

```python
result = add(5, 3)
```

Later

```python
result = add(100, 200)
```

The same function works for different values.

This is called **code reuse**.

---

# 3. Type Hints

Your functions use

```python
def add(a: int, b: int):
```

The `: int` is called a **type hint**.

It tells readers (and tools) that

```python
a
```

and

```python
b
```

should be integers.

Example

```python
def greet(name: str):
```

or

```python
def calculate(price: float):
```

Type hints improve readability but do **not** enforce types automatically.

---

# 4. Returning Values Instead of Printing

Inside every function

```python
return output
```

returns the calculated value.

Example

```python
def add(a, b):
    return a + b
```

Calling

```python
answer = add(5, 7)
```

stores

```
12
```

inside

```python
answer
```

---

# 5. Storing Function Results

Instead of

```python
print(add(a, b))
```

your program does

```python
output = add(a, b)
```

This allows the value to be reused.

Example

```python
output = multiply(5, 10)

print(output)

print(output * 2)
```

Output

```
50

100
```

---

# 6. Operation Dispatch

The program chooses which function to execute based on user input.

Example

```
User

↓

+

↓

Call add()

↓

Return Result
```

Another example

```
User

↓

*

↓

Call multiply()

↓

Return Result
```

This pattern is called **operation dispatch** or **decision-based function calling**.

---

# 7. Function Call Flow

Suppose the user enters

```
10

+

20
```

Execution

```
Read Input

↓

Operator = +

↓

Call add(10,20)

↓

Return 30

↓

Store in output

↓

Print Result
```

---

# 8. Separation of Logic and User Interface

Your program separates

### User Interface

```python
print()

input()
```

from

### Business Logic

```python
def add()

def subtract()

def multiply()

def divide()
```

This makes programs easier to modify.

If you later build a GUI or website,

only the interface changes.

The calculation functions remain the same.

---

# 9. Reusing Variables

Notice

```python
output
```

is used multiple times.

Example

```python
output = add(a, b)
```

Later

```python
output = subtract(a, b)
```

The old value is replaced.

Variables can store different values during program execution.

---

# 10. Division Returns a Float

Your divide function

```python
def divide(a, b):
    return a / b
```

Even when numbers divide evenly,

Python returns a float.

Example

```python
10 / 2
```

Result

```
5.0
```

Not

```
5
```

---

# 11. User Input Drives Program Flow

Your calculator is an example of an **interactive program**.

The user's choice determines what code executes.

Example

```
+

↓

Addition Function

-

↓

Subtraction Function

*

↓

Multiplication Function

/

↓

Division Function
```

---

# 12. Code Duplication

Notice

```python
output = ...
print(...)
```

appears several times.

This is called **code duplication**.

Later you'll learn how to eliminate duplication using loops and dictionaries.

---

# 13. Data Flow

Suppose

```
a = 8

o = *

b = 5
```

Flow

```
Input

↓

a = 8

↓

Operator = *

↓

b = 5

↓

multiply(8,5)

↓

40

↓

output

↓

Print
```

---

# 14. Program Architecture

```
          User Input

               │

               ▼

      Read Numbers & Operator

               │

               ▼

      if / elif Decision

               │

     ┌─────────┼─────────┐

     ▼         ▼         ▼

   add()   subtract() multiply()

               │

               ▼

          return value

               │

               ▼

          Print Result
```

---

# Common Beginner Mistakes

## Forgetting `return`

Wrong

```python
def add(a, b):
    output = a + b
```

Calling

```python
result = add(2,3)
```

Produces

```python
None
```

Correct

```python
return output
```

---

## Forgetting Parentheses

Wrong

```python
output = add
```

Correct

```python
output = add(a, b)
```

---

## Division by Zero

Wrong

```python
divide(10, 0)
```

Produces

```
ZeroDivisionError
```

Always ensure the divisor is not zero.

---

## Invalid Operator

If the user enters

```
%
```

Nothing happens because there is no matching condition.

A better version would include

```python
else:
    print("Invalid operation")
```

---

# Function-Based Programming vs Writing Everything Inline

Without Functions

```python
result = a + b

print(result)
```

Repeated many times.

---

With Functions

```python
def add(a, b):
    return a + b
```

Can be reused anywhere.

---

# New Concepts Learned

| Concept | Example |
|----------|----------|
| Functional Decomposition | One task per function |
| Function Reusability | `add(2,3)` multiple times |
| Type Hints | `a: int` |
| Operation Dispatch | Call function based on operator |
| Store Returned Value | `output = add(a,b)` |
| Separation of Logic & UI | Functions vs `input()` / `print()` |
| Variable Reassignment | `output = ...` |
| Division Returns Float | `10 / 2 = 5.0` |
| Interactive Program Flow | User input determines execution |
| Code Duplication | Repeated `print()` statements |

---

# One-Line Summary

The Calculator project demonstrates **function-based programming**, where each mathematical operation is encapsulated in a reusable function, illustrating concepts such as **functional decomposition, type hints, operation dispatch, return values, and the separation of program logic from user interaction**, making the code modular, reusable, and easier to maintain.