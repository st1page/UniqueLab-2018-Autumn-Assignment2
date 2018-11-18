#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from my_types import Task

def find(task_list,tid):
	for task in task_list:
		if task.tid == tid : return task;
	return None;
def get_id(task_list,tid):
	task = find(task_list,tid);
	if(task == None) :return -1;
	return task_list.index(task);
def remove(task_list,tid):
	if find(task_list,tid)==None: 
		return False;
	for task in task_list:
		if task.tid == tid: 
			task_list.remove(task);
	return True;
	