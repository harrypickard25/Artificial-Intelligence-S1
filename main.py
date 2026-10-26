import pandas as pd
df = pd.read_csv("car.data", header=None)
buying, maintenance, doors, people, boot_size, safety = [],[],[],[],[],[]

pd.options.display.max_rows = 9999
# say its a 2d array in video+essay
counter = 0
all_combinations = []
for i in range(0,len(df)):
    current_combination = []
    # print(str(df.loc[i][0]))
    counter+=1
    for item in df.loc[i]:
        current_combination+=[item]
    for current in all_combinations:
        current_spliced = current[:6]
        if current_combination == current:
            all_combinations[all_combinations.index(curent)][7]+=1
            print("MULTIPLE DETECTED " + str(current_combination))
        else:
            print(str("Added everything"))
            current_combination+=[1]
            all_combinations+=[current_combination]
    if counter>11:
        print(str(all_combinations))
        print(".....\n\n\n\n\n")
        for fr in all_combinations:
            print(str(fr))
        exit()
    # print(str(all_combinations))
# print(str(buying))