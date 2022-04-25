class GameScore:
    """Game Screen Content"""

    global score


    def __init__(self):
        self.score = [
            0, 0
        ]

    def evaluateScore(self, playerPositions , team, game):
        scoreResult = 0
        teamGamePieces = 0
        direction = (team - 1) * 2 - 1
        for x in range(game.cellCount):
            for y in range(game.cellCount):
                if playerPositions[x][y] == team:
                    teamGamePieces += 1

        for x in range(game.cellCount):
            for y in range(game.cellCount):
                if playerPositions[x][y] == team:
                    if direction != 1:
                        print('directionfoo')
                        scoreResult += x
                        print(scoreResult)
                    else:
                        scoreResult += x
            return scoreResult


