# Imports all modules used in the program,
# pandas is used for importing and reading the csv file
# platform is used to detect the os, which then uses os to clear the screen using the correct command
import pandas as pd
import platform
import os
# This function clears the screen using the correct command for the current user's os
def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
# loads the csv file into the 'df' variable
df = pd.read_csv("training_data.csv", header=None, skiprows=1)
# defines all the characteristics (column headers) for use later
characteristics = ["Age","Sex","Number of jobs","Housing","How much money in their saving account","How much money in their checking account","Credit amount","Duration(months)","Purpose"]
# making sure that every row from the dataset is loaded
pd.options.display.max_rows = 9999
# initialises a few of the lists which are used throughout the program, such as where all the unique items in each factor are stored
unique_items = [[],[],[],[],[],[],[],[],[]]
items_to_pick = [["range"], ['male', 'female'], [1, 2, 3, 0], ['free', 'rent', 'own'], ['nan', 'little', 'moderate', 'rich', 'quite rich'], ['nan', "little", 'moderate', 'rich'], ["range"], ["range"], ['repairs', 'education', 'car', 'furniture/equipment', 'radio/TV', 'business', 'vacation/others', 'domestic appliances']]
filters = ["N","N","N","N","N","N","N","N","N"]
bad_list,good_list = [],[]
# the user menu repeats while the user hasn't chosen their
filters_chosen = False
while not filters_chosen:
    clear()
    print("Main Menu")
    print("1. Add new filter")
    print("2. View filters")
    print("3. Use current filters to analyse dataset")
    # attempts to cast the input to an integer, if it doesn't work then the user has typed in something other than a
    # number, so they're then put back to the main menu again
    try:
        user_option = int(input(": "))
    except:
        input("Please type a number, enter to continue")
        continue
    if user_option == 1:
        clear()
        print("Type the number of the filter you would like to add:\n")
        # iterates through all the characteristics and prints the name of all of them, to allow the user to choose one to add
        not_chosen = True
        while not_chosen:
            clear()
            counter = 0
            for item in characteristics:
                counter+=1
                print(f"{str(counter)}. {str(item)}")
            try:
                user_option = int(input(": "))-1
                not_chosen = False
            except:
                input("Please type a number, enter to continue")
        current_options = items_to_pick[user_option]
        # if the filter chosen was one that had a range of numbers, then this part is executed
        if current_options[0] == "range":
            clear()
            print(f"What value would you like the '{str(characteristics[user_option]).lower()}' to be higher than?")
            temp_filter_value = input(": ")
        else:
            # otherwise, this part which displays each unique item
            clear()
            print(f"Type the number of the value you would like to use in the '{str(characteristics[user_option]).lower()}' filter:\n")
            counter = 0
            for item in current_options:
                counter+=1
                if item == "nan":
                    item = "No " + characteristics[user_option].replace("How much money in their ","").lower()
                print(f"{str(counter)}. {str(item)}")
            temp_filter_value = input(": ")
            temp_filter_value = current_options[int(temp_filter_value)-1]
        # edits the filters list to add the new filter
        filters[user_option] = temp_filter_value
    elif user_option == 2:
        counter = -1
        for filter in filters:
            counter+=1
            if filter!="N":
                print(str(characteristics[counter]) + " - " + str(filter))
        input("Enter to continue")
    elif user_option == 3:
        # updates the variable so that the the menu won't loop anymore
        filters_chosen = True
# This function finds all the possible items for each characteristic in each line
def discover_unique_items_in_row(df,line_to_check,unique_items):
    counter=-2
    lines_to_skip = [-1,0,6,7,9]
    for item in df.loc[line_to_check]:
        counter+=1
        if counter in lines_to_skip:
            continue
        if item not in unique_items[counter]:
            if counter==2:
                unique_items[counter]+=[int(item)]
            else:
                unique_items[counter]+=[item]
    return unique_items
