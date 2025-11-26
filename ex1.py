from pathlib import Path

path = Path(r"C:\Projects\vscode-basics\blbl.txt")

def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()
        result = []
        for line in lines:
            words = line.strip().split(",")
            result.append(words)
        salaries = []
        for item in result:
            if len(item) >= 2:
                salaries.append(int(item[1]))
        total = sum(salaries)
        average = total / len(salaries)
        return total, average

    except FileNotFoundError:
        return "Файл не найден!"
    


total, average = total_salary(path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
