#tic tac toe
board=[' 'for x in range(10)]

def insertLetter(letter,pos):
    board[pos]=letter

def spaceIsFree(pos):
    return board[pos]==' '
def printBoard(board):
    print('   |   |')
    print(' '+board[1]+ ' | '+board[2]+ ' | ' + board[3])
    print('   |   |')
    print('---------')
    print('   |   |')
    print(' '+board[4]+ ' | '+board[5]+ ' | ' + board[6])
    print('   |   |')
    print('---------')
    print(' '+board[7]+ ' | '+board[8]+ ' | ' + board[9])
    print('   |   |')
def Winner(bor,let):
    return(bor[7]==let and bor[8]==let and bor[9]==let)or(bor[4]==let and bor[5]==let and bor[6]==let)or(bor[1]==let and bor[2]==let and bor[3]==let)or(bor[1]==let and bor[4]==let and bor[7]==let)or(bor[2]==let and bor[5]==let and bor[8]==let)or(bor[3]==let and bor[6]==let and bor[9]==let)or(bor[1]==let and bor[5]==let and bor[9]==let)or(bor[3]==let and bor[5]==let and bor[7]==let)
def player_Move():
    run= True
    while run:
        move=input('Mark your Place, between(1-9): ')
        try:
            move=int(move)
            if(move>0 and move < 10):
                if spaceIsFree(move):
                    run=False
                    insertLetter('X',move)
                else:
                    print('Sorry this place is occupied')   
            else:
                print('Please Type a number within the range')
        except:
            print('Please type a number')
            
def compMove():
    possibleMoves=[x for x, letter in enumerate(board) if letter == ' ' and x!=0]
    move=0

    for let in ['O', 'X']:
        for i in possibleMoves:
            board_copy=board[:]
            board_copy[i]=let
            if Winner(board_copy,let):
                move=i
                return move
    cornersopen=[]
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersopen.append(i)
    if len(cornersopen)>0:
            move=selectRandom(cornersopen)
            return move
    if 5 in possibleMoves:
        move=5
        return move 

    edgesopen=[]
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
    if len(edgesOpen)>0:
            move=selectRandom(cornersOpen)
            return move   

    
def selectRandom(li):
    import random
    ln=len(li)
    r=random.randrange(0,ln)
    return li[r]
def isBoardFull(board):
    if board.count(' ')>1:
        return False
    else:
        return True
    
def main():
    print('Welcome to TIC TAC TOE')
    printBoard(board)

    while not(isBoardFull(board)):
              if not(Winner(board,'O')):
                  player_Move()
                  printBoard(board)
              else:
                  print('Computer won')
                  break
              if not(Winner(board,'X')):
                  move=compMove()
                  if move==0:
                      print('Its a Draw')
                  else:
                     insertLetter('O',move)
                     print('Bot placed in position',move,':')
                     printBoard(board)
              else:
                  print('Congratulations, You won')
                  break
    if isBoardFull(board):
        print('Tie Game') 
            

main()
    
