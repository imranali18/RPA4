"""

  This module pokemon contains the testing code for class Pokemon which
  needs to be written as one of Lecture 18 Exercises.
  
"""
class Pokemon(object):
    def __init__ (self, name, board_size, init_pos = (0, 0)):
        self.name = name
        self.brd_size = board_size
        self.pos = [init_pos[0], init_pos[1]]

    def move(self, direction):
        if direction == "N":
            self.pos[0] = max(self.pos[0] - 1, 0)
        elif direction == "E":
            self.pos[1] = min(self.pos[1] + 1, self.brd_size[1] - 1)
        elif direction == "S":
            self.pos[0] = min(self.pos[0] + 1, self.brd_size[0] - 1)
        elif direction == "W":
            self.pos[1] = max(self.pos[1] - 1, 0)

    def __str__(self):
        return "{} is at row {}, column {}.".format(self.name, self.pos[0], self.pos[1])

if __name__ == "__main__":
    # Set #1 of tests
    rows = 10
    cols = 12
    celebi = Pokemon("Celebi", (rows, cols), (rows // 2, cols // 2))
    celebi.move("N")
    celebi_description = str(celebi)
    print(celebi_description)
    for dummy_idx in range(8):
        celebi.move("E")
        celebi.move("S")
    print(celebi)

    ditto = Pokemon("Ditto", (rows, cols))
    ditto.move("S")
    print(ditto)
    ditto.move("W")
    print(ditto)

    # Set #2 of tests
    pmon = Pokemon("Unknown", (1, 1))
    pmon.move("S")
    pmon.move("S")
    pmon.move("E")
    pmon.move("N")
    pmon.move("S")
    pmon.move("W")
    pmon.move("W")
    pmon.move("W")
    print(pmon)