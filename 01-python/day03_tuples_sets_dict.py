# Tuple 

ai_tools = (
    "ChatGPT",
    "Claude",
    "Gemini",
    "LangChain",
    "LangGraph"
)

print(ai_tools)
print(type(ai_tools))
print("Number of AI tools:", len(ai_tools))

print(ai_tools[0])
print(ai_tools[-1])
print(ai_tools[1:4])

# ai_tools[0] = "GPT"  # This will cause an error since tuples are immutable

ai_model = (
    "GPT",
    "OpenAI",
    "LLM"
)

name, provider, model_type = ai_model

print("Name:", name)
print("Provider:", provider)
print("Type:", model_type)

devops_stack = (
    "Jenkins",
    "Docker",
    "Kubernetes"
)

tool1, tool2, tool3 = devops_stack

print("Tool 1:", tool1)
print("Tool 2:", tool2)
print("Tool 3:", tool3) 


# tuple methods count() and index()

ai_models = (
    "GPT",
    "Gemini",
    "GPT",
    "Claude",
    "Gemini",
    "GPT",
    "Llama"
)

print("Count of GPT:", ai_models.count("GPT"))
print("Count of Gemini:", ai_models.count("Gemini"))
print("Index of Claude:", ai_models.index("Claude"))
print("Index of Llama:", ai_models.index("Llama"))  # Returns the first occurrence

# Sets

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

ai_tools = {
    "ChatGPT",
    "Claude",
    "Gemini"
}

ai_tools.add("Llama")
print(ai_tools)
ai_tools.add("LangGraph")
print(ai_tools)

ai_tools.add("ChatGPT")  # Adding a duplicate element has no effect
print(ai_tools)

print("Number of unique tools:", len(ai_tools))



ai_tools = {
    "ChatGPT",
    "Claude",
    "Gemini",
    "Llama",
    "LangGraph"
}
ai_tools.remove("Claude")
print(ai_tools)

ai_tools.discard("Gemini")
print(ai_tools)

ai_tools.discard("Python")

#ai_tools.remove("Python")



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


all_tools = devops_tools | ai_tools
print("All tools:", all_tools)

common_tools = devops_tools & ai_tools
print("Common tools:", common_tools)

devops_only = devops_tools - ai_tools
print("DevOps only tools:", devops_only)


ai_only = ai_tools - devops_tools
print("AI only tools:", ai_only)

# Dictionary


ai_model = {
    "name": "GPT",
    "provider": "OpenAI",
    "type": "LLM",
    "category": "Generative AI"
}

print(ai_model)
print(type(ai_model))
print("Number of properties:", len(ai_model))


print("Name:", ai_model["name"])
print("Provider:", ai_model["provider"])
print("Type:", ai_model["type"])
print("Category:", ai_model["category"])



ai_model = {
    "name": "GPT",
    "provider": "OpenAI",
    "type": "LLM",
    "category": "Generative AI"
}


print(ai_model)

print (type(ai_model))
print("Number of Prpoperties:", len(ai_model))
print("Name:", ai_model["name"])
print("Provider:", ai_model["provider"])
print("Type:", ai_model["type"])
print("Category:", ai_model["category"])



ai_model = {
    "name": "GPT",
    "provider": "OpenAI",
    "type": "LLM"
}


ai_model["name"] = "GPT-5"

print(ai_model)


ai_model["context_window"] = 128000
print(ai_model)

ai_model["temperature"] = 0.7


print(ai_model)
print("Model:", ai_model["name"])
print("Context Window:", ai_model["context_window"])
print("Temperature:", ai_model["temperature"])



ai_model = {
    "name": "GPT-5",
    "provider": "OpenAI",
    "type": "LLM",
    "context_window": 128000,
    "temperature": 0.7
}

removed_temperature = ai_model.pop("temperature")

print("Removed Temperature:", removed_temperature)
print(ai_model)

del ai_model["context_window"]
print(ai_model)

ai_model.clear()
print(ai_model)

ai_model = {
    "name": "GPT-5",
    "provider": "OpenAI",
    "type": "LLM",
    "context_window": 128000,
    "temperature": 0.7
}

print("Keys:")
print(ai_model.keys())

print("Values:")
print(ai_model.values())

print("Items:")
print(ai_model.items())

ai_model = {
    "name": "GPT-5",
    "provider": "OpenAI",
    "type": "LLM",
    "context_window": 128000,
    "temperature": 0.7
}

print("===== AI MODEL CONFIGURATION =====")

for key, value in ai_model.items():
    print(key, "→", value)
    
    
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
    }
}



print("GPT Provider:", ai_models["GPT"]["provider"])
print("Claude Provider:", ai_models["Claude"]["provider"])
print("Gemini Provider:", ai_models["Gemini"]["provider"])



ai_models["Llama"] = {
    "provider": "Meta",
    "type": "LLM"
}


print(ai_models["Llama"]["provider"])



print("===== AI MODEL REGISTRY =====")

for model, details in ai_models.items():
    print("Model:", model)
    print("Provider:", details["provider"])
    print("Type:", details["type"])
    print()







