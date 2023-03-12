import socket
import setting
import processing
if __name__ == "__main__": 
    s = socket.socket()
    s.bind((setting.host, setting.port))
    while True:
        c,addr = s.accept()
        data = c.recv()
        processing.unified(data)
        c.send('test!')
        c.close()