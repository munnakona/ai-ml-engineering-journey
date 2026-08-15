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

# Day 2 — Python Lists

> **Focus:** Understanding Python Lists through hands-on practice and an AI Technology Inventory mini-project.

## 🎯 Objective

The goal of Day 2 was to understand how Python lists work and how they can be used to store, access, modify, organize, and process collections of data.

Lists are fundamental to AI/ML programming and will be used later for:

- Training data
- Features
- Predictions
- Tokens
- Documents
- Model outputs
- Collections of objects

---

## 📚 Topics Covered

- Creating Lists
- List Length
- Positive Indexing
- Negative Indexing
- List Slicing
- Modifying List Elements
- `append()`
- `insert()`
- `remove()`
- `pop()`
- `del`
- `extend()`
- `sort()`
- `reverse()`
- `count()`
- `index()`
- Lists with `for` loops
- Lists with `if` conditions
- Nested Lists
- Nested Loops

---

## 1. Creating a List

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

```text
['ChatGPT', 'Claude', 'Gemini']
<class 'list'>
```

---

## 2. List Length

Use `len()` to determine the number of elements.

```python
print(len(ai_tools))
```

Output:

```text
3
```

---

## 3. Positive Indexing

Python uses **zero-based indexing**.

```text
0 → First element
1 → Second element
2 → Third element
```

Example:

```python
print(ai_tools[0])
print(ai_tools[1])
print(ai_tools[2])
```

Output:

```text
ChatGPT
Claude
Gemini
```

**Key rule:** The first element is always at index `0`.

---

## 4. Negative Indexing

Negative indexes access elements from the end.

```text
-1 → Last element
-2 → Second-last element
-3 → Third-last element
```

Example:

```python
print(ai_tools[-1])
print(ai_tools[-2])
print(ai_tools[-3])
```

Output:

```text
Gemini
Claude
ChatGPT
```

---

## 5. List Slicing

Slicing extracts part of a list.

### Syntax

```python
list[start:stop]
```

The `start` index is included and the `stop` index is excluded.

Example:

```python
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
```

Output:

```text
['ChatGPT', 'GitHub Copilot', 'Claude']
```

Other examples:

```python
ai_tools[:3]    # First three
ai_tools[2:]    # From index 2 to the end
ai_tools[:]     # Complete list
```

---

## 6. Modifying List Elements

Python lists are **mutable**.

Existing elements can be changed using their index.

```python
ai_tools[2] = "Claude"
ai_tools[4] = "Llama"
```

General pattern:

```python
list[index] = new_value
```

---

## 7. append()

`append()` adds one element to the end of a list.

```python
ai_tools.append("OpenAI API")
```

```text
Before:
['ChatGPT', 'Claude', 'Gemini']

After:
['ChatGPT', 'Claude', 'Gemini', 'OpenAI API']
```

---

## 8. insert()

`insert()` adds an element at a specific index.

### Syntax

```python
list.insert(index, value)
```

Example:

```python
ai_tools.insert(2, "PyTorch")
```

Existing elements from that position move to the right.

---

## 9. remove()

`remove()` removes an element using its **value**.

```python
ai_tools.remove("Gemini")
```

Python removes the first matching occurrence.

```text
remove() → remove by VALUE
```

---

## 10. pop()

`pop()` removes an element using its **index** and returns the removed value.

```python
removed_tool = ai_tools.pop(2)
print("Removed:", removed_tool)
```

If no index is supplied:

```python
ai_tools.pop()
```

the last element is removed and returned.

---

## 11. del

`del` removes an element using its index.

```python
del ai_tools[2]
```

Unlike `pop()`, `del` does not return the removed value.

---

## 12. remove() vs pop() vs del

| Method       | Removes By | Returns Removed Value |
| ------------ | ---------- | --------------------- |
| `remove()` | Value      | ❌ No                 |
| `pop()`    | Index      | ✅ Yes                |
| `del`      | Index      | ❌ No                 |

