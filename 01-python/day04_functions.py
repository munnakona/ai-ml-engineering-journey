def start_ai_learning():
    print("Starting AI/ML Learning")
    print("Python")
    print("Machine Learning")
    print("Generative AI")
    print("LangChain")

start_ai_learning()



def learn_topic(topic):
    print("Today I am learning:", topic)


learn_topic("Python")
learn_topic("Machine Learning")
learn_topic("Generative AI")
learn_topic("LangChain")

def show_ai_model(name, provider, model_type):
    print("Model:", name)
    print("Provider:", provider)
    print("Type:", model_type)
    print()



show_ai_model("GPT ","OpenAI","LLM")

show_ai_model("Claude","Anthropic","LLM")
show_ai_model("Gemini","Google","LLM")
show_ai_model("Llama","Meta","LLM")


def calculate_sum(a, b):
    return a + b

result = calculate_sum(10, 20)

print("Sum:", result)

def calculate_model_count(models):
    return len(models)

ai_models = [
    "GPT",
    "Claude",
    "Gemini",
    "Llama"
]

count = calculate_model_count(ai_models)

print("Total AI Models:", count)



def get_model_name(model):
    return model["name"]


ai_model = {
    "name": "GPT-5",
    "provider": "OpenAI",
    "type": "LLM"
}

name = get_model_name(ai_model)

print("Model Name:", name)

def get_model_type(model):
    return model["type"]


type = get_model_type(ai_model)
print("Model Type:",type)



def introduce_ai_engineer(name="Munna", role="AI/ML Engineer"):
    print("Name:", name)
    print("Role:", role)
    
introduce_ai_engineer()

introduce_ai_engineer("Munna", "Generative AI Engineer")


def introduce_ai_engineer(name="Munna", role="AI/ML Engineer"):
    print("Name:", name)
    print("Role:", role)
    
introduce_ai_engineer(
    role="Generative AI Engineer",
    name="Munna"
)
introduce_ai_engineer(
    role="GenAI Developer"
)

def learn_topic():
    topic = "Generative AI"
    print("Inside function:", topic)


learn_topic()
# print("Outside function:", topic)


topic = "Generative AI"


def learn_topic():
    print("Inside function:", topic)


learn_topic()

print("Outside function:", topic)


def get_first_model(models):
    return models[0]


ai_models = [
    "GPT",
    "Claude",
    "Gemini",
    "Llama"
]

first_model = get_first_model(ai_models)

print("First AI Model:", first_model)

def get_last_model(models):
    return models[-1]

last_model = get_last_model(ai_models)
print("Last AI Model:",last_model)


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

def get_provider(models, model_name):
    return models[model_name]["provider"]

print("GPT Provider:", get_provider(ai_models, "GPT"))
print("Claude Provider:", get_provider(ai_models, "Claude"))
print("Gemini Provider:", get_provider(ai_models, "Gemini"))
print("Llama Provider:", get_provider(ai_models, "Llama"))


def display_models(models):

    for model, details in models.items():
        print("Model:", model)
        print("Provider:", details["provider"])
        print("Type:", details["type"])
        print()
        
display_models(ai_models)


def count_models(models):
    return len(models)

total = count_models(ai_models)

print("Total AI Models:", total)






