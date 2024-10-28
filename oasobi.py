import socket

class operate_server:
    def port_creat():#ポート、サーバー設立
        port_number = input("port番号を入力してください")
        yorn = input(port_number+"で間違いないですか？(Y/N):")
        while True:
            if yorn == "y" or "Y" or "yes" or "Yes":
                operate_server.port_connect(port_number)
                #ここにメッセージ送信などの関数を入れる
                break
            else:
                print("goodbye!")
                break

    def port_connect(port_number):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        
operate_server.port_creat()
operate_server.port_connect
