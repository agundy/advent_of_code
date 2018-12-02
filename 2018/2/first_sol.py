input_file = open("input.txt")

def count_exact_2_and_3(box_id):
    letter_counts = {}
    for char in box_id:
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1

    exactly_2_count = 0
    exactly_3_count = 0

    for count in letter_counts.values():
        if count == 2:
            exactly_2_count += 1
        if count == 3:
            exactly_3_count += 1
    return exactly_2_count, exactly_3_count

exactly_twice_ids = 0
exactly_thrice_ids = 0

for line in input_file:
    line = line.strip()
    two, three = count_exact_2_and_3(line)
    if two > 0:
        exactly_twice_ids += 1
    if three > 0:
        exactly_thrice_ids += 1

print(exactly_twice_ids*exactly_thrice_ids)

input_file.close()
