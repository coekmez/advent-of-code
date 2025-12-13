import argparse
import importlib
import os

YEARS = ["2023", "2025"]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code")
    parser.add_argument("-y", "--year", default="2025", type=str, help="Year")
    args = parser.parse_args()
    year = args.year

    print(5 * "#", f"YEAR {year}", 5 * "#")
    for i in range(1, 25):
        try:
            print(21 * "-")
            # import the day module
            curr_day = importlib.import_module(f"year_{year}.day_{i}")
            # load data
            root_path = f"year_{year}/dataset"
            with open(os.path.join(root_path, f"day_{i}.txt"), "r") as f:
                data = f.read().splitlines()
            # solve
            sol_1, sol_2 = curr_day.solve(data)
            # display solution
            print(f"Results for Day {i}")
            print(f"Part 1: {sol_1}")
            print(f"Part 2: {sol_2}")
        except (ModuleNotFoundError, FileNotFoundError):
            print(f"Day {i} data file not found.\n")
            break
