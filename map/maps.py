from pathlib import Path
import csv

BASE_DIR = Path(__file__).resolve().parent

def load_csv_map(filename):
    path = BASE_DIR/"maps"/filename
    with path.open(newline='') as f:
        reader = csv.reader(f)
        return [[str(cell) for cell in row] for row in reader]

def get_map(map_name):
    return load_csv_map(map_name + ".csv")

if __name__ == "__main__":
    pass

