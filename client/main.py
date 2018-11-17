#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, getopt
import time
from my_types import Task
import utils
from manage_task import LocalManager
from manage_task import NetManager

def out_help():
	print(utils.read_file("help_doc"));

def main():
	if len(sys.argv)==1: 
		out_help();
	elif sys.argv[1]=='help': 		
		out_help();
	elif sys.argv[1]=='add':
		if len(sys.argv)==2 or (len(sys.argv)==3 and sys.argv[2]=='-f'):
			print('/Myrsh add <command>\n./Myrsh add -f <xxx.sh>');
		elif sys.argv[2]=='-f':
			command = utils.read_file(sys.argv[3]);
			task = Task(command);
			LocalManager.add(task);
		else: 
			command = " ".join(sys.argv[2:]);
			task = Task(command);
			LocalManager.add(task);
	elif sys.argv[1]=='remove':
		if len(sys.argv)!=3: 
			print('输入一个tid\n./Myrsh remove <tid>');
		elif not sys.argv[2].isdecimal(): 
			print('tid是一串数字');
		else :
			tid = int(sys.argv[2]);
			flag = LocalManager.remove(tid);
			if flag == False : print('任务不存在！提示：只能删除本地缓存的任务');
	elif sys.argv[1]=='status':
		task_list = LocalManager.get_all();
		if(len(sys.argv)==3 and sys.argv[2]=='-l'):	
			for task in task_list: 
				task.output();		
		else :
			for task in task_list: 
				print('tid: ',task.tid);
	elif sys.argv[1]=='commit':
		NetManager.commit();
	elif sys.argv[1]=='sstatus':
		task_list = NetManager.get_all();
		if(len(sys.argv)==3 and sys.argv[2]=='-l'):	
			for task in task_list: 
				task.output();		
		else :
			for task in task_list: 
				print('tid: ',task.tid);
	elif sys.argv[1]=='query':
		if len(sys.argv)!=3: 
			print('输入一个tid\n./Myrsh query <tid>');
		elif not sys.argv[2].isdecimal(): 
			print('tid是一串数字');
		else :
			tid = int(sys.argv[2]);
			task = LocalManager.get(tid);
			if(task==None): task = NetManager.get(tid);
			task.output();
	else: print('Myrsh：{0} 不是一个 Myrsh 命令。参见 ./Myrsh help '.format(sys.argv[1]));	

main()		