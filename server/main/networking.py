import socket
import threading

class Networking():
    def __init__(self, server, ip, port, max_connections):
        self.server=server
        self.ip=ip
        self.port=port
        self.max_connections=max_connections
        self.client_threads=[]
        
    def setup_networking(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            self.socket.bind((self.ip, self.port))
        except self.socket.error as e:
            return False
        
        self.socket.listen(self.max_connections)

        return True
        
    def server_thread(self):
        while True:
            conn, addr = self.socket.accept()
            self.server.print_log("Connected to: {}:{}".format(*addr))
            client_thread=threading.Thread(target=self.client_thread, args=(conn,))
            client_thread.start()
            self.client_threads.append(client_thread)
            
    def client_thread(self,conn):
        conn.send( str.encode('1') )
        reply = ""
        while True:
            try:
                data = conn.recv(2048).decode()

                if not data:
                    print("Disconnected")
                    break
                else:
                    reply=str(float(data)*2)

                    self.server.print_log("Received: " + data + ", Sending : " + reply)

                conn.sendall(str.encode(reply))
            except Exception as e:
                print(e)
                break

        self.server.print_log("Lost connection")
        conn.close()

    def start_server_networking_thread(self):
        self.server_thread=threading.Thread(target=self.server_thread, args=())
        self.server_thread.start()
        
