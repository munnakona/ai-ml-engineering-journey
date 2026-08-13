day = 1

while day <= 7:

    if day % 2 == 0:
        result = "Python Practice"
    else:
        result = "AI/ML Theory"

    if day % 5 == 0:
        result = result + " → Milestone Day!"

    print("Day", day, "→", result)

    day += 1