"""
Mikayla Settles-Chambers
CMSC 111
Spring 2026
Week 9 Assignment 2
"""
# Function that attempts to open a missing file
def check_file():
    try:
        # Trying to open a file that is not there
        file = open("missing_file.txt", "r")
        file.close()

    except FileNotFoundError:
        # This runs if the file does not exist
        print("File not found!")


# Main function to run the program
def main():
    check_file()


# Start the program
main()