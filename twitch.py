import socket
from ircclient import IrcClient
import time
import twitchconfig

SERVER_NAME = "irc.chat.twitch.tv"
SERVER_PORT = 6667

if __name__ == "__main__":
    print("main")

    client = IrcClient(SERVER_NAME, SERVER_PORT)
    client.login(twitchconfig.username, twitchconfig.password)
    client.join(twitchconfig.username)
    client.priv_msg(twitchconfig.username, "Hi, das ist ein test!!")

    print(client.read_messages())

    client.priv_msg(twitchconfig.username, "Hey there")

    print(client.read_messages())
        