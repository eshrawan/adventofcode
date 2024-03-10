import json

#12 red cubes, 13 green cubes, and 14 blue cubes
games = []
valid_games = []
count = 0
RED = 12
GREEN = 13
BLUE = 14
game_id = 0
flag = True

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
                if flag == False:
                    valid_games.append(int(game_id))
                    print(game_id)
                flag = False
                parts = roundn.split(":")
                #print(parts)
                game_id = parts[0].split()[1]
                print("NEW", game_id)
                number_part = parts[1].strip() 
                number_before_color = number_part.split()[0]
                #print("HERE", number_before_color)
                if "red" in roundn and int(number_before_color) > RED:
                    flag = True
                elif "blue" in roundn and int(number_before_color) > BLUE:
                    flag = True
                elif "green" in roundn and int(number_before_color) > GREEN:
                    flag = True
                continue
            number_before_color = roundn.split()[0]
            #print(number_before_color)
            if "red" in roundn and int(number_before_color) > RED:
                flag = True
            elif "blue" in roundn and int(number_before_color) > BLUE:
                flag = True
            elif "green" in roundn and int(number_before_color) > GREEN:
                flag = True
        
    
    if flag == False:
        valid_games.append(int(game_id))
        print(game_id)
                
print(valid_games)
summ = 0
for num in valid_games:
    summ += int(num)
print(summ)

