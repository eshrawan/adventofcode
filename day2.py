import json

#12 red cubes, 13 green cubes, and 14 blue cubes
games = []
valid_games = []
power_sets = []
count = 0
RED = 12
GREEN = 13
BLUE = 14
game_id = 0
flag = True
max_red = 0
max_blue = 0
max_green = 0

with open('input2.txt') as f:
    lines = f.readlines()
    #print(lines)
    for line in lines:
        line = line.strip()
        sets = line.split(';')
        #print(sets)
        for setn in sets:
            setn = setn.split(',')
            games.append(setn)

    for game in games:
        #print(game)
        for roundn in game:
            if "Game" in roundn:
                print("OLD ID", game_id)
                power_sets.append(max_red*max_blue*max_green)
                if flag == False:
                    valid_games.append(int(game_id))
                    print(game_id)
                flag = False
                max_red = 0
                max_blue = 0
                max_green = 0
                parts = roundn.split(":")
                #print(parts)
                game_id = parts[0].split()[1]
                print("NEW", game_id)
                number_part = parts[1].strip() 
                number_before_color = number_part.split()[0]
                #print("HERE", number_before_color)
                if "red" in roundn:
                    if int(number_before_color) > max_red:
                        max_red = int(number_before_color)
                    if int(number_before_color) > RED:
                        flag = True
                elif "blue" in roundn:
                    if int(number_before_color) > max_blue:
                        max_blue = int(number_before_color)
                    if int(number_before_color) > BLUE:
                        flag = True
                elif "green" in roundn:
                    if int(number_before_color) > max_green:
                        max_green = int(number_before_color)
                    if int(number_before_color) > GREEN:
                        flag = True
                continue
            number_before_color = roundn.split()[0]
            #print(number_before_color)
            if "red" in roundn:
                if int(number_before_color) > max_red:
                        max_red = int(number_before_color)
                if int(number_before_color) > RED:
                        flag = True
            elif "blue" in roundn:
                if int(number_before_color) > max_blue:
                        max_blue = int(number_before_color)
                if int(number_before_color) > BLUE:
                        flag = True
            elif "green" in roundn:
                if int(number_before_color) > max_green:
                        max_green = int(number_before_color)
                if int(number_before_color) > GREEN:
                        flag = True
    if flag == False:
        valid_games.append(int(game_id))
        print(game_id)
                
print(power_sets)
print(len(power_sets))
summ = 0
sum2 = 0
for num in valid_games:
    summ += int(num)
print(summ)
for n in power_sets:
    sum2 += n
#accounting for last game
print(sum2+(max_blue*max_red*max_green))

