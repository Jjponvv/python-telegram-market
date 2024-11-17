import makebot as data

if data.setData:
    with open("main.py") as file:
        exec(file.read())