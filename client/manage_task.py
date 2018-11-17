#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, getopt
import time
import json
import utils
import tlist_utils
import socket
from my_types import Task
class TaskListDAO(object):
	def __init__(self,file_name):
		self.file_name = file_name;
	def read(self):
		json_str = utils.read_file(self.file_name);
		task_list = utils.json_2_tasklist(json_str);
		return task_list;
	def write(self,	task_list):
		json_str  = utils.tasklist_2_json(task_list);
		utils.write_file(self.file_name,json_str);	

class Messenger(object):
	def __init__(self, address = '123.207.58.152',port = 1837):
		self.address = address;
		self.port = port;
		self.s = utils.gen_connection(self.address, self.port);
	def send(self,bytes_list):
		try:
			for bytes_str in bytes_list: self.s.send(bytes_str);
		except socket.error as e:
			print('Error sending data: %s. Exiting' %e);
			sys.exit(1);
	def get(self):
		try:
			return self.s.recv(8192);
		except socket.error as e:
			print('Error recving data: %s. Exiting' %e);
			sys.exit(1);
	def close():
		self.s.close();
#TODO rollback transaction
class LocalManager(object):	
	def add(task):	
		cache_dao = TaskListDAO('uncommited');
		task_list = cache_dao.read();
		task_list.append(task);
		cache_dao.write(task_list);
		print('add!');
		task.output();
	def get_all():
		cache_dao = TaskListDAO('uncommited');
		return cache_dao.read();
	def get(tid):
		cache_dao = TaskListDAO('uncommited');
		task_list = cache_dao.read();
		return tlist_utils.find(task_list, tid);
	def remove(tid):
		cache_dao = TaskListDAO('uncommited');
		task_list = cache_dao.read();
		res = tlist_utils.remove(task_list, tid);
		cache_dao.write(task_list);
		return res;
	def clear():
		cache_dao = TaskListDAO('uncommited');
		log_dao = TaskListDAO('commit_log');
		task_list = cache_dao.read();
		log_list = log_dao.read();
		log_list.extend(task_list);
		log_dao.write(log_list);
		cache_dao.write([]);
#TODO remove a task on server
class NetManager(object):
	def commit():
		messenger = Messenger(); 
		task_list = LocalManager.get_all();
		messenge = [b'g[2;3%$^#[AdIm/;',utils.tasklist_2_json(task_list).encode()];
		messenger.send(messenge);
		LocalManager.clear();
	def get(tid):
		messenger = Messenger();
		messenge = [b'0p[1l7s^#@6#a;[u',str(tid).encode()];
		messenger.send(messenge);
		task_list = utils.json_2_tasklist(messenger.get().decode());
		return task_list[0];
	def get_all():
		messenger = Messenger();
		messenge = [b'0p[1l7s^#@6#a;[u','-1'.encode()];
		messenger.send(messenge);
		task_list = utils.json_2_tasklist(messenger.get().decode());
		return task_list;
	def remove(tid):
		messenger = Messenger();
		messenge = [b'0p[1l7s^#@6#a;[u',str(tid).encode()];
		messenger.send(messenge);
		task_list = utils.json_2_tasklist(messenger.get().decode());
		return task_list[0];
	def update_done():
		result_dao = TaskListDAO('done');
		task_list = get_all();
		done_task_list = [];
		for task in task_list:
			if(task.status == 2)