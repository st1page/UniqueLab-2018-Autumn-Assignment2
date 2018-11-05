#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('123.207.58.152', 1234))

print(s.recv(1024));
s.send(b'some command 1234');
print(s.recv(1024));
s.close(); 