from pathlib import Path
from pytmx import load_pygame

BASE_DIR = Path(__file__).resolve().parent

def get_map(map_name: str):
    path = f"{BASE_DIR}/maps/{map_name}.tmx"
    return load_pygame(path)

maps_list = ["first_floor", "second_floor"]

