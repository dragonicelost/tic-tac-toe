import random
def display_board(board):
    print('\n')
    print('\t \t \t',end='')
    print('  '+board[1]+'   |'+'  '+board[2]+'   '+'|  '+board[3])
    print('\t \t \t',end='')
    print('- - - - - - - - - - -')
    print('\t \t \t',end='')
    print('  '+board[4]+'   |'+'  '+board[5]+'   '+'|  '+board[6])
    print('\t \t \t',end='')
    print('- - - - - - - - - - -')
    print('\t \t \t',end='')
    print('  '+board[7]+'   |'+'  '+board[8]+'   '+'|  '+board[9])
    print('\t \t \t',end='')
    print('\n')
def player_input():
    i=random.randint(1,2)
    if i == 1:
        first=1
    else:
        first=2
    print('\t \t \t',end='')
    print('Player',first,'Will Choose First')
    marker=''
    while marker != 'X' and marker != 'O':
        marker=input('\t \t \t Enter X or O::->')
        if marker!='X' and marker!='O':
            print('\t \t \t',end='')
            print('Enter The Valid Symbol')
        else:
            break
        
    if first==1:    
        if marker == 'X':
            player1='X'
            player2='O'
        else:
            player1='O'
            player2='X'
    elif first==2:
        if marker=='X':
            player1='O'
            player2='X'
        else:
            player1='X'
            player2='O'
    return [[player1,player2],first]
def place_marker(board,marker,position):
    board[position]=marker

    
def win_check(board,mark):
    count1=0
    count2=0
    row1=1
    for i in range(1,4):
        for j in range(0,3):
            
            
            
            if board[row1+j] == mark:
                count1 +=1
            if board[i+j*3] == mark:
                count2 +=1
        if count1 == 3 or count2 == 3:
            return True
        
        count1=0
        count2=0
        row1 = row1 + j +1
        
    if board[1]== mark and board[9] == mark and  board[5] == mark:
        return True
    if board[3]== mark and board[5]== mark and board[7] == mark:
        return True
    return False
    
def space_check(board,position):
    return board[position] == ' '
    
def full_board(board):
    return board.count(' ') == 0
def player_choice(board):
    choice=int(input('\t \t \t Enter The Choice::'))
    while True:
        
        if choice>=1 and choice<=9:
            break
        else:
            choice=int(input('\t \t \tChoose the correct choice::'))
            
            
            
    check=space_check(board,choice)
    if check == True:
        return choice
    else:
        return 0
def replay():
    print('\t \t \tWANT TO PLAY AGAIN???')
    print('\t \t \t',end='')
    t=input('Enter Yes or No')
    if t.lower()=='yes':
        print('\n'*100)
        the_game()
        
    else:
        print('\t \t \tThanks for Playing')


def the_game():
    board=[' ']*10
    board[0]='o'
    display_board(board)
    players=[['PLAYER1',0],['PLAYER2',0]]
    k=player_input()
    players[0][1]=k[0][0]
    players[1][1]=k[0][1]
    first=k[1]-1
    end_game=False
    game_tie=False
    winner=False
    while not end_game:
        in1=0
        print('\t \t \t',end='')
        print(players[first][0],':->')
        check=player_choice(board)
        if check != 0:
            place_marker(board,players[first][1],check)
            win=win_check(board,players[first][1])
            if win:
                end_game=True
                winner=True
                display_board(board)
                break
            b_full=full_board(board)
            if b_full == True:
                game_tie=True
                end_game=True
                display_board(board)
                break
        else:
            print('\t \t \t',end='')
            print('INVALID CHOICE!!!,Please Enter Again')
            in1=1
        if in1==1:
            pass
        else:
            first=(first+1)%2
            display_board(board)
        
    if end_game==True:
   
        print('\n'*20)
        print('-'*80)
        if winner==True:
            display_board(board)
            print('\t \t \t',end='')
            print(players[first][0],'--  IS THE WINNER ',chr(5)*4)
        if game_tie:
            display_board(board)
            print('\t \t \t',end='')
            print('Game Tied')
        print('-'*80)
    replay()
  


print('\t \t \t @@@@@WELCOME TO THE GAME@@@@')
the_game()
        
