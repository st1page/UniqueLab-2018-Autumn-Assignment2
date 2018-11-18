#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#TODO modify all
import socket
import utils
import json
from my_types import Task

class Servlet(object):
	def __init__(self,task_manager):
		self.task_mgr = task_manager;
	def __query(self,s):
		print('in query');
		tid = int(s.recv(15).decode());
		print('query',tid);
		if tid == -1: task_list = self.task_mgr.get_all();
		else: task_list = [self.task_mgr.get(tid)];
		json_str = utils.tasklist_2_json(task_list);
		print(json_str);
		s.send(json_str.encode());
		print('over');
	def __add(self,s):
		print('now recive a commit');
		json_str = s.recv(8192).decode();
		s.close();
		print('recive :',end = ' ');
		print(json_str);
		task_list = utils.json_2_tasklist(json_str);
		for task in task_list:	
			task.output();	
		self.task_mgr.add(task_list);
		print('__add over');
	def __remove(self,s):
		print('now to remove');
		tid = int(s.recv(10).decode());
		print('tid ',tid);
		res = self.task_mgr.remove(tid);
		s.send(str(res).encode());
		s.close();
		#TODO###############################################
	def listen_net(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
		HOST = s.getsockname()[0];
		PORT = 1898;
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		s.bind(( HOST, PORT));
		s.listen(5);
		while True:
			c, addr = s.accept();
			c.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			opt = c.recv(16);	
			print(opt);
			if(  opt==b'0p[1l7s^#@6#a;[u'): self.__query(c);
			elif(opt==b'g[2;3%$^#[AdIm/;'): self.__add(c);
			elif(opt==b'2s3(E&M.[:3si|"5'): self.__remove(c);
			c.close();


