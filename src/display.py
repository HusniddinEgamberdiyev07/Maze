class Display:

    RESET = "\033[0m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    CYAN = "\033[96m"
    GRAY = "\033[90m"

    SYMBOLS = {
        0: "█",   # wall
        1: " ",   # path
        2: "·",   # solution path
        3: ".",   # explored
    }

    @staticmethod
    def render(grid):
        lines = []

        for r, row in enumerate(grid.cells):
            line = ""

            for c, cell in enumerate(row):
                pos = (r, c)

                # PLAYER
                if pos == grid.player:
                    line += Display.YELLOW + "P" + Display.RESET

                # START
                elif pos == grid.start:
                    line += Display.GREEN + "S" + Display.RESET

                # END
                elif pos == grid.end:
                    line += Display.RED + "E" + Display.RESET

                # GRID CELLS
                else:
                    if cell == 0:
                        line += Display.GRAY + "█" + Display.RESET
                    elif cell == 1:
                        line += " "
                    elif cell == 2:
                        line += Display.CYAN + "·" + Display.RESET
                    elif cell == 3:
                        line += "."

            lines.append(line)

        return "\n".join(lines)