Easy way to remember:

```text
remove() → VALUE
pop()    → INDEX + returns value
del      → INDEX
```

---

## 13. extend()

`extend()` adds multiple elements from another list.

```python
new_tools = [
    "Ollama",
    "LangChain",
    "LangGraph"
]

ai_tools.extend(new_tools)
```

### append() vs extend()

```python
ai_tools.append(["Ollama", "LangChain"])
```

adds one nested list.

Whereas:

```python
ai_tools.extend(["Ollama", "LangChain"])
```

adds both elements individually.

```text
append() → one object
extend() → multiple elements
```

---

## 14. sort()

`sort()` sorts the original list.

```python
ai_tools.sort()
```

For strings, this sorts alphabetically.

Reverse alphabetical order:

```python
ai_tools.sort(reverse=True)
```

**Important:** `sort()` modifies the original list.

---

## 15. reverse()

`reverse()` reverses the current order.

```python
ai_tools.reverse()
```

Difference:

```text
sort()    → Sort based on values
reverse() → Reverse current order
```

`reverse()` does not alphabetically sort the list.

---

## 16. count()

`count()` returns how many times a value appears.

```python
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
print(ai_models.count("Claude"))
print(ai_models.count("Llama"))
```

Output:

```text
3
2
1
1
```

---

## 17. index()

`index()` returns the index of the **first occurrence**.

```python
print(ai_models.index("GPT"))
print(ai_models.index("Gemini"))
print(ai_models.index("Claude"))
print(ai_models.index("Llama"))
```

Output:

```text
0
1
3
6
```

Even though `"GPT"` appears multiple times:

```python
ai_models.index("GPT")
```

returns the first occurrence:

```text
0
```

---

## 18. Looping Through Lists

A `for` loop can process every element in a list.

```python
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
```

Output:

```text
Learning AI Tool: ChatGPT
Learning AI Tool: Claude
Learning AI Tool: Gemini
Learning AI Tool: Llama
Learning AI Tool: LangChain
Learning AI Tool: LangGraph
```

In:

```python
for tool in ai_tools:
```

`tool` is simply the loop variable representing the current element.

---

## 19. Lists + Conditional Logic

Lists can be combined with `if` conditions.

```python
for tool in ai_tools:

    if tool == "LangChain" or tool == "LangGraph":
        print(tool, "→ AI Framework")
    else:
        print(tool, "→ AI Model/Tool")
```

Output:

```text
ChatGPT → AI Model/Tool
Claude → AI Model/Tool
Gemini → AI Model/Tool
Llama → AI Model/Tool
LangChain → AI Framework
LangGraph → AI Framework
```

---

## 20. Nested Lists

A list can contain other lists.

```python
ai_categories = [
    ["ChatGPT", "Claude", "Gemini"],
    ["LangChain", "LangGraph"],
    ["PyTorch", "TensorFlow", "Scikit-learn"]
]
```

Access the first category:

```python
print(ai_categories[0])
```

Access `Claude`:

```python
print(ai_categories[0][1])
```

Nested indexing pattern:

```text
outer_list[outer_index][inner_index]
```

---

## 21. Nested Loops

Nested lists can be processed using nested loops.

```python
for category in ai_categories:
    for tool in category:
        print("AI Technology:", tool)
```

Output:

```text
AI Technology: ChatGPT
AI Technology: Claude
AI Technology: Gemini
AI Technology: LangChain
AI Technology: LangGraph
AI Technology: PyTorch
AI Technology: TensorFlow
AI Technology: Scikit-learn
```

Mental model:

```text
Outer loop
    ↓
Get one category
    ↓
Inner loop
    ↓
Process each technology
```

---

# 🚀 Day 2 Mini Project — AI Technology Inventory

## Objective

Build a structured inventory of AI models, AI frameworks, and ML frameworks.

### Data Structure

