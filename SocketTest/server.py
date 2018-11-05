#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
HOST = s.getsockname()[0];
s.bind(( HOST, 1234));
s.listen(5);
print(HOST);
print('waiting');

while True:
	print(HOST);
	c, addr = s.accept();
	c.send(b'connect successfully!');
	print('get a connection from {0}'.format(addr));
	commond = c.recv(1024);
	print('get a commond {0}'.format(commond));
	c.send(b'some result 5678');
	print('connection over');
	c.close();
