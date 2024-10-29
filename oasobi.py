import socket

yes_list = ["y","yes","Yes","Y"]
no_list = ["n","no","No","N"]
name = "unknown"

class operate_server:
    send_port_num = int
    #port_creat()のportnumberを使ってサーバー設立
    def port_connect(port):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(("", port))
        server_socket.listen(5)

    def send_port_setting(send_port_setting):
        send_port_setting = send_port_setting

def start():
    port_num = int(input("port番号を入力してください"))
    operate_server.port_connect(port_num)

def previw():
    num = int(input("\n\nHello!\n1:view\n2:open_port_change\n3:send_message\n4:exit\n\n"))

    if num == 1:#port_view
        global name
        name_y_or_n = input("あなたは" + name + "です。\n名前を変更しますか？[Y/N]")
        if name_y_or_n in yes_list:
            new_name = input("名前を設定してください:")
            name = new_name

        elif name_y_or_n in no_list:
            print("OK,Goodbye!")
    elif num == 2:#send_port_setting
        send_port_input = int(input("送信先のportを入力してください"))
        operate_server.send_port_setting(send_port_input)
    #elif num == 5:

while True:
    previw()
    
