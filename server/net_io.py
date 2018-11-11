#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#TODO modify all
from multiprocessing import Queue
import socket
import utils
import json
from manage_tasks import Task

class Servlet(object):
	def __init__(self,task_manager):
	def __query(self,s):
		tid = int(s.recv(4096).decode());
		if tid == -1: task = self.task_manager.query_all();
		else: task = self.task_manager.query_by_tid(tid);
		json_str = json.dumps(task,default = lambda obj: obj.__dict__,sort_keys=True);	
		s.send(json_str.encode());
	def __add(self,s):
		def json_2_task_handle(d):
			task = Task('','');
			task.__dict__ = d;
			return task;
		json_str = s.recv(8192).decode()
		tasks_list = json.loads(json_str,object_hook=json_2_task_handle);
		self.task_manager.add_new_tasks(tasks_list);
	def listen(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
		HOST = s.getsockname()[0];
		PORT = 1234;
		s.bind(( HOST, PORT));
		s.listen(5);
		while True:
			c, addr = s.accept();
			opt = c.recv(1024);	
			if(opt==b'0'): self.__query(c);
			else: self.__add(c);
			c.close();	