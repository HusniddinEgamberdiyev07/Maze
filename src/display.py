class Display:

    SYMBOLS = {
        0: "#",
        1: " ",
        2: ".",
        3: "·"
    }

    @staticmethod
    def render(grid, game=None):
        lines = []

        for r, row in enumerate(grid.cells):
            line = ""

            for c, cell in enumerate(row):

                if game and game.player == (r, c):
                    line += "P"
                elif grid.start == (r, c):
                    line += "S"
                elif grid.end == (r, c):
                    line += "E"
                else:
                    line += Display.SYMBOLS.get(cell, "?")

            lines.append(line)

        return "\n".join(lines)