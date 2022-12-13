from datetime import datetime as dt

def log(a, b, op, res):
    time = dt.now().strftime('%H:%M')
    with open("log.txt", 'a', encoding="utf-8") as file:
        file.write(f"{time}: {a} {op} {b} = {res} \n")