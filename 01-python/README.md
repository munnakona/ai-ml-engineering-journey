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



# Day 2 — Python Data Structures: Lists

## Overview

Day 2 focused on Python Lists and practical data manipulation.

Lists are one of the most important Python data structures for AI/ML because they are frequently used to store:

- Training data
- Features
- Predictions
- AI tools
- Model outputs
- Tokens
- Documents
- Collections of objects

The goal was to understand how to create, access, modify, organize, and process lists using Python.

---

## 1. Creating Lists

A Python list is created using square brackets `[]`.

```python
ai_tools = [
    "ChatGPT",
    "Claude",
    "Gemini"
]

print(ai_tools)

print(type(ai_tools))
```



Output:

['ChatGPT', 'Claude', 'Gemini']
<class 'list'>
2. List Length

Use len() to determine the number of elements in a list.

print(len(ai_tools))

Output:

3
3. Positive Indexing

Python list indexing starts from 0.

Index 0 → First element
Index 1 → Second element
Index 2 → Third element

Example:

print(ai_tools[0])
print(ai_tools[1])
print(ai_tools[2])

Output:

ChatGPT
Claude
Gemini
Important

Python uses zero-based indexing.

Therefore:

ai_tools[0]

means the first element, not the second.

4. Negative Indexing

Negative indexes allow us to access elements from the end of a list.

-1 → Last element
-2 → Second-last element
-3 → Third-last element

Example:

print(ai_tools[-1])
print(ai_tools[-2])
print(ai_tools[-3])

Output:

Gemini
Claude
ChatGPT
Key Concept
ai_tools[-1]

always refers to the last element of the list.

5. List Slicing

Slicing allows us to extract a portion of a list.

Syntax:

list[start:stop]

The start index is included.

The stop index is excluded.

Example:

ai_tools = [
    "ChatGPT",
    "GitHub Copilot",
    "Claude",
    "Gemini",
    "Llama",
    "LangChain",
    "LangGraph"
]

print(ai_tools[0:3])

Output:

['ChatGPT', 'GitHub Copilot', 'Claude']
Other slicing examples

First three:

ai_tools[:3]

From index 2 to the end:

ai_tools[2:]

Complete list:

ai_tools[:]
Important Rule
[start:stop]

start → included
stop  → excluded
6. Modifying List Elements

Python lists are mutable.

This means existing elements can be changed after the list is created.

Example:

ai_tools[2] = "Claude"

General syntax:

list[index] = new_value

Example:

ai_tools[4] = "Llama"

The original list is modified.

7. append()

append() adds one element to the end of a list.

Example:

ai_tools.append("OpenAI API")

If the list was:

['ChatGPT', 'Claude', 'Gemini']

after append():

['ChatGPT', 'Claude', 'Gemini', 'OpenAI API']
Important

append() adds exactly one object to the list.

8. insert()

insert() adds an element at a specific index.

Syntax:

list.insert(index, value)

Example:

ai_tools.insert(2, "PyTorch")

The element is inserted at index 2.

Existing elements from that position onward move to the right.

Important

Adding or removing elements can change the indexes of subsequent elements.

9. remove()

remove() removes an element based on its value.

Example:

ai_tools.remove("Gemini")

Python searches for "Gemini" and removes the first matching occurrence.

Important

remove() works with the value, not the index.

10. pop()

pop() removes an element using its index.

Example:

removed_tool = ai_tools.pop(2)

print("Removed:", removed_tool)

The removed element is returned by pop().

Example output:

Removed: Claude
Default behavior

If no index is provided:

ai_tools.pop()

Python removes and returns the last element.

11. del

del can remove an element using its index.

Example:

del ai_tools[2]

This removes the element currently at index 2.

Unlike pop(), del does not return the removed value.

