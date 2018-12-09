duplicate_freq = False
curr_freq = 0
previous_freq = [0]
while not duplicate_freq:
    print("Start of file")
    print("Len of prev freqs: {}".format(len(previous_freq)))
    freq_list = open("inputd1.txt")
    for input_freq in freq_list:
        curr_freq += int(input_freq)
        if curr_freq in previous_freq:
            print("First dupe freq: {}".format(curr_freq))
            duplicate_freq = True
            break
        else:
            previous_freq.append(curr_freq)

