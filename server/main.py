#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Process, Queue;
import threading
import time
import os;
from my_types import Task
from net_io import Servlet
from manage_tasks import *;						
def execute(waiting_queue, done_queue):
	executor = TaskExecutor(waiting_queue, done_queue);
	print('execute process run');
	while(True):
		executor.execute();		
def listen(servlet):
	print('listen thread run');
	servlet.listen();
def update_tasks(manager,done_queue):
	print('update thread run');
	while True:	
		task = done_queue.get(True);
		print('update thread get a task');
		task.output();
		manager.update_done_task(task);
		
waiting_queue = Queue();
done_queue = Queue();
manager = TaskManager(waiting_queue);
servlet = Servlet(manager);
pexecutor = Process(target=execute, args= (waiting_queue, done_queue,));
tlistener = threading.Thread(target=listen, args=(servlet,));
tupdater = threading.Thread(target=update_tasks, args=(manager,done_queue));

pexecutor.start();
tlistener.start();
tupdater.start();