import itertools, random

class Chess960():
    pieces = "RNBQKBNR"

    def __init__(self) -> None:
        allPermutations = set(itertools.permutations(self.pieces))
        self.positions = [x for x in allPermutations if self.isValid(x)]

    def random(self):
        return self.positions[random.randint(0, len(self.positions) - 1)]
    
    def randomGlyph(self):
        return "".join(self.glyphize(self.random()))

    def isValid(self, perm):
        rooksBeforeKing = 0
        bishopParity = 0
        for i, c in enumerate(perm):
            if c == "R":
                rooksBeforeKing += 1
            if c == "K" and rooksBeforeKing != 1:
                return False
            if c == "B":
                bishopParity += i%2
        return bishopParity == 1

    def glyphize(self, pos):
        piecesGlyphs = {
            "R": "♖",
            "N": "♘",
            "B": "♗",
            "Q": "♕",
            "K": "♔"
        }
        result = []
        for x in pos:
            result.append(piecesGlyphs[x])
        if type(pos) == str:
            return "".join(result)
        else:
            return result
    
if __name__ == "__main__":
    # We're going to brute-force permuate the pieces, and then weed out the duplicates and invalids
    chess960 = Chess960()

    print(chess960.randomGlyph())
