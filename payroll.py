#Assignment -3 , Task -2(b)

from tabulate import tabulate
print (tabulate([],headers=['\nEmployee Number\t','\nEmployee Name','\t\nHours Worked']))
readFile = open("data.txt", "r")
print(readFile.read())