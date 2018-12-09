box_list = open("inputd2.txt")

duplicate_boxes = 0
triplicate_boxes = 0
for box in box_list:
    checked_letters = []
    duplicate = False
    triplicate = False
    for letter in box:
        # only check each letter once
        if letter in checked_letters:
            continue
        checked_letters.append(letter)
        multiple_count = box.count(letter)
        if multiple_count == 2:
            duplicate = True
        elif multiple_count == 3:
            triplicate = True
    if duplicate:
        duplicate_boxes += 1
    if triplicate:
        triplicate_boxes += 1

print(duplicate_boxes)
print(triplicate_boxes)
print(duplicate_boxes * triplicate_boxes)

