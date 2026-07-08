# Python Fundamentals – Object-Oriented Programming (OOP)

> This chapter covers the fundamentals taught in:
>
> - Why do we need OOP and how does it work?
> - Classes and Objects
> - Constructing Objects
> - Attributes
> - Methods
> - Installing Python Packages
> - Using PyPI
> - Modifying Object Attributes
> - Calling Object Methods

---

# Topics Covered

- What is OOP?
- Why OOP Exists
- Procedural Programming vs OOP
- Classes
- Objects
- Creating Objects
- Constructors
- Attributes
- Methods
- Object State
- Modifying Attributes
- Calling Methods
- Python Packages
- PyPI
- Installing Packages using pip

---

# 1. What is Object-Oriented Programming (OOP)?

Object-Oriented Programming (OOP) is a programming paradigm where software is built using **objects**.

An object combines:

- **Data (Attributes)**
- **Behavior (Methods)**

Instead of thinking about functions first,

you think about **things**.

---

## Real World Example

Think about a Dog.

A dog has

### Attributes

```
Name

Breed

Age

Weight
```

### Behaviors

```
Bark()

Eat()

Sleep()

Run()
```

A Dog object combines both.

---

# 2. Why Do We Need OOP?

Imagine creating a game.

Without OOP

```python
player_name = "Alex"

player_health = 100

player_attack = 25

enemy_name = "Goblin"

enemy_health = 50
```

Now imagine having

- 100 players
- 500 enemies

You would need thousands of variables.

---

With OOP

```python
player1 = Player()

player2 = Player()

enemy1 = Enemy()

enemy2 = Enemy()
```

Each object stores its own data.

Much easier to manage.

---

# 3. Procedural Programming vs OOP

## Procedural Programming

Everything is functions.

```
deposit()

withdraw()

transfer()

calculate_interest()
```

Data is passed between functions.

---

## Object-Oriented Programming

Everything revolves around objects.

```
BankAccount

↓

balance

account_number

deposit()

withdraw()

transfer()
```

Everything related to a bank account stays together.

---

# 4. What is a Class?

A class is a **blueprint**.

It describes how an object should be built.

Example

```python
class Dog:
    pass
```

This creates a blueprint.

No dog exists yet.

---

## Blueprint Analogy

```
Blueprint

↓

House 1

House 2

House 3
```

The blueprint isn't a house.

It only describes one.

---

# 5. What is an Object?

An object is an **instance of a class**.

Example

```python
class Dog:
    pass

dog1 = Dog()

dog2 = Dog()
```

Now

```
dog1

dog2
```

are two different objects.

---

# 6. Creating Objects

Syntax

```python
object_name = ClassName()
```

Example

```python
class Car:
    pass

tesla = Car()

bmw = Car()
```

Python allocates memory for each object.

---

# 7. Constructors (`__init__`)

When an object is created,

Python automatically calls

```python
__init__()
```

This is called the **constructor**.

---

Example

```python
class Dog:

    def __init__(self):
        print("Dog Created")
```

Creating

```python
dog = Dog()
```

Output

```
Dog Created
```

---

# 8. Why Use Constructors?

Without a constructor

every object starts empty.

With a constructor

objects receive initial values.

Example

```python
class Dog:

    def __init__(self, name):

        self.name = name
```

Creating

```python
dog = Dog("Bruno")
```

Automatically stores

```
Bruno
```

inside the object.

---

# 9. Understanding `self`

One of the most important concepts in Python.

`self`

represents **the current object**.

Example

```python
class Dog:

    def __init__(self, name):

        self.name = name
```

Suppose

```python
dog1 = Dog("Bruno")
```

Python internally does

```
self

↓

dog1
```

---

If

```python
dog2 = Dog("Rocky")
```

Then

```
self

↓

dog2
```

`self` always refers to the object calling the method.

---

# 10. Attributes

Attributes are variables stored inside an object.

Example

```python
class Dog:

    def __init__(self, name, age):

        self.name = name

        self.age = age
```

Object

```
Dog

↓

Name = Bruno

Age = 4
```

---