```python
ai_technology_inventory = [
    ["AI Models", ["ChatGPT", "Claude", "Gemini", "Llama"]],
    ["AI Frameworks", ["LangChain", "LangGraph"]],
    ["ML Frameworks", ["PyTorch", "TensorFlow", "Scikit-learn"]]
]
```

### Final Project

```python
ai_technology_inventory = [
    ["AI Models", ["ChatGPT", "Claude", "Gemini", "Llama"]],
    ["AI Frameworks", ["LangChain", "LangGraph"]],
    ["ML Frameworks", ["PyTorch", "TensorFlow", "Scikit-learn"]]
]

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
```

### Final Output

```text
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
```

---

# 💡 Key Lessons

### Zero-Based Indexing

```text
First element  → index 0
Second element → index 1
```

### Lists Are Mutable

```python
ai_tools[2] = "Claude"
```

### Indexes Can Change

Adding or removing elements can shift subsequent indexes.

### List Methods

```text
append()  → Add one item
insert()  → Add at a position
remove()  → Remove by value
pop()     → Remove by index
extend()  → Add multiple items
sort()    → Sort values
reverse() → Reverse order
count()   → Count occurrences
index()   → Find first occurrence
```

### Data Structure Design

A good data structure can reduce unnecessary conditions and make code easier to maintain and scale.

---

# 🧪 Day 2 Practice Files

```text
01-python/
│
├── day02_lists.py
└── day02_project.py
```

### day02_lists.py

Contains the hands-on exercises completed while learning Python Lists.

### day02_project.py

Contains the final AI Technology Inventory mini-project.

---

# ✅ Day 2 Completion

**Status: COMPLETED**

- [X] Creating Lists
- [X] Positive Indexing
- [X] Negative Indexing
- [X] Slicing
- [X] Modifying List Elements
- [X] append()
- [X] insert()
- [X] remove()
- [X] pop()
- [X] del
- [X] extend()
- [X] sort()
- [X] reverse()
- [X] count()
- [X] index()
- [X] List Iteration
- [X] Conditional Logic
- [X] Nested Lists
- [X] Nested Loops
- [X] AI Technology Inventory Mini Project

---

# 🎯 Day 2 Learning Principle

> **Don't just memorize Python syntax. Understand how data is structured and how your code operates on that data.**

The goal is to move from:

**Syntax → Logic → Problem Solving → Practical AI/ML Engineering**

---

# 🔜 Next — Day 3

## Python Tuples, Sets and Dictionaries

Upcoming topics:

- Tuples
- Tuple indexing
- Tuple immutability
- Sets
- Set operations
- Dictionaries
- Dictionary keys and values
- Adding and updating dictionary data
- Nested dictionaries
- Lists vs Tuples vs Sets vs Dictionaries
- Practical AI/ML examples



# Day 3 — Tuples, Sets & Dictionaries

> **Focus:** Understanding Python Tuples, Sets, and Dictionaries through hands-on practice and an AI Model Registry mini-project.

## 🎯 Objective

Day 3 focused on three important Python data structures:

- Tuples
- Sets
- Dictionaries

The goal was to understand when to use each structure, how to access and modify data, and how these structures can be combined to represent real-world AI/ML information.

---

# 1. Tuples

A tuple is an ordered collection of values.

Tuples use parentheses:

```python
ai_tools = (
    "ChatGPT",
    "Claude",
    "Gemini",
    "LangChain",
    "LangGraph"
)
```

Check the type:

```python
print(type(ai_tools))
```

Output:

```text
<class 'tuple'>
```

Check the length:

```python
print("Number of AI tools:", len(ai_tools))
```

## Tuple Indexing

Tuples support zero-based indexing just like lists.

```python
print(ai_tools[0])
print(ai_tools[-1])
```

Output:

```text
ChatGPT
LangGraph
```

## Tuple Slicing

```python
print(ai_tools[1:4])
```

Output:

```text
('Claude', 'Gemini', 'LangChain')
```

## Tuple Immutability

