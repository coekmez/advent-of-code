import importlib
import inspect

YEARS = ['2023']

if __name__ == "__main__":
    print("Results for 2023")
    for i in range(1,5):
        # import the day module
        curr_day = importlib.import_module(f"year_2023.day_{i}")
        # load data
        with open(f'year_2023/dataset/day_{i}.txt', 'r') as f:
            data = f.read().splitlines()
        # display solution
        print(25*'-')
        print(f"Results for Day {i}")
        curr_day.solve(data)






