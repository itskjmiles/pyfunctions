# Task 1: Write a function that lets the user add items to a list
def add_item(shopping_list, item):
    shopping_list.append(item)
    print(f"{item} has been added to the list.")

# Task 2: Include a feature to remove items from the list
def remove_item(shopping_list, item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removed from the list.")
    else:
        print(f"{item} is not in the list.")

# Task 3: Add a function that prints out the entire list in a formatted way
def print_list(shopping_list):
    print("Shopping List:")
    for index, item in enumerate(shopping_list, start=1):
        print(f"{index}. {item}")

# Main function to run the shopping list program
def shopping_list_program():
    shopping_list = []

    while True:
        print("\nOptions:")
        print("1. Add item to the list")
        print("2. Remove item from the list")
        print("3. Print the shopping list")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ")
            add_item(shopping_list, item)
        elif choice == '2':
            item = input("Enter the item to remove: ")
            remove_item(shopping_list, item)
        elif choice == '3':
            print_list(shopping_list)
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    shopping_list_program()
