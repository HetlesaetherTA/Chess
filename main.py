from game import Board
import moves

Board.render()
turn = 0

while True:
    player = "white" if turn % 2 == 0 else "black" 
    move = input("move: ")
    #TODO Add support for chess notation to use as input
    if len(move) == 4:
        mfrom = move[0:2]
        mto = move[2:4]
    else: 
        mfrom = move[0]
        mto = move[1:3]
    print(mfrom, mto)
    print(move_to)
    for i in Board.white:
        print(Board.white[i]["loc"])
        if Board.white[i]["loc"] == move_from:
            Board.white[i]["loc"] = move_to
    Board.render() 

