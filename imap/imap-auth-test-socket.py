#!/usr/bin/env python3

import socket, ssl, base64

HOSTNAME, PORT = 'imap-mail.outlook.com', 993

USER = 'mazafaka14@hotmail.com'
TOKEN = 'abracadabra'

AUTH = base64.b64encode('user={}\x01auth=Bearer {}\x01\x01'.format(USER, TOKEN).encode('ascii'))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as s:
    with ssl.SSLContext().wrap_socket(s) as ss:
        ss.connect((HOSTNAME, PORT))
        print(ss.recv().decode())

        ss.sendall(b'1 AUTHENTICATE XOAUTH2 {}\r\n'.fomat(AUTH))
        print(ss.recv().decode())

        ss.sendall(b'2 LIST "" ""\r\n')
        print(ss.recv().decode())
