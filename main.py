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
uniqueItems = [[],[],[],[],[],[],[],[],[]]
itemsToPick = [["range"], ['male', 'female'], [1, 2, 3, 0], ['free', 'rent', 'own'], ['nan', 'little', 'moderate', 'rich', 'quite rich'], ['nan', "little", 'moderate', 'rich'], ["range"], ["range"], ['repairs', 'education', 'car', 'furniture/equipment', 'radio/TV', 'business', 'vacation/others', 'domestic appliances']]
filters = ["N","N","N","N","N","N","N","N","N"]
badList,goodList = [],[]
# the user menu repeats while the user hasn't chosen their
filtersChosen = False
while not filtersChosen:
    clear()
    print("Main Menu")
    print("1. Add new filter")
    print("2. View filters")
    print("3. Use current filters to analyse dataset")
    # attempts to cast the input to an integer, if it doesn't work then the user has typed in something other than a
    # number, so they're then put back to the main menu again
    try:
        userOption = int(input(": "))
    except:
        input("Please type a number, enter to continue")
        continue
    if userOption == 1:
        clear()
        print("Type the number of the filter you would like to add:\n")
        # iterates through all the characteristics and prints the name of all of them, to allow the user to choose one to add
        notChosen = True
        while notChosen:
            clear()
            counter = 0
            for item in characteristics:
                counter+=1
                print(f"{str(counter)}. {str(item)}")
            try:
                userOption = int(input(": "))-1
                notChosen = False
            except:
                input("Please type a number, enter to continue")
        currentOptions = itemsToPick[userOption]
        # if the filter chosen was one that had a range of numbers, then this part is executed
        if currentOptions[0] == "range":
            clear()
            print(f"What value would you like the '{str(characteristics[userOption]).lower()}' to be higher than?")
            tempFilterValue = input(": ")
        else:
            # otherwise, this part which displays each unique item
            clear()
            print(f"Type the number of the value you would like to use in the '{str(characteristics[userOption]).lower()}' filter:\n")
            counter = 0
            for item in currentOptions:
                counter+=1
                if item == "nan":
                    item = "No " + characteristics[userOption].replace("How much money in their ","").lower()
                print(f"{str(counter)}. {str(item)}")
            tempFilterValue = input(": ")
            tempFilterValue = currentOptions[int(tempFilterValue)-1]
        # edits the filters list to add the new filter
        filters[userOption] = tempFilterValue
    elif userOption == 2:
        counter = -1
        for filter in filters:
            counter+=1
            if filter!="N":
                print(str(characteristics[counter]) + " - " + str(filter))
        input("Enter to continue")
    elif userOption == 3:
        # updates the variable so that the the menu won't loop anymore
        filtersChosen = True
# This function finds all the possible items for each characteristic in each line
def discover_unique_items_in_row(df,lineToCheck,uniqueItems):
    counter=-2
    linesToSkip = [-1,0,6,7,9]
    for item in df.loc[lineToCheck]:
        counter+=1
        if counter in linesToSkip:
            continue
        if item not in uniqueItems[counter]:
            if counter==2:
                uniqueItems[counter]+=[int(item)]
            else:
                uniqueItems[counter]+=[item]
    return uniqueItems
# This function checks each characteristic against each filter's value
def validate_condition(df,lineToCheck,filters):
    validated = [False,False,False,False,False,False,False,False,False]
    log_file.write("\n\nStarted checking line " + str(lineToCheck))
    for currentCondition in range(0,9):
        if filters[currentCondition] == "N":
            validated[currentCondition] = True
            continue
        if itemsToPick[currentCondition][0] == "range":
            if int(df.loc[lineToCheck][currentCondition+1]) > int(filters[currentCondition]):
                validated[currentCondition] = True
                log_file.write(str(df.loc[lineToCheck][currentCondition+1]) + " equalling " + str(filters[currentCondition]) + " is " + str(df.loc[lineToCheck][currentCondition+1] == filters[currentCondition]) + "  trueeeeeeee\n")
                log_file.write(str(currentCondition) + str(validated) + "\n")  
        else:
            if str(df.loc[lineToCheck][currentCondition+1]) == filters[currentCondition]:
                validated[currentCondition] = True
                log_file.write(str(df.loc[lineToCheck][currentCondition+1]) + " equalling " + str(filters[currentCondition]) + " is " + str(df.loc[lineToCheck][currentCondition+1] == filters[currentCondition]) + "  trueeeeeeee\n")
                log_file.write(str(currentCondition) + str(validated) + "\n")  
            else:
                log_file.write(str(df.loc[lineToCheck][currentCondition+1]) + " equalling " + str(filters[currentCondition]) + " is " + str(df.loc[lineToCheck][currentCondition+1] == filters[currentCondition]) + "  falseeeeeee\n")
                validated[currentCondition] =  False
    log_file.write("\n" + str(validated) + "\n")
    if False not in validated:
        return True
    else:
        return False
