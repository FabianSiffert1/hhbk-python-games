class GameTable:
    """Game Screen Content"""

    global chessPositions
    global checkersPositions
    playerColors = ["blue","red"]
    def __init__(self):
        self.chessPositions = [
                [2,2,2,2,2,2],
                [0,0,0,0,0,0],
                [0,0,0,0,0,0],
                [0,0,0,0,0,0],
                [0,0,0,0,0,0],
                [1,1,1,1,1,1]
            ]

        self.checkersPositions = [
                [0,0,0,0,0,2],
                [2,0,2,0,2,0],
                [0,0,2,0,0,0],
                [0,0,0,2,0,0],
                [0,0,0,0,2,0],
                [1,1,1,1,1,1]
            ]

        

