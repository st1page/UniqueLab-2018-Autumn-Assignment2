#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#TODO modify all
import socket
import utils
import json
from my_types import Task

class Servlet(object):
	def __init__(self,task_manager):
		self.task_manager = task_manager;
	def __query(self,s):
		tid = int(s.recv(4096).decode());
		if tid == -1: task_list = self.task_manager.query_all();
		else: task_list = [self.task_manager.query_by_tid(tid)];
		json_str = utils.tasklist_2_json(task_list);
		s.send(json_str.encode());
	def __add(self,s):
		print('now recive a commit');
		json_str = s.recv(8192).decode();
		print('recive :',end = ' ');
		print(json_str);
		tasks_list = utils.json_2_tasklist(json_str);
		for task in tasks_list:	
			task.output();	
		self.task_manager.add_new_tasks(tasks_list);
	def __remove(self,s):
		print('now to remove');
		tid = int(s.recv(10).decode());
		print('tid ',tid);
		#TODO###############################################
	def listen(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
		HOST = s.getsockname()[0];
		PORT = 1837;
		s.bind(( HOST, PORT));
		s.listen(5);
		while True:
			c, addr = s.accept();
			opt = c.recv(16);	
			print(opt);
			if(  opt==b'0p[1l7s^#@6#a;[u'): self.__query(c);
			elif(opt==b'g[2;3%$^#[AdIm/;'): self.__add(c);
			elif(opt==b'2s3(E&M.[:3si|"5'): self.__remove(c);
			c.close();


