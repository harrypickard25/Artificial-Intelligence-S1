import pandas as pd
df = pd.read_csv("training_data.csv", header=None, skiprows=1)
# buying, maintenance, doors, people, boot_size, safety = [],[],[],[],[],[]
factors = ["Age","Sex","Job","Housing","Saving accounts","Checking account","Credit amount","Duration","Purpose","Risk"]
pd.options.display.max_rows = 9999
unique_items = [[],[],[],[],[],[],[],[],[]]
filters = ["N","N","N","N","N","N","N","N","N"]
bad_list,good_list = [],[]
def discover_unique_items_in_row(df,line_to_check,unique_items):
    counter=-2
    lines_to_skip = [-1,0,6,7,9]
    for item in df.loc[line_to_check]:
        counter+=1
        if counter in lines_to_skip:
            print("AHHH\n" + str(counter) + "AHHH\n")
            continue
        if item not in unique_items[counter]:
            if counter==2:
                unique_items[counter]+=[int(item)]
            else:
                unique_items[counter]+=[item]
    return unique_items
def validate_condition(df,line_to_check,filters):
    validated = [False,False,False,False,False,False,False,False,False]
    file.write("\n\nStarted checking line " + str(line_to_check))
    for current_condition in range(0,9):
        file.write(str(current_condition))
        if filters[current_condition] == "N":
            validated[current_condition] = True
        elif str(df.loc[line_to_check][current_condition+1]) == filters[current_condition]:
            validated[current_condition] = True
            file.write(str(df.loc[line_to_check][current_condition+1]) + " equalling " + str(filters[current_condition]) + " is " + str(df.loc[line_to_check][current_condition+1] == filters[current_condition]) + "  trueeeeeeee\n")
            file.write(str(current_condition) + str(validated) + "\n")  
        else:
            file.write(str(df.loc[line_to_check][current_condition+1]) + " equalling " + str(filters[current_condition]) + " is " + str(df.loc[line_to_check][current_condition+1] == filters[current_condition]) + "  falseeeeeee\n")
            validated[current_condition] =  False
    file.write("\n" + str(validated) + "\n")
    if False not in validated:
        return True
    else:
        return False
counter = 0
all_combinations = []
avg_data = [0,0,0,0,0,0]
file = open("log.txt", "a")
for i in range(0,len(df)):
    print(str(counter))
    alreadyexists = False
    current_combination = []
    counter+=1
    if validate_condition(df,i,filters):
        file.write("YES IT EXISTS LINE " + str(counter))
        for item in df.loc[i]:
            current_combination+=[item]
            file.write(str("Added everything") + str(i) + "\n")
        # current_combination+=[1]
        try:
            avg_data[1]+=int(str(current_combination[1]))
            avg_data[0]+=1
        except:
            a=1
        try:
            avg_data[3]+=int(str(current_combination[7]))
            avg_data[2]+=1
        except:
            a=1
        try:
            avg_data[5]+=int(str(current_combination[8]))
            avg_data[4]+=1
        except:
            a=1
        all_combinations+=[current_combination]
        unique_items = discover_unique_items_in_row(df,i,unique_items)
        if df.loc[i][10] == "bad":
            bad_list+=[current_combination]
        elif df.loc[i][10] == "good":
            good_list+=[current_combination]
    else:
        file.write("\nuhhh didnt work on line " + str(counter) + str(current_combination) + "\n")
        continue
    file.write("on line " + str(counter) + " for some reason " + str(current_combination) + "\n has worked yay\n\n")
    # for item in df.loc[i]:
    #     current_combination+=[item]
    current = []

    # current_combination+=[1]
    # all_combinations+=[current_combination] 
    # for current in all_combinations:
    #     # file.write("on loop" + str(counter) + "all combinations is " + str(all_combinations) + "\n")
    #     current_spliced = current[:7]   
    #     file.write(str(current_combination) + "\n" + str(current_spliced) + "\n\n\n")
    #     if current_combination == current_spliced:
    #         # file.write(str("anything going on here??????"))
    #         all_combinations[all_combinations.index(current)][7]+=1
    #         alreadyexists = True
    #         print("MULTIPLE DETECTED " + str(current_combination))
    #     # else:
    #     #     # file.write(str("Added everything") + str(counter) + "\n")
    #     #     current_combination+=[1]
    #     #     # file.write(str(current_combination) + "\n\n")
    #     #     all_combinations+=[current_combination]
    # print(str(all_combinations))
