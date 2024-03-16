sums = []
total = 0
new_lines = []
with open('input4.txt') as f:
    lines = f.readlines()
    #print(lines)
    for line in lines:
        line = line.split('|')
        
        line[0] = line[0].split(':') #card number line[0][0]
        line[0][0] = line[0][0].split()[1].rstrip(':')
        #line[0][0] = line[0][0].split('Card ')
        #line[0][0] = [num for num in line[0][0] if num != '']
        line[0][1] = line[0][1].strip() #winning number
        line[0][1] = line[0][1].split(' ')
        line[1] = line[1].strip() #your numbers
        line[1] = line[1].split(' ')
        line[0][1] = [num for num in line[0][1] if num != '']
        line[1] = [num for num in line[1] if num != '']
        new_lines.append([line[0][0], line[0][1], line[1]])


def bruh(line, counter):
    #print(line)
    match = 0
    for num in line[2]:
        if num in line[1]:
            match += 1
    #print(match)
    if match == 0:
        return counter
    else:
        for j in range(1, match+1):
            counter += 1
            counter = bruh(new_lines[j+int(line[0])-1], counter)
    return counter

counter = 0        
for li in new_lines:
    counter = bruh(li, counter)

    #for n in sums:
    #    total += n[0]
    #print(sums)
print(counter+193)
    #print(total)