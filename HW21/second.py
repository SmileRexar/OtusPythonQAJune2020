import email
import json
import random
import socket
from io import StringIO

LOCALHOST = "127.0.0.1"


def random_port():
    return random.randint(20000, 30000)


def echo_server():
    my_socket = socket.socket()
    address_and_port = (LOCALHOST, random_port())
    my_socket.bind(address_and_port)
    print("Started socket on", address_and_port)

    my_socket.listen(10)

    conn, addr = my_socket.accept()
    print("Got connection", conn, addr)

    # Получаем данные из соединения
    data = conn.recv(1024)
    print("Got data", data)

    # https://stackoverflow.com/a/39091087
    # pop the first line so we only process headers
    _, headers = data.decode("utf-8").split('\r\n', 1)
    # construct a message from the request string
    message = email.message_from_file(StringIO(headers))
    # construct a dictionary containing the headers
    headers = dict(message.items())
    # # prett-print the dictionary of headers
    # pprint.pprint(headers, width=160)

    # Пример отправки html ответа
    # conn.send("HTTP/1.1 200 OK\n Content-Length: 100\n Connection: close\n Content-Type: application/json\n\n <h1>Hello from OTUS!</h1>".encode("utf-8"))

    r = json.dumps(headers)
    loaded_r = json.loads(r)
    conn.send(
        f"HTTP/1.1 200 OK\n Content-Length: 100\n Connection: close\n Content-Type: application/json\n\n "
        f"{loaded_r}".encode("utf-8"))
    print(str(loaded_r))
    my_socket.close()


if __name__ == "__main__":
    # execute only if run as a script
    echo_server()
