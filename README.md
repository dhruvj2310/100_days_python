# 100_days_python
100 days of basics to advanced python projects. A roadmap to becoming a better developer.

# Python Basics - A Quick Handbook

## What is Python?

Python is a **high-level, interpreted, object-oriented, and general-purpose programming language** known for its simple syntax and readability. It is widely used in web development, data analysis, automation, artificial intelligence, machine learning, scripting, and software development.

---

## Why Learn Python?

- Easy to read and write
- Beginner-friendly syntax
- Huge standard library
- Cross-platform (Windows, macOS, Linux)
- Large community support
- Used by companies like Google, Netflix, Meta, Amazon, and OpenAI

---

## Python Program Execution

Python executes code **from top to bottom**.

```python
print("Hello")
print("World")
```

Output:

```
Hello
World
```

---

## Variables

Variables store data in memory.

```python
name = "Dhruv"
age = 24
```

---

## Data Types

```python
int     # Whole numbers
float   # Decimal numbers
str     # Text
bool    # True or False
list    # Ordered collection
tuple   # Immutable collection
set     # Unique values
dict    # Key-value pairs
```

---

## Input and Output

```python
name = input("Enter your name: ")
print(name)
```

---

## Operators

### Arithmetic

```python
+  -  *  /  //  %  **
```

### Comparison

```python
==  !=  >  <  >=  <=
```

### Logical

```python
and
or
not
```

---

## Conditional Statements

```python
if condition:
    ...
elif condition:
    ...
else:
    ...
```

Used for decision making.

---

## Loops

### For Loop

```python
for i in range(5):
    print(i)
```

### While Loop

```python
while condition:
    ...
```

Loops repeat code efficiently.

---

## Functions

Functions group reusable code.

```python
def greet(name):
    return f"Hello {name}"
```

---

## Lists

Ordered, mutable collections.

```python
numbers = [1, 2, 3]
numbers.append(4)
```

---

## Dictionaries

Store data as key-value pairs.

```python
student = {
    "name": "Dhruv",
    "age": 24
}
```

---

## Strings

Strings are sequences of characters.

```python
name.upper()
name.lower()
name.strip()
name.replace()
```

Useful methods:

- `split()`
- `join()`
- `find()`
- `startswith()`
- `endswith()`

---

## Modules

Modules contain reusable Python code.

```python
import random
import math
import datetime
```

Install external packages using:

```bash
pip install package_name
```

---

## Object-Oriented Programming (OOP)

Python supports OOP using:

- Classes
- Objects
- Attributes
- Methods
- Inheritance
- Polymorphism
- Encapsulation
- Abstraction

Example:

```python
class Dog:
    def bark(self):
        print("Woof")
```

---

## Error Handling

Prevent program crashes using:

```python
try:
    ...
except:
    ...
```

Common exceptions:

- ValueError
- TypeError
- IndexError
- KeyError
- ZeroDivisionError

---

## File Handling

```python
with open("file.txt") as file:
    data = file.read()
```

Read and write files safely using the `with` statement.

---

## Common Built-in Functions

```python
print()
input()
len()
type()
range()
sum()
max()
min()
sorted()
enumerate()
zip()
```

---

## Useful Data Structures

| Structure | Use |
|-----------|-----|
| List | Ordered mutable collection |
| Tuple | Ordered immutable collection |
| Set | Unique values |
| Dictionary | Fast key-value lookup |

---

## Python Naming Conventions

- Variables: `snake_case`
- Functions: `snake_case`
- Classes: `PascalCase`
- Constants: `UPPER_CASE`

Example:

```python
user_name
calculate_total()
BankAccount
MAX_SIZE
```

---

## Indentation

Python uses **indentation** to define code blocks.

```python
if age >= 18:
    print("Adult")
```

Incorrect indentation results in an `IndentationError`.

---

## Comments

Single-line:

```python
# This is a comment
```

Multi-line:

```python
"""
Documentation
"""
```

---

## Important Python Concepts

- Variables store references to objects.
- Everything in Python is an object.
- Functions are first-class objects.
- Lists are mutable; tuples are immutable.
- Dictionaries provide fast key-based lookups.
- Strings are immutable.
- Python uses dynamic typing.
- Code is interpreted at runtime.
- Readability is a core design principle ("Readability counts" – The Zen of Python).

---

## Good Programming Practices

- Use meaningful variable names.
- Keep functions short and focused.
- Avoid repeating code (DRY principle).
- Write comments only when necessary.
- Handle exceptions gracefully.
- Test your code frequently.
- Follow PEP 8 style guidelines.
- Break large problems into smaller functions.

---

## Where Python is Used

- Web Development (Django, Flask, FastAPI)
- Data Analysis (Pandas, NumPy)
- Machine Learning (Scikit-learn)
- Deep Learning (TensorFlow, PyTorch)
- Artificial Intelligence
- Automation & Scripting
- Web Scraping
- Cybersecurity
- Desktop Applications
- APIs & Backend Development
- Data Engineering
- Cloud Computing

---

## Python Philosophy

> "Simple is better than complex."

Python emphasizes **clarity, simplicity, readability, and developer productivity**, making it one of the most popular programming languages for beginners and professionals alike.