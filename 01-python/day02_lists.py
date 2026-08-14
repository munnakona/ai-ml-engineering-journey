# Lists in Python

technologies = [
    "Python",
    "Docker",
    "Kubernetes",
    "Jenkins",
    "Azure"
]

print(technologies)
print(type(technologies))

print("Number of technologies:", len(technologies))


ai_tools = ["ChatGPT", "GitHub Copilot", "Amazon CodeWhisperer"]

print(ai_tools)
print(type(ai_tools))
print("Number of AI tools:", len(ai_tools))


# Normal Indexing 
print("First AI tool:", ai_tools[0])
print("Second AI tool:", ai_tools[1])
print("Third AI tool:", ai_tools[2])


# Negative Indexing
print("Last AI tool:", ai_tools[-1])
print("Second last AI tool:", ai_tools[-2])
print("Third last AI tool:", ai_tools[-3])


# Slicing

ai_tools = [
    "ChatGPT",
    "GitHub Copilot",
    "Amazon CodeWhisperer",
    "Gemini",
    "Ollama",
    "LangChain",
    "LangGraph"
]

print(ai_tools[0:3])  # First three tools
print(ai_tools[4:7])  # last three tools
print(ai_tools[2:6])  # Third three tools
print(ai_tools[0:7])  # complete list



# changine the elements

ai_tools[2] = "Claude"
ai_tools[4] = "Llama"

print(ai_tools)

# append() method to add new elements to the list

ai_tools.append("OpenAI API")
ai_tools.append("Hugging Face")
ai_tools.append("Ollama")

print(ai_tools)
print("Number of AI tools:", len(ai_tools))


# insert() method to add new elements to the list at a specific index

ai_tools.insert(5, "PyTorch")
ai_tools.insert(4, "TensorFlow")
ai_tools.insert(0, "Scikit-learn")

# remove method to remove elements from the list

ai_tools.remove("GitHub Copilot")
ai_tools.remove("Ollama")

print(ai_tools)
print("Number of AI tools:", len(ai_tools))



# del and pop() methods to remove elements from the list


ai_tools = [
    "Scikit-learn",
    "ChatGPT",
    "Claude",
    "Gemini",
    "TensorFlow",
    "Llama"
]

ai_tools.remove("Gemini")
ai_tools.pop(2)  # removes the element at index 2
del ai_tools[3]  # removes the element at index 4

removed_tool = ai_tools.pop(2)
print("Removed tool:", removed_tool)

print(ai_tools)





# extending a list using extend() method

ai_tools = [
    "ChatGPT",
    "Claude",
    "Gemini"
]

new_tools = [
    "Ollama",
    "LangChain",
    "LangGraph"
]

ai_tools.extend(new_tools)
print(ai_tools)
print("Total tools:", len(ai_tools))

cloud_tools = ["Azure OpenAI", "Azure AI Search"]

ai_tools.extend(cloud_tools)    
print(ai_tools)
print("Total tools:", len(ai_tools))


# sort () method to sort the list in ascending order


ai_tools = [
    "LangGraph",
    "ChatGPT",
    "Azure OpenAI",
    "Gemini",
    "Claude"
]

ai_tools.sort()
print(ai_tools)

ai_tools.sort(reverse=True) 
print(ai_tools)


# revers () method to reverse the list

ai_tools = [
    "LangGraph",
    "ChatGPT",
    "Azure OpenAI",
    "Gemini",
    "Claude"
]

print(ai_tools)

ai_tools.reverse()
print(ai_tools)

languages = [
    "Python",
    "Java",
    "C++",
    "Go"
]

languages.sort()
print(languages)

languages.reverse()

print(languages)



# Count() method to count the number of occurrences of an element in the list

ai_models = [
    "GPT",
    "Gemini",
    "GPT",
    "Claude",
    "Gemini",
    "GPT",
    "Llama"
]

ai_models.count("GPT")  # returns 3
print(ai_models.count("GPT"))

ai_models.count("Gemini")  # returns 2
print(ai_models.count("Gemini"))

ai_models.count("Claude")  # returns 1
print(ai_models.count("Claude"))

ai_models.count("Llama")  # returns 0
print(ai_models.count("Llama"))



# index() method to find the index of an element in the list

ai_models = [
    "GPT",
    "Gemini",
    "GPT",
    "Claude",
    "Gemini",
    "GPT",
    "Llama"
]

print(ai_models.index("GPT"))
print(ai_models.index("Gemini"))
print(ai_models.index("Claude"))
print(ai_models.index("Llama"))


# Loops through lists

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



# loop and if   

ai_tools = [
    "ChatGPT",
    "Claude",
    "Gemini",
    "Llama",
    "LangChain",
    "LangGraph"
]
for tool in ai_tools:

    if tool == "LangChain" or tool == "LangGraph":
        print(tool, "→ AI Framework")
    else:
        print(tool, "→ AI Model/Tool")
        
        
        
# nested lists

ai_categories = [
    ["ChatGPT", "Claude", "Gemini"],
    ["LangChain", "LangGraph"],
    ["PyTorch", "TensorFlow", "Scikit-learn"]
]

print(ai_categories[0])  # First category
print(ai_categories[0][1])  # Second tool in the first category
print(ai_categories[1])  # First tool in the second category
print(ai_categories[2][1])  # Second tool in the third category
print(len(ai_categories))
print(len(ai_categories[2]))



# nested loop

ai_categories = [
    ["ChatGPT", "Claude", "Gemini"],
    ["LangChain", "LangGraph"],
    ["PyTorch", "TensorFlow", "Scikit-learn"]
]

for item in ai_categories:
    for tool in item:
        print("AI Technology:", tool)
        
        