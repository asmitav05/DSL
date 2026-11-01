Create P-7 hashing using chain
# Assignment 7: Hashing Using Chaining


# Class to create a hash table
class HashTable:

    # Initialize the hash table
    def __init__(self, size=10):

        self.size = size  # Store the size of the table

        # Create 10 empty lists
        self.table = [[] for _ in range(size)]


    # Function to calculate the index
    def hash_function(self, key):

        # Find the remainder to get the index
        return key % self.size


    # Function to insert a key and value
    def insert(self, key, value):

        # Find the index for the key
        index = self.hash_function(key)

        # Check whether the key already exists
        for i, pair in enumerate(self.table[index]):

            # If the key exists, update its value
            if pair[0] == key:
                self.table[index][i] = (key, value)
                print("Key updated successfully.")
                return

        # Add the new key-value pair to the bucket
        self.table[index].append((key, value))

        print("Key inserted successfully.")


    # Function to search for a key
    def search(self, key):

        # Find the index for the key
        index = self.hash_function(key)

        # Check every pair at that index
        for pair in self.table[index]:

            # If the key matches, return its value
            if pair[0] == key:
                return pair[1]

        # Return None if the key is not found
        return None


    # Function to delete a key
    def delete(self, key):

        # Find the index for the key
        index = self.hash_function(key)

        # Check every pair at that index
        for pair in self.table[index]:

            # Check whether the key matches
            if pair[0] == key:

                # Remove the key-value pair
                self.table[index].remove(pair)

                print("Key deleted successfully.")
                return

        # Display this message if the key is not found
        print("Key not found.")


    # Function to display the hash table
    def display(self):

        # Visit every index
        for i in range(self.size):

            # Display the index and its contents
            print(i, ":", self.table[i])


# Main function
def main():

    # Create a hash table of size 10
    ht = HashTable(10)

    # Repeat the menu until the user exits
    while True:

        print("\n--- Hash Table Menu ---")
        print("1. Insert")
        print("2. Search")
        print("3. Delete")
        print("4. Display")
        print("5. Exit")

        # Accept the user's choice
        choice = input("Enter your choice: ")


        # Option 1: Insert a key-value pair
        if choice == '1':

            key = int(input("Enter key: "))
            value = input("Enter value: ")

            ht.insert(key, value)


        # Option 2: Search for a key
        elif choice == '2':

            key = int(input("Enter key to search: "))

            result = ht.search(key)

            # Check whether the key was found
            if result is not None:
                print("Value found:", result)
            else:
                print("Key not found.")


        # Option 3: Delete a key
        elif choice == '3':

            key = int(input("Enter key to delete: "))

            ht.delete(key)


        # Option 4: Display the hash table
        elif choice == '4':

            ht.display()


        # Option 5: Exit the program
        elif choice == '5':

            print("Program ended.")
            break


        # Handle an invalid choice
        else:
            print("Invalid choice. Try again.")


# Start the program
if __name__ == "__main__":
    main()