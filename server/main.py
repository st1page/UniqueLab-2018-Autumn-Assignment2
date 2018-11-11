#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Process, Queue;
import threading
import time
import os;
import net_io;
import manage_tasks;
								
def execute(waiting_queue, done_queue)：
	TaskExecutor executor;
	while(True):
		executor.execute(waiting_queue, done_queue);		
def listen(servlet):
	servlet.listen();
def update_tasks(manager,done_queue):
	while True:	
		task = done_queue.get(True);
		manager.update_done_task(task);
		
waiting_queue = Queue();
done_queue = Queue();
manager = TaskManager(waiting_queue);
servlet = Servlet(manager);
pexecutor = Process(target=execute, args=(waiting_queue, done_queue,));
tlistener = threading.Thread(target=listen, args=(servlet,));
tupdater = threading.Thread(target=update_tasks, args=(manage,done_queue));

tlistener.start();
tupdater.start();