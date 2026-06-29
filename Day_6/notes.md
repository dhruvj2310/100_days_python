# Python Fundamentals – Functions, While Loops, and Indentation

This guide covers three fundamental Python concepts:

- Functions
- While Loops
- Indentation

These concepts are essential for writing reusable, organized, and efficient Python programs.

---

# Part 1: Functions

---

# 1. What is a Function?

A **function** is a reusable block of code that performs a specific task.

Instead of writing the same code multiple times, you write it once inside a function and call it whenever needed.

Think of a function as a **machine**.

```
Input
   │
   ▼
Function
   │
   ▼
Output
```

---

# 2. Why Use Functions?

Without functions:

```python
print("Hello")
print("Welcome")

print("Hello")
print("Welcome")

print("Hello")
print("Welcome")
```

With functions:

```python
def greet():
    print("Hello")
    print("Welcome")

greet()
greet()
greet()
```

The code becomes shorter and easier to maintain.

---

# 3. Defining a Function

## Syntax

```python
def function_name():
    code
```

Example

```python
def greet():
    print("Hello")
```

Nothing happens yet because the function is only defined.

---

# 4. Calling a Function

To execute a function:

```python
greet()
```

Example

```python
def greet():
    print("Hello")

greet()
```

Output

```
Hello
```

---

# 5. Function Execution Flow

```python
def greet():
    print("Hello")

print("Start")

greet()

print("End")
```

Execution:

```
Start

↓

Function called

↓

Hello

↓

End
```

Output

```
Start
Hello
End
```

---

# 6. Function Parameters

A parameter is a variable that receives data.

Example

```python
def greet(name):
    print(f"Hello {name}")
```

Calling:

```python
greet("Alice")
```

Output

```
Hello Alice
```

---

# 7. Multiple Parameters

```python
def add(a, b):
    print(a + b)
```

Call

```python
add(5, 3)
```

Output

```
8
```

---

# 8. Arguments

The actual values passed to a function are called **arguments**.

```python
def greet(name):
    print(name)

greet("Dhruv")
```

Parameter

```
name
```

Argument

```
"Dhruv"
```

---

# 9. Return Statement

Functions can send data back using `return`.

Example

```python
def square(number):
    return number * number
```

Calling

```python
result = square(5)

print(result)
```

Output

```
25
```

---

# 10. Difference Between print() and return

Using print

```python
def add(a, b):
    print(a + b)
```

Displays the answer.

---

Using return

```python
def add(a, b):
    return a + b
```

Stores the answer for later use.

---

# 11. Function Scope

Variables created inside a function are local.

```python
def demo():
    x = 10

print(x)
```

Produces

```
NameError
```

because `x` exists only inside the function.

---

# Part 2: While Loops

---

# 12. What is a While Loop?

A while loop repeats code **as long as a condition is True**.

Unlike a `for` loop, you don't know in advance how many times it will run.

---

# 13. Syntax

```python
while condition:
    code
```

---

# 14. Basic Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output

```
1
2
3
4
5
```

---

# 15. How While Loops Work

```
Condition

↓

True?

↓

Run Code

↓

Go Back

↓

Check Again

↓

False?

↓

Exit Loop
```

---

# 16. Updating the Condition

Always update the variable controlling the loop.

Correct

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

Wrong

```python
count = 1

while count <= 5:
    print(count)
```

This creates an **infinite loop**.

---

# 17. Infinite Loop

A loop that never ends.

Example

```python
while True:
    print("Hello")
```

Output

```
Hello
Hello
Hello
...
```

---

# 18. User-Controlled While Loop

Example

```python
answer = ""

while answer != "quit":
    answer = input("Enter quit to stop: ")
```

The loop continues until the user types:

```
quit
```

---

# 19. Using break

`break` immediately exits a loop.

Example

```python
while True:
    word = input("Type exit: ")

    if word == "exit":
        break
```

---

# 20. Using continue

`continue` skips the current iteration.

Example

```python
for number in range(5):

    if number == 2:
        continue

    print(number)
```

Output

```
0
1
3
4
```

---

# Part 3: Indentation

---

# 21. What is Indentation?

Indentation is the space at the beginning of a line.

Python uses indentation to define blocks of code.

Most languages use braces `{}`.

Python uses indentation instead.

---

# 22. Example

```python
if True:
    print("Hello")
```

Everything indented belongs to the `if` block.

---

# 23. Indentation in Functions

```python
def greet():
    print("Hello")
    print("Welcome")
```

Both print statements belong to the function.

---

# 24. Indentation in Loops

```python
for i in range(3):
    print(i)

print("Done")
```

Only the first print belongs to the loop.

---

# 25. Nested Indentation

Example

```python
for i in range(2):

    if i == 1:

        print("One")
```

Visualization

```
for
│
├── if
│   └── print()
```

---

# 26. Indentation Errors

Wrong

```python
if True:
print("Hello")
```

Produces

```
IndentationError
```

---

Correct

```python
if True:
    print("Hello")
```

---

# 27. Python Style Guide

Python recommends **4 spaces** for each indentation level.

Example

```python
def greet():
    print("Hello")
```

Avoid mixing tabs and spaces.

---

# Common Beginner Mistakes

## Forgetting to Call a Function

```python
def greet():
    print("Hello")
```

Nothing happens because the function was never called.

Correct

```python
greet()
```

---

## Infinite While Loop

Wrong

```python
count = 1

while count <= 5:
    print(count)
```

The value of `count` never changes.

---

## Forgetting Colon

Wrong

```python
while True
```

Correct

```python
while True:
```

---

## Wrong Indentation

Wrong

```python
def greet():
print("Hello")
```

Correct

```python
def greet():
    print("Hello")
```

---

# Comparison: for Loop vs while Loop

| Feature | for Loop | while Loop |
|----------|----------|------------|
| Number of iterations | Usually known | Usually unknown |
| Uses | Lists, strings, ranges | Conditions, user input |
| Stops when | Sequence ends | Condition becomes False |

---

# New Concepts Learned

| Concept | Example |
|----------|----------|
| Function | `def greet():` |
| Function Call | `greet()` |
| Parameters | `def add(a, b):` |
| Arguments | `add(5, 3)` |
| Return Statement | `return value` |
| Local Scope | Variables inside functions |
| While Loop | `while condition:` |
| Infinite Loop | `while True:` |
| `break` | Exit a loop |
| `continue` | Skip current iteration |
| Indentation | Defines code blocks |
| Nested Indentation | Loops inside conditions |

---

# One-Line Summary

Functions allow you to **organize and reuse code**, while loops enable programs to **repeat actions until a condition changes**, and indentation defines the **structure and hierarchy** of Python code, making it readable and enforcing block-based execution.