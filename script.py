import socket

HOST = '127.0.0.1'
PORT = 8000

def fileResp(content, contentType):
    return (
        "HTTP/1.1 200 OK\r\n"
        f"Content-Type: {contentType}; charset=UTF-8\r\n"
        f"Content-Length: {len(content.encode())}\r\n"
        "Connection: keep-alive\r\n"
        "Cache-Control: no-cache\r\n"
        "\r\n"
        f"{content}"
    )

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Listening on {HOST}:{PORT}")
    
    while True:
        conn, addr = s.accept()
        with conn:
            try:
                rawRequest = conn.recv(1024).decode()
                request = rawRequest.split(" ") 
                print(f"Request:\n{rawRequest}")
                method = request[0]
                path = request[1]


                if method == "GET":
                    if path == "/close":
                        break
                    if path == "/":
                        with open("static/index.html") as file:
                            content = file.read()
                            response = fileResp(content, 'text/html')
                            conn.sendall(response.encode())

                    if path == "/index.js":
                        with open("static/index.js") as file:
                            content = file.read()
                            response = fileResp(content, 'text/js')
                            conn.sendall(response.encode())

                    if path == "/style.css":
                        with open("static/style.css") as file:
                            content = file.read()
                            response = fileResp(content, 'text/css')
                            conn.sendall(response.encode())

            except IndexError:
                print("haah what to say lol")
