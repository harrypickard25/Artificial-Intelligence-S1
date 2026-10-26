import pandas as pd
df = pd.read_csv("car.data", header=None)
buying, maintenance, doors, people, boot_size, safety = [],[],[],[],[],[]

pd.options.display.max_rows = 9999
# say its a 2d array in video+essay
counter = 0
all_combinations = []
file = open("log.txt", "a")
for i in range(0,len(df)):
    current_combination = []
    # print(str(df.loc[i][0]))
    counter+=1
    # print("ok no actually go away rnnnn")
    for item in df.loc[i]:
        current_combination+=[item]
    current = []
    if counter==1:
        current_combination+=[1]
        all_combinations+=[current_combination]
        continue
    # current_combination+=[1]
    # all_combinations+=[current_combination]
    for current in all_combinations:
        # print(str("hello bro???"))
        current_spliced = current[:7]
        # print
        file.write(str(current_combination) + "\n" + str(current_spliced) + "\n\n\n")
        if current_combination == current_spliced:
            file.write(str("anything going on here??????"))
            all_combinations[all_combinations.index(current)][7]+=1
        #   print("MULTIPLE DETECTED " + str(current_combination))
        else:
            file.write(str("Added everything") + str(counter))
            current_combination+=[1]
            all_combinations+=[current_combination]
    if counter>11:
        # print(str(all_combinations))
        print(".....\n\n\n\n\n")
        for fr in all_combinations:
            print(str(fr))
        exit()
    # print(str(all_combinations))
# print(str(buying))