import socket
import setting
if __name__ == "__main__": 
    s = socket.socket()
    s.bind((setting.host, setting.port))
    while True:
        c,addr = s.accept()
        data = c.recv()
        c.send('test!')
        c.close()