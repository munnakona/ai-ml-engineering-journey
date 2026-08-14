ai_technology_inventory = [
    ["AI Models", ["ChatGPT", "Claude", "Gemini", "Llama"]],
    ["AI Frameworks", ["LangChain", "LangGraph"]],
    ["ML Frameworks", ["PyTorch", "TensorFlow", "Scikit-learn"]]
]

print ("===== AI TECHNOLOGY INVENTORY =====")

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