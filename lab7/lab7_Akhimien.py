"""
Efuah Akhimien-Mhonan
Feb 19, 2026
Lab 7, Working with data in Python
"""

print("\n ----- Example 1: read file")
with open("phrases.txt", "r") as file1:
    filecontent = file1.read(30)
    print(filecontent)
    filecontent = file1.read(5)
    print(filecontent)

# check if the file is closed.
print(f"\nIs the file closed? {file1.closed}")


print("\n ----- Example 2: readline file")
with open("phrases.txt", "r") as file1:
    filecontent = file1.readline(30)
    print(filecontent)
    filecontent = file1.readline(5)
    print(filecontent)


print("\n ----- Example 3: readlines file")
# readlines makes a list of all the lines in the text file.
with open("phrases.txt", "r") as file1:
    filecontent = file1.readlines()
    print(filecontent)
    filecontent = file1.readlines(5)
    print(filecontent)


print("\n ----- Example 4: loop through each line in a file")
with open("phrases.txt", "r") as file1:
    filecontent = file1.readlines()
    for eachline in filecontent:
        print(eachline.strip())   # strip() method removes \n in each line


print("\n ----- Example 5: create file")
# w mode create a file if the file doesn't exist.
# On the other hand, if the file exists, w mode will overwrite the data in the file
with open("Akhimien.txt", "w") as file:
    file.write("Python basics for data science\n")
    file.write("Efuah Akhimien-Mhonan")


print("\n ----- Example 6: append data into an existing file")
# append the date and time into "lastname.txt" file
from datetime import datetime

with open("Akhimien.txt", "a") as file:
    file.write(f"\nLast update: {datetime.now()}")


print("\n ----- Example 7: copy a file")
# copy file "Akhimien.txt" into a new file
with open("Akhimien.txt", "r") as readfile:
    with open("newfile.txt", "w") as writefile:
        for eachline in readfile:
            writefile.write(eachline)


print("\n ----- Example 8: pandas a file")

import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age' : [25, 30, 35]
}

df = pd.DataFrame(data)
print(df)


print("\n ----- Example 9: creating df with pandas from an excel file")
df = pd.read_excel("classdata.xlsx")
print(df)
print(df.head())

print("\n ----- EXERCISE ")

def email_read(filename):
    gmail = 0
    yahoo = 0
    hotmail = 0

    try:
        with open(filename, "r") as file:
            for line in file:
                if "@gmail.com" in line:
                    gmail += 1
                elif "@yahoo.com" in line:
                    yahoo += 1
                elif "@hotmail.com" in line:
                    hotmail += 1

    except FileNotFoundError:
        print("File not found.")
        return None
    except Exception as e:
        print("Error:", e)
        return None

    return gmail, yahoo, hotmail


# ---- TEST THE FUNCTION ----
result = email_read("user_email.txt")

if result:
    gmail, yahoo, hotmail = result

    # create report file
    with open("reportemail.txt", "w") as report:
        report.write(f"gmail = {gmail}\n")
        report.write(f"yahoo = {yahoo}\n")
        report.write(f"hotmail = {hotmail}\n")

    print("Email report created successfully.")