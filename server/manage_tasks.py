#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Queue
import subprocess;
import time
import my_types
#TODO transform task_list to file
#TODO remove task
class TaskManager:
	def __init__(self, to_excute_queue, task_list=[], to_excute_addr = 0, to_update_addr = 0):
		self.to_excute_queue = to_excute_queue;
		self.task_list = task_list;
		self.to_excute_addr = to_excute_addr;
		self.to_update_addr = to_update_addr;
	def add_new_tasks(self, new_task_list):
		if new_task_list:		
			self.task_list.extend(new_task_list);
			for task in self.task_list[self.to_excute_addr:]:
				task.status = 1;
				self.to_excute_queue.put(task);
			self.to_excute_addr = len(self.task_list);
	def update_done_task(self, done_task):
		if done_task.tid != self.task_list[self.to_update_addr].tid:
			raise Exception("wrong update tid not equal", task);
		self.task_list[self.to_update_addr] = done_task;
		self.to_update_addr += 1;	
	def query_by_tid(self, task_tid):
		for task in self.task_list:
			if(task.tid == task_tid):
				return task;
	def query_all(self):
		return self.task_list;
	def remove(tid):
		

#TODO: manage some wrong when shell
#TODO: stop the task
class TaskExecutor:	
	def __init__(self,waiting_queue,done_queue):
		self.waiting_queue = waiting_queue;
		self.done_queue = done_queue;
	def isIdel(self):
		return self.waiting_queue.empty();
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
		self.done_queue.put(task);
