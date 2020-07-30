import random

# Nian Calculator
# This script calculates experimentally your chances of
# getting a Nian based on how many times you roll
# Ex. For 500 pulls, chance of getting 6 Nian(s) is 0.3605
#     For 50 pulls, chance of getting 1 Nian(s) is 0.2966
# -----------------------------------
# Change variables here

# This is the percent chance where the script will stop
# Ex. 0.9 means the script will stop when it get to 90% chance of success
Desired_Percentage = 0.7
# This is how many Nians you want
# 1 means chance of 1 Nian, 6 means potential 6 Nian
Desired_Potential_Primary = 2
Desired_Potential_Secondary = 1
# This is how many times we're testing each pull amount
# 10,000 means test each interval 10,000 times. Higher will be more "accurate"
Number_Of_Samples_Per_Test = 100000
# Interval for pulling
# How granular you want the results. 10 means you are doing 10-pulls
Test_Increment = 10

# Don't touch below this line
# -----------------------------------

baseSixStarChance = 0.02
rateUpChance = 0.7
numRateUpsOnBanner = 2
pityStartNum = 50

def onePull(numFails):
    sixStarChance = baseSixStarChance
    if (numFails >= pityStartNum):
        sixStarChance = baseSixStarChance + (0.02*(numFails-(pityStartNum - 1)))
        #print("Triggered Pity! Current chance: {}".format(sixStarChance))
    if (random.random() > (1-sixStarChance)):
        if (random.random() < rateUpChance):
            if (random.random() < (1/numRateUpsOnBanner)):
                #print("GOT NIAN")
                return 2
            else:
                #print("GOT AAK")
                return 3
        return 1
    return 0
    
def oneTest(numPulls):
    numWins = 0
    numLosses = 0
    numAak = 0
    numNian = 0
    for i in range (0,numPulls):
        result = onePull(numLosses)
        if (result == 0): #fail
            numLosses += 1
        elif (result == 1): #Not Nian or Aak
            numWins += 1
            numLosses = 0
        elif (result == 2): #Nian
            numWins += 1
            numLosses = 0
            numNian += 1
        else: #Aak
            numWins += 1
            numLosses = 0
            numAak += 1
    #print("Number of 6 stars: {} / {}".format(numWins, numPulls))
    #print("Number of Nians: {} / {}".format(numNian, numPulls))
    #print("Number of Aaks: {} / {}".format(numAak, numPulls))
    return [numNian, numAak]

def runTest(desiredPercentage, numNiansWanted, numAaksWanted, numRuns):
    resultPercent = 0
    numPulls = 0
    while (resultPercent < desiredPercentage):
        numWins = 0
        numPulls += Test_Increment
        for trialNum in range (0,numRuns):
            testResult = oneTest(numPulls)
            if ((testResult[0] >= numNiansWanted) and (testResult[1] >= numAaksWanted)):
                numWins += 1     
        resultPercent = numWins / numRuns
        print("For {} pulls, chance of getting {} Nian(s) and {} Aak(s) is {}".format(numPulls, numNiansWanted, numAaksWanted, resultPercent))
    return numPulls
    
print(runTest(Desired_Percentage, Desired_Potential_Primary, Desired_Potential_Secondary, Number_Of_Samples_Per_Test))
