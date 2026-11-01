Create P-4 undo redo
# Undo/Redo System in Python

class TextEditor:
    # Initialize the document and stacks
    def __init__(self):
        self.document = ""      # Stores the current text
        self.undo_stack = []    # Stores previous states
        self.redo_stack = []    # Stores undone states

    # Add new text to the document
    def make_change(self, change):
        self.undo_stack.append(self.document)  # Save previous state
        self.document += change               # Add new text
        self.redo_stack.clear()               # Clear redo history
        print("\nChange made.")
        self.display_state()                  # Display current text

    # Undo the last change
    def undo_action(self):
        if self.undo_stack:  # Check if undo is possible
            self.redo_stack.append(self.document)  # Save current state
            self.document = self.undo_stack.pop()  # Restore previous state
            print("\nUndo performed.")
        else:
            print("\nNo more actions to undo.")

        self.display_state()  # Display current text

    # Redo the undone change
    def redo_action(self):
        if self.redo_stack:  # Check if redo is possible
            self.undo_stack.append(self.document)  # Save current state
            self.document = self.redo_stack.pop()  # Restore undone state
            print("\nRedo performed.")
        else:
            print("\nNo more actions to redo.")

        self.display_state()  # Display current text

    # Display the current document
    def display_state(self):
        print("Current Document State: '" + self.document + "'")

    # Display the menu and accept user choices
    def run_editor(self):
        while True:
            print("\n--- MENU ---")
            print("1. Make a Change")
            print("2. Undo")
            print("3. Redo")
            print("4. Display Document State")
            print("5. Exit")

            choice = input("Enter your choice: ")  # Get user choice

            if choice == '1':
                change = input("Enter text to add: ")
                self.make_change(change)  # Call make_change()

            elif choice == '2':
                self.undo_action()  # Call undo_action()

            elif choice == '3':
                self.redo_action()  # Call redo_action()

            elif choice == '4':
                self.display_state()  # Show current document

            elif choice == '5':
                print("Exiting...")
                break  # Stop the loop

            else:
                print("Invalid choice. Try again.")


# Create an object of the TextEditor class
editor = TextEditor()

# Start the editor
editor.run_editor()