12. remove() vs pop() vs del
    Operation	Removes By	Returns Removed Value
    remove()	Value	No
    pop()	Index	Yes
    del	Index	No
    Easy way to remember
    remove() → remove this VALUE
    pop()    → remove this INDEX and return it
    del      → delete this INDEX
13. extend()

extend() adds multiple elements from another iterable, such as a list.

Example:

new_tools = [
    "Ollama",
    "LangChain",
    "LangGraph"
]

ai_tools.extend(new_tools)

The elements are added individually.

append() vs extend()

Using append():

ai_tools.append(["Ollama", "LangChain"])

creates a nested list:

['ChatGPT', ['Ollama', 'LangChain']]

Using extend():

ai_tools.extend(["Ollama", "LangChain"])

adds the elements individually:

['ChatGPT', 'Ollama', 'LangChain']
14. sort()

sort() sorts the original list.

Example:

ai_tools.sort()

This sorts strings alphabetically.

Example:

['Azure OpenAI', 'ChatGPT', 'Claude', 'Gemini', 'LangGraph']
Reverse sorting
ai_tools.sort(reverse=True)

This sorts the list in descending order.

Important

sort() modifies the original list.

15. reverse()

reverse() reverses the current order of the list.

Example:

ai_tools.reverse()

If the list is:

['Gemini', 'ChatGPT', 'Claude']

after reverse():

['Claude', 'ChatGPT', 'Gemini']
Important Difference
sort()
    ↓
Sort based on values

reverse()
    ↓
Simply reverse the current order

reverse() does not perform alphabetical sorting.

16. count()

count() returns how many times a value occurs in a list.

Example:

ai_models = [
    "GPT",
    "Gemini",
    "GPT",
    "Claude",
    "Gemini",
    "GPT",
    "Llama"
]

print(ai_models.count("GPT"))
print(ai_models.count("Gemini"))

Output:

3
2
17. index()

index() returns the index of the first occurrence of a value.

Example:

print(ai_models.index("GPT"))

Output:

0

Even though "GPT" appears multiple times, index() returns the first matching position.

Important
list.index(value)

returns the first occurrence.

18. Looping Through Lists

A for loop can process each element in a list.

Example:

ai_tools = [
    "ChatGPT",
    "Claude",
    "Gemini",
    "Llama",
    "LangChain",
    "LangGraph"
]

for tool in ai_tools:
    print("Learning AI Tool:", tool)

Output:

Learning AI Tool: ChatGPT
Learning AI Tool: Claude
Learning AI Tool: Gemini
Learning AI Tool: Llama
Learning AI Tool: LangChain
Learning AI Tool: LangGraph
Important Concept

In:

for tool in ai_tools:

tool is simply the loop variable.

It represents the current element.

19. Lists with Conditional Logic

Lists can be combined with if conditions.

Example:

for tool in ai_tools:

    if tool == "LangChain" or tool == "LangGraph":
        print(tool, "→ AI Framework")
    else:
        print(tool, "→ AI Model/Tool")

Output:

ChatGPT → AI Model/Tool
Claude → AI Model/Tool
Gemini → AI Model/Tool
Llama → AI Model/Tool
LangChain → AI Framework
LangGraph → AI Framework
20. Nested Lists

A list can contain other lists.

Example:

ai_categories = [
    ["ChatGPT", "Claude", "Gemini"],
    ["LangChain", "LangGraph"],
    ["PyTorch", "TensorFlow", "Scikit-learn"]
]

This creates a list containing three inner lists.

Conceptually:

ai_categories
│
├── AI Models
│   ├── ChatGPT
│   ├── Claude
│   └── Gemini
│
├── AI Frameworks
│   ├── LangChain
│   └── LangGraph
│
└── ML Frameworks
    ├── PyTorch
    ├── TensorFlow
    └── Scikit-learn
21. Accessing Nested Lists

Access the first category:

print(ai_categories[0])

Output:

['ChatGPT', 'Claude', 'Gemini']

Access Claude:

print(ai_categories[0][1])

