from pathlib import Path
path = Path(r"C:\Projects\vscode-basics\cats.txt")
def get_cats_info(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        result = []
        for line in lines:
            words = line.strip().split(",")
            if len(words) == 3:
                cat = {"id": words[0], "name": words[1], "age": int(words[2])}
                result.append(cat)
        return result

    except FileNotFoundError:
        return "Файл не найден!"

cats_info = get_cats_info(path)
print(cats_info)
