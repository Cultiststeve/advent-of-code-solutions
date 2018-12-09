box_list = open("inputd2.txt")
# box_list = open("sample_input.txt")


for idx_box, box in enumerate(box_list, 0):
    comparison_list = open("inputd2.txt")
    # comparison_list = open("sample_input.txt")
    for idx_comparison, comparison_box in enumerate(comparison_list, idx_box):
        mismatch_count = 0
        for idx_character, character in enumerate(box):
            if character != comparison_box[idx_character]:
                mismatch_count += 1
            if mismatch_count > 1:
                # bad box
                break

        if mismatch_count == 1:
            # matching box
            print("box: {}, comp box: {}".format(box, comparison_box))
            for idx_final_char, char in enumerate(box):
                if char != comparison_box[idx_final_char]:
                    print("mismatch: {} at {}".format(char, idx_final_char))
                    print("Cleaned string: {}{}".format(box[:idx_final_char], box[idx_final_char+1:]))
            exit(0)
