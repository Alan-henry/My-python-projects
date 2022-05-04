import random

board =[" "]*9

def bo():
    row_1="{}|{}|{}".format(board[0],board[1],board[2])
    row_2="{}|{}|{}".format(board[3],board[4],board[5])
    row_3="{}|{}|{}".format(board[6],board[7],board[8])

    print(row_1+"\n"+row_2+"\n"+row_3)

    return row_1, row_2, row_3

def check_win():
    i=0
    while i<2:
        if i==0:
            a="x"
        if i==1:
            a="o"
        
        #Diagonal
        if board[0]==a and board[4]==a and board[8]==a:
            print(a+" Wins")
            return True
        elif board[2]==a and board[4]==a and board[6]==a:
            print(a+" Wins")
            return True
        #Horizontal
        elif board[0]==a and board[1]==a and board[2]==a:
            print(a+" Wins")
            return True
        elif board[3]==a and board[4]==a and board[5]==a:
            print(a+" Wins")
            return True
        elif board[6]==a and board[7]==a and board[8]==a:
            print(a+" Wins")
            return True
        #Vertical
        elif board[0]==a and board[3]==a and board[6]==a:
            print(a+" Wins")
            return True
        elif board[1]==a and board[4]==a and board[7]==a:
            print(a+" Wins")
            return True
        elif board[2]==a and board[5]==a and board[8]==a:
            print(a+" Wins")
            return True

        else:
            return False
        
        
def main():
    print("1 for pvp 2 for pvc: ", end="")
    decision=input()
    print()
    i=0
    #Against person
    if decision=="1":
        while i<=8:
            x=0
            o=0
            if i%2==0:
                print("Player one: ", end="")
                x=input()
                x=int(x)-1
                if board[int(x)]==" ":
                    board[int(x)]="x"
                    bo()
                    i+=1
                else:
                    print("Try again: ", end="")

            else:
                print("Player two: ", end="")
                o=input()
                o=int(o)-1
                if board[int(o)]==" ":
                    board[int(o)]="o"
                    bo()
                    i+=1
                else:
                    print("Try again: ", end="")

            if check_win()==True:
                check_win()
                break
        if check_win==False:
            print("Draw")

    if decision=="2":
        while i<=8:
            x=0
            o=0
            if i%2==0:
                print("Player one: ", end="")
                x=input()
                x=int(x)-1
                if board[int(x)]==" ":
                    board[int(x)]="x"
                    bo()
                    i+=1
                else:
                    print("Try again: ", end="")

            else:
                o=random.randint(1,9)
                o=int(o)-1
                if board[int(o)]==" ":
                    print("Player two:{}".format(o))
                    board[int(o)]="o"
                    bo()
                    i+=1

            if check_win()==True:
                check_win()
                break
        if check_win==False:
            print("Draw")


main()


            
                



    