task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"'{task}'"

if time_bound == "yes":
    print(f"Reminder: {reminder} that requires immediate attention today!")
else:
    if priority == "low":
        print(f"{reminder}. Consider completing it when you have free time.")
    else:
        print(f"Reminder: {reminder}.")