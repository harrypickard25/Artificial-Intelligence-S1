import pandas as pd
df = pd.read_csv("car.data", header=None)
buying, maintenance, doors, people, boot_size, safety = [],[],[],[],[],[]

pd.options.display.max_rows = 9999
# say its a 2d array in video+essay
filters = ["vhigh","low","5more","more","small","N"]
def validate_condition(df,line_to_check,filters):
    validated = [False,False,False,False,False,False]
    file.write("\n\nStarted checking line " + str(line_to_check))
    for current_condition in range(0,6):
        file.write(str(current_condition))
        if filters[current_condition] == "N":
            validated[current_condition] = True
        elif df.loc[line_to_check][current_condition] == filters[current_condition]:
            validated[current_condition] = True
            file.write(str(df.loc[line_to_check][current_condition]) + " equalling " + str(filters[current_condition]) + " is " + str(df.loc[line_to_check][current_condition] == filters[current_condition]) + "  trueeeeeeee\n")
            file.write(str(current_condition) + str(validated) + "\n")  
        else: 
            file.write(str(df.loc[line_to_check][current_condition]) + " equalling " + str(filters[current_condition]) + " is " + str(df.loc[line_to_check][current_condition] == filters[current_condition]) + "  falseeeeeee\n")
            validated[current_condition] =  False
    file.write("\n" + str(validated) + "\n")
    if False not in validated:
        return True
    else:
        return False
counter = 0
firstitemtoadd = True
all_combinations = []
file = open("log.txt", "a")
for i in range(0,len(df)):
    print(str(counter) + str(len(all_combinations)))
    alreadyexists = False
    current_combination = []
    counter+=1
    if validate_condition(df,i,filters):
        file.write("YES IT EXISTS LINE " + str(counter))
        for item in df.loc[i]:
            current_combination+=[item]
        # current_combination+=[1]
        # all_combinations+=[current_combination]
    else:
        file.write("uhhh didnt work on line " + str(counter) + str(current_combination) + "\n")
        continue
    file.write("on line " + str(counter) + " for some reason " + str(current_combination) + "\n has worked yay\n\n")
    # for item in df.loc[i]:
    #     current_combination+=[item]
    current = []
    if firstitemtoadd:
        print(str("hello") + str(counter) )
        current_combination+=[1]
        all_combinations+=[current_combination]
        firstitemtoadd = False
        continue
    
    # current_combination+=[1]
    # all_combinations+=[current_combination] 
    for current in all_combinations:
        file.write("on loop" + str(counter) + "all com-binations is " + str(all_combinations) + "\n")
        # print(str("hello bro???"))
        current_spliced = current[:7]
        file.write(str(current_combination) + "\n" + str(current_spliced) + "\n\n\n")
        if current_combination == current_spliced:
            # file.write(str("anything going on here??????"))
            # all_combinations[all_combinations.index(current)][7]+=1
            alreadyexists = True
        #   print("MULTIPLE DETECTED " + str(current_combination))
        # else:
        #     # file.write(str("Added everything") + str(counter) + "\n")
        #     current_combination+=[1]
        #     # file.write(str(current_combination) + "\n\n")
        #     all_combinations+=[current_combination]
    # print(str(all_combinations))
    if not alreadyexists:
        file.write(str("Added everything") + str(counter) + "\n")
        current_combination+=[1]
        all_combinations+=[current_combination] 
# print(str(buying))
for fr in all_combinations:
    print(str(fr))