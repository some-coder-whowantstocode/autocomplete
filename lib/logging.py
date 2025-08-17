def write(msg):
    file_path = "monitor/loger.txt"
    with open(file_path, "w") as f:
        f.write(msg)