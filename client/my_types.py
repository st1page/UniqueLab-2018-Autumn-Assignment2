#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time;
class Task(object):
	# status -1 uncommited; 0 waiting; 1 running; 2 done
	def __init__(self, command ,status = -1,tid = 0, result = ""):
		self.command = command;
		self.tid = hash(hash(command)+hash(time.time()))%1234567890;
		self.status	 = status;
		self.result = result;
		self.start_time = None;	
		self.done_time = None;
	def output(self):
		print('{:=^80}'.format(self.tid));
		print('command:',self.command);
		print('status :', end=' ');
		table = ['uncommited','waiting','running','done'];
		print(table[self.status+1]);
		print('{:-^50}'.format('result'));
		print(self.result);
		print('{:-^50}'.format(''));
		def format_time(the_time):
			return time.asctime(time.localtime(the_time));
		print('start_time', end=' ');
		if(self.start_time!=None):print(format_time(self.start_time));
		else: print('None');
		print('end_time  ', end=' ');
		if(self.done_time!=None):print(format_time(self.start_time));
		else: print('None');
