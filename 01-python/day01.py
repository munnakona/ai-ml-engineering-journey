name = input("Enter your name: ")
experience = input("Enter your years of experience: ")

print("Before conversion:", type(experience))

experience = int(experience)

print("After conversion:", type(experience))

future_experience = experience + 5

print("Name:", name)
print("Current Experience:", experience)
print("Experience after 5 years:", future_experience)