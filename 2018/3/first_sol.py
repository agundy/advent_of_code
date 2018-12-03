input_file = open("input.txt")

claims = input_file.readlines()

input_file.close()

fabric = [['.']*1000 for i in range(1000)]

def claim_fabric(claim_id, start_x, start_y, length_x, length_y):
    for i in range(start_x, start_x + length_x):
        for j in range(start_y, start_y + length_y):
            if fabric[j][i] == '.':
                fabric[j][i] = claim_id
            else:
                fabric[j][i] = "#"


    fabric

for claim in claims:
    print(claim)
    claim_id, remainder = claim.split(' @ ')
    start, dimensions = remainder.split(': ')

    start_x, start_y = start.split(',')
    start_x, start_y = int(start_x), int(start_y)
    length_x, length_y = dimensions.split('x')
    length_x, length_y = int(length_x), int(length_y)
    print(claim_id)
    print(start_x, start_y)
    print(length_x, length_y)
    claim_fabric(claim_id, start_x, start_y, length_x, length_y)

count = 0
for row in fabric:
    for square in row:
        if square == '#':
            count += 1

print(count)
