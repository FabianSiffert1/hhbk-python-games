class GameScore:
    """Game Screen Content"""

    global score


    def __init__(self):
        self.score = [
            0, 0
        ]

    def evaluateScore(self, figurePositions , team, cellCount):
        scoreReturn = 0
        result = [0,0,0,0,0,0]

        
        x = 0
        y = 0
        while x < cellCount:
            while y < cellCount:
                if figurePositions[y][x] == team:
                    if team == 1:
                        result[x] = cellCount - y - 1
                        scoreReturn += result[x] * result[x] / cellCount
                    else:
                        result[x] = y 
                        scoreReturn += result[x] * result[x] / cellCount
                y +=1
            y = 0
            x+=1

        return scoreReturn
