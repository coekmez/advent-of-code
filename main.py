import importlib
import os

YEARS = ["2023", "2025"]

if __name__ == "__main__":
    for year in YEARS:
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
                # display solution
                print(f"Results for Day {i}")
                curr_day.solve(data)
            except (ModuleNotFoundError, FileNotFoundError):
                print(f"Day {i} data file not found.\n")
                break
