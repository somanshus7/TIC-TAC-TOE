#!/usr/bin/env python
# coding: utf-8

# # day4 assignement2 TIC TAC TOE GAME

# In[3]:


from IPython.display import clear_output

def displaygameboard(board):
    clear_output()
    print(' '+board[7]+' | '+board[8]+' | '+board[9]+' ')
    print('---------')
    print(' '+board[4]+' | '+board[5]+' | '+board[6]+' ')
    print('---------')
    print(' '+board[1]+' | '+board[2]+' | '+board[3]+' ')


# In[4]:


board = ['#','X','O','X','O','X','O','X','O','X','O']


# In[5]:


displaygameboard(board)


# In[6]:


def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == "O"):
        marker = input("Enter a Marker X/O for player one : ").upper()
    
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')


# In[7]:


player_input()


# In[8]:


def place_marker(board,marker,position):
    board[position] = marker


# In[9]:


place_marker(board,"X",5)


# In[10]:


displaygameboard(board)


# In[11]:


def win_check(board,marker):
    
    if( (board[7]==marker and board[8]==marker and board[9]==marker) or
        (board[4]==marker and board[5]==marker and board[6]==marker) or
        (board[1]==marker and board[2]==marker and board[3]==marker) or
        (board[7]==marker and board[4]==marker and board[1]==marker) or
        (board[8]==marker and board[5]==marker and board[2]==marker) or
        (board[9]==marker and board[6]==marker and board[3]==marker) or
        (board[7]==marker and board[5]==marker and board[3]==marker) or
        (board[9]==marker and board[5]==marker and board[1]==marker)):
        return True
    else:
        return False


# In[12]:


win_check(board,'X')


# In[13]:


win_check(board,'O')


# In[14]:


import random 

def choose_first():
    num = random.randint(0,1)
    
    if num == 1:
        return 'Player 1'
    else:
        return 'Player 2'


# In[15]:


choose_first()


# In[16]:


board = ['#','X',' ',' ','O','X',' ','X',' ','X','O']


# In[17]:



def space_check(board,position):
    return board[position]==''


# In[18]:


space_check(board,6)


# In[19]:


def full_board_check(board):
    itsFull = True
    for i in board:
        if i == ' ':
            itsFull = False
    return itsFull


# In[20]:


full_board_check(board)


# In[21]:


def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


# In[22]:


full_board_check(board)


# In[23]:


def players_choice(board):
    position = 0
    
    while not position in [1,2,3,4,5,6,7,8,9] or not space_check(board,position) : 
        position = int(input("Enter your next position : "))
        
    return position


# In[ ]:


players_choice(board)


# In[ ]:


def replay():
    return input("Do you want to play again (Y/N) : ").lower().startswith('y')


# In[ ]:


replay()


# In[ ]:


#logic


# In[ ]:


while True:
    
    board = [' ']* 10
    
    
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    
    print(turn + " Will play First")
    
    play_game = input("Are you ready to play the game Y/N").lower().startswith('y')
    
    if play_game:
        game_on = True
    else:
        game_on = False
    
    while game_on:
        if turn == 'Player 1':
            # player1 logic
            
            display_board(board)
            position = players_choice(board)
            place_marker(board,player1_marker,position)
            
            if win_check(board,player1_marker):
                display_board(board)
                print("PLAYER1 WON THE GAME")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('OOPS ITS A DRAW GAME!!')
                    break
                else:
                    turn = "Player 2"
        else:
            # Player 2 Logic 
            
            display_board(board)
            position = players_choice(board)
            place_marker(board,player2_marker,position)
            
            if win_check(board,player2_marker):
                display_board(board)
                print("PLAYER 2 WON THE GAME")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('OOPS ITS A DRAW GAME  !!')
                    break
                else:
                    turn = "Player 1"
    
    if not replay():
        break


# In[ ]:





# In[ ]:




