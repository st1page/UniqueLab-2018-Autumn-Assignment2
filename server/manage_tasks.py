#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import multiprocessing
import threading
from multiprocessing import Process, Queue
import subprocess;
import time
import my_types
import tlist_utils;
#TODO transform task_list to file
#TODO remove task
class TaskExecutor:	
	def __init__(self,waiting_queue,done_queue,lock):
		self.waiting_queue = waiting_queue;
		self.done_queue = done_queue;
		self.lock = lock;
	def execute(self):
		task = self.waiting_queue.get();
		print('execute get a task');
		task.output();
		self.now_task = task;
		command = task.command;
		task.start_time = time.time();
		try:
			res = subprocess.check_output(command,shell = True);
			task.result = res.decode();
		except BaseException as e:
			task.result = str(e);
		task.done_time = time.time();
		task.status = 2; 
		self.lock.acquire();
		self.done_queue.put(task);
		self.lock.release();

class TaskManager:
	def __init_executor(self):
		def execute(waiting_queue, done_queue,executor_lock):
			executor = TaskExecutor(waiting_queue, done_queue, executor_lock,);
			print('execute process run');
			while True:
				executor.execute();
		self.pexecute = Process(target=execute, args = 
								(self.waiting_queue, self.done_queue,self.executor_lock));
		self.pexecute.start();
	def __init__(self):
		self.status = 0; # 0 free 1 running
		self.waiting_queue = Queue();
		self.done_queue = Queue();
		self.executor_lock = multiprocessing.Lock(); #the queue
		self.tasklist_lock = threading.Lock();		#the tasklist and status
		self.task_list = [];
		self.flag_addr = 0;
		self.__init_executor();
	def __execute_one(self):
		task = self.task_list[self.flag_addr];
		self.status = 1;
		task.status = 1;
		self.waiting_queue.put(task);
	def add(self, new_task_list):
		print('add start');
		self.tasklist_lock.acquire();
		self.task_list.extend(new_task_list);
		if(self.status == 0 and self.flag_addr<len(self.task_list)):
			self.__execute_one();
		self.tasklist_lock.release();
		print("add over");
	def __update_done_task(self, done_task):
		self.task_list[self.flag_addr] = done_task;
		self.flag_addr += 1;
	def listen_excutor(self):
		while True:
			task = self.done_queue.get(True);
			print('update thread get a task');
			self.tasklist_lock.acquire();
			task.output();
			self.__update_done_task(task);
			if(self.flag_addr == len(self.task_list)):
				status = 0;
			else :
				self. __execute_one();
			self.tasklist_lock.release();
	def get(self, tid):
		self.tasklist_lock.acquire();
		res = tlist_utils.find(self.task_list,tid);
		self.tasklist_lock.release();
		return res;
	def get_all(self):
		self.tasklist_lock.acquire();
		res = self.task_list;
		self.tasklist_lock.release();
		return res;
	def remove(self,tid):
		self.executor_lock.acquire();
		self.tasklist_lock.acquire();
		if(not self.done_queue.empty()):
			task = self.done_queue.get(False);
			self.__update_done_task(task);
		i = tlist_utils.get_id(self.task_list, tid);
		if(i==-1) : return False;
		if(self.status == 1 and 
			self.flag_addr<len(self.task_list) and
			self.task_list[self.flag_addr].tid == tid):
			
			self.pexcecute.terminate();
			self.__init_executor();
			res = tlist_utils.remove(task_list,tid);
			if(flag_addr == len(self.task_list)):
				status = 0;
			else :
				self. __execute_one();	
		else :
			res = tlist_utils.remove(self.task_list,tid);	
			if(i<self.flag_addr):
				self.flag_addr -= 1;
			elif(i>self.flag_addr):
				self.flag_addr += 1;
		self.tasklist_lock.release();
		self.executor_lock.release();
		return res;
		####################x

#TODO: manage some wrong when shell
#TODO: stop the task
