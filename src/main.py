import sys
from parse import ConfigParser, ParseError

class Fly_in:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def run(self):
        parser = ConfigParser(self.filepath)
        route_map = parser.parsetxt()

        simulation = Simulation(route_map)
        simulation.run()

        viz = Visualize(route_map)
        viz.run()


def main() -> None:
    if (len(sys.argv) != 2 ):
        print("Correct Usage: python3 main.py <map_file.txt>")
        return
    
    file_path = sys.argv[1]

    try:
        game = Fly_in(file_path)
        game.run()
    except (OSError, ValueError, RuntimeError) as error:
        print(f"Error: {error}")
    return


if __name__ == "__main__":
    main()