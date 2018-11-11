#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Queue
import subprocess;
import time;

class Task(object):
	# status -1 uncommited; 0 waiting; 1 running; 2 done
	def __init__(self, command ,tid = 0, status = 0, result = ""):
		self.command = command;
		self.tid = tid;
		self.status	 = status;
		self.result = result;
		self.start_time = None;	
		self.done_time = None;
	def output(self):
		print(self.tid);
		print(self.command);
		print(self.result);
		print("start",time.localtime(self.start_time));
		print("finish",time.localtime(self.done_time));
#TODO transform task_list to file
#TODO remove task
class TaskManager:
	def __init__(self, to_excute_queue, task_list=[], to_excute_addr = 0, to_update_addr = 0):
		self.to_excute_queue = to_excute_queue;
		self.task_list = task_list;
		self.to_excute_addr = to_excute_addr;
		self.to_upate_addr = to_upate_addr;
	def add_new_tasks(self, new_task_list):
		self.task_list.extend(new_task_list);
		for task in task_list[to_excute_addr:]:
			task.status = 1;
			to_excute_queue.put(task);
	def update_done_task(self, done_task):
		if done_task.tid != task_list[to_update_addr].tid:
			raise Exception("wrong update tid not equal", task);
		task_list[to_update_addr] = done_task;
		to_update_addr += 1;	
	def query_by_tid(self, task_tid):
		for task in task_list:
			if(task.tid == task_tid):
				return task;
	def query_all(self):
		return task_list;

#TODO: manage when some wrong when shell
class TaskExecutor:	
	def __init__(self,waiting_queue,done_queue):
		self.waiting_queue = waiting_queue;
		self.done_queue = done_queue;
	def isIdel(self):
		return self.waiting_queue.empty();
	def execute(self):
		task = self.waiting_queue.get();
		command = task.command;
		task.start_time = time.time();
		task.result = subprocess.check_output(command,shell = True);
		task.done_time = time.time();
		task.status = 2; 
		self.done_queue.put(task);

