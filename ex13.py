# Parameters, Unpacking, Variables

from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

print("This script is called: ", script)
print("Your first variable is: ", first)
print("Your second variable is: ", second)
print("Your third variable is: ", third)

# to run this script, type: python3 ex13.py anything1 anything2 anything3

###
# REAL WORLD EXAMPLE 1: Batch File Renamer Script 
# USE CASE: You want to rename a file from the command line. (rename rename_file.py)
###

from sys import argv
import os

script, old_name, new_name = argv

os.rename(old_name, new_name)
print(f"renamed '{old_name}' to '{new_name}'")
# To run this code, type: python rename_file.py oldfile.txt newfile.txt

###
# REAL WORLD EXAMPLE 2: CSV Filter by Column
# USE CASE: Filter a CSV file and save only rows with a specific value in a column. (filter_csv.py)
###

from sys import argv
import csv

script, input_file, comlumn_name, value = argv

with open(input_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row[comlumn_name] == value:
            print(row)

# To run this code, type: python filter_csv.py data.csv country Malaysia
# It will print rows in data.csv where the country column equals Malaysia
