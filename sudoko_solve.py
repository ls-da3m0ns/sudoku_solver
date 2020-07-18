import numpy as np
import sys 

#set recursion limit 
sys.setrecursionlimit(10**6)

#defining variables which will be used during recursion
row, column = 0,0
unsolved_ar = np.zeros((9,9))

#function to find next empty box
def find_empty_box():
    for i in range(9):
        for j in range(9):
            if unsolved_ar[i][j] == 0:
                row = i
                column = j
                return row,column
    return -1,-1

#check whether a box filled with any number is allowed or not
def is_safe(i,j):
    box_x = int(i/3)*3
    box_y = int(j/3)*3

    current_num = unsolved_ar[i][j]

    box_elements = unsolved_ar[box_x:box_x+3, box_y:box_y+3].reshape(9)

    for index in range(9):
        if ((unsolved_ar[index][j] == current_num and index != i) or (unsolved_ar[i][index] == current_num and index != j) or box_elements[index] == current_num and index != (3*(i-box_x)+j-box_y) ):
            return False

    return True

#function to check if unsolved sudoko is initially legal or not
def find_illegal_sudoko():
    for i in range(9):
        for j in range(9):
            if (is_safe(i,j) == False and unsolved_ar[i,j]!=0 ):
                print("Not a Valid sudoko : ",i,j)
                return False
    return True 

def solve():
    row, column = find_empty_box()
    if row == -1 :
        return True

    for num in range(1,10):
        unsolved_ar[row,column] = num
        if(is_safe(row,column)):
            if solve():
                return True
            unsolved_ar[row,column] = 0
        else:
            unsolved_ar[row,column] = 0
    return False


def check_and_solve(raw_sudoko):
    #perfom few checks before continuing
    global unsolved_ar
    try :
        len(raw_sudoko) == 81
    except:
        print("Length of sudoko received was {}".format(len(raw_sudoko)))
    
    unsolved_ar = np.array(raw_sudoko)
    unsolved_ar = unsolved_ar.reshape(9,9)

    print("The sudoko recieved is \n",unsolved_ar)

    if find_illegal_sudoko() :
        solve()
    print("The Solved sudoko is \n",unsolved_ar)
    solved = unsolved_ar

    return solved 
#raw = [0, 5, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 1, 0, 0, 7, 0, 0, 0, 5, 0, 0, 2, 0, 0, 9, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 1, 0, 9, 0, 0, 4, 8, 0, 7, 0]
#check_and_solve(raw)
    



    