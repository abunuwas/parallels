from random import randint
import datetime
import sched
import time
import multiprocessing as mp
import os
import threading 

def generate_random_int(ID):
	return randint(1,1000)

def events(num_events, ID):
	scheduler = sched.scheduler(time.time, time.sleep)
	for i in range(0,num_events):
		scheduler.enter(randint(0,3), randint(0,3), generate_random_int, (ID,))
	scheduler.run()

def event_threading():
	jobs = []
	for i in range(0,10):
		process = threading.Thread(target=events, args=(10,i))
		jobs.append(process)
	for j in jobs:
		j.start()
	for j in jobs:
		j.join()

def event_processing():
	jobs = []
	for i in range(0,10):
		process = mp.Process(target=events, args=(10,i))
		jobs.append(process)
	for j in jobs:
		j.start()
	for j in jobs:
		j.join()

if __name__ == '__main__':
	pass
	#Eevent_threading()
