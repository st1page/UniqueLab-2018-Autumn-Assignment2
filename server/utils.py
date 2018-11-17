#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time, json
from my_types import Task
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
