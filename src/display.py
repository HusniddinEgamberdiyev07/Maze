class Display:

    SYMBOLS = {
        0: "█",   # wall
        1: "·",   # path
        2: "*",   # SOLUTION PATH
        3: "·"    # explored
    }

    @staticmethod
    def render(grid):
        lines = []

        for r, row in enumerate(grid.cells):
            line = ""

            for c, cell in enumerate(row):
                pos = (r, c)

                if pos == grid.start:
                    line += "S"
                elif pos == grid.end:
                    line += "E"
                elif pos == grid.player:
                    line += "P"
                else:
                    line += Display.SYMBOLS.get(cell, " ")

            lines.append(line)

        return "\n".join(lines)