import pandas as pd
import platform
import os
def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
df = pd.read_csv("training_data.csv", header=None, skiprows=1)
# buying, maintenance, doors, people, boot_size, safety = [],[],[],[],[],[]
factors = ["Age","Sex","Number of jobs","Housing","How much money in their saving account","How much money in their checking account","Credit amount","Duration(months)","Purpose"]
pd.options.display.max_rows = 9999
unique_items = [[],[],[],[],[],[],[],[],[]]
items_to_pick = [["range"], ['male', 'female'], [1, 2, 3, 0], ['free', 'rent', 'own'], ['nan', 'little', 'moderate', 'rich', 'quite rich'], ['nan', "little", 'moderate', 'rich'], ["range"], ["range"], ['repairs', 'education', 'car', 'furniture/equipment', 'radio/TV', 'business', 'vacation/others', 'domestic appliances']]
filters = ["N","N","N","N","N","N","N","N","N"]
bad_list,good_list = [],[]
factors_chosen = False
while not factors_chosen:
    clear()
    print("Main Menu")
    print("1. Add new filter")
    print("2. View filters")
    print("3. Use current filters to analyse dataset")
    try:
        user_option = int(input(": "))
    except:
        input("Please type a number, enter to continue")
        continue
    if user_option == 1:
        print("Type the number of the factor you would like to add:\n")
        counter = 0
        for item in factors:
            counter+=1
            print(f"{str(counter)}. {str(item)}")
        not_chosen = True
        while not_chosen:
            try:
                user_option = int(input(": "))-1
                not_chosen = False
            except:
                input("Please type a number, enter to continue")
        current_options = items_to_pick[user_option]
        if current_options[0] == "range":
            print(f"What value would you like the '{str(factors[user_option]).lower()}' to be higher than?")
            temp_filter_value = input(": ")
        else:
            print(f"Type the number of the value you would like to use in the '{str(factors[user_option]).lower()}' filter:\n")
            counter = 0
            for item in current_options:
                counter+=1
                if item == "nan":
                    item = "No " + factors[user_option].replace("How much money in their ","").lower()
                print(f"{str(counter)}. {str(item)}")
            temp_filter_value = input(": ")
            temp_filter_value = current_options[int(temp_filter_value)-1]
        filters[user_option] = temp_filter_value
    elif user_option == 2:
        print(str(filters))
        input("Enter to continue")
    elif user_option == 3:
        factors_chosen = True
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
        if filters[current_condition] == "N":
            validated[current_condition] = True
            continue
        if items_to_pick[current_condition][0] == "range":
            if int(df.loc[line_to_check][current_condition+1]) > int(filters[current_condition]):
                validated[current_condition] = True
                file.write(str(df.loc[line_to_check][current_condition+1]) + " equalling " + str(filters[current_condition]) + " is " + str(df.loc[line_to_check][current_condition+1] == filters[current_condition]) + "  trueeeeeeee\n")
                file.write(str(current_condition) + str(validated) + "\n")  
        else:
            if str(df.loc[line_to_check][current_condition+1]) == filters[current_condition]:
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
    # print(str(counter))
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
if len(good_list) == 0 and len(bad_list) == 0:
    print("No data found with specified filters, please try again with different/less filters")
    quit()
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
# print(str(unique_items))
# print(str(buying))
# print(str(len(all_combinations)))
increase_chances,lower_chances = [],[]
proportions = []
# for current in bad_list:
#     print(str(current))
# for current in good_list:
#     print(str(current))
# print(str(avg_data))
for i in range(0,3):
    # print("dividing " + str(avg_data[(i*2)+1]) + " by " + str(avg_data[i*2]))
    avg_data[i] = avg_data[(i*2)+1]/avg_data[i*2]
print("\n\n\n\n\n")
# print(str(bad_list))
# print(str(good_list))
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
                increase_chances+=[[int(i),"morethanavg"]]
            elif proportion_of_bad_from_total<0.41:
                lower_chances+=[[int(i),"morethanavg"]]                
    

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
                increase_chances+=[[int(i),"lessthanavg"]]
            elif proportion_of_bad_from_total<0.41:
                lower_chances+=[[int(i),"lessthanavg"]]               
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
                    increase_chances+=[[i,item]]
                elif proportion_of_bad_from_total<0.41:
                    lower_chances+=[[i,item]]
# print(str(increase_chances))
# print(str(lower_chances))
# print(str(proportions))
# print(str(unique_items))
# print(str("Lower chances:\n"))
for factor in lower_chances:
    print(f"If someone has a value of {str(factor[1])} in the {str(factors[factor[0]])} class")
print(str("Increase chances:\n"))
for factor in increase_chances:
    print(f"If someone has a value of {str(factor[1])} in the {str(factors[factor[0]])} class")
# for current_combination in all_combinations:
#     print(str(current_combination))
# print(str(avg_data))
# print("hello")