def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # This is the array implementation
    
    while True:
        display_menu()  # This calls the display_menu function
        
        try:
            choice = int(input("Enter your choice (1-4): "))  # Ensures input is a number
        except ValueError:
            print("Please enter a number between 1 and 4.")
            continue
        
        if choice == 1:
            item = input("Enter item to add: ")
            shopping_list.append(item)
            print(f"'{item}' added to the list.")
        elif choice == 2:
            if not shopping_list:
                print("The shopping list is empty.")
                continue
            item = input("Enter item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' removed from the list.")
            else:
                print(f"'{item}' not found in the list.")
        elif choice == 3:
            if not shopping_list:
                print("Your shopping list is empty.")
            else:
                print("\nCurrent Shopping List:")
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-4.")

if __name__ == "__main__":
    main()