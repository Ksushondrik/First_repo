import sys
from pathlib import Path

rec_count: int = 0

def main(way: str) -> None:
    global rec_count
    rec_count += 1
    direct = Path(way)
    if direct.exists():
        print(f"{'\t'*(rec_count-1)}Директорія {direct.name} :")
        for element in direct.iterdir():
            if element.is_dir():
                main(element)
            elif element.is_file():
                print(f"{'\t'*rec_count}Файл {element.name}")
            else:
                print("Невизначений формат об'єкта.")
    else:
        print("Директорія не існує!")
    rec_count -= 1 if rec_count > 0 else rec_count

main("D:\\Programs\\fop")