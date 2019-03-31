import socket

class IrcClient():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self, server_name, server_port):
        self.client.connect((server_name, server_port))
        self.client.setblocking(0)

    def login(self, nickname, password):
        self.send_line("PASS " + password)
        self.send_line("NICK " + nickname)
    
    def join(self, channel):
        self.send_line("JOIN #" + channel)

    def part(self, channel):
        self.send_line("PART #" + channel)

    def priv_msg(self, channel, msg):
        self.send_line("PRIVMSG #" + channel + " :" + msg)

    def send_line(self, text):
        print(text)
        self.client.send(bytes(text + "\n\r", 'utf-8'))
    
    def read_messages(self):
        messages = ""
        data_found = 1

        while data_found:
            try:
                message = self.client.recv(1024)
                if message:
                    messages += str(message, "utf-8")
                    data_found = 1
                else:
                    data_found = 0
            except:
                if messages:
                    data_found = 0


        return messages