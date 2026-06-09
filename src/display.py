class Display:
    RESET = "\033[0m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    CYAN = "\033[96m"
    GRAY = "\033[90m"

    @staticmethod
    def render(grid):
        lines = []

        for r, row in enumerate(grid.cells):
            line = ""

            for c, cell in enumerate(row):
                pos = (r, c)

                if pos == grid.player:
                    line += Display.YELLOW + "P" + Display.RESET

                elif pos == grid.start:
                    line += Display.GREEN + "S" + Display.RESET

                elif pos == grid.end:
                    line += Display.RED + "E" + Display.RESET

                elif pos in grid.solution_path:
                    line += Display.CYAN + "·" + Display.RESET

                else:
                    if cell == 0:
                        line += Display.GRAY + "█" + Display.RESET
                    else:
                        line += " "

            lines.append(line)

        return "\n".join(lines)