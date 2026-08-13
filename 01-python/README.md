
# Day 1 — Python Fundamentals

## Overview

Day 1 is the foundation of the 6-month AI/ML and GenAI learning journey.

The focus was on understanding Python fundamentals through hands-on coding rather than watching recorded course videos.

The goal is to understand the concepts, write the code independently, execute it, identify errors, and understand why the code behaves the way it does.

---

## Environment Setup

### Operating Environment

* OS: macOS
* IDE: Visual Studio Code
* Python Distribution: Anaconda
* Conda Version: 25.7.0
* Python Version: 3.12.13

### Conda Environment

A dedicated environment was created for the AI/ML learning journey:

```bash
conda create -n ai-learning python=3.12
```

Activate the environment:

```bash
conda activate ai-learning
```

Verify Python:

```bash
python --version
```

Expected:

```text
Python 3.12.13
```

Verify Python location:

```bash
which python
```

Expected:

```text
/opt/anaconda3/envs/ai-learning/bin/python
```

---

# Project Structure

The overall 6-month learning workspace was created as:

```text
AI-Learning/
│
├── 01-python/
├── 02-math/
├── 03-machine-learning/
├── 04-deep-learning/
├── 05-nlp/
├── 06-llm/
├── 07-rag/
├── 08-agentic-ai/
├── 09-mlops/
├── 10-llmops/
├── 11-azure/
└── projects/
```

Day 1 work is stored under:

```text
AI-Learning/01-python/
```

---

# Topics Learned

## 1. Variables

Variables store values that can be used later in a program.

Example:

```python
name = "Munna"
experience = 14
current_role = "DevOps Engineer"
```

Python determines the data type automatically.

---

## 2. Python Data Types

The basic data types practiced:

### String

```python
name = "Munna"
```

Type:

```text
str
```

### Integer

```python
experience = 14
```

Type:

```text
int
```

### Float

```python
height = 5.6
```

Type:

```text
float
```

### Boolean

```python
is_learning_ai = True
```

Type:

```text
bool
```

Check the type using:

```python
type(variable)
```

Example:

```python
print(type(experience))
```

---

# 3. Input

Python's `input()` function receives user input.

Example:

```python
name = input("Enter your name: ")
experience = input("Enter your years of experience: ")
```

Important:

`input()` returns a string by default.

Even if the user enters:

```text
14
```

Python initially stores:

```python
"14"
```

not:

```python
14
```

---

# 4. Type Conversion

Convert a string to an integer using:

```python
int()
```

Example:

```python
experience = input("Enter your experience: ")

experience = int(experience)
```

Now Python can perform mathematical operations:

```python
future_experience = experience + 5
```

Example:

```text
"14" → 14
str     int
```

Other common conversions include:

```python
float("5.6")
str(14)
bool(1)
```

---

# 5. Arithmetic Operators

The following operators were practiced:

| Operator | Meaning            |
| -------- | ------------------ |
| `+`    | Addition           |
| `-`    | Subtraction        |
| `*`    | Multiplication     |
| `/`    | Division           |
| `//`   | Floor division     |
| `%`    | Remainder / Modulo |
| `**`   | Power              |

Example:

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

---

# 6. Comparison Operators

Comparison operators return a Boolean value:

```text
True
False
```

Examples:

```python
experience > 10
experience < 10
experience >= 10
experience <= 10
experience == 10
experience != 10
```

Important:

```python
=
```

means assignment.

Whereas:

```python
==
```

means comparison.

---

# 7. Logical Operators

The following logical operators were practiced:

```text
and
or
not
```

Example:

```python
experience = 14
has_devops = True
has_genai = True

if experience >= 10 and has_devops and has_genai:
    print("Strong candidate for AI Platform Engineering")
```

All conditions connected using `and` must be true.

---

# 8. if / elif / else

Python uses conditional statements to make decisions.

Example:

```python
if experience >= 15:
    print("AI Architect")
elif experience >= 10:
    print("AI Platform Engineer")
elif experience >= 5:
    print("AI Engineer")
else:
    print("Continue learning")
```

Important concept:

Python evaluates conditions from top to bottom and executes the first matching branch.

---

# 9. for Loop

A `for` loop iterates through items in a sequence.

Example:

```python
technologies = [
    "Python",
    "Docker",
    "Kubernetes",
    "Jenkins",
    "Azure"
]

for technology in technologies:
    print("Learning:", technology)
```

The loop processes each element one at a time.

Conceptually:

```text
technology = "Python"
technology = "Docker"
technology = "Kubernetes"
...
```

---

# 10. Loop with Conditions

A `for` loop can be combined with `if / elif / else`.

Example:

```python
for technology in technologies:

    if technology == "Kubernetes":
        print(technology, "→ Container orchestration")

    elif technology == "Python":
        print(technology, "→ AI/ML programming language")

    elif technology == "LangGraph":
        print(technology, "→ Agentic AI framework")

    else:
        print(technology, "→ Currently learning")
```

Important:

