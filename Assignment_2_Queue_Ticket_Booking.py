# Assignment 2: Queue Implementation
# Scenario: Ticket Booking Counter

class Queue:
    def __init__(self, size):
        self.queue = [None] * size
        self.size = size
        self.front = -1
        self.rear = -1

    # Enqueue - Add customer to the queue
    def enqueue(self, customer):
        if self.rear == self.size - 1:
            print("Queue is full.")
        else:
            if self.front == -1:
                self.front = 0

            self.rear += 1
            self.queue[self.rear] = customer
            print(f"{customer} joined the ticket booking queue.")

    # Dequeue - Remove customer from the front
    def dequeue(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue is empty.")
        else:
            customer = self.queue[self.front]
            print(f"{customer} got the ticket and left the queue.")
            self.queue[self.front] = None
            self.front += 1

            if self.front > self.rear:
                self.front = -1
                self.rear = -1

    # Display - Show all customers in the queue
    def display(self):
        if self.front == -1:
            print("Queue is empty.")
        else:
            print("\nCustomers in the queue:")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i])


# Main program
size = int(input("Enter the size of the queue: "))
queue = Queue(size)

while True:
    print("\n--- Ticket Booking Queue ---")
    print("1. Enqueue (Add Customer)")
    print("2. Dequeue (Serve Customer)")
    print("3. Display Queue")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        customer = input("Enter customer name: ")
        queue.enqueue(customer)

    elif choice == "2":
        queue.dequeue()

    elif choice == "3":
        queue.display()

    elif choice == "4":
        print("Program ended.")
        break

    else:
        print("Invalid choice. Please try again.")
