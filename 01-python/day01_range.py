for number in range(1, 11):
    print(number)
    
for day in range(1, 8):
    print("AI Learning Day:", day)
    

for number in range(1, 21):

    if number % 2 == 0:
        result = "Even"
    else:
        result = "Odd"

    if number % 5 == 0:
        result = result + " → Divisible by 5"

    print(number, "→", result)