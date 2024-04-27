# Task 1
def log_activities(activities, duration):
    log = dict(zip(activities, duration))
    return log

# Task 2
def calculate_calories_burned(activity, duration):
    return duration * 3.5  # Assuming a constant calorie burn rate

# Task 3
def generate_summary(activity_log):
    total_calories = 0
    print("Fitness Activity Log:")
    for activity, duration in activity_log.items():
        calories_burned = calculate_calories_burned(activity, duration)
        total_calories += calories_burned
        print(f"{activity}: {duration} minutes | Calories Burned: {calories_burned}")
    print(f"Total Calories Burned Today: {total_calories}")

def run_fitness_tracker():
    activities = ['Dancing', 'Swimming', 'Biking']
    duration = [10, 20, 15]
    activity_log = log_activities(activities, duration)
    generate_summary(activity_log)
    
if __name__ == "__main__":
    run_fitness_tracker()
