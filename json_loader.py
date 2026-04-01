"""
Mikayla Settles-Chambers
CMSC 111
Spring 2026
Week 9 Assignment 3
"""
# This program tries to load a JSON file and handles errors if the formatting is incorrect.

import json


# Function to load JSON data
def load_json_file():
    try:
        # Attempt to open and read the JSON file
        with open("data.json", "r") as file:
            data = json.load(file)

        # If no errors happen
        print("JSON loaded successfully.")

    except json.JSONDecodeError:
        # Runs if JSON format is invalid
        print("Invalid JSON format!")

    except FileNotFoundError:
        # Runs if file is missing
        print("File not found!")


# Run the program
def main():
    load_json_file()


main()