# This function checks each characteristic against each filter's value
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
# Iterates through every line in the dataset
for i in range(0,len(df)):
    alreadyexists = False
    current_combination = []
    counter+=1
    # validates each line
    if validate_condition(df,i,filters):
        file.write("line has been validated " + str(counter))
        for item in df.loc[i]:
            current_combination+=[item]
        # adds each characteristic which has a range of numbers to the avg_data list,
        # to allow the average of each characteristic to be calculated later
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
        unique_items = discover_unique_items_in_row(df,i,unique_items)
        # sorts each verified line into either the good or bad lists, depending on the risk factor
        if df.loc[i][10] == "bad":
            bad_list+=[current_combination]
        elif df.loc[i][10] == "good":
            good_list+=[current_combination]
    else:
        file.write("\nline " + str(counter) +  " wasn't validated, with combination " + str(current_combination) + "\n")
        continue
    file.write("on line " + str(counter) + " combination " + str(current_combination) + "\n has worked\n\n")
    current = []
# makes sure that any lines actually match the current filters before continuing
if len(good_list) == 0 and len(bad_list) == 0:
    print("No data found with specified filters, please try again with different/less filters")
    quit()
increase_chances,lower_chances = [],[]
proportions = []
# Works out the average value for each of the characteristics with a large range of numbers
for i in range(0,3):
    avg_data[i] = avg_data[(i*2)+1]/avg_data[i*2]
# This section works out which values for each characteristic increase or decrease the chances of
# paying back the loan
for i in range(0,9):
    file.write("\n\n\n\n\n" + str(i))
    if filters[i] == "N":
        # for the 3 characteristics which have a large range of values, uses the average value
        # to check if a value is more or less than the average,
        # to add that value to the lower or higher chances lists
        if i==0 or i==6 or i==7:
            if i!=0:
                avg_data_index=i-5
            else:
                avg_data_index = 0
            temp_good = []
            temp_bad = []
            for current in good_list:
                if current[i+1]>avg_data[avg_data_index]:
                    temp_good+=[item]
            for current in bad_list:
                if current[i+1]>avg_data[avg_data_index]:
                    temp_bad+=[item]
            proportion_of_bad_from_total = len(temp_bad)/(len(temp_bad)+len(temp_good))
            proportions+=[proportion_of_bad_from_total]
            if proportion_of_bad_from_total>0.59:
                increase_chances+=[[int(i),"morethanavg"]]
            elif proportion_of_bad_from_total<0.41:
                lower_chances+=[[int(i),"morethanavg"]]                
    
        # repeat of the section above, but checking if each value is less than average rather than more
            temp_good = []
            temp_bad = []
            for current in good_list:
                if current[i+1]<avg_data[avg_data_index]:
                    temp_good+=[item]
            for current in bad_list:
                if current[i+1]<avg_data[avg_data_index]:
                    temp_bad+=[item]
            proportion_of_bad_from_total = len(temp_bad)/(len(temp_bad)+len(temp_good))
            proportions+=[proportion_of_bad_from_total]
            if proportion_of_bad_from_total>0.59:
                increase_chances+=[[int(i),"lessthanavg"]]
            elif proportion_of_bad_from_total<0.41:
                lower_chances+=[[int(i),"lessthanavg"]]               
        else:
            # adding each value to the increase or lower chances lists, just depending on if
            # 60% or more of one value per characteristic has a good or bad risk
            for item in unique_items[i]:
                temp_good = []
                temp_bad = []
                for current in good_list:
                    file.write("\n\n" + str(current[i+1]) + "\n")
                    file.write(str(item) + "\n")
                    if str(current[i+1]) == str(item):
                        temp_good+=[item]
                for current in bad_list:
                    if str(current[i+1]) == str(item):
                        file.write("\added\n")
                        temp_bad+=[item]
                file.write("\ncurrentlengthofbad " + str(len(temp_bad)) + "\n")
                file.write("\ncurrentlengthofgood " + str(len(temp_good)) + "\n")
                proportion_of_bad_from_total = len(temp_bad)/(len(temp_bad)+len(temp_good))
                proportions+=[proportion_of_bad_from_total]
                if proportion_of_bad_from_total>0.59:
                    increase_chances+=[[i,item]]
                elif proportion_of_bad_from_total<0.41:
                    lower_chances+=[[i,item]]
# Displays all of the characteristics which increase or decrease the risk
clear()
print(str("Lower chances:\n"))
for factor in lower_chances:
    print(f"If someone has a value of {str(factor[1])} in the {str(characteristics[factor[0]])} class")
print(str("Increase chances:\n"))
for factor in increase_chances:
    print(f"If someone has a value of {str(factor[1])} in the {str(characteristics[factor[0]])} class")
