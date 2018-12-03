input_file = open("input.txt")

claim_lines = input_file.readlines()

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

def check_claim(claim):
    start_x, start_y, length_x, length_y = claim['start_x'], claim['start_y'], claim['length_x'], claim['length_y']
    for i in range(start_x, start_x + length_x):
        for j in range(start_y, start_y + length_y):
            if fabric[j][i] == '#':
                return False

    return True


claims = []
for claim in claim_lines:
    claim_id, remainder = claim.split(' @ ')
    start, dimensions = remainder.split(': ')

    start_x, start_y = start.split(',')
    start_x, start_y = int(start_x), int(start_y)
    length_x, length_y = dimensions.split('x')
    length_x, length_y = int(length_x), int(length_y)

    claims.append({
        'claim_id': claim_id,
        'start_x': start_x,
        'start_y': start_y,
        'length_x': length_x,
        'length_y': length_y,
        })

for claim in claims:
    claim_fabric(claim['claim_id'], claim['start_x'], claim['start_y'], claim['length_x'], claim['length_y'])

for claim in claims:
    if check_claim(claim):
        print(claim)
    
count = 0
for row in fabric:
    for square in row:
        if square == '#':
            count += 1

print(count)
