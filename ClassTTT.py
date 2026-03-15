
print("Tic-Tac-Toe")

# setup
s1 = 1
s2 = 2
s3 = 3
s4 = 4
s5 = 5
s6 = 6
s7 = 7
s8 = 8
s9 = 9

# displays the board
def show_board():
    print("=====")
    print(s1, "|", s2, "|", s3, sep="")
    print("-----")
    print(s4, "|", s5, "|", s6, sep="")
    print("-----")
    print(s7, "|", s8, "|", s9, sep="")
    print("=====")


player = "O"

# checks win conditions
def winner():
    if s1 == s2 and s2 == s3:
        return True
    elif s4 == s5 and s5 == s6:
        return True
    elif s7 == s8 and s8 == s9:
        return True
    elif s1 == s4 and s4 == s7:
        return True
    elif s2 == s5 and s5 == s8:
        return True
    elif s3 == s6 and s6 == s9:
        return True
    elif s1 == s5 and s5 == s9:
        return True
    elif s3 == s5 and s5 == s7:
        return True


# play
show_board()
while True:
    if player == "X":
        player = "O"
    else:
        player = "X"
    spot = input("Which spot? ")
    spot = int(spot)
    if spot == 1:
        s1 = player
    elif spot == 2:
        s2 = player
    elif spot == 3:
        s3 = player
    elif spot == 4:
        s4 = player
    elif spot == 5:
        s5 = player
    elif spot == 6:
        s6 = player
    elif spot == 7:
        s7 = player
    elif spot == 8:
        s8 = player
    elif spot == 9:
        s9 = player
    show_board()
    if winner():
        print("Nice Job")
        break
