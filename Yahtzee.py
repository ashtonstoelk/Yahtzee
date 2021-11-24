
import random

#start function
def yahtzee():
    #generate five random numbers and assign them to dice
    dice1 = random.randrange(1, 7)
    dice2 = random.randrange(1, 7)
    dice3 = random.randrange(1, 7)
    dice4 = random.randrange(1, 7)
    dice5 = random.randrange(1, 7)
    print(dice1, dice2, dice3, dice4, dice5)
    
    #present five dice to player and ask which ones to roll again
    answer1 = eval(input("Which dice would you like to keep? (ex: [1,3] or 'all') "))
    
    #skip if all five is the answer
    if answer1 == 'all':
        print('Final Roll = '+str(dice1)+' '+str(dice2)+' '+str(dice3)+' '+str(dice4)+' '+str(dice5))
        savedDice = {'dice1':dice1, 'dice2':dice2, 'dice3':dice3, 'dice4':dice4, 'dice5':dice5}
        return checkResults(savedDice)
    else:
        #save the other dice and randomly generate how ever many they want to keep
        savedDice = {'dice1':dice1, 'dice2':dice2, 'dice3':dice3, 'dice4':dice4, 'dice5':dice5} #dictionary of saved results
    
        for num in answer1:
            if num == 1:
                savedDice['dice1'] = dice1
            elif num == 2:
                savedDice['dice2'] = dice2
            elif num == 3:
                savedDice['dice3'] = dice3
            elif num == 4:
                savedDice['dice4'] = dice4
            elif num == 5:
                savedDice['dice5'] = dice5
        print('Roll 1 = ' +str(dice1)+' '+str(dice2)+' '+str(dice3)+' '+str(dice4)+' '+str(dice5))
    
        #take the other dice not in the response and re-roll
        d = [1,2,3,4,5]
        for num in answer1:
            if num in d:
                d.remove(num)
                
        #print(d)
        for dice in d:
            if dice == 1:
                dice1 = random.randrange(1,7)
                savedDice['dice1'] = dice1
            elif dice == 2:
                dice2 = random.randrange(1,7)
                savedDice['dice2'] = dice2
            elif dice == 3:
                dice3 = random.randrange(1,7)
                savedDice['dice3'] = dice3
            elif dice == 4:
                dice4 = random.randrange(1,7)
                savedDice['dice4'] = dice4
            elif dice == 5:
                dice5 = random.randrange(1,7)
                savedDice['dice5'] = dice5
        print(dice1, dice2, dice3, dice4, dice5)
    
        #repeat
        answer2 = eval(input("Which dice would you like to keep? (ex: [1,3], 'all') "))
        
        if answer2 == 'all':
            print('Final Roll = '+str(dice1)+' '+str(dice2)+' '+str(dice3)+' '+str(dice4)+' '+str(dice5))
            return checkResults(savedDice)
        else:
            for num in answer2:
                if num == 1:
                    savedDice['dice1'] = dice1
                elif num == 2:
                    savedDice['dice2'] = dice2
                elif num == 3:
                    savedDice['dice3'] = dice3
                elif num == 4:
                    savedDice['dice4'] = dice4
                elif num == 5:
                    savedDice['dice5'] = dice5
            print('Roll 2 = '+str(dice1)+' '+str(dice2)+' '+str(dice3)+' '+str(dice4)+' '+str(dice5))    
        
            #second re-roll
            d = [1,2,3,4,5]
            for num in answer2:
                if num in d:
                    d.remove(num)
                
            #print(d)
            for dice in d:
                if dice == 1:
                    dice1 = random.randrange(1,7)
                    savedDice['dice1'] = dice1
                elif dice == 2:
                    dice2 = random.randrange(1,7)
                    savedDice['dice2'] = dice2
                elif dice == 3:
                    dice3 = random.randrange(1,7)
                    savedDice['dice3'] = dice3
                elif dice == 4:
                    dice4 = random.randrange(1,7)
                    savedDice['dice4'] = dice4
                elif dice == 5:
                    dice5 = random.randrange(1,7)
                    savedDice['dice5'] = dice5
            print(dice1, dice2, dice3, dice4, dice5)        
            print('Final Roll = '+str(dice1)+' '+str(dice2)+' '+str(dice3)+' '+str(dice4)+' '+str(dice5))
            return checkResults(savedDice)

def checkResults(dice):
    """ This method checks the results of your saved roll, printing the highest value result """

    diceList = []
    for i in dice:
        # appends dictionary values to a list
        diceList.append(dice[i])
    diceList.sort() # sorts list numerically

    if diceList[0] == diceList[4]:
        # compares first and last index of the list
        return "You got a Yahtzee"
    
    elif len(set(diceList)) == 5 and diceList[0] == 2 and diceList[4] == 6:
        # checks if the list is ordered between 2-6
        return "You got a High Straight" 
    
    elif len(set(diceList)) == 5 and diceList[4] == 5:
        # checks if the list is ordered between 1-5
        return "You got a Low Straight"
    
    elif len(set(diceList)) == 2: # checks if there is only 2 unique values in the list
        if diceList[0] != diceList[3] and diceList[1] != diceList[4]:
            # checks if there is a more than one of each unique value
            return "You got a Full House"
        else:
            return "You got Four of a Kind"
    
    elif diceList[0] == diceList[2] or diceList[1] == diceList[3] or diceList[2] == diceList[4]:
        # checks for three of the same number
        return "You got Three of a Kind" 
   
    else:
        return "You Lose"