#!/usr/bin/env python3

import imaplib

HOSTNAME, PORT = 'imap-mail.outlook.com', 993

USER = 'mazafaka14@hotmail.com'
TOKEN = 'abeacadabra'

conn = imaplib.IMAP4_SSL(HOSTNAME, PORT)
conn.authenticate('XOAUTH2', lambda x: "user={}\x01auth=Bearer {}\x01\x01".format(USER, TOKEN))
print('STATE:', conn.state)

conn.select('INBOX')
print(conn.list())
