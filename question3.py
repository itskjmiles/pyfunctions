# Task 1: Code a function to calculate the average grade
def calculate_average(grades):
    if not grades:
        return "No grades provided."
    return sum(grades) / len(grades)

# Task 2: Implement a function to find the highest and lowest grade
def find_highest_lowest(grades):
    if not grades:
        return "No grades provided."
    highest = max(grades)
    lowest = min(grades)
    return highest, lowest

# Task 3: Create a feature that categorizes grades into letter grades
def categorize_grades(grades):
    if not grades:
        return "No grades provided."
    letter_grades = []
    for grade in grades:
        if grade >= 90:
            letter_grades.append("A")
        elif grade >= 80:
            letter_grades.append("B")
        elif grade >= 70:
            letter_grades.append("C")
        elif grade >= 60:
            letter_grades.append("D")
        else:
            letter_grades.append("F")
    return letter_grades

# Main function to analyze grades
def analyze_grades(grades):
    average = calculate_average(grades)
    highest, lowest = find_highest_lowest(grades)
    letter_grades = categorize_grades(grades)

    print("Grade Statistics:")
    print("Average Grade:", average)
    print("Highest Grade:", highest)
    print("Lowest Grade:", lowest)
    print("Letter Grades:", letter_grades)

# Example usage
if __name__ == "__main__":
    grades = [85, 92, 78, 90, 88]
    analyze_grades(grades)
