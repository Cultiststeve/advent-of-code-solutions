input = open("input/day1.txt")

freq = 0
for line in input:
    freq += int(line)

print(freq)
