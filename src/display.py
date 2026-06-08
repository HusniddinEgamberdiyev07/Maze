class Display:

    SYMBOLS = {
        0: "#",   # wall
        1: " ",   # path
        2: ".",   # solution path
    }

    @staticmethod
    def render(grid):
        lines = []

        for r, row in enumerate(grid.cells):
            line = ""

            for c, cell in enumerate(row):

                if grid.start == (r, c):
                    line += "S"
                elif grid.end == (r, c):
                    line += "E"
                else:
                    line += Display.SYMBOLS[cell]

            lines.append(line)

        return "\n".join(lines)