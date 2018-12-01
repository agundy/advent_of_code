f = open('first_input.txt')
lines = f.readlines()

starting_frequency = 0

for line in lines:
  starting_frequency += int(line)

print(starting_frequency)

f.close()
