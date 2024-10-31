import socket

yes_list = ["y","yes","Yes","Y"]
no_list = ["n","no","No","N"]
message_stack_list = []
message_stack_str = ''
my_port = int
send_port = int()
name = "hoge"
self_introduction = "profile"
end = False

class operate_server:
    send_port_num = int
    #port_creat()のportnumberを使ってサーバー設立
    def port_connect(port):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(("", port))
        server_socket.listen(5)

    def send_port_setting(send_port_setting):
        global send_port
        send_port = send_port_setting

def start():
    global my_port
    global send_port
    my_port = int(input("port番号を入力してください"))
    operate_server.port_connect(my_port)
#    send_port = int(input("送信先のport番号を入力してください"))

#常に稼働するHome画面
def Home():
    num = input("\n\nHello!\n1:profile\n2:send_port_change\n3:send_message\n4:exit\n\n")

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
        global send_port
        send_port_input = int(input("送信先のportを入力してください"))
        send_port = send_port_input
        operate_server.send_port_setting(send_port)
    
    #messageを送る
    elif num == "3":
        #global send_port
        while True:
            if send_port == None:
                print("Setting send_port!")
                continue
            #else:
                
            #portに接続する
            global message_stack_list
            global message_stack_str
            print(message_stack_str)
            while True:
                send_message = input("\n\nmessage:")
                if send_message == "/exit":
                    break
                else:
                    message_stack_list.append(send_message)
                    message_stack_str = '\n'.join(message_stack_list)#履歴を表示
                    print(message_stack_str)
    #elif num == 5:
    else:
        global end
        end = True
        print("OK,Goodbye!")

start()
while end == False:
    Home()
    
