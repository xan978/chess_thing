import socket, pickle

class Network:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn = None

    def server_host(self, ip, port):
        self.sock.bind((ip, port))
        self.sock.listen(1)
        print(f"[SERVER] Waiting for connection on {ip}:{port}...")
        self.conn, addr = self.sock.accept()
        print(f"[SERVER] Connected to {addr}")

    def client_connect(self, ip, port):
        try:
            self.sock.connect((ip, port))
            self.conn = self.sock
            print(f"[CLIENT] Connected to server at {ip}:{port}")
        except Exception as e:
            print(f"[CLIENT] Connection failed: {e}")

    def send_move(self, start, end):
        if self.conn:
            data = pickle.dumps((start, end))
            self.conn.sendall(data)

    def receive_move(self):
        data = b""
        while True:
            packet = self.conn.recv(4096)
            if not packet:
                break
            data += packet
            try:
                return pickle.loads(data)
            except EOFError:
                continue