Tuples are **immutable**. Existing elements cannot be changed.

```python
ai_tools[0] = "GPT"
```

This produces:

```text
TypeError: 'tuple' object does not support item assignment
```

### Key Concept

```text
List  → Mutable
Tuple → Immutable
```

Use a tuple when the collection should remain fixed.

---

# 2. Tuple Unpacking

Tuple values can be assigned to multiple variables.

```python
ai_model = (
    "GPT",
    "OpenAI",
    "LLM"
)

name, provider, model_type = ai_model

print("Name:", name)
print("Provider:", provider)
print("Type:", model_type)
```

Output:

```text
Name: GPT
Provider: OpenAI
Type: LLM
```

Another example:

```python
devops_stack = (
    "Jenkins",
    "Docker",
    "Kubernetes"
)

tool1, tool2, tool3 = devops_stack

print("Tool 1:", tool1)
print("Tool 2:", tool2)
print("Tool 3:", tool3)
```

---

# 3. Tuple Methods

## count()

Counts how many times a value appears.

```python
ai_models = (
    "GPT",
    "Gemini",
    "GPT",
    "Claude",
    "Gemini",
    "GPT",
    "Llama"
)

print(ai_models.count("GPT"))
print(ai_models.count("Gemini"))
```

Output:

```text
3
2
```

## index()

Returns the index of the first occurrence.

```python
print(ai_models.index("Claude"))
print(ai_models.index("Llama"))
```

Output:

```text
3
6
```

---

# 4. List vs Tuple

| Feature      | List   | Tuple  |
| ------------ | ------ | ------ |
| Syntax       | `[]` | `()` |
| Ordered      | Yes    | Yes    |
| Indexing     | Yes    | Yes    |
| Slicing      | Yes    | Yes    |
| Mutable      | Yes    | No     |
| `append()` | Yes    | No     |
| `remove()` | Yes    | No     |
| `count()`  | Yes    | Yes    |
| `index()`  | Yes    | Yes    |

> Use a **List** when the data may change. Use a **Tuple** when the data should remain fixed.

---

# 5. Sets

A set is a collection that stores **unique values**.

```python
ai_tools = {
    "ChatGPT",
    "Claude",
    "Gemini",
    "ChatGPT",
    "Claude",
    "LangChain"
}

print(ai_tools)
print(type(ai_tools))
print("Number of unique tools:", len(ai_tools))
```

Output contains only unique values:

```text
<class 'set'>
Number of unique tools: 4
```

### Key Concept

```text
List → Duplicates allowed
Set  → Unique values
```

The display order of a set should not be relied upon.

---

# 6. Adding to a Set

Use `add()` to add one value.

```python
ai_tools.add("Llama")
ai_tools.add("LangGraph")
```

Adding an existing value does not create a duplicate:

```python
ai_tools.add("ChatGPT")
```

---

# 7. remove() vs discard()

### remove()

```python
ai_tools.remove("Claude")
```

If the value does not exist, `remove()` raises a `KeyError`.

### discard()

```python
ai_tools.discard("Claude")
```

If the value does not exist, `discard()` does nothing.

```text
remove()  → Missing value causes KeyError
discard() → Missing value is ignored
```

---

# 8. Set Operations

Example:

```python
devops_tools = {
    "Python",
    "Docker",
    "Kubernetes",
    "Jenkins",
    "Linux"
}

ai_tools = {
    "Python",
    "LangChain",
    "LangGraph",
    "Docker",
    "Linux"
}
```

## Union

```python
all_tools = devops_tools | ai_tools
```

Returns all unique values from both sets.

## Intersection

```python
common_tools = devops_tools & ai_tools
```

Returns values present in both sets:

```text
Python
Docker
Linux
```

## Difference

```python
devops_only = devops_tools - ai_tools
ai_only = ai_tools - devops_tools
```

Results:

```text
DevOps only:
Jenkins
Kubernetes

AI only:
LangChain
LangGraph
```

