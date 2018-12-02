input_file = open("input.txt")

def off_by_one(box_id_1, box_id_2):
    off_by = 0
    for i in range(len(box_id_1)):
        if box_id_1[i] != box_id_2[i]:
            off_by += 1

        if off_by > 1:
            return False

    return off_by == 1

box_ids = input_file.read().strip().split()

for i in range(0, len(box_ids)):
    for j in range(1, len(box_ids)):
        if off_by_one(box_ids[i], box_ids[j]):
            print(box_ids[i], box_ids[j])

input_file.close()
