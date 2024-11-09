import socket
import sys
import threading
import time

yes_list = ["y","yes","Yes","Y"]
no_list = ["n","no","No","N"]
message_stack_list = ['\n\n\n\n\n\n\n\n']
message_stack_str = ''
server_socket = None
my_port = int
send_port = None
name = "hoge"
self_introduction = "profile"
end = False
friend_list_str = ''
friend_list_path = "friend.txt"
friend_list = open(friend_list_path, 'r')

class operate_server:
    send_port_num = int
    global server_socket
    #port_creat()のportnumberを使ってサーバー設立
    def port_connect(port):
        global server_socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((socket.gethostname(), int(port)))
        server_socket.listen(5)
    #send_portを変える関数
    def send_port_setting(send_port_setting):
        global send_port
        send_port = send_port_setting

    def send_message(message, send_message_port):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((socket.gethostname(), int(send_message_port)))
        client_socket.send(message.encode('utf-8'))
        client_socket.close()

    def receive_message(self):
        #while self.running
        global send_port
        if send_port == None:
            return
        else:
            self = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.connect((send_port))
            message = self.recv(1024).decode('utf-8')
            print(f"\n受信メッセージ from {send_port[1]}: {message}")

        

def start():
    global my_port
    global send_port
    my_port = int(input("port番号を入力してください"))
    operate_server.port_connect(my_port)
#    send_port = int(input("送信先のport番号を入力してください"))

#常に稼働するHome画面
def Home():
    global my_port
    global send_port
    global server_socket
    operate_server.receive_message(server_socket)
    num = input("\nHello!\n1:profile\n2:setting_send_port\n3:send_message\n4:add_friend\n5:exit\n\n")
    global name

    if num == "1":#profile
        global name
        global self_introduction
        global my_port
        profile = input("あなたのプロフィール\n\nあなたのport:" + str(my_port) +"\n名前:" + name + "\n自己紹介:" + self_introduction + "\n何を変更しますか？\n1:名前\n2:プロフィール\n3:exit\n\n")
        if profile == "1":
            new_name = input("名前を設定してください:")
            name = new_name

        elif profile == "2":
            new_self = input("プロフィールを入力してください:")
            self_introduction = new_self

    elif num == "2":#send_port_setting
        print()
    
    #messageを送る
    elif num == "3":
        global friend_list
        global friend_list_str
        global friend_list_path
        while True:
            friend_list_open = open(friend_list_path, 'a', encoding='UTF-8')
            friend_list_data_str = str(friend_list_open.read)
            friend_choice = input(str(friend_list_data_str) + "\n\n+add_friend[/add]\n\n")
            if friend_choice == "/add":
                add_friend_port = input("フレンドのポートを入力してください:")
                print("フレンドを追加しました！")
                friend_list_data = open(friend_list_path, 'a', encoding='UTF-8')
                friend_list_data.write('\n' + add_friend_port)
                continue
            elif friend_choice in friend_list:
                send_port = friend_choice
                break
            break
        #global send_port
        while True:
            if send_port == None:
                input("Setting send_port!")
                break
            else:
                operate_server.send_port_setting(send_port)
                print("接続完了")
                
            #portに接続する
            #operate_server.send_message()

            global message_stack_list
            global message_stack_str

            print(message_stack_str)
            while True:
                send_message = input("\n\nmessage:")
                if send_message == "/exit":
                    break
                else:
                    send_message = name + ":" + send_message
                    message_stack_list.append(send_message)
                    message_stack_str = '\n'.join(message_stack_list)#履歴を表示
                    operate_server.send_message(message_stack_str, send_port)
                    print(message_stack_str)
            break
    #elif num == 5:
    else:
        global end
        end = True
        print("OK,Goodbye!")

start()
while end == False:
    Home()
