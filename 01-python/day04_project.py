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

def display_models(models):
    
    for model, details in models.items():
            print("Model:", model)
            print("Provider:", details["provider"])
            print("Type:", details["type"])
            print()
print("===== AI MODEL UTILITY =====")
         
display_models(ai_models)


        
def count_models(models):
    return len(models)


print("===== SUMMARY =====")

total_ai_models = count_models(ai_models)
print("Total AI Models:", total_ai_models)

def get_provider(models, model_name):
    return models[model_name]["provider"]

provider1 = get_provider(ai_models,"GPT")
provider2 = get_provider(ai_models,"Gemini")
print("GPT Provider:",provider1)
print("Gemini Provider:",provider2)

def get_model_names(models):
    model_names = []

    for item  in models:
        model_names.append(item)

    return model_names

model_names = get_model_names(ai_models)

print("Model Names:", model_names)