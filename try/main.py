# # Name = ( Farhan Nawaz )
# # Roll No = ( 22569 )
# # Contact No = ( 03480278285 )
# # Gmail + ( farhannawazofficial@gmial.com )



# # ----------------------Start Coding ------------------------------------------

# def sum (a , b , c):
#     return a + b + c
# def prinrBoard(xState , yState):
#     zero = 'X' if xState [0] else ('0' if yState[0] else 0)
#     one = 'X' if xState [1] else ('1' if yState[1] else 1)
#     tow = 'X' if xState [2] else ('2' if yState[2] else 2)
#     three = 'X' if xState [3] else ('3' if yState[3] else 3)
#     four = 'X' if xState [4] else ('4' if yState[4] else 4)
#     fif = 'X' if xState [5] else ('5' if yState[5] else 5)
#     six = 'X' if xState [6] else ('6' if yState[6] else 6)
#     seven = 'X' if xState [7] else ('7' if yState[0] else 7)
#     eight = 'X' if xState [8] else ('8' if yState[8] else 8)
#     print(f" {zero} | {one} | {tow} ")
#     print(f"---|---|---")
#     print(f" {three} | {four} | {fif} ")
#     print(f"---|---|---")
#     print(f" {six} | {seven} | {eight} ")

# def checkWin (xState , yState)  :
#     wins = [[ 0 , 1 , 2 ] , [ 3 , 4 , 5 ] , [ 6 , 7 , 8 ] , [ 0 , 3 , 6 ] , [ 1 , 4 , 7 ] , [ 2 , 5 , 8 ] , [ 0 , 4 , 8 ] , [ 2 , 4 , 6 ]] 
#     for win in wins:
#         if (sum(xState[win[0]] , xState[win[1]] , xState[win[2]]) == 3):
#             print ("X is Won the Game")
#             return 1
#         if (sum(yState[win[0]] , yState[win[1]] , yState[win[2]]) == 3):
#             print ("O is won the Game")
#             return 0
#     return -1

# if __name__ == "__main__":
#     xState = [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ]
#     yState = [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ]
#     ture = 1
#     print("Well Come To Tic Tac Toe Game")
#     print ("Ap Apna 'X' Kha Liko Gay") 
#     while (True):
#         prinrBoard(xState , yState)
#         if (ture == 1):
#             print ("'X' ki Bari hy ")
#             value = int(input("Enter the value: "))
#             xState[value] = 1
#         else:
#             print("'O' ki Bari hy ")
#             value = int(input("Enter the value: "))
#             yState[value] = 1
#         cwin = checkWin(xState , yState)    
#         if (cwin!=-1):
#             print("Game is Over")
            
#         ture = 1 - ture    

# def foo(i, x=[]): 
#   x.append(x.append(i)) 
#   return x for i in range(3): print(foo(i)) 