from termcolor import colored
# "loc": (x, y)
class Board:
    white = {
            "lRook": {
                "loc": (0, 0),
                "moved": False,
                "piece": "r"},
            "lKnight": {
                "loc": (1, 0),
                "moved": False,
                "piece": "n"},
            "lBishop": {
                "loc": (2, 0),
                "moved": False,
                "piece": "b"},
            "queen": {
                "loc": (3, 0),
                "moved": False,
                "piece": "q"},
            "king": {
                "loc": (4, 0),
                "moved": False,
                "piece": "k"},
            "rBishop": {
                "loc": (5, 0),
                "moved": False,
                "piece": "b"},
            "rKnight": {
                "loc": (6, 0),
                "moved": False,
                "piece": "n"},
            "rRook": {
                "loc": (7, 0),
                "moved": False,
                "piece": "r"},
            "Apawn": {
                "loc": (0,1),
                "moved": False,   
                "piece": "p"},
            "Bpawn": {
                "loc": (1,1),
                "moved": False,
                "piece": "p"},
            "Cpawn": {
                "loc": (2,1),
                "moved": False,
                "piece": "p"},
            "Dpawn": {
                "loc": (3,1),
                "moved": False,
                "piece": "p"},
            "Epawn": {
                "loc": (4,1),
                "moved": False,
                "piece": "p"},
            "Fpawn": {
                "loc": (5,1),
                "moved": False,
                "piece": "p"},
            "Gpawn": {
                "loc": (6,1),
                "moved": False,
                "piece": "p"},
            "Hpawn": {
                "loc": (7,1),
                "moved": False,
                "piece": "p"}}
            
    black = {
            "lRook": {
                "loc": (0, 7),
                "moved": False,
                "piece": "R"},
            "lKnight": {
                "loc": (1, 7),
                "moved": False,
                "piece": "N"},
            "lBishop": {
                "loc": (2, 7),
                "moved": False,
                "piece": "B"},
            "queen": {
                "loc": (3, 7),
                "moved": False,
                "piece": "Q"},
            "king": {
                "loc": (4, 7),
                "moved": False,
                "piece": "K"},
            "rBishop": {
                "loc": (5, 7),
                "moved": False,
                "piece": "B"},
            "rKnight": {
                "loc": (6, 7),
                "moved": False,
                "piece": "N"},
            "rRook": {
                "loc": (7, 7),
                "moved": False,
                "piece": "R"},
            "Apawn": {
                "loc": (0,6),
                "moved": False,   
                "piece": "P"},
            "Bpawn": {
                "loc": (1,6),
                "moved": False,
                "piece": "P"},
            "Cpawn": {
                "loc": (2,6),
                "moved": False,
                "piece": "P"},
            "Dpawn": {
                "loc": (3,6),
                "moved": False,
                "piece": "P"},
            "Epawn": {
                "loc": (4,6),
                "moved": False,
                "piece": "P"},
            "Fpawn": {
                "loc": (5,6),
                "moved": False,
                "piece": "P"},
            "Gpawn": {
                "loc": (6,6),
                "moved": False,
                "piece": "P"},
            "Hpawn": {
                "loc": (7,6),
                "moved": False,
                "piece": "P"}}
    #TODO clean this shit up...
    def render():
        for y in reversed(range(9)):
            if y != 0:
                print(str(y) + " ", end="")
            for x in range(9):
                fileFree = True
                for i in Board.white:
                    if Board.white[i]["loc"] == (x, y - 1):
                        print(colored(Board.white[i]["piece"][0] + " ", "blue"), end="")
                        fileFree = False
                        break
                    if Board.black[i]["loc"] == (x, y - 1 ):
                        print(colored(Board.black[i]["piece"][0] + " ", "red"), end="")
                        fileFree = False
                        break
                if y == 0 and x == 0:
                    print("  ", end="")
                    fileFree = False
                if y == 0 and x != 8:
                    print(chr(65 + x) + " ", end="")
                    fileFree = False
                if x == 8:
                    fileFree = False
                if fileFree == True and x > -1 and y > 0:
                    print("* ", end="")
                if x == 7:
                    print("\n", end="")
                # Current naive worse case is 64 * 32 iterations (2048) per frame. 
                # Ideas for improvement:

                # Check white first if y > 4 & black first if y < 4 (optimize probability).
                # Store board in sorted array and iterate though that array insted, gives: (O(n log(n) + 64)) (224) per frame.
                # Store dictonary as loc: piece. Gives O(n) (64) per frame. But can cause complications in other parts of the program.
