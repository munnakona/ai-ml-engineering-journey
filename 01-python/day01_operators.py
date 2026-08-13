experience = 14
genai_years = 2
devops_years = 12

print("Total relevant experience:", genai_years + devops_years)
print("Experience after 5 years:", experience + 5)
print("Is experience greater than 10?", experience > 10)
print("Is GenAI experience greater than 1?", genai_years > 1)


has_devops = True
has_genai = True


if experience >= 10 and has_devops and has_genai:
    print("Strong candidate for AI Platform Engineering")
    
    
if experience >= 15:
    print("Career Level: AI Architect")
elif experience >= 10:
    print("Career Level: AI Platform Engineer")
elif experience >= 5:
    print("Career Level: AI Engineer")
else:
    print("Career Level: Continue building experience")
    
    

experience = 14
genai_years = 2
devops_years = 12


if experience >= 15 and genai_years >= 3 and devops_years >= 10:
    print("Recommended: AI Architect / AI Platform Architect")
elif experience >= 10 and genai_years >= 2 and devops_years >= 10:
    print("Recommended: AI Platform / MLOps Engineer")
else:
    print("Continue developing AI/ML skills")
          