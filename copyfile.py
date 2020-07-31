# Assignment -3 Task: 1

Source = input(" Source : ")


Destination = input(" Destination : ")

with open(Source) as f:
    with open(Destination, "w") as f1:
        for line in f:
            f1.write(line)



           