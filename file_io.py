"""
Mikayla Settles-Chambers
CMSC 111
Spring 2026
Week 9 Assignment 1
"""

# This program reads from a file, writes user input to a new file, and then adds more text to that file.

# Part 1: Read and display the file
def read_input_file():
    with open("input.txt", "r") as file:
        data = file.read()
        print("Here is what is inside input.txt:\n")
        print(data)


# Part 2: Write user input to a new file
def write_output_file():
    text = input("\nEnter something to save into a file: ")
    
    with open("output.txt", "w") as file:
        file.write(text)

    print("Your input was saved.")


# Part 3: Append extra text
def append_to_file():
    with open("output.txt", "a") as file:
        file.write("\nHello, World!")

    print("Added more text to the file.")


# Run everything
def main():
    read_input_file()
    write_output_file()
    append_to_file()


main()