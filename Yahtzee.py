
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
        print('Final roll = '+str(dice1)+' '+str(dice2)+' '+str(dice3)+' '+str(dice4)+' '+str(dice5))
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
        print('turn1 = ' +str(savedDice))
    
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
            print('Final roll = '+str(dice1)+' '+str(dice2)+' '+str(dice3)+' '+str(dice4)+' '+str(dice5))
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
            print('turn2 = '+str(savedDice))    
        
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
            print('final result = '+str(savedDice))
        

#store final five numbers maybe total them for the results section


def checkResults():
    # code here
    return