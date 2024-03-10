import json
import re

digits = ['1','2','3','4','5','6','7','8','9','0']
word_digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

configs = []
liste=[]
listb = []
with open('input.txt') as f:
    lines = f.readlines()
    print(len(lines))
    word = ''
    for line in lines[10:14]:
        liste = []
        listb = []
        word = ''
        first = None
        last = None
        line = line.strip()
        curr_digit = -1
        last_dig = -1
        first_dig = -1
        for char in line:
            curr_digit +=1
            if char in digits:
                if first == None:
                    first = char
                    first_dig = curr_digit
                    print("FIRST HERE", first)
                else:
                    last = char
                    last_dig = curr_digit
                    #print("UPDATING LAST")

        print("WOED", first, last)
        for words in word_digits:
            if words in line:
                r = re.compile(r'%s' % re.escape(words), re.I)
                m = r.search(line)
                if m:
                    index = m.start()
                    liste.append(index)  
                    listb.append(words)

        print("LAST", last_dig)
        print("FIRST", first_dig)
        print(liste, listb)
        if liste and listb:
            last = str(int(word_digits.index(listb[liste.index(max(liste))]))+1) if max(liste) > last_dig else last
            if first_dig != -1:
                first = str(int(word_digits.index(listb[liste.index(min(liste))]))+1) if min(liste) < first_dig else first
            else:
                first = str(int(word_digits.index(listb[liste.index(min(liste))]))+1)
            print("FINAL", first, last)
        if last == None:
            configs.append(int(first+first))
        else:
            configs.append(int(first+last))

print(configs)
summ = 0
for num in configs:
    summ += num
print(summ)

