# Tower of Hanoi

def moves(discs, trivial):
    if trivial:
        return 0
    moves = 1
    while discs > 1:
        moves += moves + 1
        discs -= 1
    return moves

i = open("Tower-of-Hanoi_InputForSubmission_1.txt")
lines = i.readlines()
for line in lines:
    l = line.split(",")
    print(moves(int(l[0]),l[1]==l[2][0]))
