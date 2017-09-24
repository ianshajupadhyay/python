a1=[]
print("TIC-TAC-TOE")
print("===========")
for k in range(3):
    a1.append([0,0,0])
flag=0
x=0
for z in range(0,9):
    while(flag==0):
        if(x%2==0):
            print("Player 1 enter the position of  'X'")
            i=int(input())
            j=int(input())
            a1[i][j]='X'
        else:
            print("Player 1 enter the position of  'O'")
            i=int(input())
            j=int(input())
            a1[i][j]='O'
        if((a1[i][0]==a1[i][1]==a1[i][2]=='X')or(a1[0][j]==a1[1][j]==a1[2][j]=='X')):
            flag=1
        elif((a1[0][0]==a1[1][1]==a1[2][2]=='X')or(a1[0][2]==a1[1][1]==a1[2][0]=='X')):
            flag=1
        if((a1[i][0]==a1[i][1]==a1[i][2]=='O')or(a1[0][j]==a1[1][j]==a1[2][j]=='O')):
            flag=2
        elif((a1[0][0]==a1[1][1]==a1[2][2]=='O')or(a1[0][2]==a1[1][1]==a1[2][0]=='O')):
            flag=2
        x=x+1
    break
if(flag==1):
    print("Player 1 wins")
elif(flag==2):
    print("Player 2 wins")
else:
    print("The match was a draw!")

    
