
# Assignment -3 , Task - 2(b)

# File Name: payroll.py
# Author's name: Anuben Keshavala
# Student Number: 301120629
# File description: Copy the source file and paste into the Destination file

Source = input(" Source : ")

# It will ask user to input the Destination File name:

Destination = input(" Destination : ")

with open(Source) as f:
    with open(Destination, "w") as f1:
        for line in f:
            f1.write(line)



           