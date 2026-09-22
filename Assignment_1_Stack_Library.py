# Assignment 1: Stack Implementation
# Scenario: Library Returned Books

class Stack:
    def __init__(self):
        self.stack = []

    # Return Book - Push
    def push(self, book):
        self.stack.append(book)
        print(f"{book} returned and added to the stack.")

    # Arrange Book - Pop
    def pop(self):
        if not self.stack:
            print("No books in the stack.")
        else:
            book = self.stack.pop()
            print(f"{book} arranged and removed from the stack.")

    # Top Book - Peek
    def peek(self):
        if not self.stack:
            print("No books in the stack.")
        else:
            print(f"Top book: {self.stack[-1]}")

    # Display Stack
    def display(self):
        if not self.stack:
            print("Stack is empty.")
        else:
            print("\nBooks in the stack (Top to Bottom):")
            for book in reversed(self.stack):
                print(book)


# Main program
stack = Stack()

while True:
    print("\n--- Library Book Stack ---")
    print("1. Return Book (Push)")
    print("2. Arrange Book (Pop)")
    print("3. Top Book (Peek)")
    print("4. Display Stack")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        stack.push(book)

    elif choice == "2":
        stack.pop()

    elif choice == "3":
        stack.peek()

    elif choice == "4":
        stack.display()

    elif choice == "5":
        print("Program ended.")
        break

    else:
        print("Invalid choice. Please try again.")