Strings must be enclosed in quotes:

```python
"Kubernetes"
```

not:

```python
Kubernetes
```

unless `Kubernetes` has been defined as a variable.

---

# 11. range()

`range()` generates a sequence of numbers.

Example:

```python
for number in range(1, 11):
    print(number)
```

Output:

```text
1
2
3
4
5
6
7
8
9
10
```

Important:

The stop value is excluded.

Therefore:

```python
range(1, 11)
```

means:

```text
1 through 10
```

not 11.

Other forms:

```python
range(5)
range(2, 6)
range(2, 10, 2)
```

---

# 12. Modulo Operator `%`

The modulo operator returns the remainder.

Example:

```python
10 % 2
```

Result:

```text
0
```

Therefore:

```python
number % 2 == 0
```

can be used to check whether a number is even.

Example:

```python
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

Divisibility by 5:

```python
if number % 5 == 0:
    print("Divisible by 5")
```

---

# 13. Multiple Independent Conditions

Important distinction:

Using:

```python
if
elif
```

means only the first matching branch executes.

Using separate `if` statements means each condition is evaluated independently.

Example:

```python
if number % 2 == 0:
    result = "Even"
else:
    result = "Odd"

if number % 5 == 0:
    result = result + " → Divisible by 5"
```

For `10`:

```text
10 → Even → Divisible by 5
```

---

# 14. while Loop

A `while` loop continues as long as a condition is true.

Example:

```python
day = 1

while day <= 5:
    print("AI Learning Day:", day)
    day += 1
```

Output:

```text
AI Learning Day: 1
AI Learning Day: 2
AI Learning Day: 3
AI Learning Day: 4
AI Learning Day: 5
```

Important:

The following:

```python
day += 1
```

is equivalent to:

```python
day = day + 1
```

It is called an augmented assignment operator.

---

# 15. Infinite Loops

Be careful with:

```python
day = 1

while day <= 5:
    print(day)
```

The value of `day` never changes, so the condition remains true forever.

This creates an infinite loop.

To stop a running program in Terminal:

```text
Ctrl + C
```

---

# Important Lessons From Day 1

### `for` vs `while`

Use `for` when iterating over a known sequence or range:

```python
for number in range(1, 11):
    print(number)
```

Use `while` when continuing based on a condition:

```python
while day <= 7:
    ...
```

---

### `if` vs `elif`

`if` starts a condition.

`elif` checks another condition only if the previous conditions were false.

```python
if condition1:
    ...
elif condition2:
    ...
else:
    ...
```

---

### `if` vs separate `if`

Use separate `if` statements when multiple conditions may independently be true.

```python
if condition1:
    ...

if condition2:
    ...
```

---

# Day 1 Practice Files

The following files were created/practiced:

```text
01-python/
│
├── day01.py
├── day01_operators.py
├── day01_loops.py
├── day01_range.py
└── day01_while.py
```

---

# Key Python Concepts Completed

* [X] Python environment
* [X] Conda environment
* [X] Python 3.12
* [X] VS Code
* [X] Variables
* [X] Strings
* [X] Integers
* [X] Floats
* [X] Booleans
* [X] `type()`
* [X] `input()`
* [X] Type conversion
* [X] Arithmetic operators
* [X] Comparison operators
* [X] Logical operators
* [X] `if`
* [X] `elif`
* [X] `else`
* [X] `for`
* [X] `while`
* [X] `range()`
* [X] Modulo `%`
* [X] `+=`
* [X] Conditional logic
* [X] Basic debugging

---

# Practical Learning Approach

The Day 1 learning method was:

```text
Learn
  ↓
Understand
  ↓
Write code
  ↓
Run code
  ↓
Observe output
  ↓
Make mistakes
  ↓
Debug
  ↓
Understand why
  ↓
Practice again
```

The objective is **not memorizing Python syntax**.

The objective is to understand programming logic well enough to write and troubleshoot code independently.

---

# Connection to Future AI/ML Learning

The Python fundamentals learned today will be used throughout the remaining curriculum.

```text
Python Fundamentals
        ↓
Lists / Dictionaries
        ↓
NumPy / Pandas
        ↓
Machine Learning
        ↓
Deep Learning
        ↓
NLP
        ↓
LLMs
        ↓
RAG
        ↓
Agentic AI
        ↓
MLOps / LLMOps
        ↓
Docker / Kubernetes
        ↓
Azure
```

The ultimate goal is to combine Python and AI with existing DevOps experience to build production-grade AI systems.

---

# Day 1 Status

**Status: COMPLETED ✅**

Next:

## Day 2 — Python Data Structures

Topics:

* Lists
* Indexing
* Negative indexing
* Slicing
* Adding/removing elements
* Updating lists
* List methods
* Nested lists
* Looping through lists
* Practical AI/ML examples

---

## Learning Principle

> **Don't just watch. Build.**

The goal of this six-month journey is to move from:

**Course Knowledge → Practical Knowledge → Production Skills → AI Engineering Capability**