Output:

Claude
Nested indexing pattern
outer_list[outer_index][inner_index]
22. Nested Loops

Nested lists can be processed using nested for loops.

Example:

for category in ai_categories:

    for tool in category:
        print("AI Technology:", tool)

Output:

AI Technology: ChatGPT
AI Technology: Claude
AI Technology: Gemini
AI Technology: LangChain
AI Technology: LangGraph
AI Technology: PyTorch
AI Technology: TensorFlow
AI Technology: Scikit-learn
Concept
Outer loop
    ↓
Get one category
    ↓
Inner loop
    ↓
Process each technology
Day 2 Mini Project — AI Technology Inventory
Objective

Create a structured inventory of AI models, AI frameworks, and ML frameworks.

ai_technology_inventory = [
    ["AI Models", ["ChatGPT", "Claude", "Gemini", "Llama"]],
    ["AI Frameworks", ["LangChain", "LangGraph"]],
    ["ML Frameworks", ["PyTorch", "TensorFlow", "Scikit-learn"]]
]

The program processes the nested structure using loops.

Example:

print("===== AI TECHNOLOGY INVENTORY =====")

for category in ai_technology_inventory:

    category_name = category[0]
    tools = category[1]

    print(category_name + ":")

    for tool in tools:
        print(" - " + tool)

total_technologies = 0

for category in ai_technology_inventory:
    tools = category[1]
    total_technologies += len(tools)

print("Total Categories:", len(ai_technology_inventory))
print("Total Technologies:", total_technologies)
Output
===== AI TECHNOLOGY INVENTORY =====

AI Models:

- ChatGPT
- Claude
- Gemini
- Llama

AI Frameworks:

- LangChain
- LangGraph

ML Frameworks:

- PyTorch
- TensorFlow
- Scikit-learn

Total Categories: 3
Total Technologies: 9
Day 2 — Key Lessons

1. Python uses zero-based indexing
   First element → index 0
   Second element → index 1
2. Lists are mutable

Existing list elements can be changed.

ai_tools[2] = "Claude"
3. Indexes can change

Adding or removing elements can shift the indexes of other elements.

4. append() and extend() are different
   append() → Adds one object
   extend() → Adds multiple elements
5. remove(), pop(), and del are different
   remove() → Value
   pop()    → Index + returns removed value
   del      → Index
6. sort() and reverse() are different
   sort()    → Sorts the values
   reverse() → Reverses the current order
7. Data structure design matters

Good data structures can reduce unnecessary if/elif logic and make programs easier to maintain.

Day 2 — Practical Skills

During Day 2, the following practical skills were demonstrated:

Creating lists
Accessing list elements
Changing list elements
Adding elements
Removing elements
Sorting
Reversing
Counting
Searching
Iterating
Nested data structures
Nested loops
Dynamic calculations
Day 2 Status

COMPLETED ✅

Topics Completed
 Creating Lists
 type()
 len()
 Positive Indexing
 Negative Indexing
 Slicing
 Modifying List Elements
 append()
 insert()
 remove()
 pop()
 del
 extend()
 sort()
 reverse()
 count()
 index()
 List Iteration
 Conditional Logic
 Nested Lists
 Nested Loops
 AI Technology Inventory Mini Project
Day 2 — Learning Principle

Good programming is not only about writing code that works. It is also about choosing data structures that make the code simple, readable, reusable, and scalable.

Next
Day 3 — Python Tuples, Sets and Dictionaries

Next we will learn:

Tuples
Tuple indexing
Tuple immutability
Sets
Set operations
Dictionaries
Dictionary keys and values
Nested dictionaries
Lists vs Tuples vs Sets vs Dictionaries
Practical AI/ML data examples

## Learning Principle

> **Don't just watch. Build.**

The goal of this six-month journey is to move from:

**Course Knowledge → Practical Knowledge → Production Skills → AI Engineering Capability**
