file = open("log.txt")
lines = file.readlines()
file.close()

val = 0

for line in lines:
    val += (int(line.split(">")[1].split("/")[0]))


print(val)
