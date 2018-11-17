#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time, json, sys
import socket
from my_types import Task
def gen_connection(address, port):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
	except socket.error as e:
		print('Error creating socket: %s .Exiting.' %e);
		sys.exit(1);
	
	try:
		s.connect((address, port));
	except socket.gaierror as e:
		print('Address-related error connectiong to server: %s. Exiting.' %e);
		sys.exit(1);
	except socket.error as e:
		print('Connection error: %s. Exiting.' %e);
		sys.exit(1);
	if 's' in locals(): return s;
	else: return None;
def read_file(file_name):
	try:
		fo = open(file_name,'r');
		res = fo.read();
	except IOError as e:
		print('File error:'+str(e));
		sys.exit(1);
	finally:
		if 'fo' in locals(): fo.close();
		if 'res' in locals(): return res;
		else :return None;

def write_file(file_name,wstr):
	try:
		fo = open(file_name,'w');
		fo.write(wstr);
	except IOError as e:
		print('File error:'+str(e));
		sys.exit(1);
	finally:
		if 'fo' in locals(): fo.close();

def task_2_json(task):
	return json.dumps(task,default = lambda obj: obj.__dict__,sort_keys=True);	

def tasklist_2_json(task_list):
	return json.dumps(task_list,default = lambda obj: obj.__dict__,sort_keys=True);	

def json_2_task(json_str):
	def json_2_task_handle(d):
		task = Task('','');
		task.__dict__ = d;
		return task;
	return json.loads(json_str,object_hook=json_2_task_handle);

def json_2_tasklist(json_str):
	def json_2_task_handle(d):
		task = Task('','');
		task.__dict__ = d;
		return task;
	if json_str=='' :return [];
	return json.loads(json_str,object_hook=json_2_task_handle);
