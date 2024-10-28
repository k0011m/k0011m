import socket


class operate_server:


    #port_creat()のportnumberを使ってサーバー設立
    def port_connect(port):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(("", port))
        server_socket.listen(5)



port = int(input("port番号を入力してください"))
operate_server.port_connect(port)
