digits = ['1','2','3','4','5','6','7','8','9','0']
curr_num = ''
start = 0
end = 0
valid_parts = []
all_parts = []
gear_ratios = []
mult = 1

with open('input3.txt') as f:
    lines = f.readlines()
    print(lines)
    for j, line in enumerate(lines):
        line = line.strip()
        for i, char in enumerate(line):
            if char in digits:
                if curr_num == '':
                    start = i
                curr_num += char
            elif char not in digits and curr_num != '':
                print(curr_num)
                print(j)
                end = i
                j_prime = j
                print("ENDBJCBD", end, j)
                if start != 0 and end == 0:
                    end = len(line)-1
                    j_prime = j-1
                print("START END", start, end)
                all_parts.append([int(curr_num), j_prime, start, end-1])
                if start != 0:
                    start = start-1
                if end != len(line)-1:
                    end = end+1
                for k in range(start, end):
                    if j_prime-1 >= 0:
                        print("BEFORE", lines[j_prime-1][k])
                        if lines[j_prime-1][k] not in digits and lines[j_prime-1][k] != '.':
                            valid_parts.append(curr_num)
                    print("IN", lines[j_prime][k])
                    if lines[j_prime][k] not in digits and lines[j_prime][k] != '.':
                        valid_parts.append(curr_num)
                    if j_prime+1 <= len(lines)-1:
                        print("AFTER", lines[j_prime+1][k])
                        if lines[j_prime+1][k] not in digits and lines[j_prime+1][k] != '.':
                            valid_parts.append(curr_num)
                curr_num = ''
                start = 0
                end = 0

int_valid = []
summ = 0
for num in valid_parts:
    summ += int(num)
    int_valid.append(int(num))
#print(len(valid_parts))
#print(summ)
#print(int_valid)
#print(lines[39][137])
print(all_parts)

ratios = set()

with open('input3.txt') as f:
    lines = f.readlines()
    #print(lines)
    for j, line in enumerate(lines):
        line = line.strip()
        for i, char in enumerate(line):
            if char == '*':
                print("NEW", j, i)
                if j > 0:
                    #print(lines[j-1][i-1], lines[j-1][i], lines[j-1][i+1])
                    if lines[j-1][i-1] or lines[j-1][i] or lines[j-1][i+1] in digits:
                        for n in all_parts:
                            if n[1] == j-1:
                                #print(i-1, i+2, n[3])
                                #print(n[0], n[2] in range(i-1, i+2), n[3] in range(i-1, i+2))
                                if n[2] in range(i-1, i+2) or n[3] in range(i-1, i+2):
                                    ratios.add((n[0],n[1]))
                #print(lines[j][i-1], lines[j][i+1])
                if lines[j][i-1] or lines[j][i+1] in digits:
                    for n in all_parts:
                        if n[1] == j:
                                #print(i-1, i+2, n[3])
                                #print(n[0], n[2] in range(i-1, i+2), n[3] in range(i-1, i+2))
                            if n[2] in range(i-1, i+2) or n[3] in range(i-1, i+2):
                                ratios.add((n[0],n[1]))
                if j != len(lines)-1:
                    #print("ADF", lines[j+1][i-1], lines[j+1][i], lines[j+1][i+1])
                    if lines[j+1][i-1] or lines[j+1][i] or lines[j+1][i+1] in digits:
                        if lines[j+1][i-1] != '.' or lines[j+1][i] != '.' or lines[j+1][i+1] != '.':
                            for n in all_parts:
                                if n[1] == j+1:
                                        #print(i-1, i+2, n[3])
                                        #print(n[0], n[2] in range(i-1, i+2), n[3] in range(i-1, i+2))
                                    if n[2] in range(i-1, i+2) or n[3] in range(i-1, i+2):
                                        ratios.add((n[0],n[1]))
            print(ratios)
            if(len(ratios) == 2):
                print(ratios)
                for ele in ratios:
                    mult *= ele[0]
                gear_ratios.append(mult)
            ratios = set()
            mult = 1

print(gear_ratios)
summ = 0
for n in gear_ratios:
    summ += n

print(summ)

#print(lines[1][60:])                
#print(lines[2][60:])