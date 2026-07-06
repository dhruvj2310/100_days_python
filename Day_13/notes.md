# Python Fundamentals – Debugging

> This guide covers the essential concepts of **debugging Python programs**. Debugging is the process of finding, understanding, and fixing errors (bugs) in your code.

---

# Topics Covered

- What is Debugging?
- Types of Errors
- Describing a Problem
- Reproducing a Bug
- Code Evaluation
- Reading Error Messages
- Watching for Red Underlines
- Debugging with `print()`
- Using a Debugger
- Common Debugging Techniques
- Best Practices

---

# 1. What is Debugging?

A **bug** is an error or flaw in a program that causes it to behave unexpectedly.

**Debugging** is the process of:

1. Finding the bug.
2. Understanding why it happened.
3. Fixing it.
4. Testing that the fix works.

---

## Example

```python
age = int(input("Age: "))

print(age + " years")
```

Error

```
TypeError
```

Debugging means finding why this happened and correcting it.

Correct

```python
print(f"{age} years")
```

---

# 2. Types of Errors

Python errors generally fall into three categories.

---

## Syntax Errors

The program cannot even start.

Example

```python
if age > 18
    print("Adult")
```

Error

```
SyntaxError
```

Reason

Missing colon.

---

## Runtime Errors (Exceptions)

The program starts but crashes while running.

Example

```python
10 / 0
```

Error

```
ZeroDivisionError
```

---

## Logical Errors

The program runs successfully but gives the wrong result.

Example

```python
radius = 5

area = 2 * 3.14 * radius
```

The code runs.

But this calculates **circumference**, not **area**.

---

# 3. Describing a Problem

Before fixing a bug, clearly describe it.

Instead of saying

> "My code doesn't work."

Say

> "When I enter 25, the program crashes with a TypeError."

A good bug report includes:

- What you expected
- What actually happened
- Steps to reproduce it
- Error message

---

# 4. Reproducing a Bug

A bug should be reproducible.

Example

Program

```python
number = int(input())
```

Bug occurs when entering

```
hello
```

Now you can reproduce it every time.

Without reproduction, debugging becomes difficult.

---

# 5. Code Evaluation

Read the code like Python does.

Example

```python
x = 5

y = x + 2

print(y)
```

Evaluate step by step.

```
x = 5

↓

y = 7

↓

Print 7
```

Never assume.

Always trace execution.

---

# 6. Reading Error Messages

Python provides valuable information.

Example

```
Traceback (most recent call last):

File "main.py", line 5

TypeError:
```

Important parts:

- File name
- Line number
- Error type
- Error message

Always read from the bottom upward.

---

# 7. Watching for Red Underlines

Modern editors (VS Code, PyCharm) underline problems.

Examples

- Missing imports
- Misspelled variable names
- Missing parentheses
- Wrong indentation

Example

```python
pritn("Hello")
```

Editor immediately underlines

```
pritn
```

before running the program.

Fix warnings early.

---

# 8. Debugging with print()

One of the oldest and most effective debugging techniques.

Print variable values to understand what's happening.

Example

```python
x = 10

print(x)

y = x + 5

print(y)
```

Output

```
10

15
```

---

## Printing Inside Loops

Example

```python
for number in range(5):

    print(number)
```

Output

```
0
1
2
3
4
```

Useful to verify loop execution.

---

## Printing Variables

Example

```python
print("Age =", age)
```

Instead of

```python
print(age)
```

This provides context.

---

# 9. Tracing Program Flow

Example

```python
print("Program Started")

print("Reading Input")

print("Calculating")

print("Finished")
```

Output

```
Program Started

Reading Input

Calculating

Finished
```

Now you know exactly where execution stopped.

---

# 10. Using a Debugger

A debugger allows you to inspect a program **while it is running**.

Instead of adding many `print()` statements,

you can pause execution.

---

## Common Debugger Features

### Breakpoints

A breakpoint pauses execution.

```
Program

↓

Breakpoint

↓

Paused
```

Now you can inspect variables.

---

### Step Over

Runs the next line.

```
Line 1

↓

Line 2

↓

Line 3
```

---

### Step Into

