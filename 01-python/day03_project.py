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


model_categories = (
    "LLM",
    "Generative AI",
    "Foundation Model"
)

providers = set()

for model, details in ai_models.items():
    providers.add(details["provider"])
    
print("Unique Providers:", providers)

model_names = []

for model in ai_models:
    model_names.append(model)


print("Models:", model_names)


print("===== AI MODEL REGISTRY =====")

for model, details in ai_models.items():
    print("Model:", model)
    print("Provider:", details["provider"])
    print("Type:", details["type"])
    print()
    
    
print("===== REGISTRY SUMMARY =====")
print("Total Models:", len(ai_models))
print("Total Providers:", len(providers))
print("Model Categories:", model_categories)
