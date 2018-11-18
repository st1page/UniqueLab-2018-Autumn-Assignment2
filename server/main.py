#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Process, Queue;
import threading
import time
import os;
from my_types import Task
from net_io import Servlet
from manage_tasks import *;						
	
def listen_net(servlet):
	print('listen thread run');
	servlet.listen_net();
def listen_excutor(manager):
	print('update thread run');
	manager.listen_excutor();
		
manager = TaskManager();
servlet = Servlet(manager);


tlistener = threading.Thread(target=listen_net, args=(servlet,));
tupdater = threading.Thread(target=listen_excutor, args=(manager,));

tlistener.start();
tupdater.start();