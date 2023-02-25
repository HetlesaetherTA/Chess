class Move():
    # Takes a string in chess format like nC3 (knight to C3)
    # and converts it to a better format for processing ({piece: n, move: (2,2)})
    def convert(string):
        if len(string) == 3:
            output = {"piece": string[0], "helper": "", "move": string[1:3]}
        else:
            output = {"piece": string[0], "helper": [1], "move": string[2:4]}

x_lim = y_lim = (0,7)


