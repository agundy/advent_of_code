f = open('first_input.txt')
lines = f.readlines()
f.close()

frequency = 0
ending_frequencies = set()
found = False

while not found:
    for line in lines:
      frequency += int(line)
      if frequency in ending_frequencies:
        print(frequency)
        found = True
        break
      else:
        ending_frequencies.add(frequency)
