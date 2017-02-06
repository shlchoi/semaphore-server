import socket
import threading
import util.client_handler as handler
from json import load, dumps
from os.path import isfile


class Server(object):
    def __init__(self, host, port, config_path='config'):
        self._db_url = 'https://smartbox-041.firebaseio.com'
        self._email = ''
        self._secret = ''
        self._host = host
        self._port = port
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._sock.bind((self._host, self._port))
        if isfile(config_path):
            self.load_config(config_path)

    def load_config(self, config_path):
        with open(config_path, 'r') as _txt_file:
            _data = load(_txt_file)
            self._db_url = _data['db_url']
            self._email = _data['email']
            self._secret = _data['secret']
            _txt_file.close()

    def listen(self):
        self._sock.listen(5)
        while True:
            client, address = self._sock.accept()
            client.settimeout(60)
            threading.Thread(target=self.client, args=(client, address)).start()

    def client(self, client, address):
        size = 1024
        while True:
            try:
                data = client.recv(size)
                if data:
                    handler.process_data(self._db_url, self._email, self._secret, data)
                    client.send("OK")
                else:
                    raise Exception('Client disconnected')
            except:
                client.close()
                return False


if __name__ == "__main__":
    Server('', 8080).listen()
