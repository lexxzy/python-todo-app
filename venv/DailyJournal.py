Journal = "journal"
Daily_Date = input("Enter today's date: ")
Mood = input("How do you rate your mood today from 1 to 10? ")
thoughts = input("Let you thoughts flow:\n")
with open(f"./{Journal}/{Daily_Date}.txt", "w") as file:
    file.write(Mood + "\n" * 2)
    file.write(thoughts)