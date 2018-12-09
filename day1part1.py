freq_list = open("input/day1.txt")

freq = 0
for line in freq_list:
    freq += int(line)

print(freq)
