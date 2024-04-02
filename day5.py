destinations = []
destinations2 = []
destinations3 = []
destinations4 = []
destinations5 =[]
destinations6 = []
destinations7 = []
seeds = []
with open('input5.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        #print(line)
    seeds_init = lines[0].split(' ')
    seeds_init = seeds_init[1:]
    #print(seeds_init)
    for j in range(0, int(seeds_init[1])):
        seeds.append(int(seeds_init[0])+j)
    print(len(seeds))
    seed_to_soil = lines[3:18] #seed to soil map
    soil_to_fert = lines[20:33]
    fert_to_water = lines[35:66]
    water_to_light = lines[68:90]
    light_to_temp = lines[92:125]
    temp_to_humidity = lines[127:171]
    humidity_to_location = lines[173:193]
    #print(soil_to_fert)
    for seed in seeds:
        map_found = False
        for sts in seed_to_soil:
            dest_start, source_start, ran = sts.split(' ')
            if int(seed) >= int(source_start) and int(seed) <= int(source_start)+int(ran):
                #print("EE", seed, source_start, dest_start)
                map_found = True
                destinations.append((int(seed), (int(dest_start)+int(ran))-(int(source_start)+int(ran)-int(seed))))
        if map_found == False:
            destinations.append((int(seed), int(seed)))

    for tup in destinations:
        map_found = False
        for stf in soil_to_fert:
            dest_start, source_start, ran = stf.split(' ')
            if int(tup[1]) >= int(source_start) and int(tup[1]) <= int(source_start)+int(ran):
                #print("EE", seed, source_start, int(source_start)+int(ran))
                map_found = True
                destinations2.append((int(tup[1]), (int(dest_start)+int(ran))-(int(source_start)+int(ran)-int(tup[1]))))
        if map_found == False:
            destinations2.append((int(tup[1]), int(tup[1])))
    
    for tup in destinations2:
        map_found = False
        for stf in fert_to_water:
            dest_start, source_start, ran = stf.split(' ')
            if int(tup[1]) >= int(source_start) and int(tup[1]) <= int(source_start)+int(ran):
                #print("EE", seed, source_start, int(source_start)+int(ran))
                map_found = True
                destinations3.append((int(tup[1]), (int(dest_start)+int(ran))-(int(source_start)+int(ran)-int(tup[1]))))
        if map_found == False:
            destinations3.append((int(tup[1]), int(tup[1])))

    for tup in destinations3:
        map_found = False
        for stf in water_to_light:
            dest_start, source_start, ran = stf.split(' ')
            if int(tup[1]) >= int(source_start) and int(tup[1]) <= int(source_start)+int(ran):
                #print("EE", seed, source_start, int(source_start)+int(ran))
                map_found = True
                destinations4.append((int(tup[1]), (int(dest_start)+int(ran))-(int(source_start)+int(ran)-int(tup[1]))))
        if map_found == False:
            destinations4.append((int(tup[1]), int(tup[1])))

    for tup in destinations4:
        map_found = False
        for stf in light_to_temp:
            dest_start, source_start, ran = stf.split(' ')
            if int(tup[1]) >= int(source_start) and int(tup[1]) <= int(source_start)+int(ran):
                #print("EE", seed, source_start, int(source_start)+int(ran))
                map_found = True
                destinations5.append((int(tup[1]), (int(dest_start)+int(ran))-(int(source_start)+int(ran)-int(tup[1]))))
        if map_found == False:
            destinations5.append((int(tup[1]), int(tup[1])))
    
    for tup in destinations5:
        map_found = False
        for stf in temp_to_humidity:
            dest_start, source_start, ran = stf.split(' ')
            if int(tup[1]) >= int(source_start) and int(tup[1]) <= int(source_start)+int(ran):
                #print("EE", seed, source_start, int(source_start)+int(ran))
                map_found = True
                destinations6.append((int(tup[1]), (int(dest_start)+int(ran))-(int(source_start)+int(ran)-int(tup[1]))))
        if map_found == False:
            destinations6.append((int(tup[1]), int(tup[1])))

    for tup in destinations6:
        map_found = False
        for stf in humidity_to_location:
            dest_start, source_start, ran = stf.split(' ')
            if int(tup[1]) >= int(source_start) and int(tup[1]) <= int(source_start)+int(ran):
                #print("EE", seed, source_start, dest_start)
                map_found = True
                destinations7.append((int(tup[1]), (int(dest_start)+int(ran))-(int(source_start)+int(ran)-int(tup[1]))))
        if map_found == False:
            destinations7.append((int(tup[1]), int(tup[1])))


    #print(destinations[0])
    #print(destinations2[0])
    #print(destinations3[0])
    min = 100000000000000000
    for tup in destinations7:
        if tup[1] <= min:
            min = tup[1]

    print(min)