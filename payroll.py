# Assignment -3 , Task - 2(b)

# File Name: payroll.py
# Author's name: Anuben Keshavala
# Student Number: 301120629
# File description: Read .txt file and print the output

from tabulate import tabulate
print (tabulate([],headers=['\nEmployee Number\t','\nEmployee Name','\t\nHours Worked']))

# It will read the data.txt file and ignore the comma and then give output

with open("data.txt", "r") as filestream:

        for line in filestream:
            currentline = line.split(",")
            total = str(str(currentline[0]) + str(currentline[1] + str(currentline[2])))
            print(total)
            

