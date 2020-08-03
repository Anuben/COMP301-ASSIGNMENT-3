#Assignment -3 , Task -2(b)

from tabulate import tabulate
print (tabulate([],headers=['\nEmployee Number\t','\nEmployee Name','\t\nHours Worked']))
with open("data.txt", "r") as filestream:

        for line in filestream:
            currentline = line.split(',')
            total = str(str(currentline[0]) + str(currentline[1] + str(currentline[2])))
            #filestreamtwo.write(total)
            print(total)