### Remember

```text
| → Union        → Everything
& → Intersection → Common values
- → Difference   → Only in the first set
```

---

# 9. Dictionaries

A dictionary stores data as **key-value pairs**.

```python
ai_model = {
    "name": "GPT",
    "provider": "OpenAI",
    "type": "LLM",
    "category": "Generative AI"
}
```

Structure:

```text
name      → GPT
provider  → OpenAI
type      → LLM
category  → Generative AI
```

Check the type:

```python
print(type(ai_model))
```

Output:

```text
<class 'dict'>
```

---

# 10. Accessing Dictionary Values

Dictionaries are accessed using keys.

```python
print("Name:", ai_model["name"])
print("Provider:", ai_model["provider"])
print("Type:", ai_model["type"])
print("Category:", ai_model["category"])
```

---

# 11. Updating and Adding Dictionary Values

Update an existing key:

```python
ai_model["name"] = "GPT-5"
```

Add a new key:

```python
ai_model["context_window"] = 128000
ai_model["temperature"] = 0.7
```

### Key Concept

```python
dictionary["key"] = value
```

does two things:

```text
Existing key → UPDATE
New key      → ADD
```

---

# 12. Removing Dictionary Data

## pop()

Removes a key and returns its value.

```python
removed_temperature = ai_model.pop("temperature")
```

## del

Removes a specific key.

```python
del ai_model["context_window"]
```

## clear()

Removes all key-value pairs.

```python
ai_model.clear()
print(ai_model)
```

Output:

```text
{}
```

### Remember

```text
pop()   → Remove key + return value
del     → Remove key
clear() → Remove everything
```

---

# 13. Dictionary keys(), values() and items()

```python
print(ai_model.keys())
print(ai_model.values())
print(ai_model.items())
```

### Remember

```text
keys()   → Keys
values() → Values
items()  → Key + Value
```

---

# 14. Looping Through Dictionaries

Loop through keys:

```python
for key in ai_model:
    print("Key:", key)
```

Loop through values:

```python
for value in ai_model.values():
    print("Value:", value)
```

Loop through key-value pairs:

```python
for key, value in ai_model.items():
    print(key, "→", value)
```

Output:

```text
name → GPT-5
provider → OpenAI
type → LLM
context_window → 128000
temperature → 0.7
```

This pattern is especially useful when processing structured data and JSON/API responses.

---

# 15. Nested Dictionaries

A dictionary can contain other dictionaries as values.

```python
ai_models = {
    "GPT": {
        "provider": "OpenAI",
        "type": "LLM"
    },
    "Claude": {
        "provider": "Anthropic",
        "type": "LLM"
    },
    "Gemini": {
        "provider": "Google",
        "type": "LLM"
    },
    "Llama": {
        "provider": "Meta",
        "type": "LLM"
    }
}
```

Access nested data:

```python
print(ai_models["GPT"]["provider"])
print(ai_models["Claude"]["provider"])
print(ai_models["Gemini"]["provider"])
```

Pattern:

```python
dictionary["outer_key"]["inner_key"]
```

---

# 16. Looping Through Nested Dictionaries

```python
for model, details in ai_models.items():
    print("Model:", model)
    print("Provider:", details["provider"])
    print("Type:", details["type"])
    print()
```

This combines:

```text
Dictionary
+
Nested Dictionary
+
items()
+
Tuple Unpacking
+
for Loop
```

---

# 🚀 Day 3 Mini Project — AI Model Registry

## Objective

Build an AI Model Registry using Lists, Tuples, Sets, Dictionaries, Nested Dictionaries, and Loops.

### Final Project Code