print(str(unique_items))
# print(str(buying))
# print(str(len(all_combinations)))
increase_chances,lower_chances = [],[]
proportions = []
for current in bad_list:
    print(str(current))
print("ahadhashdisahasiud")
for current in good_list:
    print(str(current))
print(str(avg_data))
for i in range(0,3):
    # print("dividing " + str(avg_data[(i*2)+1]) + " by " + str(avg_data[i*2]))
    avg_data[i] = avg_data[(i*2)+1]/avg_data[i*2]
print("\n\n\n\n\n")
print(str(bad_list))
print(str(good_list))
print("\n\n\n")
for i in range(0,9):
    file.write("\n\n\n\n\n" + str(i))
    if filters[i] == "N":
        if i==0 or i==6 or i==7:
            if i!=0:
                avg_data_index=i-5
            else:
                avg_data_index = 0
            temp_good = []
            temp_bad = []
            for current in good_list:
                if current[i+1]>avg_data[avg_data_index]:
                    # print(str(current[i+1]) + " is higher than " + str(avg_data[avg_data_index]))
                    temp_good+=[item]
            for current in bad_list:
                if current[i+1]>avg_data[avg_data_index]:
                    # print(str(current[i+1]) + " is higher than " + str(avg_data[avg_data_index]))
                    temp_bad+=[item]
            proportion_of_bad_from_total = len(temp_bad)/(len(temp_bad)+len(temp_good))
            proportions+=[proportion_of_bad_from_total]
            if proportion_of_bad_from_total>0.59:
                lower_chances+=[str(i),"morethanavg"]
            elif proportion_of_bad_from_total<0.41:
                increase_chances+=[[str(i),"morethanavg"]]                
    

            temp_good = []
            temp_bad = []
            for current in good_list:
                if current[i+1]<avg_data[avg_data_index]:
                    # print(str(current[i+1]) + " is higher than " + str(avg_data[avg_data_index]))
                    temp_good+=[item]
            for current in bad_list:
                if current[i+1]<avg_data[avg_data_index]:
                    # print(str(current[i+1]) + " is higher than " + str(avg_data[avg_data_index]))
                    temp_bad+=[item]
            proportion_of_bad_from_total = len(temp_bad)/(len(temp_bad)+len(temp_good))
            proportions+=[proportion_of_bad_from_total]
            if proportion_of_bad_from_total>0.59:
                lower_chances+=[str(i),"lessthanavg"]
            elif proportion_of_bad_from_total<0.41:
                increase_chances+=[[str(i),"lessthanavg"]]               
        else:
            for item in unique_items[i]:
                print("\n\n\n" + str(item) + "\n\n\n")
                temp_good = []
                temp_bad = []
                for current in good_list:
                    file.write("\n\n" + str(current[i+1]) + "\n")
                    file.write(str(item) + "\n")
                    if str(current[i+1]) == str(item):
                        temp_good+=[item]
                for current in bad_list:
                    # print(str(current[i+2]))
                    if str(current[i+1]) == str(item):
                        file.write("\nADDED\n")
                        temp_bad+=[item]
                # file.write("\nhellothisislenofbad " + str(len(temp_bad)) + "\n")
                # file.write("\nhellothisislenofgood " + str(len(temp_good)) + "\n")
                proportion_of_bad_from_total = len(temp_bad)/(len(temp_bad)+len(temp_good))
                proportions+=[proportion_of_bad_from_total]
                if proportion_of_bad_from_total>0.59:
                    lower_chances+=[[i,item]]
                elif proportion_of_bad_from_total<0.41:
                    increase_chances+=[[i,item]]
print(str(increase_chances))
print(str(lower_chances))
# print(str(proportions))
# print(str(unique_items))
# for factor in lower_chances:
    
# for current_combination in all_combinations:
#     print(str(current_combination))
# print(str(avg_data))
# print("hello")