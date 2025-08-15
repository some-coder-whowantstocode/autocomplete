def write(msg):
    file_path = "../monitor/loger.txt"
    with open(file_path) as file:
        file.write(msg)