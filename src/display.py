class Display:

    SYMBOLS = {
        0: "#",   # wall
        1: " ",   # path
        2: "."    # explored path
    }

    @staticmethod
    def render(grid):

        lines = []

        for row in grid.cells:
            line = ""

            for cell in row:
                line += Display.SYMBOLS[cell]

            lines.append(line)

        return "\n".join(lines)