If the next line calls a function,

the debugger enters the function.

Example

```python
result = add(5, 3)
```

Step Into

↓

```
def add(a, b)
```

---

### Step Out

Finish the current function and return to the caller.

---

### Continue

Resume execution until the next breakpoint.

---

# 11. Inspecting Variables

Example

```python
name = "Alice"

age = 25
```

The debugger lets you inspect

```
name

↓

Alice

age

↓

25
```

without printing them.

---

# 12. Debugging Checklist

When something is wrong:

✔ Does the program start?

✔ Is the correct function called?

✔ Are variables holding expected values?

✔ Does the loop execute?

✔ Are conditions correct?

✔ Is the returned value correct?

---

# 13. Rubber Duck Debugging

Explain your code aloud,

even to an object like a rubber duck.

Example

> "First this variable stores the input..."

Very often you'll discover the mistake while explaining.

---

# 14. Binary Search Debugging

When debugging a long program,

don't inspect every line.

Split the program into sections.

Example

```
Program

│

├── Input

├── Processing

└── Output
```

Determine which section contains the bug.

Then narrow it further.

---

# 15. Common Debugging Strategy

```
Observe Problem

↓

Reproduce Bug

↓

Read Error Message

↓

Find Error Line

↓

Understand Why

↓

Fix

↓

Test Again
```

---

# 16. Defensive Programming

Prevent bugs before they happen.

Example

```python
age = input()

if age.isdigit():
    age = int(age)
```

Instead of assuming the user enters valid input.

---

# 17. Common Python Errors

| Error | Cause |
|--------|------|
| SyntaxError | Invalid syntax |
| NameError | Variable doesn't exist |
| TypeError | Wrong data type |
| ValueError | Invalid value |
| IndexError | Invalid list index |
| KeyError | Dictionary key missing |
| ZeroDivisionError | Division by zero |
| IndentationError | Incorrect indentation |
| AttributeError | Method doesn't exist |
| ModuleNotFoundError | Missing module |

---

# 18. Best Debugging Practices

- Read the entire error message.
- Fix the first error before looking at others.
- Change one thing at a time.
- Test after every change.
- Don't guess—verify.
- Use meaningful variable names.
- Keep functions small.
- Write code incrementally.

---

# Common Beginner Mistakes

## Ignoring the Error Message

Wrong approach

> "Python is broken."

Correct approach

Read the error carefully.

---

## Changing Too Many Things

Changing ten lines at once makes it hard to know what fixed the bug.

Instead

Fix one issue.

Test.

Repeat.

---

## Not Reproducing the Bug

If you cannot consistently reproduce the problem,

it's difficult to verify the fix.

---

## Removing `print()` Statements Too Early

During debugging,

`print()` is your friend.

Remove temporary debugging prints only after the issue is resolved.

---

# Debugging Workflow

```
Write Code

↓

Run Program

↓

Error?

↓

Yes

↓

Read Error

↓

Locate Bug

↓

Fix Code

↓

Run Again

↓

Passes?

↓

Yes

↓

Done
```

---

# New Concepts Learned

| Concept | Description |
|----------|-------------|
| Bug | An error in a program |
| Debugging | Finding and fixing bugs |
| Syntax Error | Invalid Python syntax |
| Runtime Error | Error during execution |
| Logical Error | Incorrect program logic |
| Reproducing a Bug | Triggering the same issue consistently |
| Code Evaluation | Tracing execution step by step |
| Traceback | Python's error report |
| Red Underlines | IDE warnings before execution |
| `print()` Debugging | Display variable values and execution flow |
| Breakpoint | Pause program execution |
| Step Over | Execute the next line |
| Step Into | Enter a function call |
| Step Out | Exit the current function |
| Continue | Resume execution |
| Variable Inspection | View variable values during execution |
| Rubber Duck Debugging | Explain the code aloud |
| Defensive Programming | Prevent invalid input and errors |

---

# One-Line Summary

Debugging is the systematic process of **identifying, reproducing, understanding, and fixing bugs** using tools such as **error messages, print statements, debuggers, and careful code evaluation**, enabling developers to write reliable, maintainable, and correct Python programs.