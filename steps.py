def main():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    week_number = int(input("How many weeks are you tracking your steps?"))

    total_steps = 0
    total_days = week_number * 7

    for week in range(1, week_number + 1):
        print(f"Week {week}:")
        for day in days:
            steps = int(input(f"Enter steps for {day}:"))
            total_steps += steps


    average_steps = total_steps / total_days

    print(f"In {total_days} days:")
    print(f"Total steps: {total_steps}")
    print(f"Average steps per day: {average_steps:.2f}")
main()