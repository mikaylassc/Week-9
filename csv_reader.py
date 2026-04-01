"""
Mikayla Settles-Chambers
CMSC 111
Spring 2026
Assignment 4, Week 9
"""
# This program reads student data from a CSV file and checks for missing or invalid values.

import csv

print("Program is running...")  # This makes sure the program actually starts

def process_csv(filename):
    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            name = row["name"]
            age = row["age"]
            grade = row["grade"]

            # Check for missing values first
            if age == "":
                print(f"Invalid record for {name}: missing age")
                continue

            if grade == "":
                print(f"Invalid record for {name}: missing grade")
                continue

            # Check for invalid numbers using try/except
            try:
                age = int(age)
            except ValueError:
                print(f"Invalid record for {name}: age is not a number")
                continue

            try:
                grade = int(grade)
            except ValueError:
                print(f"Invalid record for {name}: grade is not a number")
                continue

            # If everything is valid
            print(f"Valid record: {name} (Age: {age}, Grade: {grade})")

# Run the program
def main():
    process_csv("./students.csv")  # Use ./ to point to the current folder

main()