```python
ai_models = {
    "GPT": {
        "provider": "OpenAI",
        "type": "LLM"
    },
    "Claude": {
        "provider": "Anthropic",
        "type": "LLM"
    },
    "Gemini": {
        "provider": "Google",
        "type": "LLM"
    },
    "Llama": {
        "provider": "Meta",
        "type": "LLM"
    }
}

# Tuple: fixed model categories
model_categories = (
    "LLM",
    "Generative AI",
    "Foundation Model"
)

# Set: store unique providers
providers = set()

for model, details in ai_models.items():
    providers.add(details["provider"])

# List: store model names
model_names = []

for model in ai_models:
    model_names.append(model)

# Display AI Model Registry
print("===== AI MODEL REGISTRY =====")

for model, details in ai_models.items():
    print("Model:", model)
    print("Provider:", details["provider"])
    print("Type:", details["type"])
    print()

# Registry Summary
print("===== REGISTRY SUMMARY =====")
print("Total Models:", len(ai_models))
print("Total Providers:", len(providers))
print("Model Names:", model_names)
print("Model Categories:", model_categories)
```

### Final Output

```text
===== AI MODEL REGISTRY =====

Model: GPT
Provider: OpenAI
Type: LLM

Model: Claude
Provider: Anthropic
Type: LLM

Model: Gemini
Provider: Google
Type: LLM

Model: Llama
Provider: Meta
Type: LLM

===== REGISTRY SUMMARY =====
Total Models: 4
Total Providers: 4
Model Names: ['GPT', 'Claude', 'Gemini', 'Llama']
Model Categories: ('LLM', 'Generative AI', 'Foundation Model')
```

---

# 💡 Key Lessons

## List

```text
Mutable
Ordered
Duplicates allowed
Uses []
```

## Tuple

```text
Immutable
Ordered
Duplicates allowed
Uses ()
```

## Set

```text
Unique values
Duplicates removed
Useful for comparisons
Uses {}
```

## Dictionary

```text
Key-value pairs
Access using keys
Useful for structured data
Uses {}
```

### Quick Comparison

| Data Structure | Ordered             | Mutable | Duplicates | Main Use                      |
| -------------- | ------------------- | ------- | ---------- | ----------------------------- |
| List           | Yes                 | Yes     | Yes        | Changing collections          |
| Tuple          | Yes                 | No      | Yes        | Fixed data                    |
| Set            | No guaranteed order | Yes     | No         | Unique values and comparisons |
| Dictionary     | Insertion order     | Yes     | Keys: No   | Key-value structured data     |

---

# 🧪 Day 3 Practice Files

```text
01-python/
├── day03_tuples_sets_dict.py
└── day03_project.py
```

### day03_tuples_sets_dict.py

Contains the hands-on exercises completed during Day 3.

### day03_project.py

Contains the final AI Model Registry mini-project.

---

# ✅ Day 3 Completion

**Status: COMPLETED**

- [X] Tuples
- [X] Tuple indexing
- [X] Tuple slicing
- [X] Tuple immutability
- [X] Tuple unpacking
- [X] `count()`
- [X] `index()`
- [X] Sets
- [X] Set uniqueness
- [X] `add()`
- [X] `remove()`
- [X] `discard()`
- [X] Union
- [X] Intersection
- [X] Difference
- [X] Dictionaries
- [X] Key-value pairs
- [X] Adding dictionary data
- [X] Updating dictionary data
- [X] `pop()`
- [X] `del`
- [X] `clear()`
- [X] `keys()`
- [X] `values()`
- [X] `items()`
- [X] Dictionary loops
- [X] Nested dictionaries
- [X] AI Model Registry mini-project

---

# 🎯 Day 3 Learning Principle

> **Choose the data structure based on the problem: List for changing collections, Tuple for fixed data, Set for unique values, and Dictionary for structured key-value data.**

The goal is to move from:

**Syntax → Data Structures → Logic → Problem Solving → AI/ML Engineering**

---

# 🔜 Next — Day 4

## Python Functions

Upcoming topics:

- Defining functions
- Parameters
- Arguments
- Return values
- Default parameters
- Multiple parameters
- Function scope
- Reusable functions
- Practical AI/ML functions
- Mini-project
