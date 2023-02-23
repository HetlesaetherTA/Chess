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
    def render():
        for y in range(9):
            if y != 8:
                print(str(8 - y) + " |", end="")
            for x in range(9):
                for i in Board.white:
                    if Board.white[i]["loc"] == (x, y):
                        print(Board.white[i]["piece"][0] + " ", end="")
                    if Board.black[i]["loc"] == (x, y):
                        print(Board.black[i]["piece"][0] + " ", end="")
                if y == 8 and x == 0:
                    print("  ", end="")
                if y == 8 and x != 8:
                    print(chr(65 + x) + " ", end="")
                if x == 8:
                    print("\n", end="")
                # You could add logic to check white first if y > 4 and black first if y < 4.
                # But there is only 1792 (32 * 56) iterations worse case so I can't be bothered. 
                # Another alternative that's even faster is to put all locations in an array 
                # then sort, print, and pop it. That gives you O(nlogn+56) (32 * log(32) + 56 = 216).
                # Or I could've formated the dictonary like this: board[loc] = piece to make it O(n). 
Board.render()
