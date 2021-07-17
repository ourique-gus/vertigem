import socket
import threading
import numpy as np
import time
from main.character import Character

class Networking():
    def __init__(self, server, ip, port, max_connections):
        self.server=server
        self.ip=ip
        self.port=port
        self.max_connections=max_connections
        self.client_threads={}
        self.max_id=8192
        
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
            player_id=np.random.randint(*self.server.entity_manager.id_range['character'])
            while player_id in self.client_threads:
                player_id=np.random.randint(*self.server.entity_manager.id_range['character'])
            self.server.print_log("Connected to: {}:{}".format(*addr))
            client_thread=threading.Thread(target=self.client_thread, args=(conn,player_id,))
            client_thread.start()
            self.client_threads[player_id]=client_thread
            self.server.entity_manager.entities[player_id]=Character(self.server, player_id, np.random.rand()*10, np.random.rand()*10, 0)
            
    def client_thread(self,conn, player_id):
        st=time.time()
        conn.send( str(player_id).encode() )
        self.server.entity_manager.entities[0].info[player_id]={'last_time':time.time()}

        while True:
            try:
                data = conn.recv(2048).decode()
                
                if not data:
                    print("Disconnected")
                    break
                else:
                    try:
                        controls=[i for i in map(int,data.split(':'))]
                        self.server.entity_manager.entities[player_id].controls=controls
                    except:
                        pass
                
                    reply=''
                    if len(self.server.entity_manager.entities):
                        entity_data=self.server.entity_manager.get_entities_data(player_id)
                        ents=np.sort([ent for ent in entity_data])
                        reply=','.join([entity_data[ent] for ent in ents])
                        
                    #self.server.print_log("Received: " + data + ", Sending : " + reply)
                st=time.time()
                conn.sendall(str.encode(reply))
            except Exception as e:
                print(e)
                break

        self.server.print_log("Lost connection")
        conn.close()
        self.client_threads.pop(player_id)
        self.server.entity_manager.entities.pop(player_id)
        self.server.entity_manager.entities[0].info.pop(player_id)

    def start_server_networking_thread(self):
        self.server_networking_thread=threading.Thread(target=self.server_thread, args=())
        self.server_networking_thread.start()
 
