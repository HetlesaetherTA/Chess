def convert(string): 
    lookupTable = {
            "a": 0,
            "b": 1,
            "c": 2,
            "d": 3,
            "e": 4,
            "f": 5,
            "g": 6, 
            "h": 7}
    # Creates the output based on string length (E1 = pawn to e1, RB2 means rook to B2, N2B2 means Knight on 2. file to B2)
    # piece = piece to be moved, helper = helper information if piece + move is ambiguous, move: where the piece should end up.
    if len(string) == 2:
        output = {"piece": "p", "helper": "", "move": (lookupTable[string[0].lower()], int(string[1]) - 1)}
    elif len(string) == 3:
        output = {"piece": string[0], "helper": "", "move": (lookupTable[string[1].lower()], int(string[2]) - 1)}
    elif len(string) == 4:
        output = {"piece": string[0], "helper": "", "move": (lookupTable[string[2].lower()], int(string[3]) - 1)}
        try:
            output["helper"] = (int(string[1]) - 1, "y")
        except:
            try:
                output["helper"] = (lookupTable[string[1].lower()], "x")
            except:
                return {"error": 2, "message": "String is likely out of bound on x axys"}
    else:
        return {"error": 2, "message": "String has to be 3 or 4 characters long"}
    
    # Checks if move or helper is out of bound 
    if output["move"][0] >= 0 and output["move"][0] <= 7 and output["move"][1] >= 0 and output["move"][1] <= 7:
        if output["helper"] and output["helper"][0] < 0 and output["helper"][0] > 7:
            return {"error": 2, "message": "String is out of bound and can not be converted to a move"}
        return output    
    #TODO clean up code and add support for castling
print(convert("Rab4"))
