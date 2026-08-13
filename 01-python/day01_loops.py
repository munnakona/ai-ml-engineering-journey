technologies = [
    "Python",
    "Docker",
    "Kubernetes",
    "Jenkins",
    "Azure",
    "Linux",
    "Tomcat",
    "WebLogic",
    "LangChain",
    "LangGraph"
]

for technology in technologies:
    if technology == "Kubernetes":
        print(technology, "→ Container orchestration")
    elif technology == "Python":
        print(technology, "→ AI/ML programming language")
    elif technology == "LangGraph":
        print(technology, "→ Agentic AI framework")
    else:
        print(technology, "→ Currently learning")