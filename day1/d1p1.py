freq_list = open("inputd1.txt")

freq = 0
for line in freq_list:
    freq += int(line)

print(freq)
