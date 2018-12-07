from IPython.display import clear_output

nums=['#' for i in range(9)]
count=0
gameround=1
def player():
    return ('Player1' if count%2 else 'Player2') if gameround%2 else ('Player2' if count%2 else 'Player1')
def print_board():
    print(f'1|2|3           {nums[0]}|{nums[1]}|{nums[2]}',f'4|5|6           {nums[3]}|{nums[4]}|{nums[5]}',
          f'7|8|9           {nums[6]}|{nums[7]}|{nums[8]}',sep='\n-------           -------\n')
    print('\n')
def replay():
    global gameround
    replay = input('Do you want to replay? Yes or No :')
    if replay.lower().startswith('y'):
        gameround= gameround+1
        clear_output()
        for i in range(9):nums[i]='#'
        print_board()
        return False
    else : return True
def checkOver():
    clear_output()
    print_board()
    for i in range(3):
        if set(nums[3*i:3*i+3:1]) < {'O','X'} or set(nums[i::3])< {'O','X'} :
            print(player()+' win!')
            return replay()
    if nums[0]==nums[4]==nums[8]!='#' or nums[2]==nums[4]==nums[6]!='#' :
        print(player()+' win!')
        return replay()
    if set(nums)<={'X','O'}:
        print('All set, game over, DRAW!')
        return replay()
    return False

while not checkOver():
    count = count+1
    inp_num = input(player()+' : pls input your number')
    while not (inp_num.isdigit() and 1<=int(inp_num)<=9 and nums[int(inp_num)-1]=='#'):
        print('Not a number between 1~9 or number has already been set')
        inp_num = input(player()+' : pls input your number')
    nums[int(inp_num)-1]= 'O' if count%2 else 'X'
