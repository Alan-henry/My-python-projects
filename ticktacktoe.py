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
    while i<=2:
        i+=1
        #Diagonal
        if board[0] == board[4] and board[8]==board[4] and board[0]!=" ":
            a=board[0]
            type= True
        elif board[2] == board[4] and board[6]==board[4] and board[2]!=" ":
            a=board[2]
            type= True
        #Horizontal
        elif board[0] == board[1] and board[2]==board[0] and board[0]!=" ":
            a=board[0]
            type= True
        elif board[3] == board[4] and board[5]==board[4] and board[3]!=" ":
            a=board[3]
            type= True
        elif board[6] == board[8] and board[8]==board[7] and board[6]!=" ":
            a=board[6]
            type= True
        #Vertical
        elif board[0] == board[3] and board[3]==board[6] and board[0]!=" ":
            a=board[0]
            type= True
        elif board[1] == board[4] and board[7]==board[4] and board[1]!=" ":
            a=board[1]
            type= True
        elif board[2] == board[5] and board[8]==board[5] and board[2]!=" ":
            a=board[2]
            type= True

        else:
            type= False
        if type==True:
            print(a+" Wins")
        return type

        
        
        
def main():
    
    print("1 for pvp 2 for pvc: ", end="")
    decision=input()
    type=check_win()
    print()
    i=0
    #Against person
    if decision=="1":
        while i<=8 and type!=True:
            if type==True:
                check_win()
                break
            type=check_win()
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


        if type==False:
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


            
                



    