counter = 0
allCombinations = []
avgData = [0,0,0,0,0,0]
log_file = open("log.txt", "a")
# Iterates through every line in the dataset
for i in range(0,len(df)):
    alreadyExists = False
    currentCombination = []
    counter+=1
    # validates each line
    if validate_condition(df,i,filters):
        log_file.write("line has been validated " + str(counter))
        for item in df.loc[i]:
            currentCombination+=[item]
        # adds each characteristic which has a range of numbers to the avg_data list,
        # to allow the average of each characteristic to be calculated later
        try:
            avgData[1]+=int(str(currentCombination[1]))
            avgData[0]+=1
        except:
            a=1
        try:
            avgData[3]+=int(str(currentCombination[7]))
            avgData[2]+=1
        except:
            a=1
        try:
            avgData[5]+=int(str(currentCombination[8]))
            avgData[4]+=1
        except:
            a=1
        uniqueItems = discover_unique_items_in_row(df,i,uniqueItems)
        # sorts each verified line into either the good or bad lists, depending on the risk factor
        if df.loc[i][10] == "bad":
            badList+=[currentCombination]
        elif df.loc[i][10] == "good":
            goodList+=[currentCombination]
    else:
        log_file.write("\nline " + str(counter) +  " wasn't validated, with combination " + str(currentCombination) + "\n")
        continue
    log_file.write("on line " + str(counter) + " combination " + str(currentCombination) + "\n has worked\n\n")
    current = []
# makes sure that any lines actually match the current filters before continuing
if len(goodList) == 0 and len(badList) == 0:
    print("No data found with specified filters, please try again with different/less filters")
    quit()
increaseChances,lowerChances = [],[]
proportions = []
# Works out the average value for each of the characteristics with a large range of numbers
for i in range(0,3):
    avgData[i] = avgData[(i*2)+1]/avgData[i*2]
# This section works out which values for each characteristic increase or decrease the chances of
# paying back the loan
for i in range(0,9):
    log_file.write("\n\n\n\n\n" + str(i))
    if filters[i] == "N":
        # for the 3 characteristics which have a large range of values, uses the average value
        # to check if a value is more or less than the average,
        # to add that value to the lower or higher chances lists
        if i==0 or i==6 or i==7:
            if i!=0:
                avgDataIndex=i-5
            else:
                avgDataIndex = 0
            tempGood = []
            tempBad = []
            for current in goodList:
                if current[i+1]>avgData[avgDataIndex]:
                    tempGood+=[item]
            for current in badList:
                if current[i+1]>avgData[avgDataIndex]:
                    tempBad+=[item]
            proportionOfBadFromTotal = len(tempBad)/(len(tempBad)+len(tempGood))
            proportions+=[proportionOfBadFromTotal]
            if proportionOfBadFromTotal>0.59:
                increaseChances+=[[int(i),"more than average"]]
            elif proportionOfBadFromTotal<0.41:
                lowerChances+=[[int(i),"more than average"]]                
    
        # repeat of the section above, but checking if each value is less than average rather than more
            tempGood = []
            tempBad = []
            for current in goodList:
                if current[i+1]<avgData[avgDataIndex]:
                    tempGood+=[item]
            for current in badList:
                if current[i+1]<avgData[avgDataIndex]:
                    tempBad+=[item]
            proportionOfBadFromTotal = len(tempBad)/(len(tempBad)+len(tempGood))
            proportions+=[proportionOfBadFromTotal]
            if proportionOfBadFromTotal>0.59:
                increaseChances+=[[int(i),"less than average"]]
            elif proportionOfBadFromTotal<0.41:
                lowerChances+=[[int(i),"less than average"]]
        else:
            # adding each value to the increase or lower chances lists, just depending on if
            # 60% or more of one value per characteristic has a good or bad risk
            for item in uniqueItems[i]:
                tempGood = []
                tempBad = []
                for current in goodList:
                    log_file.write("\n\n" + str(current[i+1]) + "\n")
                    log_file.write(str(item) + "\n")
                    if str(current[i+1]) == str(item):
                        tempGood+=[item]
                for current in badList:
                    if str(current[i+1]) == str(item):
                        log_file.write("\added\n")
                        tempBad+=[item]
                log_file.write("\ncurrentlengthofbad " + str(len(tempBad)) + "\n")
                log_file.write("\ncurrentlengthofgood " + str(len(tempGood)) + "\n")
                proportionOfBadFromTotal = len(tempBad)/(len(tempBad)+len(tempGood))
                proportions+=[proportionOfBadFromTotal]
                if proportionOfBadFromTotal>0.59:
                    increaseChances+=[[i,item]]
                elif proportionOfBadFromTotal<0.41:
                    lowerChances+=[[i,item]]
# Displays all of the characteristics which increase or decrease the risk
clear()
# mire likely to pay back
lowerChancesResultsAchieved, increaseChancesResultsAchieved = 0,0
lowerChancesExpectedResults = [[0,"more than average"],[2,3],[3,"own"], [4,"rich"], [5,"rich"], [8,"radio/tv"]]
increaseChancesExpectedResults = [[0,"less than average"],[2,0],[3,"rent"], [4,"little"], [5,"little"], [8,"car"]]
print(str("Lower chances:\n"))
for factor in lowerChances:
    print(f"If someone has a value of {str(factor[1])} in the {str(characteristics[factor[0]])} class")
print(str("Increase chances:\n"))
for factor in increaseChances:
    print(f"If someone has a value of {str(factor[1])} in the {str(characteristics[factor[0]])} class")
for factor in lowerChances:
    for characteristic in lowerChancesExpectedResults:
        if int(factor[0]) == characteristic[0]:
            lowerChancesResultsAchieved+=1
    for characteristic in increaseChancesExpectedResults:
        if int(factor[0]) == characteristic[0]:
            increaseChancesResultsAchieved+=1
print("\n\nPerformance metrics:\n")
print(str(len(lowerChancesExpectedResults)))
print(str(lowerChancesResultsAchieved))
print(f"{str(lowerChancesResultsAchieved/len(lowerChancesExpectedResults)*100)[:4]}% of expected results to be discovered to decrease chances were discovered")
print(f"{str((increaseChancesResultsAchieved/len(increaseChancesExpectedResults))*100)[:4]}% of expected results to be discovered to increase chances were discovered")