# 11. Accessing Attributes

Syntax

```python
object.attribute
```

Example

```python
print(dog.name)

print(dog.age)
```

Output

```
Bruno

4
```

---

# 12. Modifying Attributes

Attributes can change.

Example

```python
dog.age = 5
```

Old value

```
4
```

New value

```
5
```

---

# 13. Methods

Methods are functions that belong to a class.

Example

```python
class Dog:

    def bark(self):

        print("Woof!")
```

Calling

```python
dog.bark()
```

Output

```
Woof!
```

---

# 14. Calling Methods

Syntax

```python
object.method()
```

Example

```python
dog.bark()
```

Python internally passes

```
self

↓

dog
```

---

# 15. Attributes vs Methods

| Attributes | Methods |
|------------|----------|
| Data | Actions |
| Variables | Functions |
| `name` | `bark()` |
| `age` | `sleep()` |

---

# 16. Object State

Every object stores its own data.

Example

```python
dog1 = Dog("Bruno")

dog2 = Dog("Rocky")
```

Memory

```
dog1

↓

Name = Bruno

dog2

↓

Name = Rocky
```

Changing one doesn't affect the other.

---

# 17. Everything in Python is an Object

These are objects

```python
5
```

```python
"Hello"
```

```python
[]
```

```python
{}
```

Even functions are objects.

---

# 18. Packages

A **package** is a collection of Python modules.

Example

```
NumPy

Pandas

Requests

Flask
```

Packages save developers from writing everything from scratch.

---

# 19. What is PyPI?

PyPI stands for

**Python Package Index**

It is the official repository for Python packages.

Think of it as

```
App Store

↓

For Python Libraries
```

Website

```
https://pypi.org
```

---

# 20. Installing Packages

Python uses

```bash
pip
```

Example

```bash
pip install requests
```

Another example

```bash
pip install pandas
```

---

# 21. Importing Packages

After installation

```python
import requests
```

or

```python
import pandas as pd
```

Now you can use the package.

---

# 22. Program Flow

```
Create Class

↓

Create Object

↓

Constructor Runs

↓

Attributes Created

↓

Methods Available

↓

Modify Attributes

↓

Call Methods
```

---

# Common Beginner Mistakes

## Forgetting Parentheses

Wrong

```python
dog = Dog
```

Correct

```python
dog = Dog()
```

---

## Forgetting `self`

Wrong

```python
class Dog:

    def bark():

        print("Woof")
```

Correct

```python
def bark(self):
```

---

## Accessing Class Instead of Object

Wrong

```python
Dog.name
```

Correct

```python
dog.name
```

---

## Calling a Method Without Parentheses

Wrong

```python
dog.bark
```

Correct

```python
dog.bark()
```

---

## Modifying the Wrong Object

```python
dog1.age = 5
```

does not change

```python
dog2.age
```

Objects are independent.

---

# Real-World Examples

| Class | Attributes | Methods |
|--------|------------|----------|
| Car | Brand, Speed | Start(), Stop() |
| Student | Name, Marks | Study(), Sleep() |
| BankAccount | Balance | Deposit(), Withdraw() |
| Dog | Name, Age | Bark(), Eat() |
| Book | Title, Author | Read() |

---

# New Concepts Learned

| Concept | Example |
|----------|----------|
| Object-Oriented Programming | Organizing software using objects |
| Class | `class Dog:` |
| Object | `dog = Dog()` |
| Constructor | `__init__()` |
| `self` | Current object reference |
| Attribute | `self.name` |
| Method | `def bark()` |
| Object State | Each object has its own data |
| Modify Attributes | `dog.age = 5` |
| Call Methods | `dog.bark()` |
| Package | Collection of modules |
| PyPI | Python Package Index |
| pip | `pip install package_name` |

---

# One-Line Summary

Object-Oriented Programming (OOP) organizes programs around **classes** and **objects**, where each object encapsulates **attributes (data)** and **methods (behavior)**. Python automatically initializes objects using constructors, uses `self` to reference the current instance, and extends functionality through packages available on the **Python Package Index (PyPI)**, which can be installed using **pip**.