# Python Fundamentals Explained Using the Band Name Generator

## Complete Code

```python
print("Welcome to Band Name generator!")

city = input("\nWhich city do you live in?: ")
pet = input("What is the name of your pet?: ")

bandname = f"{city} {pet}"

print(f"\nYour band name is {bandname}")
```

---

# 1. Comments

```python
# Starting with the basics - some variables, f strings and input & print statements #
```

### What is a Comment?

A comment is text written for humans to read.

Python ignores comments when running the program.

### Purpose

- Explain code
- Add notes
- Improve readability

### Syntax

```python
# This is a comment
```

### Example

```python
# Ask user for their name
name = input("Enter your name: ")
```

---

# 2. print() Function

```python
print("Welcome to Band Name generator!")
```

### What is print()?

The `print()` function displays output on the screen.

### Syntax

```python
print(value)
```

### Examples

```python
print("Hello")
print(10)
print(True)
```

### Output

```
Hello
10
True
```

---

# 3. Strings

```python
"Welcome to Band Name generator!"
```

### What is a String?

A string is a collection of characters enclosed in quotes.

### Types of Quotes

```python
"Hello"
'Hello'
```

Both are valid strings.

### Examples

```python
name = "Dhruv"
city = "Mumbai"
```

---

# 4. Variables

```python
city = input(...)
pet = input(...)
```

### What is a Variable?

A variable stores data in memory.

Think of it as a labeled box.

### Syntax

```python
variable_name = value
```

### Example

```python
name = "Dhruv"
age = 24
```

### Visualization

```
city  ──► "Mumbai"
pet   ──► "Bruno"
```

---

# 5. Assignment Operator (=)

```python
city = input(...)
```

### What does = mean?

In Python, `=` means:

> Store the value on the right into the variable on the left.

### Example

```python
x = 10
```

This means:

```
x ← 10
```

Not:

```
10 = x ❌
```

---

# 6. input() Function

```python
city = input("\nWhich city do you live in?: ")
```

### What is input()?

`input()` allows the user to enter data from the keyboard.

### Syntax

```python
variable = input("Message")
```

### Example

```python
name = input("Enter your name: ")
```

User enters:

```
Dhruv
```

Stored as:

```python
name = "Dhruv"
```

### Important

`input()` always returns a string.

Example:

```python
age = input("Enter age: ")
```

If user types:

```
25
```

Python stores:

```python
age = "25"
```

not

```python
age = 25
```

---

# 7. Escape Characters

```python
"\nWhich city do you live in?: "
```

### What is \n?

`\n` means:

**New Line**

### Example

```python
print("Hello\nWorld")
```

### Output

```
Hello
World
```

### Common Escape Characters

| Escape Character | Meaning |
|-----------------|----------|
| \n | New line |
| \t | Tab space |
| \' | Single quote |
| \" | Double quote |
| \\ | Backslash |

Example:

```python
print("Name:\tDhruv")
```

Output:

```
Name:   Dhruv
```

---

# 8. User Input Storage

Suppose user enters:

```
City: Mumbai
Pet: Bruno
```

Then:

```python
city = "Mumbai"
pet = "Bruno"
```

Memory:

```
city ─► Mumbai
pet  ─► Bruno
```

---

# 9. f-Strings (Formatted Strings)

```python
bandname = f"{city} {pet}"
```

### What is an f-string?

An f-string lets you insert variables directly inside a string.

### Syntax

```python
f"{variable}"
```

### Example

```python
name = "Dhruv"

message = f"Hello {name}"
```

Result:

```
Hello Dhruv
```

---

# 10. String Interpolation

```python
f"{city} {pet}"
```

### What is String Interpolation?

Replacing placeholders with variable values.

Example:

```python
city = "Mumbai"
pet = "Bruno"

bandname = f"{city} {pet}"
```

Result:

```python
"Mumbai Bruno"
```

---

# 11. Creating New Variables

```python
bandname = f"{city} {pet}"
```

### What's happening?

Python:

1. Reads `city`
2. Reads `pet`
3. Combines them
4. Stores result in `bandname`

Example:

```python
city = "Mumbai"
pet = "Bruno"

bandname = "Mumbai Bruno"
```

---

# 12. String Concatenation

The same thing can be written as:

```python
bandname = city + " " + pet
```

### Example

```python
city = "Mumbai"
pet = "Bruno"
```

Result:

```
Mumbai Bruno
```

### Why f-strings are preferred

Cleaner:

```python
f"{city} {pet}"
```

Instead of:

```python
city + " " + pet
```

---

# 13. Output Using Variables

```python
print(f"\nYour band name is {bandname}")
```

### Process

Suppose:

```python
bandname = "Mumbai Bruno"
```

Python creates:

```python
"\nYour band name is Mumbai Bruno"
```

Then prints it.

### Output

```
Your band name is Mumbai Bruno
```

---

# 14. Program Execution Flow

Python runs code from top to bottom.

### Step 1

```python
print("Welcome to Band Name generator!")
```

Output:

```
Welcome to Band Name generator!
```

### Step 2

```python
city = input(...)
```

User enters:

```
Mumbai
```

### Step 3

```python
pet = input(...)
```

User enters:

```
Bruno
```

### Step 4

```python
bandname = f"{city} {pet}"
```

Creates:

```
Mumbai Bruno
```

### Step 5

```python
print(...)
```

Output:

```
Your band name is Mumbai Bruno
```

---

# 15. Data Flow Diagram

```
User Input
    │
    ▼
city = "Mumbai"

User Input
    │
    ▼
pet = "Bruno"

    │
    ▼

bandname = "Mumbai Bruno"

    │
    ▼

print()

    │
    ▼

Your band name is Mumbai Bruno
```

---

# Key Concepts Learned

| Concept | Example |
|----------|----------|
| Comment | `# This is a comment` |
| String | `"Hello"` |
| Variable | `name = "Dhruv"` |
| Assignment Operator | `=` |
| print() | `print("Hello")` |
| input() | `input("Enter name: ")` |
| Escape Character | `\n` |
| f-string | `f"Hello {name}"` |
| String Concatenation | `"Hello " + name` |
| Program Flow | Top to Bottom Execution |

---

# Beginner Practice Exercises

### Exercise 1

```python
name = input("Enter your name: ")
print(f"Hello {name}")
```

### Exercise 2

```python
food = input("Favorite food: ")
print(f"I love {food}")
```

### Exercise 3

```python
school = input("School Name: ")
friend = input("Best Friend: ")

print(f"{school} {friend}")
```

### Exercise 4

Create a program that asks:

- First Name
- Last Name

And prints:

```
Your full name is John Smith
```

---

# One-Line Summary

This program teaches the most fundamental Python concepts: **comments, strings, variables, assignment, input(), print(), escape characters, f-strings, string concatenation, and top-to-bottom program execution.**