import os
import random

PlayerList = {"PlayerTwo" : "Y", "PlayerOne" : "X"}


Board = [
         "", "",  "", "",  "",
         "",  1,   2,  3,  "",
         "",  4,   5,  6,  "", 
         "",  7,   8,  9,  "", 
         "", "",  "", "",  "",
        ]

Turn = 0

def GetPlayerSymbol():
    global Turn
    if Turn%2 == 0:                    #even
        return PlayerList["PlayerTwo"] 

    else:                              #odd
        return PlayerList["PlayerOne"] 


InputList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def TakeInput():
    global InputList  
    
    #Num = int(input("Box Number: "))    # for Player
    #idx = InputList.index(Num)
    #InputList.pop(idx)
    #return Num
      
    tmp = len(InputList)
    if(tmp > 0):
        RandNum = InputList[random.randrange(0, tmp)] #tmp exclusive
        idx = InputList.index(RandNum)
        InputList.pop(idx)
        return RandNum
    
    else:
        return 0


def DrawBoard():     
    os.system("cls")
    print(Board[6], " ", Board[7], " ", Board[8])
    print(Board[11], " ", Board[12], " ", Board[13])
    print(Board[16], " ", Board[17], " ", Board[18])        

   

def UpdateBoard(Location, PlayerSymbol): 
    Board[Location] = PlayerSymbol  
    DrawBoard()


def ChkBoardEmpty():    
    for idx in Board:
        if idx != "" and idx in range(1, 10):
            return True
        else:
            continue
    
    return False
    

Won = False

def CheckCondition(Location): 
    global Won
    
    if Board[Location] != "" and Location >= 6 and Location <= 19:      
        
        if ( (Board[Location] == Board[Location - 5] if Location - 5 > 5 else False ) or \
            (Board[Location] == Board[Location + 10] if Location + 10 < 19 else False ) ) \
            and \
            ( (Board[Location] == Board[Location + 5] if Location + 5 < 19 else False ) or \
              (Board[Location] == Board[Location - 10] if Location - 10 > 5 else False )): #Check Up, Down, or both
            Won = True
            return Won


        elif ( (Board[Location] == Board[Location - 1] if Location - 1 > 5 else False ) or \
             (Board[Location] == Board[Location + 2] if Location + 2 < 19 else False ) ) \
            and \
            ( (Board[Location] == Board[Location + 1] if Location + 1 < 19 else False ) or \
              (Board[Location] == Board[Location - 2] if Location - 2 > 5 else False )):  #Check Left, Right, or both
            Won = True
            return Won


        elif ( (Board[Location] == Board[Location - 6] if Location - 6 > 5 else False ) or \
             (Board[Location] == Board[Location + 12] if Location + 12 < 19 else False ) ) \
            and \
            ( (Board[Location] == Board[Location + 6] if Location + 6 < 19 else False ) or \
              (Board[Location] == Board[Location - 12] if Location - 12 > 5 else False )): #Check Left Up, Right Down, or both
            Won = True
            return Won


        elif ( (Board[Location] == Board[Location - 4] if Location - 4 > 5 else False ) or \
             (Board[Location] == Board[Location + 8] if Location + 8 < 19 else False ) ) \
            and \
            ( (Board[Location] == Board[Location + 4] if Location + 4 < 19 else False ) or \
              (Board[Location] == Board[Location - 8] if Location - 8 > 5 else False )): #Check Right Up, Left Down, or both
            Won = True
            return Won                

        else:            
            print(f"\nNo Pattern Matched @ {Location} \n")
            Won = False
            return Won

    else:        
        print(f"\nExternal Failure @ {Location} \n")
        Won = False
        return Won      


DrawBoard()

BoxNumber = -1

while not CheckCondition(BoxNumber):
   
    tmp = TakeInput()

    if tmp == 0:
        break

    if tmp >= 1 and tmp <= 3 :
        BoxNumber = tmp+5

    elif tmp >= 4 and tmp <= 6 :
        BoxNumber = tmp+7
    
    elif tmp >= 7 and tmp <= 9:
        BoxNumber = tmp+9
    
    else:
        print("\nWrong Input \n")
        continue
    
    if(Board[BoxNumber] != PlayerList["PlayerOne"] and Board[BoxNumber] != PlayerList["PlayerTwo"]): # if selected box is not previously used
        Turn+=1
        PlayerSymbol = GetPlayerSymbol()
        UpdateBoard(BoxNumber, PlayerSymbol)        
    
    else:
        if ChkBoardEmpty():                       # check if there are empty spaces on the board
            print(f"\n first empty spot: {BoxNumber}\n")

        else:             
            Won = False
            print("No space on the board")
            break
        


if Won == True:
    print("\n" + list(PlayerList)[(Turn)%2] + " Won") #even = Player2, Odd = Player1
else:
    print("Match Draw")